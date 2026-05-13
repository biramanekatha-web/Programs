'''check user age of eligibility criteria for appliying for driving license the age should be greater than 18 and below 75. display 
appropriate message to the user for less display wait for --- years and age is above 75 then display you are not eligible for driving license. 
otherwise welcome to pune RTO office.'''

age=int(input("enter the age:"))
if(18<=age <75):
    print("welcome to pune RTO office..")
elif(age<18):
    print(f"wait for {18-age} years..")
else:
    print("you are not eligible for driving license..")
