
class Queue:
    def __init__(self):
        '''
        Objective: To initialize data members of object of type Queue
        Input Parameter: self (implicit parameter) - object of type Queue
        Return Value: None
        '''
        self.values = list()
    def enqueue(self, element):
        '''
        Objective: To insert an element at the rear end
        Input Parameters: 
            self (implicit parameter) - object of type Queue
            element - value to be inserted
        Return Value: None
        '''
        self.values.append(element)
    def dequeue(self):
        '''
        Objective: To remove an element from the front of queue
        Input Parameter:
            self (implicit parameter) - object of type Queue
        Return Value: Front element of the queue, if queue is not empty, else none
        '''
        if not(self.isEmpty()):
            return self.values.pop(0)
        else:
            print("Queue underflow")
            return None
    def isEmpty(self):
        '''
        Objective: To determine whether the queue is empty
        Input Parameter:
            self (implicit parameter) - object of type Queue
        Return Value: True if the queue is empty else False
        '''
        return len(self.values) == 0
    def front(self):
        '''
        Objective: To return element at the front of queue
        Input Parameter:
            self (implicit parameter) - object of type Queue
        Return Value: Front element of the queue, if queue is not empty, else None
        '''
        if not(self.isEmpty()):
            return self.values[0]
        else:
            print('Queue Empty')
            return None
    def size(self):
        '''
        Objective: To return no.of elements in the queue
        Input Parameter:
            self (implicit parameter) - object of type Queue
        Return Value: number of elements in queue - numeric
        '''
        return len(self.values)
    def __str__(self):
        '''
        )bjective: To return string representation of object of type Queue
        Input Parameter: self (implicit parameter) - object of typw Queue
        Return Value: string
        '''
        stringRepr = ''
        for i in self.values:
            stringRepr += str(i) + '\t'
        return stringRepr