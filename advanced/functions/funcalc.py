num1=int(input("Input num1 "))
num2=int(input("Input num2 "))
def add (n1,n2):
    print (n1,"+",n2,"=",n1+n2)
def sub (n1,n2):
    print (n1,"-",n2,"=",n1-n2)
def mul (n1,n2):
    print (n1,"X",n2,"=",n1*n2)
def div (n1,n2):
    if num2!=0:
        print (n1,"/",n2,"=",n1/n2)  
    else :
        print("Cant divide by zero" )
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
opp=int(input())
match opp:
    case 1:
       add(num1,num2)
    case 2:
        sub(num1,num2)
    case 3:
        mul(num1,num2)
    case 4:
       div(num1,num2)
    case _:
        print("enter a proper opparator")