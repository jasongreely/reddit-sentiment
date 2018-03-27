# reddit-sentiment

Utilizes [TextBlob](https://textblob.readthedocs.io/en/dev/) and [PRAW](http://praw.readthedocs.io/en/latest/index.html) 
to retrieve and analyze subreddit submission comments

Results will output to a CSV file at a defined folder path for use in Excel or other reporting tools

## Installation

Install import requirements:
```
$ pip install praw
$ pip install textblob
$ python3 -m textblob.download_corpora
```

At this point you must create your own Reddit script application in [your account's preferences page](https://www.reddit.com/prefs/apps/)

You must also create a file named `praw_config.py` in the same directory as `sentiment.py` to house your Reddit credentials. You can do this in terminal with the following commands:
```commandline
touch praw_config.py
echo $"user_agent = '[YOUR USER AGENT NAME]'" >> praw_config.py
echo $"client_id = '[YOUR CLIENT ID]'" >> praw_config.py
echo $"client_secret = '[YOUR CLIENT SECRET]'" >> praw_config.py
echo $"username = '[YOUR USERNAME]'" >> praw_config.py
echo $"password = '[YOUR PASSWORD]'" >> praw_config.py
```

Or alternatively create the file with an IDE/editor using the following code:
```python
user_agent = '[YOUR USER AGENT NAME]'
client_id = '[YOUR CLIENT ID]'
client_secret = '[YOUR CLIENT SECRET]'
username = '[YOUR USER NAME]'
password = '[YOUR PASSWORD]'
```
## Usage
Run the program from console, terminal, or an IDE:
```commandline
python3 sentiment.py
```

Four prompts are then required:
```commandline
Analyze which Subreddit?: [Subreddit name]
How would you like to sort? (hot/top): [Sort filter]
How many posts would you like to analyze?: [Post count limit]
Define the path for the CSV file: [/user/folder/path/]
```

Results will be printed to the console:
```commandline
Analyze which Subreddit?: news
How would you like to sort? (hot/top): hot
How many posts would you like to analyze?: 10
Define the path for the CSV file: /path/to/folder/
Success: CSV created in /path/to/folder/reddit_news_analysis_1522181235.csv
```

The CSV includes:
* Unique Submission ID
* Submission title
* Total (top level) comments
* Total positive comments
* Total neutral comments
* Total negative comments
