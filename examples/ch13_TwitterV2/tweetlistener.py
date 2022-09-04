# tweetlistener.py
"""StreamListener subclass that processes tweets as they arrive."""
from deep_translator import GoogleTranslator
import tweepy

class TweetListener(tweepy.StreamingClient):
    """Handles incoming Tweet stream."""

    def __init__(self, bearer_token, limit=10):
        """Create instance variables for tracking number of tweets."""
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
        
        # GoogleTranslator object for translating tweets to English 
        self.translator = GoogleTranslator(source='auto', target='en')

        super().__init__(bearer_token, wait_on_rate_limit=True)  

    def on_connect(self):
        """Called when your connection attempt is successful, enabling 
        you to perform appropriate application tasks at that point."""
        print('Connection successful\n')

    def on_response(self, response):
        """Called when Twitter pushes a new tweet to you."""
        
        try:
            # get username of user who sent the tweet
            username = response.includes['users'][0].username
            print(f'Screen name: {username}')
            print(f'   Language: {response.data.lang}')
            print(f' Tweet text: {response.data.text}')

            if response.data.lang != 'en' and response.data.lang != 'und':
                english = self.translator.translate(response.data.text)
                print(f' Translated: {english}')

            print()
            self.tweet_count += 1 
        except Exception as e:
            print(f'Exception occured: {e}')
            self.disconnect()
            
        # if TWEET_LIMIT is reached, terminate streaming
        if self.tweet_count == self.TWEET_LIMIT:
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
