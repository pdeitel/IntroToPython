# locationlistener.py
"""Receives tweets matching a search string and stores a list of
dictionaries containing each tweet's username/text/location."""
import tweepy
from tweetutilities import get_tweet_content

class LocationListener(tweepy.StreamingClient):
    """Handles incoming Tweet stream to get location data."""

    def __init__(self, bearer_token, counts_dict, 
                 tweets_list, topic, limit=10):
        """Configure the LocationListener."""
        self.tweets_list = tweets_list
        self.counts_dict = counts_dict
        self.topic = topic
        self.TWEET_LIMIT = limit
        super().__init__(bearer_token, wait_on_rate_limit=True) 

    def on_response(self, response):
        """Called when Twitter pushes a new tweet to you."""

        # get tweet's username, text and location
        tweet_data = get_tweet_content(response)  
        
        # ignore retweets and tweets that do not contain the topic
        if (tweet_data['text'].startswith('RT') or
            self.topic.lower() not in tweet_data['text'].lower()):
            return

        self.counts_dict['total_tweets'] += 1 # it's an original tweet

        # ignore tweets with no location
        if not tweet_data.get('location'):  
            return

        self.counts_dict['locations'] += 1 # user account has location
        self.tweets_list.append(tweet_data) # store the tweet
        print(f"{tweet_data['username']}: {tweet_data['text']}\n")

        # if TWEET_LIMIT is reached, terminate streaming
        if self.counts_dict['locations'] == self.TWEET_LIMIT:
            self.disconnect()



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
