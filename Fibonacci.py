# Program to make a fiboncci series
n=int(input("Enter the level upto which series need to made:"))
a=0
b=1
print(a)
print(b)
for i in range (1,n+1) :
    c=a+b
    print(c)
    a=b
    b=c
    


    
    
