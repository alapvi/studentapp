import student as st
class StudentController():
    def __init__(self):
        self.__students = {}
    

    def addStudent(self,dni,name,surname,age,city,province,email):
        if dni not in self.__students:
            student = st.Student(dni,name,surname,age,city,province,email)
            self.__students[dni] = student
            return True
        return False
    
    def delStudent(self,dni):
        if dni in self.__students:
            student = self.__students.pop(dni)
            return student
        return None
