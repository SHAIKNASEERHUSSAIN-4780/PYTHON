import sys
sys.path.append("Python")
from node import Node
class LinkedQueue:
    def __init__(self):
        '''
        Objective: To initialize an object of class LinkedQueue
        Input Parameter: self (implicit parameter) - object of type LinkedQueue
        Return Value: None
        '''
        self.front = self.rear = None
    def enqueue(self, value):
        '''
        objective: To insert a node in the queue at teh rear end
        Input Parameter:
            self (implicit paramter) - object of type LinkedQueue
            value - data for the node to be inserted
        Return Value: None
        '''
        if self.front is None:
            self.front = self.rear = Node(value)
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
    def dequeue(self):
        '''
        Objective: To remove a value from the front of LinkedQueue
        Input Parameter: self (implicit parameter) - object of type LinkedQueue
        Return Value: Value of the data attribute of the front node if the queue is not 
        empty, None otherwise
        '''
        if self.front is None: # Empty list
            print("Queue Underflow")
            return None
        else:
            temp = self.front
            value = self.front.data
            self.front = self.front.next
            del temp
            return value
    def isEmpty(self):
        '''
        Objective: To determine whether the queue is empty
        Input paramter: self (implicit parameter) - object of type LinkedQueue
        Return Value: True if the queue is empty, otherwise False
        '''
        return self.front is None
    def getFront(self):
        '''
        Objective: To return value at the front of LinkedQueue
        Input Parameter: self (implicit parameter) - object of type LinkedQueue
        Return Value: Value of the data attribute of the front node of the queue if the 
        queu is not empty, None otherwise
        '''
        if not(self.isEmpty()):
            return self.front.data
        else:
            print("Queue Empty")
            return None
    def __str__(self):
        '''
        objective: To return string representation of object of type Queue
        Input Paramter: self (implcit paramter) - object of type LinkedQueue
        REturn Value: string
        '''
        temp = self.front
        result = ''
        if temp != None:
            while temp.next != None:
                result += str(temp.data) + '->'
                temp = temp.next
            result += str(temp.data)
        else:
            result = "Empty Queue"
        return result