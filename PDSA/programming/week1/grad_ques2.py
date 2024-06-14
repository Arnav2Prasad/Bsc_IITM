QUESTION :  GOLDBACH'S CONJECTURE

ANSWER:

def isPrime(n):
    if n==1:
        return 0
    if n==0:
        return 0
    if n==2:
        return 1
        
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

def Goldbach(n):
    l=[]
    for i in range(3,int(n/2)+1):
        if isPrime(i)==1:
            if isPrime(n-i)==1:
                l.append((i,n-i))
                
    return l
                
        
    
n=int(input())
print(sorted(Goldbach(n)))
