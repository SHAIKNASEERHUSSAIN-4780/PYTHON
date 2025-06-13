from person import Person
from date import MyDate
class Employee(Person):
    nextId = 1001
    employeeCount = 0
    def __init__(self, name, DOB, address, basicSalary, dateOfJoining):
        '''
        Objective: To initialize an object of class Employee
        Input Parameters:
            self (implicit parameter) - object of type Employee
            name, address - string
            DOB - Date of Birth - object of type MyDate
            basicSalary - numeric value
            dateOfJoining - object of type MyDate
        Return Value: None
        '''
        Person.__init__(self, name, DOB, address)
        self.idNum = Employee.nextId
        self.basicSalary = basicSalary
        self.dateOfJoining = dateOfJoining
        Employee.nextId +=1
        Employee.employeeCount +=1
    def getId(self):
        '''
        Objective: To retrieve id of the Employee
        Input Parameter: self (implicit parameter) - object of type Employee
        Return Value: id -numeric value
        '''
        return self.idNum
    def getSalary(self):
        '''
        Objective: To retrieve salary of the Employee
        Input Parameter: self (implicit paramter) - object of type Employee
        Return Value: basicSalary - numeric value
        '''
        return self.basicSalary
    def reviseSalary(self, newSalary):
        '''
        Objective: To update salary of the Employee
        Input Parameter: 
            self (implicit parameter) - object of type Employee
            newSalary - numeric value
        Return value: None
        '''
        self.basicSalary = newSalary
    def getJoiningDate(self):
        '''
        Objective: To retrieve joining date of the Employee
        Input Parameter: self (implicit parameter) - object of type Employee
        Return Value: dateOfJoining - object of type MyDate
        '''
        return self.dateOfJoining
    def __str__(self):
        '''
        Objective: To return string representation of object of type Employee.
        Input Parameter: self (implicit parameter) - object of type Employee
        Return Value: string
        '''
        return Person.__str__(self)+'\nId:'+str(self.getId())+\
        '\nSalary:'+str(self.getSalary())+\
        '\nDate of Joining:'+str(self.getJoiningDate())
    def __lt__(self, other):
        '''
        Objective: To check if id of the first employee is less than the other
        Input Parameter:
            self (implicit parameter) - object of type Employee
            other - object of type Parameter
        Return Value: True if self.getId() < other.getId(), else False
        '''
        return self.getId() < other.getId()
    def __del__(self):
        '''
        Objective: To be invoked on the deletion of an instance of a class Employee
        Input Parameter:
            self (implicit parameter) - object of type Employee
        Return Value: None
        '''
        Person.__del__(self)
        Employee.employeeCount -= 1