"""student=("Ara",45,"19/02/2024")
name,age,dob,x=student
print(name)
print(age)
print (dob)"""
marks=(23,56,78,67,45,46,87)
a,*b,c=marks
print(a)
print(b)
print(c)
print("****************************")
marks=(23,56,78,67,45,46,87)
a,b,*c=marks
print(a)
print(b)
print(c)
print("****************************")

marks=(23,56,78,67,45,46,87)
*a,b,c=marks
print(a)
print(b)
print(c)
print("****************************")
