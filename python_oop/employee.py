class Employee: 
    DEDUCTION_PERCENT = 0.10
    employee_num = 0
    def __init__(self, name, age, gender, salary):
        
        self.name = name
        self.age = age 
        self.salary = salary 
        self.gender = gender
        Employee.employee_num +=1
    def salary_deduction(self, salary,):
        ans = input(f"Was the employee {self.name} absent ?\n")
        if ans == "yes" or ans == "Yes" or ans == "YES" or ans == "y" or ans =="Y" or ans =="true"or ans== "True" or ans == "TRUE" :
            cal = salary*self.DEDUCTION_PERCENT
            deduct = salary-cal
            return deduct
        else: 
            return "No deduction made"
    def full_info(self):
        print(f"Employee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Gender: {self.gender}\nEmployee Salary: {self.salary}\n")
    def __str__(self):
        return f"Employee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Gender: {self.gender}\nEmployee Salary: {self.salary}\n"

emp1 = Employee("Malak",22,"Female", 25000)
print(emp1.full_info())
print(Employee.employee_num)
print("=======Printing an object using __str__ ========")
print(emp1)
print("*! we notice that the None keyword is removed due to built in return modified using str\n"
      "method and it will no longer return None but the statement it holds in return block\n")
# user = emp1.salary_deduction(emp1.salary)
# if not (emp1.salary == user):
#     print(f"{emp1.full_info()}\nDeduction Salary: {user}")
print("=======Printing an object using __str__ ========")
class Strings:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
    def __str__(self):
        return f"{self.name}\n{self.hobby}"

u = Strings("Malak", "ML coding")
print(u)
