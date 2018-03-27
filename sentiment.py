import praw
import praw_config
import re
from textblob import TextBlob

TARGET_SUB = "nfl"
TARGET_SORT = "hot"
TARGET_COUNT = 25


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
        print("Processing post: {}".format(submission.title))

        tot = 0

        pos = 0
        neu = 0
        neg = 0

        for comment in submission.comments.list():
            tot += 1

            if hasattr(comment, "body"):
                polarity = analyze_comment(comment)

                if polarity > 0:
                    pos += 1
                if polarity == 0:
                    neu += 1
                if polarity < 0:
                    neg += 1

        print("Analysis complete: {:.1%} positive, {:.1%} neutral, {:.1%} negative".format((pos/tot), (neu/tot), (neg/tot)))


def clean_comment(comment):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", comment).split())


def analyze_comment(comment):
    analysis = TextBlob(clean_comment(comment.body))

    return analysis.sentiment.polarity


main()
