import tweepy
import subprocess
import os

def normalise(string):
  return string.replace('\n', ' ').replace('\r', '').replace('  ', ' ')

access_token = os.getenv('ACCESS_TOKEN')
access_secret_token = os.getenv('ACCESS_SECRET_TOKEN')

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

tweets = api.direct_messages()

voice = '-ven-us+f3'
speed = '-s180'

tweet_list = []

for tweet in tweets:
  t = str(tweet.id)
  t+= ' ' + tweet.sender_screen_name
  t+= ' ' + normalise(tweet.text)
  t+= '\n'
  tweet_list.append(t)

# Write to file
f = open('messages.txt', 'w')

for tweet in reversed(tweet_list):
  f.write(tweet)

f.close()
