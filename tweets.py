import tweepy
import subprocess
import os
import re

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

f = open('messages.txt', 'r+')
messages = f.readlines()

stored_messages = []

# Get tweet ID from each message on file
for message in messages:
  id = re.findall(r'^\d+', message)
  stored_messages.append(id[0])

tweet_list = []

for tweet in tweets:
  if str(tweet.id) not in stored_messages:
    t = str(tweet.id)
    t+= ' ' + tweet.sender_screen_name
    t+= ' ' + normalise(tweet.text)
    t+= '\n'
    tweet_list.append(t)

for tweet in reversed(tweet_list):
  f.write(tweet)

f.close()
