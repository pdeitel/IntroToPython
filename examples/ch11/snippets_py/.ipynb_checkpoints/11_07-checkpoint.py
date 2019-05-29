# Section 11.7 snippets

# Linear Search Implementation
def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return -1

import numpy as np

np.random.seed(11)

values = np.random.randint(10, 91, 10)

values

linear_search(values, 78)

linear_search(values, 61)

linear_search(values, 66)




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
