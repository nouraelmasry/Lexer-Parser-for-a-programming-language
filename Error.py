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

class InvalidSyntaxError(Error):
		def __init__(self, details=''):
				super().__init__('Invalid Syntax', details)
