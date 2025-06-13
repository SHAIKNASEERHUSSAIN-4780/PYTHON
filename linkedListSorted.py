from node import Node
class LinkedList:
    def __init__(self):
        '''
        Objective: To initialize object of class LinkedList
        Input Parameter: self (implicit parameter) - object of type LinkedList
        Return Value: None
        '''
        self.head = None
    def insertSort(self, value):
        '''
        Objective: To insert a node with given value in the sorted LinkedList
        Input Parameterr:
            self (implicit parameter) - object of type LinkedList
            value - data for the node to be inserted
        Return Valuue: None
        '''
        if self.head is None:
            self.head = Node(value)
        elif value < self.head.data:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        else:
            current = self.head
            prev = None
            while current != None:
                if current.data > value:
                    break
                prev = current
                current = current.next
            temp = Node(value)
            prev.next = temp
            temp.next = current
        print("Value inserted! !")
    def __str__(self):
        '''
        Objective: To return string representation of object of type LinkedList
        Input Parameter: self (implicit paramter) - object of type LinkedList
        Return value: string
        '''
        temp = self.head
        result = ''
        if temp != None:
            while temp.next != None:
                result += str(temp.data)+ '->'
                temp = temp.next
            result += str(temp.data)
        else:
            result = "Empty List"
        return result