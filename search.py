li=list(map(int,input("Enter the list:").split()))
key=int(input("Enter the key:"))
def search(lis,key):
	if key in lis:
		return 1
	else :
		return 0

r=search(li,key)
print(r)
