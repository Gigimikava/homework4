# #N1
# class People:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def get_email(self):
#         print (f"{self.firstname}.{self.lastname}.school@edu.ge")
# class Lecturer(People):
#     def __init__(self,firstname,lastname,salary):
#         super().__init__(firstname, lastname)
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#     def get_email(self):
#         print (f"{self.firstname}.{self.lastname}@edu.ge")
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         super().__init__(firstname,lastname)
#         self.firstname = firstname
#         self.lastname = lastname
#         self.courses = list(courses)
#     def get_email(self):
#         print(f"{self.firstname}.{self.lastname}.1@edu.ge")
# p1 = People("gigi","mikava")
# p1.get_email()
# l1 = Lecturer("ioseb","stalini",1800)
# l1.get_email()
# s1 = Student("aldus","manucius",["math","english", "history"])
# s1.get_email()


# #N3
# class Person:
#     def __init__(self,firstname,lastname,age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#     def __str__(self):
#         return f"hi {self.firstname} {self.lastname} . your age is {self.age}"
# class Employee:
#     def __init__(self,profession,monthly_salary,working_hours):
#         self.profession = profession
#         self.monthly_salary = monthly_salary
#         self.working_hours = working_hours
#     def hourly_salary(self):
#         return f"you have {self.monthly_salary / 30 / self.working_hours} GEl per hour"
# class Doctor(Person,Employee):
#     def __init__(self,firstname,lastname,age,profession,monthly_salary,working_hours):
#        Person.__init__(self,firstname, lastname , age)
#        Employee.__init__(self,profession,monthly_salary,working_hours)
#     def perform_operation(self):
#         return "operation performed succesfully"
# d1 = Doctor("gigi","mikava",24,"doctor",9000,10)
# print(d1)
# print(d1.hourly_salary())
# print(d1.perform_operation())






