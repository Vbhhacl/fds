m=int(input("Enter the number of students : "))

FDS=[]
print("Enter the marks of the students : ")
for i in range (0,m):
    element=int(input())
    FDS.append(element)
print("list of marks of students in FDS",FDS)

#function to count average marks of student
def average(list1,number):
   s=0
   for i in range(0,m):
       s += list1[i]
   return(s/number)
Average=average(FDS,m)

#function to find maximum marks of student
def maxmarks(list1,number):
    max=0
    for i in range(0,m):
        if max<list1[i]:
           max=list1[i]
    return max
maximum=maxmarks(FDS,m)


#function to find minimum marks of student
def minmarks(list1,number):
    min=list1[0]
    for i in range(0,m):
        if min>list1[i]:
           min=list1[i]
    return min
minimum=minmarks(FDS,m)

#function to find largest frequency
def largestmfreq(number,list1):
   count=0
   check=maxmarks(list1,number)
   for i in range(0,m):
      if check ==list1[i]:
         count+=1
   return count
lfreq=largestmfreq(m,FDS)


#function to find absent number of student
def absent(list1,number):
   count=0
   for i in range(0,m):
      if list1[i]==0:
         count+=1
   return count
Absent=absent(FDS,m)

flag =1
while (flag==1): 

  print("1=the average score of  class:")
  print("2=highest score of class :")
  print("3=lowest score of class:")
  print("4=absent student's count:")
  print("5=display marks with highest frequency")
  print("6=exit")
  choice=int(input("enter your choice:"))
   
  if choice==1:
     print("Average marks of student in FDS",Average)

  elif choice==2:
     print("Maximum marks in FDS is",maximum)
  elif choice==3:
     print("minimum marks in FDS is ",minimum)

  elif choice==4: 
     print("number of students absent for exam ",Absent)

  elif choice==5:
     print("maximum frequency of marks is ",lfreq) 
  elif choice==6:
     flag=0
  else:
    print("enter valid choice")
  
 	
 
