n=int(input("please enter how many numbers of fibonacci terms,you want:"))
a=0
b=1
i=0
if n<=0:
    print("Please enter a positive integer.")
elif n==1:
    print("Fibonacci series upto",a,"term:")
    print(a)
else :
    print("Fibonacci series upto",n,"terms:")
    while i < n:
        print(a)
        c=a+b
        a=b
        b=c
        i=i+1
