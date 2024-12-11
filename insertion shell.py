x=int(input("enter the total numbers of students : "))
y=[]
print("enter the percentage of the students : ")
for i in range (0,x):
 element =float(input())
 y.append(element)
print(" percentage of students : ",y)

def insertionSort(y,x):
  for i in range (1,x):
     key=y[i]
     j=i-1
     while(key<y[j] and  j>=0 ):
        temp=y[j]
        y[j]=y[j+1]
        y[j+1]=temp
        j=j-1   
     y[j+1]=key   
  print("sorted list is",y)
  y.reverse()
  print("top 5 scores",y[0:5])   

def shellSort(y,x):
  n = x // 2
  while (n > 0):
        for i in range(n, x):
            temp = y[i]
            j = i
            while (j >= n and  y[j - n] > temp):
                y[j] =y[j - n]
                j -= n
            y[j] = temp
        n //= 2
        print("sorted list is",y)
  y.reverse()
  print("top 5 scores",y[0:5])   

flag =1
while (flag==1): 

  print("1=INSERTION SORT ")
  print("2=SHELL SORT ")
  print("3=exit:")
 
  choice=int(input("enter your choice:"))
  if choice==1:
     print("search by insertion sorting method",insertionSort(y,x) )
     break
  elif choice==2:
     print("search by shell sorting method",shellSort(y,x))
     break
  elif choice==3:
     flag=0
  else:
    print("enter valid choice")
   
