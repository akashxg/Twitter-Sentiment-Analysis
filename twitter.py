# Twitter Sentiment Analysis
# Author: Akash Gheewala

import tweepy
from textblob import TextBlob

# Authenticate
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'

access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_selection = str(input("What keyword would you like to analyze? "))
# Retrieve tweets
public_tweets = api.search(user_selection)

for tweet in public_tweets:
	print("\n" + "\t" + '"' + tweet.text + '"')
	analysis = TextBlob(tweet.text)

	# Shows the exact numbers of the polarity and subjectivity of each public_tweets
	print(analysis.sentiment)

	# Sentiment Analysis
	mood = analysis.sentiment.polarity
	sub = analysis.sentiment.subjectivity
	
	# Determining mood and subjectivity of tweet with certain threshold
	if mood == 0:
		print("Sentiment: This tweet is useless")
	elif mood > 0:
		print("Sentiment: This tweet is happy :)")
	elif mood < 0:
		print("Sentiment: This tweet is angry!")

	if sub == 0:
		print("Subjectivity: Neutral")
	elif sub > 0.5:
		print("Subjectivity: Subjective")
	elif sub < 0.5:
		print("Subjectivity: Objective")