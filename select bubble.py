x=int(input("enter the total numbers of students : "))
y=[]
print("enter the percentage of the students : ")
for i in range (0,x):
 element =float(input())
 y.append(element)
print("given list of percentage of students : ",y)

def bubble(a):
  for i in range (x-1):
   for j in range (x-1):
     if (y[j]>y[j+1]):
      temp=a[j+1]
      y[j+1]=y[j] 
      y[j]=temp
  print("sorted list of percentage : ",y)
 
  y.reverse()
  print("top 5 scores",y[0:5])
  
def  selection(a) :
  for i in range (x-1):
    for j in range (i+1,x):
      min=i
      if (y[j]<y[min]):
        temp=y[j]
        y[j]=y[min]
        y[min]=temp
  print("selection sorted list",y)  

  y.reverse()
  print("top 5 scores",y[0:5])   
  
  
flag =1
while (flag==1): 

  print("1=bubble sorting")
  print("2=selection sorting")
  print("3=exit:")
 
  choice=int(input("enter your choice:"))
  if choice==1:
     bubble(y) 

  elif choice==2:
     selection(y)
   
  elif choice==3:
     flag=0
  else:
    print("enter valid choice")
   





    
