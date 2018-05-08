# TwitterSentimentAnalysis
Repository for project files for a twitter sentiment analysis tool that uses python and some libraries to connect interpret and analyze tweets on a topic. 

This version of the project was done to analyze videogames on realeases but by getting tweets on a topic that have their sentiment assigned and create the ML model based on those, this way it can analyze any topic you wish to focus it to.

# Setup
In order to use this project you need to have the following things:

  * Python 3, 3.6 version and required dependencies.
  * A Twitter App linked to an acount that will be used to tweet to and respond.
  * A MongoDB database.

# Creating your Twitter App and Credentials
To create a Twitter app head on to https://apps.twitter.com/ and create a new app. After creating it generate your keys and enable the use of tokens as both will be used to connect to Twitter via Python. If you want your project to tweet out the response you need to enable the app to read and write to Twitter.

# Setting up python
To be able to use the python programs you need to install several dependencies via the use of pip install
  + pip install tweepy
  + pip install numpy
  + pip install pandas
  + pip install scipy
  + pip install sklearn
  + pip install pymongo
  + pip install flask
  
Additionally you will need a file in the TSADB2018 folder named "config.py" where you need to declare the variables to use the twitter app credentials.

```python

consumer_key = 'Your Key Here'
consumer_secret = 'Your Key Here'
access_token = 'Your Token Here'
access_secret = 'Your Token Here'

```

# MongoDB
This project uses MongoDB to store the analyzed tweets and use them to present the data. In order to connect to create a mongoDB database you could create your own local database. Our version uses a cluster created on MongoDB Atlas you can create your own in https://www.mongodb.com/cloud/atlas to create your own, there you can find different ways to connect python and mongo. We use a variable defined in config.py that has the url to connect.

```python
mongo_url = 'url here'
```

# What everything does
In the repository there is a folders TSADB2018 that has the twitter mining section as well as analysis and responding via twitter and includes the maps webpage to show the map locally.

+ TSADB2018
  This folder contain several things:
  * 4 .py files
    - streamer.py is the main program, by running that the twitter account will be listening and once it is tweeted to it, it will mine and give a result about the analyzed tweets.
    - pseudoSorter.py uses resources.py to organize tweets into categories in order to sort them and use them to train the model, the files are saved in the different folders. if you wish to use this for your own topic you can use this to mine and categorize the tweets of a topic.
    - page.py creates a webpage locally with flask and using the folders static for javascript and the folder template that has the html to load the page
   * 2 .csv files
     - these files store the mined tweets in a csv to handle with pandas, minedtweets.csv has the tweets that are mined during streamer.py execution and sortedtweets.csv store tweets intended for training and testing.
   * A .txt file
     - This is used as a reference for the tweet structure mined by tweepy if need to use another parameter.
    
# Running
Make sure you have all dependencies installed and the config.py file set up and just run streamer.py and you are good to go. After running the file, a model will be trained using the sorted tweets and a accuracy will be returned, you can re-run the program to train the model again and get a different accuracy, you can do this until you achieve an accuracy you are comfortable with.

# Dependencies

These are libraries or software that the project uses and make it easy to implement.

- Tweepy: A library for python that lets you connect to the twitter API to get tweets, information on a user and post tweets. www.tweepy.org

- MongoDB: A document database with scalability and flexibility with the ability of querying and indexing to allow storage and retrieval of data https://www.mongodb.com/

- Numpy: A library for python that lets you manipulate large multi-dimensional arrays of arbitrary records without sacrificing too much speed for small multi-dimensional arrays. http://www.numpy.org/

- Pandas: A library for python that provides data structures to work with structured information easily. http://pandas.pydata.org/

- SciPy: Scientific Library for Python. https://www.scipy.org

- Sklearn: A set of python modules for machine learning and data mining. http://scikit-learn.org

- PyMongo: Tools for interacting with MongoDB database from Python. https://api.mongodb.com/python/current/

- Flask: A lightweight WSGI web application framework. http://flask.pocoo.org/

