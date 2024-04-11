import praw
import datetime
import pandas as pd
import sqlite3

agent = "scrape"

reddit = praw.Reddit(
    client_id = "Wn4UzZHbArVxFYFXNYlM1w" ,
    client_secret = "J81vYapyQEwODrjdHkiYTMaxMXO_CQ" ,
    # username = "kalaghsefid" ,
    # password = "1234sefid" ,
    user_agent = agent ,
)

def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)


headline = {"subreddit":[] , "title":[] , "id":[] , "author":[] , "score":[] , "name":[] , "subscribers":[] , "comments_number":[] , "time":[]}


for sub in reddit.subreddit("nba").hot(limit = 10):
    subredditt = sub.subreddit
    #print(subredditt)
    headline["subreddit"].append(subredditt)

    titlee = sub.title
    #print(titlee)
    headline["title"].append(titlee)

    idd = sub.id
    #print(idd)
    headline["id"].append(idd)

    authorr = sub.author
    #print(authorr)
    headline["author"].append(authorr)

    scoree = sub.score
    #print(scoree)
    headline["score"].append(scoree)

    namee = sub.name
    #print(namee)
    headline["name"].append(namee)

    subscriberss = sub.subreddit_subscribers
    #print(subscriberss)
    headline["subscribers"].append(subscriberss)

    commentss = sub.num_comments
    #print(commentss)
    headline["comments_number"].append(commentss)

    time = get_date(sub)
    #print(time)
    headline["time"].append(time)

    #print(30*"-")


df = pd.DataFrame(headline)
df.head()

# df.to_csv("RedditbvvNssba.csv" , header=False , encoding="utf-8" , index = False)
