b_salary = int(input("Enter your basic salary : "))

if b_salary>=100000:
    tax = b_salary * 0.05
elif b_salary>=80000:
    tax = b_salary * 0.03
else:
    tax = 0
net_salary = b_salary - tax
print("\nSalary Deatils")
print("---------------------------")
print("Basic salary \t: ",b_salary)
print("Tax \t\t: ",tax)
print("Net Salary \t: ",net_salary)
