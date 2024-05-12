import Lexer

while True:
    text = input('enter the equation: ')
    result, error = Lexer.execute(text)

    if (error):
        print(error.as_string())
    else:
        print(result)
        

