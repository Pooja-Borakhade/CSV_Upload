import string
import random

from csv_app.models import Employee

# exec(open(r"D:\Python_practice\csv\csv_upload\db_shell.py").read())
n = 7
Name = ''.join(random.choices(string.ascii_lowercase +
							string.digits, k=n))
print("The generated random string : " + str(Name))

Salary = random.randint(500000,1300000)
print(Salary)
n = 8
Company = ''.join(random.choices(string.ascii_lowercase +
							string.digits, k=n))
print("The generated random string : " + str(Company))

Designation = ''.join(random.choices(string.ascii_lowercase +
							string.digits, k=n))
print("The generated random string : " + str(Designation))

for i in range(1,51):

    a = Employee(name = Name,salary =Salary,company=Company,Designation =Designation)
    a.save()