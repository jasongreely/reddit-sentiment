# reddit-sentiment

Utilizes [TextBlob](https://textblob.readthedocs.io/en/dev/) and [PRAW](http://praw.readthedocs.io/en/latest/index.html) 
to retrieve and analyze subreddit submission comments

Current output is limited to printed statements

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

Three prompts are then required:
```commandline
Analyze which Subreddit?: [Subreddit name]
How would you like to sort? (hot/top): [Sort filter]
How many posts would you like to analyze?: [Post count limit]
```

Results will be printed to the console:
```commandline
Analyze which Subreddit?: news
How would you like to sort? (hot/top): top
How many posts would you like to analyze?: 1
#84aebi | Scientist Stephen Hawking has died aged 76 | 727 positive, 484 neutral, 265 negative
```
