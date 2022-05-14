import logging
import os
import sys

import tweepy
from dotenv import load_dotenv
from tweepy import OAuth1UserHandler

# Parse the .env file and then load all the variables found as
# environment variables
load_dotenv()

# TODO: Check if API keys are V2, and tell user how to get V1 instead
# Environment variables
# https://developer.twitter.com/en/apps
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# https://tweeterid.com/
users_to_follow = os.environ["USERS_TO_FOLLOW"]
user_list_replies_to_our_tweet = os.getenv("USER_LIST_REPLIES_TO_OUR_TWEET")
user_list_replies_to_other_tweet = os.getenv("USER_LIST_REPLIES_TO_OTHERS_TWEET")  # noqa: E501, pylint: disable=line-too-long
user_list_someone_retweets_our_tweet = os.getenv("USER_LIST_SOMEONE_RETWEETS_OUR_TWEET")  # noqa: E501, pylint: disable=line-too-long
user_list_we_retweet_someone_elses_tweet = os.getenv("USER_LIST_WE_RETWEET_SOMEONE_ELSES_TWEET")  # noqa: E501, pylint: disable=line-too-long

# https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
webhook_url = os.environ["WEBHOOK_URL"]

# Log severity. Can be CRITICAL, ERROR, WARNING, INFO or DEBUG
log_level = os.getenv("LOG_LEVEL", default="INFO")

# Where https://github.com/TheLovinator1/twitter-image-collage-maker is
# running. You can run your own version or use the default
# https://twitter.lovinator.space/
collage_maker_url = os.getenv("TWITTER_IMAGE_COLLAGE_API", default="https://twitter.lovinator.space/add")  # noqa: E501, pylint: disable=line-too-long

# Authenticate to the Twitter API
auth = OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_list_retweets_split = []
user_list_retweeted_split = []
user_list_replies_to_our_tweet_split = []
user_list_replies_to_other_tweet_split = []

logger = logging
logger.basicConfig(
    format="%(asctime)s | %(levelname)-11s | %(funcName)-21s | %(message)s",
    datefmt="%H:%M:%S",
    level=log_level,
)

if users_to_follow is not None:
    print("Users - Tweets:")
    user_list = [x.strip() for x in str(users_to_follow).split(",")]
    for twitter_id in user_list:
        username = api.get_user(user_id=twitter_id)
        print(f"\t{twitter_id} - {username.screen_name}")
else:
    sys.exit("It looks like USERS_TO_FOLLOW is empty. Did you forget to fill it out?")  # noqa: E501, pylint: disable=line-too-long


if user_list_replies_to_our_tweet is not None:
    print("Users - Replies to our tweet:")
    user_list_replies_to_our_tweet_split = [x.strip() for x in str(user_list_replies_to_our_tweet).split(",")]  # noqa: E501, pylint: disable=line-too-long
    for twitter_id in user_list_replies_to_our_tweet_split:
        username_reply = api.get_user(user_id=twitter_id)
        print(f"\t{twitter_id} - {username_reply.screen_name}")

if user_list_replies_to_other_tweet is not None:
    print("Users - Reply to others tweet:")
    user_list_replies_to_other_tweet_split = [x.strip() for x in str(user_list_replies_to_other_tweet).split(",")]  # noqa: E501, pylint: disable=line-too-long
    for twitter_id in user_list_replies_to_other_tweet_split:
        username_reply = api.get_user(user_id=twitter_id)
        print(f"\t{twitter_id} - {username_reply.screen_name}")

if user_list_we_retweet_someone_elses_tweet is not None:
    print("Users - Retweets others tweet:")
    user_list_retweets_split = [x.strip() for x in str(user_list_we_retweet_someone_elses_tweet).split(",")]  # noqa: E501, pylint: disable=line-too-long
    for twitter_id in user_list_retweets_split:
        username_reply = api.get_user(user_id=twitter_id)
        print(f"\t{twitter_id} - {username_reply.screen_name}")


if user_list_someone_retweets_our_tweet is not None:
    print("Users - Retweet on our tweet:")
    user_list_retweeted_split = [x.strip() for x in str(user_list_someone_retweets_our_tweet).split(",")]  # noqa: E501, pylint: disable=line-too-long
    for twitter_id in user_list_retweeted_split:
        username_reply = api.get_user(user_id=twitter_id)
        print(f"\t{twitter_id} - {username_reply.screen_name}")
