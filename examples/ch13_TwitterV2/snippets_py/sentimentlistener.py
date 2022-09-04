# sentimentlisener.py
"""Searches for tweets that match a search string and tallies 
the number of positive, neutral and negative tweets."""
import keys
import preprocessor as p 
import sys
from textblob import TextBlob
import tweepy

class SentimentListener(tweepy.StreamingClient):
    """Handles incoming Tweet stream."""

    def __init__(self, bearer_token, sentiment_dict, topic, limit=10):
        """Configure the SentimentListener."""
        self.sentiment_dict = sentiment_dict
        self.tweet_count = 0
        self.topic = topic
        self.TWEET_LIMIT = limit
        
        # set tweet-preprocessor to remove URLs/reserved words
        p.set_options(p.OPT.URL, p.OPT.RESERVED) 
        super().__init__(bearer_token, wait_on_rate_limit=True)

    def on_response(self, response):
        """Called when Twitter pushes a new tweet to you."""

        # if the tweet is not a retweet
        if not response.data.text.startswith('RT'):
            text = p.clean(response.data.text) # clean the tweet

            # ignore tweet if the topic is not in the tweet text
            if self.topic.lower() not in text.lower():
                return

            # update self.sentiment_dict with the polarity
            blob = TextBlob(text)
            if blob.sentiment.polarity > 0:
                sentiment = '+'
                self.sentiment_dict['positive'] += 1 
            elif blob.sentiment.polarity == 0:
                sentiment = ' '
                self.sentiment_dict['neutral'] += 1 
            else:
                sentiment = '-'
                self.sentiment_dict['negative'] += 1 

            # display the tweet
            username = response.includes['users'][0].username
            print(f'{sentiment} {username}: {text}\n')

            self.tweet_count += 1 # track number of tweets processed

            # if TWEET_LIMIT is reached, terminate streaming
            if self.tweet_count == self.TWEET_LIMIT:
                self.disconnect()

def main():
    # get search term and number of tweets
    search_key = sys.argv[1]
    limit = int(sys.argv[2]) # number of tweets to tally
    
    # set up the sentiment dictionary
    sentiment_dict = {'positive': 0, 'neutral': 0, 'negative': 0}

    # create the StreamingClient subclass object
    sentiment_listener = SentimentListener(keys.bearer_token, 
        sentiment_dict, search_key, limit)

    # redirect sys.stderr to sys.stdout
    sys.stderr = sys.stdout

    # delete existing stream rules
    rules = sentiment_listener.get_rules().data
    rule_ids = [rule.id for rule in rules]
    sentiment_listener.delete_rules(rule_ids)    

    # create stream rule
    sentiment_listener.add_rules(
        tweepy.StreamRule(f'{search_key} lang:en'))
    
    # start filtering English tweets containing search_key
    sentiment_listener.filter(expansions=['author_id'])

    print(f'Tweet sentiment for "{search_key}"')
    print('Positive:', sentiment_dict['positive'])
    print(' Neutral:', sentiment_dict['neutral'])
    print('Negative:', sentiment_dict['negative'])

# call main if this file is executed as a script
if __name__ == '__main__':
    main()

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
