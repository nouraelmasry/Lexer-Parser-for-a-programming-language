class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        # print type then print the value of the type
        if self.value: return f'{self.type}->{self.value}'
        #if the type did not has value just print the type 
        return f'{self.type}'