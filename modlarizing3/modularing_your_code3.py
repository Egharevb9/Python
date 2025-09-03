# class student:
#     def __init__(self, name, course, level): #this runs automatically
#         print("creating a new student....")
#         self.name =name
#         self.course =course
#         self.level =level
#         print(f"Student{name} has been created!")
#         # when you create a student,__init__ runs automatically
# kemi = student ("kemi adebayo", "computer science", 300)
# print(kemi.course, kemi.level)


# class NigerianStudent:
#     def __init__(self,name, state, course):
#         print(f" step 1 : Creating student object...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id  = self.generate_id()
#         print(f"step 6 : {self.name} from {self.state_of_origin} is ready!")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
    
# ayo = NigerianStudent("Ayo Daniel", "lagos","street statistics")
# print(ayo.name)
# print(ayo.student_id)


# class Phoneuser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network =network
#         self.airtime = 0
#         print(f"{self.name} joined {self.airtime} network")


#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return(f"{self.name} now has ₦{self.airtime} airtime")
    


#     # creating multiple users
# Abeeb = Phoneuser("Abeeb Bakare","MTN")
# onisemo = Phoneuser("Onisemo Williams ","Airtel")

#     #Each person"s actions  affect only their own account
# print(Abeeb.buy_airtime(500))  # Tunde now has ₦500 airtime
# print(onisemo.buy_airtime(1000)) # Blessing now has ₦1000 airtime
# print(Abeeb.airtime)              # 500 (Tunde's airtime unchanged)
# print(onisemo.airtime)           # 1000 (Blessing's airtime unchanged)


#     # defining Attributes of a student

# class student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.Cgpa = 0.0

#         #creating a stuent object

# fathia = student("fathia abdul", "Biochemistry", 300, "ogun state")

# # Accessing attributes
# print(fathia.name)
# print(fathia.course)
# print(fathia.state_of_origin)
            

# # Instance Attributes - Unique to each object
# student1 =student("Anthony Johnson","Engineering", 200, "ogun")
# student2 =student("fadilat Hassan","Medicine", 400, "lagos")

# print(student1.name)
# print(student2.name)

# #Class Attributes - Shared by all objects of the class

# class student:
#     level = 300
#     gender = "female"
#     university ="federal  university of Technology Akure"
#     def __init__(self, name,course):
#         self.name = name
#         self.course =course

# class Vehicle:
#     name = "Toyota"
#     def __init__(self, model, tyre):
#         self.model = model
#         self.tyre = tyre

# car = Vehicle("camry", 4)
# trailer = Vehicle("pick-up", 12)

# print(car.name)
# print(trailer.name)

# print(car.model)
# print(trailer.model)
# class tech:
#     program_type = "AI- Fellowship"

#     def __init__(self, programing_language, area_specialty):
#         self.programing_language = programing_language
#         self.area_specialty = area_specialty

# developer = tech("python","ai developer")
# print(developer.area_specialty)


# class Vehicle:
#     def __init__(self, model, tyre):
#         self.model = model
#         self.tyre = tyre


# student3 = student("familyman","Ai developer")
# namer = student("ope nla", "Ai Eng")
# print(student3.university)
# print(namer.gender)
# # print(student.university)
# # print(student2.university)
# # print(student2.university)


# class student:
#     def __init__(self, name, course, level):
#         #Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False


#         #method : acton the student can do
#     def pay_school_fees(self):
#         self.fees_paid  = True
#         return f"{self.name} has paid school fees for {self.level} level"


#     # method:  another action
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name}has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"

#     # method: calculates cgpa
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s cgpa is now {self.cgpa:.2f}"
#         return  "no grades provided"
# # using method
# Abiodun = student("Abiodun Akinola", "Gistology",600)
# print(Abiodun.pay_school_fees())
# # print(Abiodun.register_course())
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# #'self' refers to the specific student
# def pay_school_fees(self):
#     return f"{self.name} has paid school fees"

# @classmethod
# def get_university(cls):
#     return cls.university

# @staticmethod
# def academic_calendar():
#     return "Academic session runs from september to july"



class BankAccount:
    def __init__(self,owner , bank_name, balance = 0):
        # ATTRIBUTES -What the account Has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

        # METHODS _ What the account can do
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0 :
            self.balance += amount  #method changes attribute
            return F"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. new balance: ₦{self.balance}"
        return "Invalid deposit amount"
     

    def withdraw(self , amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self .balance:
            self.balance -= amount # method changes attribute
            return f"₦{amount: ,} withdraw from {self.owner}'s account .new balance: ₦{self.balance:,}"
        return "transfer failed: Insufficient funds"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0  and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} withdrawn from {self.owner}'s account. new balance: ₦{self.balance}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """check current balance"""
        return f"{self.owner}'s {}"

    
    