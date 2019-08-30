import string 
import random
result=string.ascii_letters+string.digits+string.punctuation
pwd=''.join([random.choice(result) for n in range(random.randint(8,10))])
print("password: ",pwd) 
