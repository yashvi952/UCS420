'''def Add(a,b):
    c=a+b
    return c

print("Add(10,20) -->",Add(10,20))
print("Add(20,50) -->",Add(20,50))
print("Add(80,200) -->",Add(80,200))'''

'''def AddN(n):
    s=sum(range(n+1))
    return s

print("AddN(10) --> ",AddN(10))
print("AddN(20) --> ",AddN(20))
print("AddN(50) --> ",AddN(50))
print("AddN(200) --> ",AddN(200))'''

'''def OddAdd(n):
    s=sum(range(1,n+1,2))
    return s

n=int(input("Enter a number: "))
print("Sum of odd numbers upto ",n," is: ",OddAdd(n))'''

def PrimeAdd(n):
    s=0
    for i in range(2,n+1):
        factor=0
        for j in range(1,n//2+1):
            if(i%j==0):
                factor+=1
        if(factor<=2):
            s+=i
    return s

n=int(input("Enter a number: "))
print("Sum of all primes upto ",n," is: ",PrimeAdd(n))
