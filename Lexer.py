
Digits = '0123456789'
INT		= 'INT'
FLOAT    = 'FLOAT'
PLUS     = 'PLUS'
MINUS    = 'MINUS'
MULTIPLY     = 'Multiply'
DIV      = 'DIV'
LeftPAREN   = 'LeftPAREN'
RightPAREN   = 'RightPAREN'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        # print type then print the value of the type
        if self.value: return f'{self.type}->{self.value}'
        #if the type did not has value just print the type 
        return f'{self.type}'

class Error:
    def __init__(self, errorName, details):
        self.errorName = errorName
        self.details = details
    def as_string(self):
        result  = f'{self.errorName}: {self.details}\n'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character: ', details)

    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.currentChar = None
        self.nextChar()

    def nextChar(self):
        self.pos+=1
        self.currentChar = self.text[self.pos] if self.pos< len(self.text) else None

    def makeToken(self):
        tokens = []
        #check what is the current char is 
        while self.currentChar!=None:
            if self.currentChar in ' \t':
                self.nextChar()
            elif self.currentChar in Digits:
                tokens.append(self.numbers())

            elif self.currentChar == '+':
                tokens.append(Token(PLUS))
                self.nextChar()
            elif self.currentChar == '-':
                tokens.append(Token(MINUS))
                self.nextChar()
            elif self.currentChar == '*':
                tokens.append(Token(MULTIPLY))
                self.nextChar()
            elif self.currentChar == '/':
                tokens.append(Token(DIV))
                self.nextChar()
            elif self.currentChar == '(':
                tokens.append(Token(LeftPAREN))
                self.nextChar()
            elif self.currentChar == ')':
                tokens.append(Token(RightPAREN))
                self.nextChar()
            else:
                #error
                char = self.currentChar
                self.nextChar()
                return [], IllegalCharError(char)


        return tokens, None
    def numbers(self):
        isFloat = 0
        numStr = ''
        #check number is integer or float 
        while self.currentChar!=None and self.currentChar in Digits + '.':
            if self.currentChar == '.':
                if(isFloat):
                    break
                isFloat=1
                numStr+='.'
            else:
                numStr+= self.currentChar
            self.nextChar()
        
        if(isFloat):
            return Token(FLOAT, float(numStr))
        else:
            return Token(INT, int(numStr))
        
def execute(text):
    lexer = Lexer(text)
    tokens, error = lexer.makeToken()
    return tokens, error


    


