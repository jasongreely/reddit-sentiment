import praw
import praw_config

TARGET_SUB = ""
TARGET_SORT = ""
TARGET_COUNT = 10

def main():
    reddit = praw.Reddit(user_agent=praw_config.user_agent,
                         client_id=praw_config.client_id, client_secret=praw_config.client_secret,
                         username=praw_config.username, password=praw_config.password)

    subreddit = reddit.subreddit(TARGET_SUB)