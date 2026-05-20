'''Write a python program to check whether a given number is perfect square or not..'''
'''num=int(input("Enter the Num:"))
sr=int(num**0.5)
num1=sr*sr
if num1==num :
    print("yes")
else:
    print("No")'''

'''Write a python program that accepts valid 10 digit number is it valid or not'''
'''mobile_no=eval(input("mobile_no : "))
if isinstance(mobile_no,int) and len(str(mobile_no))==10:
    print("The above mobile number is valid")
else:
    print("The above mobile number is invalid")'''

'''write a program to print square of any  number'''
'''num=int(input("Enter the number :"))
squr=num**2
print(squr)'''

numbers=[5,8,15,20]
'''write a program  to print a square of each number'''
'''for num in numbers:
    print(f"Square of numbers {num} is {num**2}")'''

numbers=[5,8,15,20]
#create a dictionary to represent square of each number
for num in numbers:
    print(f"Square of numbers {num} : {num**2}")

