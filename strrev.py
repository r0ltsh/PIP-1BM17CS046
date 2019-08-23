li=list(input("Enter the string:").split())
rev=li[::-1]
print(" ".join(rev))
#for i in rev:
#	print(i,end=" ")
for i in li:
	print("".join(reversed(i)),end=" ")
print()

'''Output:
   Enter the string:Welcome to BMSCE
   BMSCE to Welcome
   emocleW ot ECSMB '''

