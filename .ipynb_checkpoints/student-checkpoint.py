# Student class
class Student:
    def __init__(self, rollNo, name, marks):
        '''
        Objective: To initialize data memebers of object of type Student
        Input Parameter:
            self (implicit parameter) - object type of Student
            rollNo, marks - numeric value
            name - string
        Return Value: None
        '''
        self.rollNo = rollNo
        self.name = name
        self.marks = marks
    def __str__(self):
        '''
        Objective: To return String representation of object of type Student
        Input Parameter: self (implicit parameter) - object type of Student
        Return Value: string
        '''
        return 'Roll No: ' + str(self.rollNo) + ', Name: ' + self.name + ', Marks: ' +\
        str(self.marks) + '\n'