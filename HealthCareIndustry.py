class ClinicAppointment:
    def __init__(self):
        self.slots=["10am", "11am", "12pm", "2pm", "3pm"]
        self.doctors=["Ram", "Shyaam", "Shiva", "Vishnu", "Krishna"]
        self.appointments=[]
    
    def bookappointment(self):
        print("*"*100)
        print("New Appointment is getting created")
        print("*"*100)
        name=input("Enter your name: ")
        age=input("Enter your age: ")
        mobile=input("Enter your mobile number: ")
        print("choose your doctor from the list Given Below: ")
        for i in range(5):
            print(i+1, ". ",self.doctors[i])
        doctor=int(input("Enter your prefered doctor number: "))
        print("choose your slot from the list Given Below: ")
        for i in range(5):
            print(i+1, ". ",self.slots[i])
        slot=int(input("Enter your prefered slot number: "))
        count=0
        for i in self.appointments:
            if i["doctor"]==self.doctors[doctor-1] and i["slot"]==self.slots[slot-1]:
                count+=1
        if count>=3:
            print("*"*100)
            print("doctor for this slot is not available, please choose different slot. Try again")
            print("*"*100)
            self.menu()
        appointment={"name":name,"age":age,"mobile":mobile,"doctor":self.doctors[doctor-1],"slot":self.slots[slot-1]}
        self.appointments.append(appointment)
        print("*"*100)
        print("Appointment created successfully.")
        print("*"*100)
        self.menu()

    def viewappointment(self):
        m=(input("Please Enter your mobile Number: "))
        Found=True
        for i in self.appointments:
            if i["mobile"]==m:
                print("*"*100)
                print("your appointment is at ",i["slot"], "with doctor: ", i["doctor"])
                Found=False
                print("*"*100)
        if Found:
            print("*"*100)
            print("No Appointment Found")
            print("*"*100)
        self.menu()
    def cancelappointment(self):
        m=(input("Please Enter your mobile Number: "))
        Found=True
        for i in self.appointments:
            if i["mobile"]==m:
                self.appointments.remove(i)
                print("*"*100)
                print("Your Appointment is successfully cancelled")
                Found=False
                print("*"*100)
        if Found:
            print("*"*100)
            print("No Appointment Found")
            print("*"*100)
        self.menu()
    def menu(self):
        print("*"*100)
        print("Appointments just for information: ",self.appointments)
        print("*"*100)
        print("welcome to Apollo Hospital")
        print("*"*100)
        print("1 : select 1 to create a new appointment.")
        print("2 : select 2 to view your appointment.")
        print("3 : select 3 to cancel your appointment.")
        print("4 : select 4 to Exit System.")
        choose=int(input("Enter the menu number u wanna select: "))
        if choose==1:
            self.bookappointment()
        elif choose==2:    
            self.viewappointment()
        elif choose==3:
            self.cancelappointment()
        elif choose==4:
            print("Thank you for using Apollo hospital online portal.")
        else:
            print("Invalid Choice")
            self.menu()
        print("*"*40)

appt=ClinicAppointment()
appt.menu()