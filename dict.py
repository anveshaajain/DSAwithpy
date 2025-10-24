#Create a dictionary with key as roll.no and name for specific number of student and print the same

student={}

n=int(input("Enter the no of students that you want to enter"))

for i in range(n):

    rollno=int(input("Enter the roll no of student"))
    name=input("Enter the name").upper()

    student[rollno]=name
    
    
for rollno,name in student.items():
    print(f"Roll.NO:{rollno} \t Name:{name}")