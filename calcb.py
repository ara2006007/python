num1=int(input("Input num1 "))
num2=int(input("Input num2 "))
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
opp=int(input())
match opp:
    case 1:
        print (num1,"+",num2,"=",num1+num2)
    case 2:
        print (num1,"-",num2,"=",num1-num2)
    case 3:
        print (num1,"X",num2,"=",num1*num2)
    case 4:
        if num2!=0:
            print (num1,"/",num2,"=",num1/num2)  
        else :
            print("Cant divide by zero" )
    case _:
        print("enter a proper opparator")