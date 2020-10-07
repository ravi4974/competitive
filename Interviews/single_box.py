class Rect:
	def __init__(self,top,left):
		self.top=top
		self.left=left
		self.bottom=self.top
		self.right=self.left
	
	def is_valid(self):
		return self.right>self.left and self.bottom>self.top
	
	def max_right(self,m,x,y):
		if x==len(m[y])-1 or m[y][x]==1: return x-1
		return self.max_right(m,x+1,y)
	
	def max_bottom(self,m,x,y):
		if y==len(m)-1 or m[y][x]==1: return y-1
		return self.max_bottom(m,x,y+1)

	def trace(self,m):
		self.right=self.max_right(m,self.left,self.top)

		for x in range(self.right,self.left,-1):
			self.bottom=self.max_bottom(m,x,self.top)
			self.right=min([self.max_right(m,self.left,self.bottom),self.right])
			if self.right==x: break

		if not self.is_valid():
			raise ValueError()
	
	def __repr__(self):
		return 'Rect(({p.left},{p.top}),({p.right},{p.bottom}))'.format(p=self)

def find_rect(m):
	for i,row in enumerate(m):
		try:
			r=Rect(top=i,left=row.index(0))
			r.trace(m)
			return r
		except:
			pass

if __name__ == "__main__":
		
	m=[
		[
			[1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1],
			[1,1,1,0,0,0,1],
			[1,1,1,0,0,0,1],
			[1,1,1,1,1,1,1]
		],
		[
			[1,1,1,1,1,1,1],
			[1,1,1,0,0,0,1],
			[1,1,1,0,0,0,1],
			[1,1,1,0,0,0,1],
			[1,1,1,1,1,1,1]
		],
		[
			[1,1,1,1,1,1,1],
			[1,1,1,0,0,0,1],
			[1,1,1,0,1,0,1],
			[1,1,1,0,0,0,1],
			[1,1,1,1,1,1,1]
		],
		[
			[1,0,1,1,1,1,1],
			[1,0,0,0,0,0,1],
			[1,0,1,0,1,0,1],
			[1,0,0,0,0,0,1],
			[1,1,1,1,1,1,1]
		]
	]

	for i in m:
		print(find_rect(i))