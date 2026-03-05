day=int(input("Input a number "))
match day:
	case 1 :
		print("Monday")
	case 2 :
		print("Tuesday")
	case 3 :
		print("Wednesday")
	case 4 :
		print("Thursday")
	case 5 :
		print("Friday")
	case 6 :
		print("Saturday")	
	case 7 :
		print("Sunday")
	case _:
		print("Input a proper number between 0 and 8 ") 