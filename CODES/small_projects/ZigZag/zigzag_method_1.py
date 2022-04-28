import sys
import time

try:
    user = str(input("chalu kare? y [yes] / n [no] : ")).lower()
    if user == 'y':
        try:
            while True:
                indentation = 0
                for i in range(8):
                    indentation += 1
                    print(' ' * indentation, '********', sep='')
                    time.sleep(0.1)
                for i in range(8):
                    indentation -= 1
                    print(' ' * indentation, '********', sep='')
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print("hogaya masti... itna hi? kya yar")
            sys.exit()
    else:
        print("kya yar why would someone do that, khali fukat masti...")
except KeyboardInterrupt:
    print("\nkya yar why would someone do that")
