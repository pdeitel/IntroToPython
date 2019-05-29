# Section 11.3 snippets
# Note that the self check #5 is included here as it
# continues the section's IPython session.

def factorial(number):
    """Return factorial of number."""
    if number <= 1:
        return 1
    return number * factorial(number - 1)  # recursive call
    
for i in range(11):
    print(f'{i}! = {factorial(i)}')

# Self Check Exercise 5
factorial(50)


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
