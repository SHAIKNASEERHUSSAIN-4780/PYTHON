# Date Class
import sys
class MyDate:
    '''
    MyDate: A simple implementation of date as a class.
    '''
    def __init__(self, day = 1, month = 1, year = 2000):
        '''
        Objective: To initialize data members of object MyDate
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            day, month, year - int
        Return Value : None
        '''
        if not(isinstance(day, int) and isinstance(month, int) and isinstance(year, int)):
            print("Invalid data provided for date")
            sys.exit()
        if month>0 and month<=12:
            self.month = month
        else:
            print("Invalid data provided for month")
            sys.exit()
        if year>1990:
            self.year = year
        else:
            print("Invalid data provided for year. Year should be greater than 1990")
            sys.exit()
        self.day = self.checkDay(day) # Validate day
    def checkDay(self, day):
        '''
        Objective: To validate day component
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            day - numeric
        Return Value: day if it is correct else message 'Invalid value for the day' is
                    printed and the program is terminated
        '''
        # currentYear: list of no of days in months of current year
        if self.year%400 ==0 or (self.year%100!=0 and self.year%4 ==0): #  if leap year
            currentYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            currentYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (day > 0 and day <= currentYear[self.month - 1]):
            return day
        else:
            print("Invalid value for day")
            sys.exit()
    def __str__(self):
        '''
        Objective: To return string representation of object
        Input parameter:
            self (implicit parameter) - object of type MyDate
        Return Value: string
        '''
        # Approach: Use dd-mm-yyyy format
        if self.day <=9:
            day = '0' + str(self.day)
        else:
            day = str(self.day)
        if self.month <=9:
            month = '0' +str(self.month)
        else:
            month = str(self.month)
        return day+'-'+month+'-'+str(self.year)
    # Method to check whether two dates or equal or not
    def __eq__(self, other):
        '''
        Objective: To compare two MyDate objects for equality
        Input Parameters:
            self (implicit parameter) - object of type MyDate
            other - object of type MyDate
        Return Value: True if equal else False
        '''
        # check for equality of year, month, day
        if isinstance(other, MyDate):
            return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)
        else:
            print("Type Mismatch")
            sys.exit()
    # Method to sort the dates in ascending order
    def __lt__(self, other):
        '''
        Objective: To compare two MyDate objects
        Input Parameter:
            self (implicit parameter) - object of type MyDate
            other - object of type MyDate
        Return Value: True if value of first MyDate object is less than second, else False
        '''
        if not isinstance(other, MyDate):
            raise TypeError("Comparison is only supported between MyDate objects.")
    
        # Simplified comparison using tuple
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)