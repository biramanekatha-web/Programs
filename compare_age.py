jay=int(input("Enter the age of jay:"))
Viru=int(input("Enter the age of Viru:"))
Gabbar=int(input("Enter the age of Gabbar:"))
if(jay>Viru and jay>Gabbar):
    print("jay is older")
elif(Viru>jay and Viru>Gabbar):
    print("Viru is older")
elif(Gabbar>jay and Gabbar>Viru):
    print("Gabbar is older")
else:
    print("all are of same age")
