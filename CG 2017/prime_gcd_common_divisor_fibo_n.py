def gcd(a,b):
 if a==0: return b
 return gcd(b%a,a)

def isprime(n):
 if n==2 or n==3: return True
 if n<2 or n%2==0: return False
 if n<9: return True
 if n%3==0: return False
 r=int(n**0.5)
 f=5
 while f<=r:
  if n%f==0 or n%(f+2)==0: return False
  f+=6
 return True

def commonDivisor(a,b):
 n=gcd(a,b)
 r=0
 for i in range(1,int(math.sqrt(n))):
  if n%i==0:
   r+= 1 if n/i==i else 2
 return r

def fib(n):
 p=5**0.5
 p1=((p+1)/2)**n
 p2=(-1*((p-1)/2))**n
 r=(p1-p2)/p
 return int(r)

