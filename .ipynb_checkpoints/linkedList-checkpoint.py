from node import Node
class LinkedList:
    def __init__(self):
        '''
        Objective: To initialize object of class LinkedList
        Input Parameter: self (implicit parameter) - object of type LinkedList
        Return Value: None
        '''
        self.head = None
    def insertBegin(self, value):
        '''
        Objective: To insert a node at the beginning of LinkedList
        Input Parameter:
            self (implicit parameter) - object of type LinkedList
            value - data for the node to be inserted
        Return Value: None
        '''
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        print("Value inserted! !")
    def delBegin(self):
        '''
        Objective: To delete a node from the beginning of LinkedList
        Input Parameter:
            self (implicit parameter) - Object of type LinkedList
        Return Value: Value in the deleted node
        '''
        if self.head is None: # Empty List
            print("Empty List")
            return None
        else:
            temp = self.head
            value = self.head.data
            self.head = self.head.next
            del temp
            return value
    def delVal(self, value):
        '''
        Objective: To delete a particular value from LinkedList
        Input Parameters:
            self (implicit parameter) - object of type LinkedList,
            value - data for the node to be deleted
        Return Value: value deleted
        '''
        if self.head is None: # Empty List
            print("Empty List")
            return
        if self.head.data == value: # First element is to be deleted
            temp = self.head
            self.head = self.head.next
            del temp
            print("Value Deleted! !")
        else:
            current = self.head
            prev = None
            while current != None and current.data != value:
                prev = current
                current = current.next
            if current != None:
                prev.next = current.next
                del current
                print("Value", value, "Deleted! !")
            else:
                print("Value not Found! !")
    def __str__(self):
        '''
        Objective: To return string representation of an object of type LinkedList
        Input Parameter: self (implicit parameter) - object of type LinkedList
        Return alye: string
        '''
        current = self.head
        result = ''
        if current != None:
            while current.next is not None:
                result += str(current.data)+ '->'
                current = current.next
            result += str(current.data)
        else:
            result = "Empty List"
        return result