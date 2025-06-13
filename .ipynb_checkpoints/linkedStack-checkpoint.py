from node import Node
class LinkedStack:
    def __init__(self):
        '''
        Objective: To initialize a LinkedStack object
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: None
        '''
        self.top = None
    def push(self, value):
        '''
        Objective: To insert a node on top os the stack
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: None
        '''
        if self.top is None:
            self.top = Node(value)
        else:
            temp = Node(value)
            temp.next = self.top
            self.top = temp
    def pop(self):
        '''
        Objective: To remove a node from the top of stack
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: value of the data attribute of the Top element of the stack if stack 
        if not empty, otherwise None
        '''
        if self.top is None: # Empty List
            print("Stack Underflow")
            return None
        else:
            temp = self.top
            value = self.top.data
            self.top = self.top.next
            del temp
            return value
    def isEmpty(self):
        '''
        Objective: To determine whether the stack is empty
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: True if the stack is empty, Fasle otherwise
        '''
        return self.top is None
    def getTop(self):
        '''
        Objective: To return top element of the stack
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: value of the data attributes of the Top element of the stack if stack
        is not empty, otherwise None
        '''
        if not(self.isEmpty()):
            return self.top.data
        else:
            print("Stack Empty")
            return None
    def __str__(self):
        '''
        Objective: To return striing representation of a LinkedStack
        Input Parameter: self (implicit parameter) - object of type LinkedStack
        Return Value: string
        '''
        temp = self.top
        result = ''
        if temp != None:
            while temp.next != None:
                result += str(temp.data) + '->'
                temp = temp.next
            result += str(temp.data)
        else:
            result = "Empty Stack"
        return result