class Student():
    def __init__(self,dni,name,surname,age,city,province,email):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__city = city
        self.__province = province 
        self.__email = email
    
    def getDni(self):
        return self.__dni
    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname
    def getAge(self):
        return self.__age
    
    def setCity(self,city):
        self.__city = city

    def setProvince(self,province):
        self.__province = province
    
    def setEmail(self,email):
        self.__email = email
    

        