# tweetutilities.py
"""Utility functions for interacting with Tweepy objects."""
from deep_translator import GoogleTranslator
from geopy import OpenMapQuest
import keys
import time 
import tweepy

def print_tweets(tweets):
    # translator to autodetect source language and return English
    translator = GoogleTranslator(source='auto', target='en')
    
    """For each tweet in tweets, display the username of the sender
    and tweet text. If the language is not English, translate the text 
    with Deep Translator."""
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        print(f'{user.username}:', end=' ')

        if 'en' in tweet.lang:
            print(f'{tweet.text}\n')
        elif 'und' not in tweet.lang: # translate to English first
            print(f'\n  ORIGINAL: {tweet.text}')
            print(f'TRANSLATED: {translator.translate(tweet.text)}\n')

def get_tweet_content(response):
    """Return dictionary with data from tweet."""
    fields = {}
    fields['username'] = response.includes['users'][0].username
    fields['text'] = response.data.text
    fields['location'] = response.includes['users'][0].location

    return fields

def get_geocodes(tweet_list):
    """Get the latitude and longitude for each tweet's location.
    Returns the number of tweets with invalid location data."""
    print('Getting coordinates for tweet locations...')
    geo = OpenMapQuest(api_key=keys.mapquest_key)  # geocoder
    bad_locations = 0  

    for tweet in tweet_list:
        processed = False
        delay = .1  # used if OpenMapQuest times out to delay next call
        while not processed:
            try:  # get coordinates for tweet['location']
                geo_location = geo.geocode(tweet['location'])
                processed = True
            except:  # timed out, so wait before trying again
                print('OpenMapQuest service timed out. Waiting.')
                time.sleep(delay)
                delay += .1

        if geo_location:  
            tweet['latitude'] = geo_location.latitude
            tweet['longitude'] = geo_location.longitude
        else:  
            bad_locations += 1  # tweet['location'] was invalid
    
    print('Done geocoding')
    return bad_locations


##########################################################################
# (C) Copyright 2022 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
