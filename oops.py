# 1.) class in python
# class Student:
#     name="Tanya Mandloi"

# s1 = Student()
# print(s1.name)    

# # 2.) constructor - invokes automatically wheather wwe create or not 
# class Student:
#     clgName = "Acropolis"
#     def __init__(self, name):
#         self.name = name
#         print("added student inside database...")

#     def welcome(self):
#         print("welcome student")    

# s1 = Student("tanya")
# s1.welcome()
# print(s1.name, s1.clgName)

# s2 = Student("nisha")
# print(s2.name)

#practice question to print average of 3 students
# class Student:
#     @staticmethod
#     def hello():
#         print("hello")

#     def __init__(self, name, marks):
#         self.marks = marks

#     def calculateAvg(self):
#         sum = 0
#         for val in self.marks:
#              sum += val
#         print("hi" , "your avg marks is ", sum/3)

# s1 = Student("tony stark", [100, 90, 80])
# s1.calculateAvg()
# s1.hello()
       

# Que
class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount   
        print("Rs", amount, "was debit")
        print("total amount ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "credited")
        print("total amount", self.balance)


acc1 = Account(10000, 12345)
acc1.debit(500)
acc1.credit(1000)

