import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'Q8DOWaZIs4xkCsjQQqMmA4EmQ'
consumer_secret = 'jvIBJqgA2DpsmWMhuH2k0gYjfPKz0appA8rzYeqM3CNfADIzjA'
access_token = '976661454706429952-oIey2lGwMPiKZadXxBT9LIR9E5UWAz8'
access_secret = '0R0iBZZ4wvGc3mZTjyvuO3lOx3rdqpo91mVuXHrLczJAv'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#read own timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
    
print()

#Get own tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    print(json.dumps(tweet._json))
