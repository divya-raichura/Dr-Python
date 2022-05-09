# in our pattern method we were using nested for_while loops and
# printing rows and cols using that, here we are simply printing
# row wise


#  this method is more efficient


import sys
import time

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

try:
    while True:  # The main program loop.
        print(' ' * indent, '********', sep='')
        time.sleep(0.1)  # Pause for_while 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 8:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
