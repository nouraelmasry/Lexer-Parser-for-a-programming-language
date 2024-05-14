from Variables import *
from Token import *
from Error import *

    
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
            
        tokens.append(Token(EOF))
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
