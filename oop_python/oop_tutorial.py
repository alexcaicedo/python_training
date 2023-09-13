class Employee:
    
    # num_of_emps = 0
    # raise_amount = 1.05

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # self.wage = wage

        # Employee.num_of_emps += 1
    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@company.com'
    
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.firstname = None
        self.lastname = None

    # def apply_raise(self):
    #     self.wage = int(self.wage * self.raise_amount)
    
    # Class methods
    # @classmethod
    # def set_raise_amount(cls, amount):
    #     cls.raise_amount = amount
    
    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str.split('-')
    #     return cls(first, last, pay)
    
    # Static methods
    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True

    
    # methods with double "_" are called "special" methods or "dunder" methods
    # def __repr__(self):
    #     return f"Employee('{self.firstname}', '{self.lastname}', '{self.wage}')"

    # def __str__(self):
    #     return f'{self.fullname()} - {self.email}'
    
    # def __add__(self, other):
    #     return self.wage + other.wage

# Inherited classes
# class Developer(Employee):
#     raise_amount = 1.10
#     def __init__(self, firstname, lastname, wage, prog_lang):
#         super().__init__(firstname, lastname, wage)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, firstname, lastname, wage, employees=None):
#         super().__init__(firstname, lastname, wage)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
    
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
    
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
    
#     def print_emps(self):
#         for emp in self.employees:
#             print('--->', emp.fullname())

# emp_1 = Employee('Alex', 'Caicedo', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

## Classmethods and Staticmethods
# Employee.set_raise_amount(1.06)
# print(emp_1.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

## Before @classmethod constructor from_string
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

## After @classmethod constructor from_string
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.wage)

# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

## Inherited classes
# dev_1 = Developer('Alex', 'Caicedo', 50000, 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'JavaScript')
# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Developer, Manager))

## Dunder methods
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(3, 2))
# print(str.__add__('a', 'b'))

# print(emp_1 + emp_2)
# print(id(emp_1))

## Property decorators
emp_1 = Employee('John', 'Salchichón')
# emp_1.fullname = 'Corey Schafer'
print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname