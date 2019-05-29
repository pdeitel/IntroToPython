# ch11utilities.py
"""Utility function for printing a pass of the 
insertion_sort and selection_sort algorithms"""

def print_pass(data, pass_number, index): 
    """Print a pass of the algorithm."""
    label = f'after pass {pass_number}: '
    print(label, end='')

    # output elements up to selected item
    print('  '.join(str(d) for d in data[:index]), 
        end='  ' if index != 0 else '') 

    print(f'{data[index]}* ', end='')  # indicate swap with *

    # output rest of elements
    print('  '.join(str(d) for d in data[index + 1:len(data)]))

    # underline elements that are sorted after this pass_number
    print(f'{" " * len(label)}{"--  " * pass_number}')  

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
