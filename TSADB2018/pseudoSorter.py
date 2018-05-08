# -*- coding: utf-8 -*-
import tweepy
import config
import sys
from resources import stopWordsEN,positive,negative
import re
from tweepy import OAuthHandler

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

queryr=input("game to search in quotation marks: ")
query= queryr.replace('"','')
filepos = open("positive/tweets"+query+"pos.txt","wb")
fileneg = open("negative/tweets"+query+"neg.txt","wb")
filedump = open("dump/tweets"+query+"dump.txt","wb")

#search in twitter for a query and pseudo assign each tweet to each category
for tweetResponse in tweepy.Cursor(api.search,q=queryr+ "-filter:retweets",tweet_mode="extended",include_rts=False,lang='en').items(500):
		text=tweetResponse.full_text.lower()
		string=""
		pos = False
		neg = False

		if not "@youtube" in text:
			text = text.replace(query,'')
			for word in text.split():
				if word in negative:
					neg=True
				elif word in positive:
					pos = True

				if not (word[0]=="#" or word[0]=="@"):
					if not "http" in word:
						if word not in (stopWordsEN ):
							string+=word+" "

			string=re.sub(r'[^\w\s]','',string)
			if pos:
				stringpos=string+",1\n"
				stringb = stringpos.encode("utf-8")
				filepos.write(stringb)
			if neg:
				stringneg=string+",-1\n"
				stringb = stringneg.encode("utf-8")
				fileneg.write(stringb)
			if not (neg or pos):
				string=string+",0\n"
				stringb = string.encode("utf-8")
				filedump.write(stringb)

filepos.close()
fileneg.close()
filedump.close()
