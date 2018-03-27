import praw
import praw_config

TARGET_SUB = "nfl"
TARGET_SORT = "hot"
TARGET_COUNT = 10


def main():
    reddit = praw.Reddit(user_agent=praw_config.user_agent,
                         client_id=praw_config.client_id, client_secret=praw_config.client_secret,
                         username=praw_config.username, password=praw_config.password)

    subreddit = None

    if TARGET_SORT == "hot":
        subreddit = reddit.subreddit(TARGET_SUB).hot(limit=TARGET_COUNT)
    else:
        if TARGET_SORT == "top":
            subreddit = reddit.subreddit(TARGET_SUB).top(limit=TARGET_COUNT)
        else:
            print("Target sort is invalid")

    if subreddit is not None:
        process_subreddit(subreddit)
    else:
        print("Subreddit could not be found")


def process_subreddit(subreddit):
    for submission in subreddit:
        print(submission.title)


main()
