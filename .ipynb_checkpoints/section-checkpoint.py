# Operations for Class Section
import pickle
import sys
sys.path.append("\Ptyhon")
from student import Student
class Section:
    def __init__(self):
        '''
        Objective: To initialize data members of objects of class Section
        Input Parameters:
            self (implicit parameter) - object of type Section
        Return Value: None
        '''
        self.records = list()
    def readList(self, source):
        '''
        Objective: To read objects of Studentss class from source file and insrt them to
        list records
        Input Parameters:
            self (implcit parameter) - object of the type Section
            source - string (file name)
        Return Value: None
        '''
        self.records = list()
        f = open(source, 'rb')
        try:
            while True:
                student = pickle.load(f)
                self.records.append(student)
        except EOFError:
            pass
        print(self)
        f.close()
    def writeList(self, destination):
        '''
        Objective: To write objects of Student class in list records to destination file
        Input Parameters:
            self (implicit parameter) - object of the type Section
            destination - string (file name)
        Return Value: None
        '''
        f = open(destination, 'wb')
        for student in self.records:
            pickle.dump(student, f)
        f.close()
    def insertEnd(self, rollNo, name, marks):
        '''
        Objective: To insert a student record of type Student to list records
        Input Parameters:
            self (implict parameter) - object of the type Section
            rollNo, marks - numberic
            name - string
        Return Value: string : indicates whether the record is successfully inserted
        '''
        student = Student(rollNo, name, marks)
        if student.rollNo not in [s.rollNo for s in self.records]:
            self.records.append(student)
            return 'Record inserted succesfully'
        return 'Record cannot be inserted! Duplicate roll no.'
    def isSorted(self):
        '''
        Objective: To determine whether the list records is sorted according to the field
        roll number in increasing order
        Input Parameter: self (implicit parameter) - object of type Section
        Return Value: True if list records is sorted
                        False otherwise
        '''
        for i in range(1, len(self.records)):
            if self.records[i].rollNo < self.records[i-1].rollNo:
                return False
        return True
    def binarySearch(self, rollNo):
        '''
        Objective: To search for a roll number in the sorted list records using binary 
        search
        Input Parameters:
            self (implicit parameter) - object of type Section
            rollNo - numeric(search value)
        Return Value: Index of the matched object, if value is found else None
        Assumption: List records is sorted in ascending order by rollNo
        '''
        if not(self.isSorted()):
            print('List is not sorted')
            return False
        low, high = 0, len(self.records) - 1
        while low <= high:
            mid = (low + high)//2
            if self.records[mid].rollNo == rollNo:
                return mid
            elif rollNo < self.records[mid].rollNo:
                high = mid - 1
            else:
                low = mid + 1
        return None
    def linearSearch(self, rollNo):
        '''
        Objective: To search for a roll number in list of records using linear search
        Input Parameters:
            self (implicit parameter) - object of type Section
            rollNo - Numberic(search value)
        Return Value: Index of the matched object, if value is found else None
        '''
        for i in range(0, len(self.records)):
            if self.records[i].rollNo == rollNo:
                return i
        return None
    def insertionSort(self):
        '''
        Objective: To sort the list in ascending order of rollNo using insertion sort
        Input Parameter:
            self (implicit parameter) - object of type Selection
        Return Value: None
        '''
        for i in range(1, len(self.records)):
            temp = self.records[i]
            j = i - 1
            while j >= 0 and self.records[j].rollNo > temp.rollNo:
                self.records[j + 1] = self.records[j]
                j = j-1
            self.records[j + 1] = temp
    def sortedInsert(self, rollNo, name, marks):
        '''
        Objective: To insert a student record of type Student to sorted list records
        Input Parameters:
            self (implicit parameter) - object of type Parameter
            rollNo, marks - numeric value
        Return Value: string (indicates whether the record is successfully inserted)
        Assumption: List is already sorted with respect to roll number field
        '''
        student = Student(rollNo, name, marks)
        if len(self.records) == 0:
            self.records.append(student)
            return 'Record inserted successfully '
        low, high = 0, len(self.record) -1
        mid = (low + high)//2
        while low <= high:
            mid = (low + high)//2
            if self.records[mid].rollNo == rollNo:
                return 'Record cannot be inserted! Duplicacy in roll no. '
            elif rollNo < self.records[mid].rollNo:
                high = mid - 1
            else:
                low = mid + 1
        if self.records[mid].rollNo < rollNo:
            self.records.insert(mid + 1, student)
        else:
            self.records.insert(mid, student)
            return 'Record inserted successsfully'
            
    def delete(self, rollNo):
        '''
        Objective: To remove a student record of type Student from list records having 
        roll number rollNo
        Input Parameters:
            self (implicit parameter) - object of type Section
            rollNo - numeric
        Return Value: string (indicates whether the record is successfully deleted)
        '''
        for i in range(0, len(self.records)):
            if self.records[i].rollNo == rollNo:
                del self.records[i]
                return 'Record deleted successfully'
        return 'Record not found'
    def __str__(self):
        '''
        Objective: To return string representation of object of type Section
        Input Parameter: self (implicit parameter) - object of type Section
        Return Value: string
        '''
        str1 = ''
        for i in self.records:
            str1 += Student.__str__(i)
        return str1