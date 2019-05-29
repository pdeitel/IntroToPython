# Section 12.2.1 snippets
from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

blob


# Section 12.2.1 Self Check snippets

# Exercise 3
exercise_blob = TextBlob('This is a TextBlob')

exercise_blob


# Section 12.2.2 snippets
blob.sentences

blob.words


# Section 12.2.2 Self Check snippets

# Exercise 1
from textblob import TextBlob

ex = TextBlob('My old computer is slow. My new one is fast.')

ex.sentences

ex.words


# Section 12.2.3 snippets
blob

blob.tags


# Section 12.2.3 Self Check snippets

# Exercise 2
TextBlob('My dog is cute').tags


# Section 12.2.4 snippets
blob

blob.noun_phrases


# Section 12.2.4 Self Check snippets

# Exercise 1
TextBlob('The red brick factory is for sale').noun_phrases


# Section 12.2.5 snippets

# Getting the Sentiment of a TextBlob
blob

blob.sentiment

# Getting the polarity and subjectivity from the Sentiment Object
%precision 3

blob.sentiment.polarity

blob.sentiment.subjectivity

# Getting the Sentiment of a Sentence 
for sentence in blob.sentences:
    print(sentence.sentiment)


# Section 12.2.5 Self Check snippets

# Exercise 1
from textblob import Sentence

Sentence('The food is not good.').sentiment

Sentence('The movie was not bad.').sentiment

Sentence('The movie was excellent!').sentiment


# Section 12.2.6 snippets
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

blob

blob.sentiment

for sentence in blob.sentences:
    print(sentence.sentiment)
    

# Section 12.2.6 Self Check snippets

# Exercise 1
text = ('The food is not good. The movie was not bad. ' +
        'The movie was excellent!')  

exblob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

for sentence in exblob.sentences:
    print(sentence.sentiment)


# Section 12.2.7 snippets
blob

blob.detect_language()

spanish = blob.translate(to='es')

spanish

spanish.detect_language()

chinese = blob.translate(to='zh')

chinese

chinese.detect_language()

spanish.translate()

chinese.translate() 


# Section 12.2.7 Self Check snippets

# Exercise 1
blob = TextBlob('Today is a beautiful day.')

french = blob.translate(to='fr')

french

french.detect_language()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
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
