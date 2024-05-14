from Execute import *

while True:
    text = input('enter the equation: ')
    result, error = execute(text)

    if (error):
        print(error.as_string())
    else:
        print(result)
        
