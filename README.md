# reddit-sentiment

Utilizes [TextBlob](https://textblob.readthedocs.io/en/dev/) and [PRAW](http://praw.readthedocs.io/en/latest/index.html) 
to retrieve and analyze subreddit submission comments

Current output is limited to printed statements

## Installation
```
$ pip install praw
$ pip install textblob
$ python3 -m textblob.download_corpora
```

## Usage
Run the program from console, terminal, or an IDE:
```
python3 sentiment.py
```

Three prompts are then required:
```
Analyze which Subreddit?: [Subreddit name]
How would you like to sort? (hot/top): [Sort filter]
How many posts would you like to analyze?: [Post count limit]
```

Results will be printed to the console:
```
Analyze which Subreddit?: news
How would you like to sort? (hot/top): top
How many posts would you like to analyze?: 1
#84aebi | Scientist Stephen Hawking has died aged 76 | 727 positive, 484 neutral, 265 negative
```
