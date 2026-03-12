class SchoolManagementSystem:
    def __init__(self):
        self.admittedstudents={}
        self.student_id=1
    def newadmission(self):
        print("Creating New Admission, Please provide the below details.")
        name=input("Enter student name: ")
        age_flag=True
        while age_flag:
            age=int(input("Enter your student age: "))
            if age>=5 and age<=18:
                age_flag=False
            else:
                print("Age must be in between 5 to 18, to receive admission")
        std=input("Enter your student class(1-12): ")
        
        mobile_flag=True
        while mobile_flag:
            mobile=(input("Enter students guardian mobile number: "))
            if len((mobile))==10 and mobile.isdigit():
                mobile_flag=False
            else:
                print("Mobile Number Must Be Atleast 10 digits and only digits.")
        self.admittedstudents[self.student_id]={"name":name,"age":age,"class":std,"mobile":mobile}
        self.student_id+=1
        self.menu()
    def viewstudentdetail(self):
        a=int(input("Enter the Student_Id: "))
        student=self.admittedstudents.get(a)
        if student:
            print(student)
        else:
            print("student not found")
        self.menu()
    def updatestudentinfo(self):
        a=int(input("Enter the Student_Id: "))
        student=self.admittedstudents.get(a)
        if student:
            print("What do u wanna update mobile number or Class or both: ")
            print("Press 1 to update Both Class and Mobile")
            print("Press 2 to update only Class ")
            print("Press 3 to update only Mobile")
            x=int(input("Enter your choice: "))
            if x==1:
                student["class"]=input("Enter your correct Class: ")
                student["mobile"]=input("Enter your correct Mobile: ")
            elif x==2:
                student["class"]=input("Enter your correct Class: ")
            elif x==3:
                student["mobile"]=input("Enter your correct Mobile: ")
            else:
                print("invalid Choice")
        else:
            print("student not found")
        self.menu()

    def removestudent(self):
        a=int(input("Enter the Student_Id: "))
        student=self.admittedstudents.get(a)
        if student:
            self.admittedstudents.pop(a)
            print("Student successfully removed")
        else:
            print("student not found")
        self.menu()
    def menu(self):
        print(self.admittedstudents)
        print("Welcome to Tops Management!")
        print("1. For New Admission")
        print("2. view Admission")
        print("3. update Admission")
        print("4. remove Admission")
        print("5. Exit system")
        choose=int(input("Enter the menu number u wanna select: "))
        if choose==1:
            self.newadmission()
        elif choose==2:    
            self.viewstudentdetail()
        elif choose==3:
            self.updatestudentinfo()
        elif choose==4:
            self.removestudent()
        elif choose==5:
            print("Thank you for Tops Management online portal.")
        else:
            print("Invalid Choice")


student=SchoolManagementSystem()
student.menu()