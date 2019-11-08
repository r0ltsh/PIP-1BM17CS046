from tkinter import *

root=Tk()
root.title("BookMyShow")
root.geometry("722x435")
app=Frame(root)
app.grid()

hm=['JTHJ','YJHD','ZNMD','APKGK']
em=['MI','MI2','MI3','MI4']
km=['k1','k2','k3','k4']
hl=[]
el=[]
kl=[]
x="Hindi"
def lang():
	global x
	#print(x)
	print(v.get())
	if x=="Hindi":
		for j in hl:
			j.grid_forget()
	if x=="English":
		for j in el:
			j.grid_forget()
	if x=="Kannada":
		for j in kl:
			j.grid_forget()			
						
	
	if v.get()=="Hindi":
		for i in hm:
			c=Checkbutton(app, text=i, variable=b)
			c.grid()
			hl.append(c)
		x="Hindi"	
	if v.get()=="Kannada":
		for i in km:
			c=Checkbutton(app, text=i, variable=b)
			c.grid()
			kl.append(c)
		x="Kannada"	
	if v.get()=="English":
		for i in em:
			c=Checkbutton(app, text=i, variable=b)
			c.grid()
			el.append(c)
		x="English"	

Label(app, text="Select Language").grid()
v = StringVar(root, "hindi")
Radiobutton(app, text ="kannada", variable = v,value = "Kannada", command=lang).grid()
Radiobutton(app, text ="Hindi", variable = v,value = "Hindi", command=lang).grid()
Radiobutton(app, text ="English", variable = v,value = "English", command=lang).grid()

print(v.get())
b = StringVar(root, "hindi")

Label(app, text="Select movie").grid()
for i in hm:
	c=Checkbutton(app, text=i, variable=b)
	c.grid()
	hl.append(c)
	x="Hindi"



		





root.mainloop()


