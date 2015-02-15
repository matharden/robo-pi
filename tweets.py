import tweepy
import subprocess
import os

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

f = open('messages','r')
previous_id = f.readline()
original = f.read()
f.close()

latest = next(iter(tweets))
latest_id = str(latest.id)
print latest_id
print previous_id

if str(latest_id) != str(previous_id):

  f = open('messages','w')
  f.write(latest_id + '\n')

  for tweet in tweets:
    f.write(tweet.text + '\n')
    print tweet.id
    sentence = tweet.sender_screen_name + ' says: ' + tweet.text
    # subprocess.call('espeak ' + voice + ' ' + speed + ' "' + sentence + '"', shell=True)

  f.write(original)
  f.close()
