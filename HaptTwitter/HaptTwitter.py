from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys


consumer_key = "KqunxDVvZ13Q9b4aCE3vR9niU"
consumer_secret = "ii7l13trSyuZxWUWJYB9VgrqVDI93vVCrcpAJbdSYhJjPE187j"
access_token = "945408464477655041-jYOxGHKTE2iMtLlXMGE78jyjMSI0pRA"
access_token_secret = "955sWk0VYck8NC3BtCHL1GsTdGV0o8sxaDEnXx4va7xry"

authorization = OAuthHandler(consumer_key, consumer_secret)
authorization.set_access_token(access_token, access_token_secret)
authorization_api = API(authorization)

used = open('used.txt', 'r')
dataset = used.readlines()
used.close()
writer = open('used.txt', 'a')
class Tweet:
    def __init__(self, user):
        self.booleanText = False
        self.user = user
        self.name = user.name
        self.screen_name = user.screen_name
        self.description = user.description
        self.statuses_count = str(user.statuses_count)
        self.friends = str(user.friends_count)
        self.followers = str(user.followers_count)

        self.creation_date = user.created_at
    def avaregeTweets(self):
        delta = datetime.utcnow() - self.creation_date
        age_days = delta.days
        return "%.2f tweets/day" % (float(self.statuses_count)/float(age_days))

    def getLastTweets(self):
        new_tweets = authorization_api.user_timeline(screen_name=self.screen_name, count=1, tweet_mode="extended")
        for tweet in new_tweets:
            if str(tweet.id)+'\n' in dataset:
                return None
            addition = ('https://twitter.com/' + self.screen_name[1:] + '/status/'+ str(tweet.id))
            writer.write(str(tweet.id)+'\n')
            return tweet.full_text + '\n' + addition


    def __repr__(self):
        text = None
        welcomeName = ('User: '+self.name)
        if(self.getLastTweets())!=None:
            text = (self.getLastTweets())
        #print('Description: '+self.description)
        #print('Friends: '+self.friends)
        #print('Followers: '+self.followers)
        #print('Number of Status: '+self.statuses_count)
        #print(self.avaregeTweets())
        if text!=None:
            return welcomeName + '\n' + text
        return str(None)

account_list = []
countries = {1: 'canada.txt', 2: 'brasil.txt', 3: 'eua.txt'}

print('''
1 - Canada
2 - Brasil
3 - EUA''')
country = int(input())
file = open(countries[country], 'r')
content_file = file.readlines()
file.close()
for person in content_file:
    try:
        helper = Tweet(authorization_api.get_user(person))
        if helper.getLastTweets() != None:
            print(helper)
            print()

    except ValueError:
        print("Não foi possível receber as informações")

