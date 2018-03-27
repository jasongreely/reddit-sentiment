import praw
import praw_config
import re
from textblob import TextBlob


def _main_():
    reddit = reddit = praw.Reddit(user_agent=praw_config.user_agent,
                         client_id=praw_config.client_id, client_secret=praw_config.client_secret,
                         username=praw_config.username, password=praw_config.password)

    # Subreddit Input Prompt
    subreddit_required = True
    subreddit_input = None

    while subreddit_required:
        subreddit_input = input("Analyze which Subreddit?: ")

        if subreddit_input:
            subreddit_required = False
        else:
            print("** Must enter a value **")

    # Sort input prompt
    sort_required = True
    sort_input = None

    while sort_required:
        sort_input = input("How would you like to sort? (hot/top): ")

        if sort_input and sort_input.lower() in ["hot", "top"]:
            sort_input = sort_input.lower()
            sort_required = False

        else:
            print("** Must enter a value of hot or top **")


    # Limit input prompt
    count_required = True
    count_input = 0

    while count_required:
        try:
            count_input = int(input("How many posts would you like to analyze?: "))

            if count_input <= 0:
                print("** Input must be a whole number greater than zero **")
            else:
                count_required = False
        except ValueError:
            print("** Input must be a whole number greater than zero **")


    # Retrieve Subreddit
    subreddit = None

    if sort_input == "hot":
        subreddit = reddit.subreddit(subreddit_input).hot(limit=count_input)
    else:
        if sort_input == "top":
            subreddit = reddit.subreddit(subreddit_input).top(limit=count_input)

    if subreddit is not None:
        process_subreddit(subreddit)
    else:
        print("Subreddit could not be found")


def process_subreddit(subreddit):
    for submission in subreddit:
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

        print("#{} | {} | {} positive, {} neutral, {} negative".format(submission.id, submission.title, pos, neu, neg))


def clean_comment(comment):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", comment).split())


def analyze_comment(comment):
    analysis = TextBlob(clean_comment(comment.body))

    return analysis.sentiment.polarity


_main_()
