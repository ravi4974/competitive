def canNickEscape(size,steps,building):
 #get aware of building schematics
 location={'n':None,'s':None,'c':{},'h':{}}
 r,c=0,0
 for i in building:
  c=0
  for j in i:
  	if not any(i.find(x)!=-1 for x in ['M','S','L','H']): continue
  	if  location['n'] is None and j=='M':
  	 location['n']=(r,c)
  	elif location['s'] is None and j=='S':
  	 location['s']=(r,c)
  	elif j=='L':
  	 location['c'][(r,c)]=0
  	elif j=='H':
  	 location['h'][(r,c)]=0
  	c+=1
  r+=1
 queue=[location['n']]
 points={location['n']:0}
 def tracePath():
  t=steps
  while(t):
   c=queue.pop()
   if(c==location['s']):
    return points[location['s']]
   for i in [(1,0),(0,1),(-1,0),(0,-1)]:
    n=c[0]+i[0],c[1]+i[1]
    if n[0]<0 or n[1]<0 or n[0]>size or n[1]>size or n in location['h'] or n in location['c']:
     continue
    if n not in points:
     points[n]=points[c]+1
     queue.append(n)
   t-=1
  spreadingCommandos()
  return -1

 def spreadingCommandos():
  k=list(location['c'].keys())
  for c in k:
   for i in [(1,0),(0,1),(-1,0),(0,-1)]:
    n=c[0]+i[0],c[1]+i[1]
    if n[0]<0 or n[1]<0 or n[0]>size or n[1]>size or n in location['h'] or n in location['c'] or n==location['s']:
     continue
    location['c'][n]=0

 for i in range(0,size*size):
  path=tracePath()
  if path!=-1:
   return path-i+1
  if len(queue)==0:
   return -1

print(canNickEscape(5,1,['MOOOS','OOOO','OOOOO','OOOOO','OOOOL']))
print(canNickEscape(15,1,
	['LOOOOOOOOOOOOOO','OOOOOOOOOOOOOOO','OOOOOOOOOOOOOOO','OLOOLOOOOOOOOOO','OOOOOLLOOOOOOOO','OOOOOOOOOLOOOOO','OLOOOHOOOOOOOOO','OOOOOHOOOOOOOOO','OOOOOOOOOOHOOOO','OOOOLOOOOOOOOOO','OOOHOOOOOOHOOOO','OOOOOOOOOOOHOOO','OOOOOOOOLOOOOOO','OOOOOHOOOOOOOOO','MOOOOOOOOOOOOOS']))