# 13.13.2 Initiating Stream Processing

# Authenticating
import tweepy

import keys

# Creating a TweetListener
from tweetlistener import TweetListener

tweet_listener = TweetListener(
    bearer_token=keys.bearer_token, limit=3)

# Redirecting Standard Error Stream to Standard Output Stream
import sys

sys.stderr = sys.stdout

# Deleting Existing Stream Rules
rules = tweet_listener.get_rules().data

rule_ids = [rule.id for rule in rules]

tweet_listener.delete_rules(rule_ids)    

# Creating and Adding a Stream Rule
filter_rule = tweepy.StreamRule('football')

tweet_listener.add_rules(filter_rule)

# Starting the Tweet Stream
tweet_listener.filter(
    expansions=['author_id'], tweet_fields=['lang'])

# Stream connection closed by Twitter

# Asynchronous vs. Synchronous Streams

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
