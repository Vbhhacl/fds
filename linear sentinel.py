x=int(input("Enter total number of students attended training : "))
y=[]
print("Enter the roll no. of students : ")
for i in range (0,x):
  element=int(input())
  y.append(element)
print(y)
k=int(input("Enter the roll no. of the student to check whether he attended the program or not : "))
def linear_search(a,b):
  for i in range (0,x):
    if (a[i]==k):
      print("The student attended the training program")
      break;
    else:
      print("The student does not attended the training program")
      break;


def senitel_search(y,k):
  y.append(k)
  for i in range (0,x):
    if (y[i]==k):
        print("The student attended the training program")


flag =1
while (flag==1): 

  print("1=linear search")
  print("2=senitel search")
  print("3=exit:")
 
  choice=int(input("enter your choice:"))
  if choice==1:
     print("search by linear search method",linear_search(y,k))

  elif choice==2:
     print("search by sentinel search method",senitel_search(y,k))
   
  elif choice==3:
     flag=0
  else:
    print("enter valid choice")
   



























































































