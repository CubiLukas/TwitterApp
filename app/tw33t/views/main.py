from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
import json, requests, datetime, sys, os, uuid, re, time
import tweepy
from jinja2 import TemplateNotFound

consumer_key = "Ux2iOJHTSL8wt50zN5mm1SFQ4" 
consumer_secret = "B9nUZKjqHSuFD1BBLvVMIc9EdGE6teAmAVByyQ9wdMR30GJSRY"
access_key = "171626809-0yyB0z2IMEIsFz7Ao3zWSllocnin25b8C2wy7iRJ"
access_secret = "HW0A6zzBjc018o5SnYfVMmlZvwFeWctnFDA6unnwccin9"


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', tweets = get_tweets)

@app.route("/about")
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@app.route("/features")
def features():
    try:
        return render_template('features.html')
    except TemplateNotFound:
        abort(404)

@app.route("/get-tweets")
def get_tweets(username): 
    
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        
        auth.set_access_token(access_key, access_secret) 
  
        
        api = tweepy.API(auth) 
  
        # 3 tweets to be extracted 
        number_of_tweets=3
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            
            tmp.append(j)  
  
        
        print(tmp) 
  
  
if __name__ == '__main__': 
  
    get_tweets("twitter-handle")




'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''