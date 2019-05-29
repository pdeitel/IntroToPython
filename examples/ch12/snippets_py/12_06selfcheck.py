# Section 12.6 Self Check snippets

# Exercise 2
import spacy

nlp = spacy.load('en')  

from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())

document2 = nlp(Path('Hamlet.txt').read_text())

document1.similarity(document2)

document3 = nlp(Path('Macbeth.txt').read_text())

document1.similarity(document3)

document4 = nlp(Path('KingLear.txt').read_text())

document1.similarity(document4)


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
