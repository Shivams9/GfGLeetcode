class stack:
    def __init__(self):
        self.data = []
            
    def push(self,value):
        self.data.append(value)
    def empty(self):
        if len(self.data) <= 0:
            return True
        else:
            return False
    def pop(self):
        if self.empty():
            return None
        else:
            return self.data.pop()

