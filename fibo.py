def fibo(n):
	f=0
	s=1
	c=0
	while c<n :
		print(f)
		t=s
		s=f+s
		f=t
		c=c+1

n=int(input("enter the number of fibo elements to display"))
fibo(n)
