from pymongo import MongoClient
client = MongoClient('localhost', 27017)


def get_tweets(db_name, collection_name):
    db = client[db_name]
    tweets_cursor = db[collection_name].find()

    tweets = []

    for tweet in tweets_cursor:
        tweets.append(tweet)

    return tweets
