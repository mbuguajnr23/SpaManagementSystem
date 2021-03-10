from IDGenerator import IDGenerator

class Employee:
    '''
    employee attributes
        employeeId string
        name string
        phone number string
        specialization string
        salary int
        avg rating int
    '''

    def __init__(self, name='', phone_no='',specialization=''):
         self.__name = name
         self.__phoneNo = phone_no
         self.__specialization = specialization
         self.__employeeId = IDGenerator.generateEmployeeID


    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setPhoneNo(self, phone_no):
        self.__phoneNo = phone_no

    def getPhoneNo(self):
        return self.__phoneNo

    def getSpecialization(self):
        return self.__specialization

    def getemployeeID(self):
        return self.__employeeId

    def __str__(self):
        return self.getname()+ " " +self.getPhoneNo()+ " " + self.getSpecialization()+ " " +str(self.getemployeeID())

