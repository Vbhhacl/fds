m=int(input("Total number of students in SEComp : "))
SEComp=[]
print("Enter the name of student : ")
for i in range(0,m):
  element=input()
  SEComp.append(element)
print("name of students",SEComp) 

cricket=[]
c=int(input("Enter no.of students who plays cricket:"))
print(" Enter name of students who plays cricket:")
for i in range(0,c):
   ele=input()
   cricket.append(ele)
print("Names of the studends who plays cricket:",cricket)
    
badminton=[]
b=int(input("Enter no.of students who plays badminton:"))
print(" Enter name of students who plays badminton:")
for i in range(0,b):
   elem=input()
   badminton.append(elem)
print("Names of the studends who plays badminton:",badminton)

football=[]
f=int(input("Enter no.of students who plays football:"))
print(" Enter name of students who plays football:")
for i in range(0,f):
   element=input()
   football.append(element)
print("Names of the studends who plays football:",football)

def union(list1,list2):
  list3=list1.copy()
  for val in list2:
    if val not in list2:
     list3.append(val)
  return(list3)  

def intersection(list1,list2):
  list3=[]
  for val in list1:
    if val in list2:
     list3.append(val)
  return(list3)  

def difference(list1,list2):
  list3=[]
  for val in list1:
    if val not in list2:
     list3.append(val)
  return(list3)  

def symdifference(list1,list2):
  D1=difference(list1,list2)
  D2=difference(list1,list2)
  list3=union(D1,D2)
  return(list3)
  
def CB(cricket,badminton):
  list3=intersection(cricket,badminton)
  print("no. of student who plays cricket and badminton:",len(list3))  
  print("names of the students who plays cricket and badminton:",list3)   
  
def eCeB(cricket,badminton):
  list3=symdifference(cricket,badminton)
  print("no. of student who plays either cricket or badminton but not both:",len(list3))  
  print("names of the students who plays either cricket or badminton but not both:",list3)  
  
def nCnB(list1,list2,list3):
  a=difference(list1,union(list2,list3))
  print("no. of Students who plays neither cricket nor badminton:",len(a)) 
  print("names of Students who plays neither cricket nor badminton:",a)    
        
def CFnB(list1,list2,list3):
  b=difference(intersection(list1,list2),list3)  
  print("no. of Students who plays cricket and football but not badminton: ",len(b)) 
  print("name of Students who plays cricket and football but not badminton:",b) 
print("Names of students in SEComp: ",SEComp) 

flag =1
while (flag==1): 

 print("1=Students who plays both cricket and badminton:")
 print("2=Students who plays either cricket or badminton :")
 print("3=Students who plays neither cricket nor badminton:")
 print("4=Students who plays cricket and football but not badminton:")
 print("5=Exit")
 
 choice=int(input("Enter your choice : "))
 
 if choice==1:
   CB(cricket,badminton)
 elif choice==2:
     eCeB(cricket,badminton)
 elif choice==3:
     nCnB(SEComp,cricket,badminton)
 elif choice==4: 
   CFnB(cricket,football,badminton)
 elif choice==5:
     flag=0  
 else:
   print("enter valid choice")
  
 
