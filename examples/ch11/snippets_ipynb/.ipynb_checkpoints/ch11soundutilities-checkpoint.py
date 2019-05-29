# ch11soundutilities.py
"""Functions to play sounds."""
from pysine import sine

TWELFTH_ROOT_2 = 1.059463094359  # 12th root of 2
A3 = 220  # hertz frequency for musical note A from third octave 

def play_sound(i, seconds=0.1):
    """Play a note representing a bar's magnitude. Calculation 
    based on https://pages.mtu.edu/~suits/NoteFreqCalcs.html."""
    sine(frequency=(A3 * TWELFTH_ROOT_2 ** i), duration=seconds)
    
def play_found_sound(seconds=0.1):
    """Play sequence of notes indicating a found item."""
    sine(frequency=523.25, duration=seconds) # C5
    sine(frequency=698.46, duration=seconds) # F5
    sine(frequency=783.99, duration=seconds) # G5

def play_not_found_sound(seconds=0.3):
    """Play a note indicating an item was not found."""
    sine(frequency=220, duration=seconds) # A3
       
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
