import sys
class MyTime:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        '''
        Objective: To initialize data members of an object of class MyTime
        Input Parameters:
            self (implicit parameter) - object of type MyTime
            hours, minutes, seconds - numeric value
        Return Value: None
        '''
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
    def setHours(self, hours):
        '''
        Objective: To set hours of object of class MyTime
        Input Parameters:
            self (implicit parameter) - object of type MyTime
            hours - numeric value
        Return Value: None
        '''
        if hours >=  0 and hours <=23:
            self.hours = hours
        else:
            print("Invlaid value for hours")
            sys.exit()
    def setMinutes(self, minutes):
        '''
        Objective: To set minutes of object of class MyTime
        Input Parameters:
            self (implicit parameter) - object of type MyTime
            minutes - numeric value
        Return Value: None
        '''
        if minutes >=0 and minutes <=59:
            self.minutes = minutes
        else:
            print("Invalid value for minutes")
            sys.exit()
    def setSeconds(self, seconds):
        '''
        Objective: To set seconds of object of class MyTime
        Input Parameters:
            self (implicit parameter) - object of type MyTime
            seconds - numeric value
        Return Value: None
        '''
        if seconds >= 0 and seconds <= 59:
            self.seconds = seconds
        else:
            print("Invalid value for seconds")
            sys.exit()
    def __str__(self):
        '''
        Objective: To return string representation of object of type MyTime
        Input Parameter:
            self (implicit parameter) - object of type MyTime
        Return Value: string
        '''
        if self.hours <= 9:
            hours = '0'+ str(self.hours)
        else:
            hours = str(self.hours)
        if self.minutes <= 9:
            minutes = '0'+str(self.minutes)
        else:
            minutes = str(self.minutes)
        if self.seconds <= 9:
            seconds = '0'+ str(self.seconds)
        else:
            seconds = str(self.seconds)
        return hours +  ':' + minutes + ':' + seconds # hh:mm:ss format