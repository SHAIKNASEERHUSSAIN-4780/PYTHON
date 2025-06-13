import pickle
import sys
sys.path.append('Python')
from student import Student
def textToObject(source, destination):
    '''
    objective: To convert text data in source file to data in the form of Student objects
    and write to destination file
    Input Parameters: source, destination - string
    Return Value: None
    '''
    f1 = open(source, 'r')
    f2 = open(destination, 'wb')
    line = f1.readline()
    while line != '':
        lst = line.split(',')
        student = Student(int(lst[0]), lst[1], float(lst[2]))
        pickle.dump(student, f2)
        line = f1.readline()
    f1.close()
    f2.close()
def objectToText(source, destination):
    '''
    Objective: To convert Student object data in source file to text data and write to 
    destination file
    Input Parameters: source, destination - string
    Return Value: None
    '''
    f1 = open(source, 'rb')
    f2 = open(destination, 'w')
    try:
        while True:
            student = pickle.load(f1)
            line = str(student.rollNo) + ',' + student.name + ',' + str(student.marks) + '\n'
            f2.write(line)
    except EOFError:
        # Exception is raised when we attempt to read even after all objects have been read
        pass
    f1.close()
    f2.close()