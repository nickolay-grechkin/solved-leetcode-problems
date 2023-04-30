class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val):
        self.stack.append(val)

        if self.min is None or self.min > val:
            self.min = val

    def pop(self):
        if self.stack:
            removed = self.stack.pop()
            
            if not self.stack:
                self.min = None
            elif removed == self.min:
                self.min = min(self.stack)

    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        if self.stack:
            return self.min