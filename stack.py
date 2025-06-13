class Stack:
    def __init__(self):
        '''
        Objective: To initialize data members of the Stack
        Input Parameter:
            self (implicit parameter) - object of type Stack
        Return Value: None
        '''
        self.values = list()
    def push(self, element):
        '''
        Objective: To put element on top of the stack
        Input Parameters:
            self (implicit parameter) - object of type Stack
            element - value to be inserted
        Return Value: None
        '''
        self.values.append(element)
    def isEmpty(self):
        '''
        Objective: To determine if the stack is empty
        Input Parameter:
            self (implicit parameter) - object of type Stack
        Return Value: True if the stack is empty, else False
        '''
        return len(self.values)  == 0
    def pop(self):
        '''
        Objective: To remove an element from the top of stack
        Input Parameter: self (implicit parameter) - object of type Stack
        Return Value: top element of the stack, if Stack is not empty, else None
        '''
        if not(self.isEmpty()):
            return self.values.pop()
        else:
            print("Stack Underflow")
            return None
    def top(self):
        '''
        Objective: To return top element of the stack
        Input Parameter: self (implicit parameter) - object of type Spack
        Return Value: Top element of the stack, if stack is not empty else None
        '''
        if not(self.isEmpty()):
            return self.values[-1]
        else:
            print("Stack Empty")
            return None
    def size(self):
        '''
        Objective: To return the number of elements in the stack
        Input Parameter: self (implicit parameter) - object of type Stack
        Return Value: number of elements in stack - numeric
        '''
        return len(self.values)
    def __str__(self):
        '''
        Objective: To return string representation of a stack
        Input Parameter: self (implicit parameter) - object of type Stack
        Return Value: string
        '''
        stringRepr = ''
        for i in range(len(self.values) - 1, -1, -1):
            stringRepr += str(self.values[i]) + '\t'
        return stringRepr