def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)

try:
    boxprint('*', 15, 5)
    boxprint('O', 10, 4)
    boxprint('**', 10, 4)  # This will raise an exception
    
except Exception as e:
    print("An exception occurred: " + str(e))
    try:
        boxprint("ZZ", 3, 3)
    except Exception as e:
        print("Another exception occurred: " + str(e))
        