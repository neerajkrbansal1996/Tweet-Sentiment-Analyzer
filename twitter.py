import os
import re
import sys
import tweepy
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for App
    '''
    def __init__(self, query):
        ## Twitter credentials
        consumer_key = 'ctZTLbaNJePzANlid7emrbptw'
        consumer_secret = 'D53Vighn1zgwmWIQInC2Wj7CzZSEarGdoxiEMB5lJYjTdj0KTd'
        
        access_token = '383643880-yVaJDF5VIMDPsIB3rTnojUsYfgvXILEmQ418BvVQ'
        access_token_secret = 'HVH9cblwNZw3VtBLS9GpKUCZ93qVs2uFw6Ms51sgCpUOy'
        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.query = query
            self.api = tweepy.API(self.auth)
            self.tweet_count_max = 100 #To prevent Rate Limiting
        except:
            print("Error: Authentication Failed")        

    def set_query(self, query=''):
        self.query = query;
        
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    
    def get_tweets(self):
        tweets = []
        try:
                recd_tweets = self.api.search(q=self.query,
                                              count=self.tweet_count_max)
                if not recd_tweets:
                    pass
                for tweet in recd_tweets:
                    parsed_tweet = {}
    
                    parsed_tweet['text'] = tweet.text
                    parsed_tweet['user'] = tweet.user.screen_name
                    
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                    
                    tweets.append(parsed_tweet)
    
                return tweets
        except tweepy.TweepError as e:
                print("Error : " + str(e))

'''
twitterClient = TwitterClient('@neerajkrbansal');
twitterClient.set_query('Neeraj')
tweets = twitterClient.get_tweets();
print(tweets)
'''