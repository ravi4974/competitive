def solve(l,b,n,m,co):
 tr=[]
 rects={}
 ch={}
 
 #get perimeter of the valid rect
 def gp(tr):
  x,y=[],[]
  for c in tr:
   x.append(c[0])
   y.append(c[1])
  s,e=(min(x),min(y)),(max(x),max(y))
  if (s,e) in rects: return None,-1
  for c in ch:
   if c[0]>=s[0] and c[1]>=s[1] and c[0]<=e[0] and c[1]<=e[1] and c not in tr:
    return None,-1
  return (s,e),2*(e[0]-s[0]+e[1]-s[1]+2)
 
 def isover(r1,r2):
  if r1==r2: return True
  if r1[0]==r1[1] or r2[0]==r2[1]: return False
  if r2 in ch and ch[r2]==r1: return True
  ch[r1]=r2
  if r1[0][0]>r2[1][0] or r2[0][0]>r1[1][0]: return False
  if r1[0][1]>r2[1][1] or r2[0][1]>r1[1][1]: return False
  return True
 
 #get num of hubs at single point
 for c in co:
  if c not in ch:
   ch[c]=1
  else:
   ch[c]+=1
 
 #try and make rects 
 def checkRect(t,n):
  for c in ch:
   if c in t: continue
   n+=ch[c]
   t.append(c)
   if n==m:
    p=gp(t)
    if p[1]!=-1:
     rects[p[0]]=p[1]
   elif n<m:
    checkRect(t,n)
   n-=ch[t.pop()]
 
 for s in ch:
  if ch[s]>m: continue
  if ch[s]==m:
   rects[(s,s)]=4
   continue
  checkRect([s],ch[s])
 
 tr=[]
 ch={}
 for r1 in rects:
  for r2 in rects:
   if not isover(r1,r2):
    tr.append(rects[r1]+rects[r2])
 
 print(min(tr) if len(tr) else 0)


solve(6,5,8,3,[(1,1),(3,1),(3,3),(1,6),(4,3),(5,5),(5,5),(5,5)])