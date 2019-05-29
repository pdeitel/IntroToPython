# Section 11.4 snippets
# Note that the self check #3 is included here as it
# continues the section's IPython session.

# Function fibonacci 
def fibonacci(n):
    if n in (0, 1):  # base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Testing Function fibonacci
for n in range(41):
    print(f'Fibonacci({n}) = {fibonacci(n)}')

# Self Check Exercise 3
def iterative_fibonacci(n):
    result = 0
    temp = 1
    for j in range(0, n):
        temp, result = result, result + temp
    return result

%timeit fibonacci(32)

%timeit iterative_fibonacci(32)

%timeit fibonacci(33)

%timeit iterative_fibonacci(33)

%timeit fibonacci(34)

%timeit iterative_fibonacci(34)





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
