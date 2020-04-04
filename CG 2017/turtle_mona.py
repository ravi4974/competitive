class node:
 def __init__(self,s,path=[]):
  self.pos=s
  self.path=[]
  self.path.extend(path)
  self.path.append(s)
 def __str__(self):
  return str(self.path)+':'+str(len(self.path))

def isprime(n):
 n=n[0]-1,n[1]-1
 n=a[n[0]][n[1]]
 if n<2: return False
 for i in range(2,int(n**0.5)+1):
  if n%i==0: return False
 return True

def findPath(l,b,a):
 s=1,1
 d=l,b
 q=[node(s)]
 m={str(q[0]):True}
 while(len(q)):
  c=q.pop(0)
  if c.pos==d:
   path.append(c)
  for i in [(1,0),(0,1),(1,1)]:
   n=c.pos[0]+i[0],c.pos[1]+i[1]
   if n[0]<1 or n[1]<1 or n[0]>l or n[1]>b or not isprime(n):
    continue
   n=node(n,c.path)
   if str(n) not in m:
    q.append(n)
    m[str(n)]=True

n,m=3,3
a=[[2,3,7],[5,4,2],[3,7,11]]
path=[]
findPath(n,m,a)
for i in path:
 print i
path=sorted(path,key=lambda x:str(x))
print 'sorted'
for i in path:
 print i