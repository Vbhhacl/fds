print("enter the details of matrixs : ")
m=int(input("enter no. of rows matrix : "))
n=int(input("enter no. of coloums matrix : "))

print("enter the value of matrix 1 : ")
A1=[[int(input()) for i in range (0,m)]for j in range(0,n)]
for i in range(0,m):
	for j in range(0,n):
	   print(A1[i][j],end='  ')
	print()
	
print("enter the second  matrix : ")	
print("enter the value of matrix 2 : ")	
A2=[[int(input()) for i in range (0,m)]for j in range(0,n)]
for i in range(0,m):
	for j in range(0,n):
	   print(A2[i][j],end='  ')
	print()  
	
print("addition of the matrices : ")
add=[[0 for i in range (m)]for j in range(n)]
for i in range(0,m):
	for j in range(0,n):
	    add[i][j]=A1[i][j] + A2[i][j]
for i in range(0,m):
	for j in range(0,n):
	    print(add[i][j],end =' ')	 
	print()       
	
print("subtraction of the matrices : ")
sub=[[0 for i in range (m)]for j in range(n)]
for i in range(0,m):
	for j in range(0,n):
	    sub[i][j]=A1[i][j] - A2[i][j]
for i in range(0,m):
	for j in range(0,n):
	    print(sub[i][j],end =' ')	 
	print()     
	  
print("multiplication of the matrices : ")	
mul=[[0 for i in range (m)]for j in range(n)]
for i in range(0,m):
	for j in range(0,n):
	    for k in range (0,m ):
	        mul [i][j]=mul[i][j]+A1[i][k]*A2[k][j]
for i in range(0,m):
	for j in range(0,n):
	    print(mul[i][j],end =' ')	 
	print()     

	
print("transpose  of the matrix 1  : ")	 
trans=[[0 for i in range (m)]for j in range(n)]
for i in range(0,m):
	for j in range(0,n):
	        trans[j][i]= A1[i][j]
for i in range(0,m):
	for j in range(0,n):
	   	 print (trans[i][j],end= '  ' )
	print()     
	
print("transpose  of the matrix 2  : ")	 
trans=[[0 for i in range (m)]for j in range(n)]
for i in range(0,m):
	for j in range(0,n):
	        trans[j][i]= A2[i][j]
for i in range(0,m):
	for j in range(0,n):
	   	 print (trans[i][j],end= '  ' )
	print()     
		
	
	 
	

   
	    	
	
