import string 
import random
li=[]
#l=random.randint(8,20)
l=15
lw=random.randint(1,l//4)
up=random.randint(1,l//4)
i=random.randint(1,l//4)
s=random.randint(1,l//4)
x=l-(lw+up+i+s)
print(lw)
print(up)
print(i)
print(s)
print(x)
for j in range (0,x):
	li.append(random.choice(string.ascii_letters))
print(li)
for j in range (0,lw):
	li.append(random.choice(string.ascii_lowercase))
print(li)
for j in range (0,up):
	li.append(random.choice(string.ascii_uppercase))
print(li)
for j in range (0,i):
	li.append(str(random.randint(0,9)))
print(li)
for j in range (0,s):
	li.append(random.choice(string.punctuation))
print(li)
pwd=''.join([random.sample(li,l)])
print(pwd)
