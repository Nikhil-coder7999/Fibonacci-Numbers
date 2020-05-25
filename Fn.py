n = int(input())  #taking input from user

a = 0

b = 1

if n<1:
    print('Enter positive no. only')
elif n==1:
    print('Fibonacci Series :', a)
else:
    print ('Fibonacci Series :')
    while n>1:
        print(a, end=" ")
        c=b+a
        a=b
        b=c
        n=n-1
