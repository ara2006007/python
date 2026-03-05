def PrintMyName(name,age,grade):
    print(f"My name is {name}")
    print(f"My name is {age}")
    print(f"My name is {grade}")
    
no=int(input("Give your number of studets "))
for n in range (0,no):
    name=input(f"Please give your name ? ")
    age=input(f"Please give your age ? ")
    grade=input(f"Please give your grade ? ")   
    PrintMyName(name,age,grade)
    