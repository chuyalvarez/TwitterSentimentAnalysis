from __future__ import absolute_import, print_function
import config
import tweepy
import re
import numpy as np
import pandas as pd
import json
import pymongo
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from resources import stopWordsEN,positive,negative
from pprint import pprint
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from collections import Counter

nOfTweets=1000
fileName="minedtweets.csv"
vect = CountVectorizer(binary=True)
rf = RandomForestClassifier(n_estimators = 100)

class StdOutListener(StreamListener):
	def on_data(self, data):
		info = json.loads(data)
		print ("received request")


		mine(info)

	def on_error(self, status):
		print(status)


def mine(info):
	username=info["user"]["screen_name"]
	tweetId=info["id"]
	gameToAnalyze=""
	for title in info['text'].split():
		if not '@' in title:
			gameToAnalyze+= title+" "
	query='"'+gameToAnalyze+'"'
	print(username)
	print(tweetId)
	print(gameToAnalyze)
	file = open(fileName,"wb")

	for tweetResponse in tweepy.Cursor(api.search,q=query+ "-filter:retweets",tweet_mode="extended",include_rts=False,lang='en').items(nOfTweets):
		text=tweetResponse.full_text.lower()
		string=""
		pos = False
		neg = False

		if not "@youtube" in text:
			text = text.replace(gameToAnalyze,'')
			for word in text.split():
				if not (word[0]=="#" or word[0]=="@"):
					if not "http" in word:
						if word not in (stopWordsEN ):
							string+=word+" "

			string=re.sub(r'[^\w\s]','',string)
			if not string.replace(' ',''):
				continue
			string= string + ","+tweetResponse.id_str

			if tweetResponse.place:
				string= string+','+tweetResponse.place.country_code
				string= string+','+tweetResponse.place.place_type
				string= string+','+tweetResponse.place.name
			else:
				string = string + ",,,"

			string=string+','+str(tweetResponse.coordinates)
			string=string+"\n"
			stringb = string.encode("utf-8")
			file.write(stringb)
	file.close()
	analyzeSentiment(info,gameToAnalyze)

def analyzeSentiment(info,gameToAnalyze):
	username=info["user"]["screen_name"]
	tweetId=info["id"]
	print("analzing "+gameToAnalyze)
	print(username)
	print(tweetId)
	tcsv = pd.read_csv(fileName,names=['tweet','tweetid','countrycode','placetype','placename','coord'])
	T_test_vect = vect.transform(tcsv.tweet)
	T_pred = rf.predict(T_test_vect)
	c=Counter(T_pred)
	tot=c[1]+c[-1]
	posperc=(c[1]/tot)*100
	negperc=(c[-1]/tot)*100
	print("@{} the game {} has a review of {:.2f}% of positive reviews and {:.2f}% of negatives from {} tweets analyzed".format(username,gameToAnalyze,posperc,negperc,tot+c[0]))
	api.update_status("@{} the game {} has a positive review percentage of {:.2f}% and a negative review percentage of {:.2f}% from {} tweets analyzed".format(username,gameToAnalyze,posperc,negperc,tot+c[0]),tweetId)

	client = pymongo.MongoClient(config.mongo_url)
	db = client.test
	colnames= db.collection_names()
	if gameToAnalyze in colnames:
		posts=db[gameToAnalyze]
	else:
		posts = db.create_collection(gameToAnalyze)
	for i in range(0,len(tcsv)):
		post = {"id": str(tcsv.iloc[i]["tweetid"]),
				"tweet":tcsv.iloc[i]["tweet"],
				"sentiment":str(T_pred[i]),
				"place":{"type":tcsv.iloc[i]["placetype"],
						 "name":tcsv.iloc[i]["placename"],
						 "country":tcsv.iloc[i]["countrycode"],
						 "point":tcsv.iloc[i]["coord"]}}
		posts.insert_one(post)
	print("done uploading")


df = pd.read_csv('sortedtweets.csv', names=['tweet','sent'])
X = df.tweet
y = df.sent

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train_vect = vect.fit_transform(X_train)
X_test_vect = vect.transform(X_test)

#X_train_res, y_train_res = sm.fit_sample(X_train_vect, y_train)
#rf.fit(X_train_res, y_train_res)
print("training")
rf.fit(X_train_vect, y_train)

y_pred = rf.predict(X_test_vect)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
#f1 = f1_score(y_test, y_pred
#pprint(f1)
pprint(acc)
pprint(cm)

l = StdOutListener()
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)
stream = Stream(auth, l)
print("listening")
stream.filter(track=['@vgsentimentbot'])
