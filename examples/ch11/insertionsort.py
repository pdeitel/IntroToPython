# insertionsort.py
"""Sorting an array with insertion sort."""
import numpy as np
from ch11utilities import print_pass

def insertion_sort(data):
    """Sort an array using insertion sort."""
    # loop over len(data) - 1 elements      
    for next in range(1, len(data)):
        insert = data[next]  # value to insert 
        move_item = next  # location to place element

        # search for place to put current element         
        while move_item > 0 and data[move_item - 1] > insert:  
            # shift element right one slot
            data[move_item] = data[move_item - 1]         
            move_item -= 1                                      
                                              
        data[move_item] = insert  # place inserted element 
        print_pass(data, next, move_item)  # output pass of algorithm

def main(): 
    data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    insertion_sort(data) 
    print(f'\nSorted array: {data}\n')

# call main if this file is executed as a script
if __name__ == '__main__':
    main()



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
