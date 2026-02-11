name="Ara"
id=9001
grade="10A"
nic=200621401188

print("********************")
print("Student information")
print("********************")
print("Student name is : "+name)
print("Student id is : "+str(id))
print("Student grade is : "+grade)
print("Student NIC is : "+str(nic))

print("")
print("********************")
print("Student information")
print("********************")
print("Student name is : ",name)
print("Student id is : ",id)
print("Student grade is : ",grade)
print("Student NIC is : ",nic)

print("")
print("********************")
print("Student information")
print("********************")
print(f"Student name is : {name}")
print(f"Student id is : {id}")
print(f"Student grade is : {grade}")
print(f"Student NIC is : {nic}")

print("")
print("********************")
print("Student information")
print("********************")
print(f"Student name is : {name}\nStudent id is : {id}\nStudent grade is : {grade}\nfStudent NIC is : {nic}")

print("")
print("********************")
print("Student information")
print("********************")
print("Student name is : {0}\nStudent id is : {1}\nStudent grade is : {2}\nfStudent NIC is : {3}".format(name,id,grade,nic))

print("")
print("********************")
print("Student information")
print("********************")
print("Student name is : %s \nStudent id is : %d\nStudent grade is : %s\nfStudent NIC is : %d" %(name,id,grade,nic))