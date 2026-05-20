'''jay=int(input("Enter the age of jay:"))
Viru=int(input("Enter the age of Viru:"))
Gabbar=int(input("Enter the age of Gabbar:"))
if(jay>Viru and jay>Gabbar):
    print("jay is older")
elif(Viru>jay and Viru>Gabbar):
    print("Viru is older")
elif(Gabbar>jay and Gabbar>Viru):
    print("Gabbar is older")
else:
    print("all are of same age")'''

jay = int(input("Enter Jay age: "))
viru = int(input("Enter Viru age: "))
gabbar = int(input("Enter Gabbar age: "))

if jay > viru and jay > gabbar:
    print("Jay is older.")

elif viru > jay and viru > gabbar:
    print("Viru is older.")

elif gabbar > jay and gabbar > viru:
    print("Gabbar is older.")

elif jay == viru and jay > gabbar:
    print("Jay and Viru are of same age and older than Gabbar.")

elif jay == gabbar and jay > viru:
    print("Jay and Gabbar are of same age and older than Viru.")

elif viru == gabbar and viru > jay:
    print("Viru and Gabbar are of same age and older than Jay.")

else:
    print("All are of same age.")