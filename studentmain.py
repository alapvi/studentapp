import studentcontroller as sc
controllerStudent = sc.StudentController()

while True:
    print("STUDENT CRUD")
    print("____________")
    print("1.- Add student")
    print("2.- Delete student")
    print("3.- Modify student")
    print("4.- Search student")
    print("5.- Exit")
    option = int(input("Choose option:"))
    if (option == 5):
        print("Bye!!!!!")
        break
    elif (option == 1):
        print("Adding a new Student!")
        dni = input("DNI:")
        name = input("Name:")
        surname = input("Surname:")
        age = int(input("Age:"))
        city = input("City:")
        province = input("Province:")
        email = input("Email:")
        if controllerStudent.addStudent(dni,name,surname,age,city,province,email):
            print("Student added!!")
        else:
            print("DNI exist!")
    elif (option == 2):
        print("Deleting a Student!")
        dni = input("DNI:")
        student = controllerStudent.delStudent(dni)
        if student != None:
            print("Student deleted!",student.getDni())
        else:
            print("Student by DNI not found!")
        

print("Bye!")
    