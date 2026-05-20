'''NET SALARY(Total) CALCULATION OF AN EMPLOYEE 
Accept name and basic salary of an employee
HRA=10% of basic salary
DA=8% of basic salary
PF=12% of basic salary
Net Salary=Basic Salary+HRA+DA-PF'''
'''Employee_name=input("Enter Employee Name:")
Basic_salary=float(input("Enter Basic Salary:"))
HRA=0.10*Basic_salary
DA=0.08*Basic_salary
PF=0.12*Basic_salary
Net_Salary=Basic_salary+HRA+DA-PF
a=(f"the net salary of {Employee_name} is {Net_Salary}")
print(a)
print("|Employee_name|Basic_salary|HRA|DA|PF|Net_Salary|")
print("-"*25)
print(f"|{Employee_name:^15}|{Basic_salary:^15}|{HRA:^4}|{DA:^4}|{PF:^4}|{Net_Salary:^15}|")
print("-"*25)'''




name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
hra = 0.10 * basic_salary
da = 0.08 * basic_salary
pf = 0.12 * basic_salary
net_salary = basic_salary + hra + da - pf   
print("\n")
print("=" * 40)
print(f"{'EMPLOYEE SALARY SLIP':^40}")
print("=" * 40)

print(f"Employee Name      : {name}")
print(f"Basic Salary       : ₹{basic_salary:.2f}")
print(f"HRA (10%)          : ₹{hra:.2f}")
print(f"DA (8%)            : ₹{da:.2f}")
print(f"PF (12%)           : ₹{pf:.2f}")

print("-" * 40)
print(f"Net Salary         : ₹{net_salary:.2f}")
print("=" * 40)
