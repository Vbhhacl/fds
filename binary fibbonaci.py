x=int(input("Enter the total number of students attended the training program : "))
y=[]
print("Enter the roll no. of students")
for i in range (0,x):
  element=int(input())
  y.append(element)
  y.sort()
print(y)
k=int(input("Enter the roll no. to be found : "))
def binary(a,b):
  l=0
  u=x-1
  while(l<=u):
    mid=(l+u)//2
    if (a[mid]==k):
      print("Student attended the training program")
      break
    elif (a[mid]>k):
      u=mid-1
    elif (a[mid]<k):
      l=mid+1
  else:
      print("Student does not attended the training program")

def fibonacci(c,d):
  fib1=1
  fib2=0
  fib=fib1+fib2
  while(fib<=x):
    fib2=fib1
    fib1=fib
    fib=fib1+fib2
  offset=-1
  while(fib!=0):
    i=min((offset+fib2),x-1)
    if (k>y[i]):
      fib=fib1
      fib1=fib2
      fib2=fib-fib1
    elif (k<y[i]):
      fib=fib2
      fib1=fib1-fib2
      fib2=fib-fib1
    elif (k==y[i]):
      print("Stuedent attended the training program")
      break
  else :
    print("Student does not attended the training program")

flag=1
while(flag==1):
  print("1.Search roll no. by binary search")
  print("2.Search roll no. by fibonacci search")
 
  ch=int(input("Enter your choice : "))
  if(ch==1):
    binary(y,k)
    break;
  elif(ch==2):
    fibonacci(y,k)
    break;
  else:
    print("Invalid choice") 
