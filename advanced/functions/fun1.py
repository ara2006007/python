#def printName():
	#print ("My name is Ara")
#printName()
#printName()
#printName()
def printName(name):
	print (f"My name is {name}")
printName("Ara")
printName("Arch")
printName("Aththiya")
print ()

def printfullName(fname="Ara",lname="Selva"):
	print (f"My  full name is {fname} { lname}")
printfullName("Selvakumar","Aradanan")
printfullName("Arch","kethese")
printfullName  ("Aththiya","Aravinthon")
printfullName()

def ret (fname , lname):
    return fname+lname
funname = ret ("Ara","selva")
print (funname)


