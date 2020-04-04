def tree(n):
 t={0:[]}
 i=0
 def node(i):
  for k in [1,2]:
   if (2*i+k)<n:
    t[2*i+k]=[]
    t[i].append(2*i+k)

 while(i<n):
  node(i)
  i+=1
 return t

def delete(t,i):
 for x in t[i]:
  delete(t,x)
 del t[i]

def nleaf(t):
 leaf=0
 for k in t:
  if not len(t[k]): leaf+=1
 return leaf
#take inputs

#n=int(input("n"))
#a=input("a")
#idx=int(input("idx"))

n=5
idx=2

t=tree(n)
delete(t,idx)
print(nleaf(t))

