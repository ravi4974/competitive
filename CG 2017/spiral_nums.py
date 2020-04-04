#program to print numbers in spiral format
#output

#n = 3
#	1	2	3
#	8	9	4
#	7	6	5
#path = 00 01 02 12 22 21 20 10 11

#n = 4
#	1	2	3	4
#	12	13	14	5
#	11	16	15	6
#	10	9	8	7
#path = 00 01 02 03 13 23 33 32 31 30 20 10 11 12 22 21
#	1	2	3	4
#	5	6	7	8
#	9	10	11	12
#	13	14	15	16

# 4(+1) + 3(+10) + 3(-1) + 2(-10) + 2(+1) + 1(-10) + 1(-1)

#n = 5
#	1	2	3	4	5
#	16	17	18	19	6
#	15	24	25	20	7
#	14	23	22	21	8
#	13	12	11	10	9
#path = 00 01 02 03 04 14 24 34 44 43 42 41 40 30 20 10 11 12 13 23 33 32 31 21 22
#	1	2	3	4	5
#	6	7	8	9	10
#	11	12	13	14	15
#	16	17	18	19	20
#	21	22	23	24	25

# 5(+1) + 4(+10) + 4(-1) + 3(-10) + 3(+1) + 2(+10) + 2(-1) + 1(-10) + 1(+1)

num=1

def simple(n):
	global num
	num=1
	a=[0]*n*n
	r,c=0,-1

	def d(i,j):
		global num
		a[i*n+j]=num
		num+=1

	for i in range(n):
		c+=1
		d(r,c)

	t=n-1
	while t>0:
		#down
		for i in range(t):
			r+=1
			d(r,c)
		#left
		for i in range(t):
			c-=1
			d(r,c)
		t-=1
		#up
		for i in range(t):
			r-=1
			d(r,c)
		#right
		for i in range(t):
			c+=1
			d(r,c)
		t-=1
	
	for i in range(n):
		for j in range(n):
			print(a[i*n+j],'\t',end='')
		print()

def simplified(n):
	global num
	num=1
	a=[0]*n*n
	r,c=0,-1

	def cnt(i,j):
		global num
		a[i*n+j]=num
		num+=1

	for i in range(n):
		c+=1
		cnt(r,c)

	t=n-1
	flag=1

	while t>0:
		#down (flag=1) & up(flag=-1)
		for i in range(t):
			r+=1*flag
			cnt(r,c)

		#left(flag=1) & right (flag=-1)
		for i in range(t):
			c+=-1*flag
			cnt(r,c)

		t-=1
		flag*=-1

	#print output
	for i in range(n):
		for j in range(n):
			print(a[i*n+j],'\t',end='')
		print()

simplified(5)
print('-'*20)
simplified(4)