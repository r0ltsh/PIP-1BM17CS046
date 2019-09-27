class student :
	def __init__(self):
		self.i=None
		self.age=None
		self.marks=None
	def setter(self,i,age,marks):
		self.i=i
		self.age=age
		self.marks=marks
	def getter(self):
		print("ID :"+str(self.i)+"\n")
		print("Age :"+str(self.age)+"\n")
		print("Marks :"+str(self.marks)+"\n")
	def validate_age(self):
		if self.age>20:
			return True
		return False
	def validate_marks(self):
		if self.marks>=0 and self.marks<=100 :
			return True
		return False
	def check_qualification(self):
		if self.marks>=65 and self.validate_marks() and self.validate_age() :
			return True
		return False

if __name__ == "__main__":
	n=int(input("Enter the no. of students"))
	students=[]
	for j in range(n):
		students.append(student())
		print("Enter the student "+str(j+1)+" details\n")
		i=int(input("Enter the id :"))
		age=int(input("Enter the age :"))		
		marks=int(input("Enter the marks :"))
		students[j].setter(i,age,marks)
	for j in range(n):
		if(students[j].check_qualification()):
			print("The student with the id :"+str(students[j].i)+" IS qualified\n")
			students[j].getter()
		else:
			print("The student with the id :"+str(students[j].i)+" IS NOT qualified\n")

