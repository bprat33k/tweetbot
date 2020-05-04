import tweepy
import sys
from time import sleep
#from credentials import *

from os import environ #for production
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

my_file=open('verne.txt','r')
file_lines=my_file.readlines()
my_file.close()

def tweet():
    for line in file_lines:
        try:
            print(line)
            if line != '\n':
                api.update_status(line)
                sleep(3600)
            else:
                pass
            
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
    
tweet()

for tweet in tweepy.Cursor( api.search, 
                            q='#stockmarket',
                            since='2020-05-03').items(5):
    try:
        print('Tweet by: @' + tweet.user.screen_name)
        
        tweet.retweet()
        print('Retweeted the tweet')

        tweet.favorite()
        print('Favorited the tweet')

        if not tweet.user.following:    
            tweet.user.follow()
            print('Followed the user')

        sleep(40)

    except tweepy.TweepError as e:
        print (e.reason)

    except StopIteration:
        break    


