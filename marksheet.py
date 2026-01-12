print("*****STUDENT MARKSHEET*****")

name=input("Enter your name")
rollno=input("Enter your roll no")

english=int(input("Enter your english marks"))
urdu=int(input("Enter your urdu marks"))
pst=int(input("Enter your pst marks"))
isl=int(input("Enter your isl marks"))
bio=int(input("Enter your bio marks"))
chem=int(input("Enter your chem marks"))

totalmarks=500

obtainedmarks= english+urdu+pst+isl+bio+chem
print(f"{name} , Your obtained marks are" , obtainedmarks)

percentage=(obtainedmarks/totalmarks)*500
print(f"{name} , Your percentage is:" , percentage)

if percentage>=90:
    print(f" {name} , You Got A+ Grade")
    
elif percentage>=80:
    print(f" {name} , You Got A Grade")
    
elif percentage>=70:
    print(f" {name} , You Got B Grade")
    
elif percentage>=60:
    print(f" {name} , You Got C Grade")
    
elif percentage>=50:
    print(f" {name} , You Got D Grade")
    
else:
    print(f" So sorry {name} , You are failed")
    

    
    
