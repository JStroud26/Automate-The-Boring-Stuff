import time, sys
indent = 0 #How many spaces to indent
indent_increasing = 2 

try:
    while True: #Main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10th of a second

        if indent_increasing:
            indent += 1 
            if indent == 20:
                #indent direction
                indent_increasing = False
        else:
            #Decrease the number of spaces
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()