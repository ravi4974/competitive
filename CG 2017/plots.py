def display(p):
 for i in range(len(p)):
  for j in range(len(p[i])):
  	print(p[i][j],end='\t')
  print()

def getPlots(size,cost,nplots,plots):
 land=[['' for x in range(size[1])] for x in range(size[0])]
 plotcost={'':0}
 maxparksize=min(size)
 def updateBlock(p,i):
  p=list(map(int,p.split(',')))
  plotcost['p'+str(i)]=p[4]
  for x in range(p[0]-1,p[2]):
   for y in range(p[1]-1,p[3]):
    land[x][y]+='p'+str(i)+','
 i=0
 for x in plots:
  updateBlock(x,i)
  i+=1

 def totalCost(p):
  return sum(plotcost[i] for i in p.split(','))


 def isValidPark(s,e):
  p=''
  for i in range(s[0],e[0]):
   for j in range(s[1],e[1]):
   	if p.find(land[i][j])==-1:
   	 p+=land[i][j]
   	 if totalCost(p)>cost : return False
  return True
 
 while(maxparksize):
  for i in range(0,size[0]):
   if i+maxparksize>size[0]: break
   for j in range(0,size[1]): 
   	if j+maxparksize>size[1]: break
   	if isValidPark((i,j),(i+maxparksize,j+maxparksize)):
   	 return maxparksize
  maxparksize-=1
 return maxparksize


 

print(getPlots((6,9),42,5,['4,1,6,3,12','3,6,5,6,9','1,3,3,8,24','3,8,6,9,21','5,1,6,2,20']))
print(getPlots((6,9),0,5,['4,1,6,3,12','3,6,5,6,9','1,3,3,8,24','3,8,6,9,21','5,1,6,2,20']))
a=['4,20,6,33,9','36,18,50,32,5','3,20,13,20,6','37,6,46,11,9','17,33,28,33,4','25,34,35,47,6','29,17,40,18,2','37,40,42,47,4','5,18,19,30,7','22,33,31,33,2','35,27,45,37,8','4,10,14,23,8','5,37,15,49,3','7,8,18,9,5','4,15,12,24,3','34,5,35,7,3','33,36,41,38,8','29,32,31,39,1','27,32,27,38,8','14,17,22,26,9','33,29,36,30,4','10,33,20,38,9','20,31,31,33,8','19,27,31,27,9','16,21,29,28,9','8,35,19,37,9','41,4,42,5,3','3,8,17,16,3','28,25,30,34,1','43,29,45,31,9','7,20,13,27,1','12,32,25,41,5','50,9,50,22,8','11,26,19,38,3','17,23,26,23,6','26,22,36,33,9','17,7,23,21,8','19,10,27,15,6','8,24,10,32,5','15,22,16,22,2','1,26,12,37,2','5,16,9,28,7','39,8,41,19,9','30,4,30,10,7','8,28,15,42,6','36,25,46,37,7','46,7,50,21,8','22,20,22,20,9','36,8,47,21,1','43,36,50,50,8']
print(getPlots((50,50),0,50,a))
