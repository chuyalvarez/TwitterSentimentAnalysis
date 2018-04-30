# coding: utf-8 
import tweepy
import config
from resources import stopWordsEN,positive,negative
import re
from tweepy import OAuthHandler
 
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

query='anaya'
file = open("tweets"+query+".txt","w")
tid = 0
#read a user timeline, set amount of tweets
'''
for tweet in api.user_timeline(screen_name=query,count=3,include_rts=True):
	tid=tweet.id
	for tweetResponse in tweepy.Cursor(api.search,q=query+ "-filter:retweets",tweet_mode="extended",include_rts=False).items(300):
		if (tid==tweetResponse.in_reply_to_status_id):
			text=tweetResponse.full_text.lower()
			string=""
			
			print ("https://twitter.com/"+str(tweetResponse.user.screen_name)+"/status/"+str(tweetResponse.id))
			
			for word in text.split():
				if not (word[0]=="#" or word[0]=="@"):
					if word not in stopWords:
						string+=word+" "
			
			string=re.sub(r'[^\w\s]','',string)
			#print (tweetResponse.entities['hashtags'])
			print (string)
			#file.write(text.lower())
			print("--------------------------------")
			
'''
			
			
for tweetResponse in tweepy.Cursor(api.search,q=query+ "-filter:retweets",tweet_mode="extended",include_rts=False,lang='es').items(500):
		#if (tid==tweetResponse.in_reply_to_status_id):
		text=tweetResponse.full_text.lower()
		string=""
		useful = False
		neg = False
		
	
		print ("https://twitter.com/"+str(tweetResponse.user.screen_name)+"/status/"+str(tweetResponse.id))
		text = text.replace(query,'')
		for word in text.split():
			if word in negative:
				neg=True
			if word in positive:
				useful = True

			if not (word[0]=="#" or word[0]=="@"):
				if not "http" in word:
					#if word not in (stopWordsEN ):
					string+=word+" "
		
		string=re.sub(r'[^\w\s]','',string)
		'''
		if tweetResponse.place:
			print('	'+tweetResponse.place.name)
			print('	'+tweetResponse.place.place_type)
			print('	'+tweetResponse.place.country_code)
			print(tweetResponse.place.contained_within)
		print (tweetResponse.entities['hashtags'])
		'''
		print (string)
		if useful:
			file.write("https://twitter.com/"+str(tweetResponse.user.screen_name)+"/status/"+str(tweetResponse.id)+"\n")
			file.write(string+",1\n")
		if neg:
			file.write("https://twitter.com/"+str(tweetResponse.user.screen_name)+"/status/"+str(tweetResponse.id)+"\n")
			file.write(string+",-1\n")
		#print("--------------------------------")

file.close()
	
'''

text = ""
print("tweets with MENTION of")
for tweety in tweepy.Cursor(api.search,q=query,tweet_mode="extended",include_rts=False).items(1):
#for tweety in api.user_timeline(screen_name='tha_rami',count=20,include_rts=False):
	#if tweety.in_reply_to_user_id==uid: 
	text=tweety.full_text
	if not (text[0]=="R" and text[1]=="T" and text[2]==" "):
		
		print ("https://twitter.com/"+str(tweety.user.screen_name)+"/status/"+str(tweety.id))
		print (tweety.retweeted)
		print(text.lower())
		print("--------------------------------")
'''
		



'''

{'created_at': 'Wed Apr 18 21:07:56 +0000 2018',
 'id': 986712959610212352,
 'id_str': '986712959610212352',
 'text': "@mikeBithell Holy shit mate glad to hear you're all OK",
 'truncated': False,
 'entities':{
	'hashtags': [],
	'symbols': [],
	'user_mentions':[{
		'screen_name': 'mikeBithell',
		'name': 'Mike Bithell @ reboot (croatia)',
		'id': 13096002,
		'id_str': '13096002',
		'indices': [0, 12]}],
	'urls': []},
 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
 'in_reply_to_status_id': 986706791676502017,
 'in_reply_to_status_id_str': '986706791676502017',
 'in_reply_to_user_id': 13096002,
 'in_reply_to_user_id_str': '13096002',
 'in_reply_to_screen_name': 'mikeBithell',
 'user': {
	'id': 17064600,
	'id_str': '17064600',
	'name': 'Rami Ismail',
	'screen_name': 'tha_rami',
	'location': '30,000ft',
	'description': '50% of indie game studio @Vlambeer. Creator of presskit(). Public speaker, traveler and supporter of indie initiatives & international game dev communities.',
	'url': 'https://t.co/lnxZEhYFWO',
	'entities': {'url': {'urls': [{'url': 'https://t.co/lnxZEhYFWO', 'expanded_url': 'http://www.ramiismail.com', 'display_url': 'ramiismail.com', 'indices': [0, 23]}]},
		'description': {'urls': []}},
	'protected': False,
	'followers_count': 142178,
	'friends_count': 9592,
	'listed_count': 1460,
	'created_at': 'Thu Oct 30 13:05:20 +0000 2008',
	'favourites_count': 54185,
	'utc_offset': 7200,
	'time_zone': 'Amsterdam',
	'geo_enabled': True,
	'verified': True,
	'statuses_count': 80278,
	'lang': 'en',
	'contributors_enabled': False,
	'is_translator': False,
	'is_translation_enabled': False,
	'profile_background_color': '1A1B1F',
	'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme9/bg.gif',
	'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme9/bg.gif',
	'profile_background_tile': False,
	'profile_image_url': 'http://pbs.twimg.com/profile_images/2198521011/rami-thumg_normal.png',
	'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2198521011/rami-thumg_normal.png',
	'profile_banner_url': 'https://pbs.twimg.com/profile_banners/17064600/1393729549',
	'profile_link_color': '2FC2EF',
	'profile_sidebar_border_color': '666666',
	'profile_sidebar_fill_color': 'FFFFFF',
	'profile_text_color': '000000',
	'profile_use_background_image': True,
	'has_extended_profile': True,
	'default_profile': False,
	'default_profile_image': False,
	'following': True,
	'follow_request_sent': False,
	'notifications': False,
	'translator_type': 'none'},
 'geo': None,
 'coordinates': None,
 'place': {
	'id': '8d65596349ee2e01',
	'url': 'https://api.twitter.com/1.1/geo/id/8d65596349ee2e01.json',
	'place_type': 'country',
	'name': 'Republic of Croatia',
	'full_name': 'Republic of Croatia',
	'country_code': 'HR',
	'country': 'Republic of Croatia',
	'contained_within': [],
	'bounding_box': {
		'type': 'Polygon',
		'coordinates': [[[13.4897243, 42.3776665],[19.4480171, 42.3776665], [19.4480171, 46.5549896], [13.4897243, 46.5549896]]]},
	'attributes': {}},
 'contributors': None,
 'is_quote_status': False,
 'retweet_count': 0,
 'favorite_count': 7,
 'favorited': False,
 'retweeted': False, 
 'lang': 'en'}

'''
