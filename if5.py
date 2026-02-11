sal=float(input("Please input your salary : Rs "))
if sal>=0:
	if sal>=100000 :
		tax=sal*0.05
	elif sal>=80000 :
		tax=sal*0.03
	else :
		tax=sal*0
else :
	print("please input a proper salary")

print("*******************")
print("Employee salary details")
print("*******************")
print("Basic salary : Rs",sal)
print ("Tax : Rs",tax)
print("Net salary : Rs",(sal-tax))