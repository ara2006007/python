for i in range (3,10 ):
    if i%2!=0 :
        print(i , end=" ")
        i+=1
print("\n*********************\n")
for i in range (3,11 ):
    if i%2==0 :
        print(i , end=" ")
        i+=1
print("\n*********************\n")
for i in range (1,5):
    n=(i*(i+1))//2
    print(n , end=" ")
    i+=1
print("\n*********************\n")
for i in range (1,6):
    n=i**2
    print(n , end=" ")
    i+=1
print("\n*********************\n")
for i in range (1,10 ):
    if i%2!=0 :
        print(i , end=" ")  
    else :
        print("*", end=" ")
    i+=1
print("\n*********************\n")

for i in range (1,6):
    for j in range (1,6) :
        print (i , end =" ")
        j+=1
    i+=1
    print ("")
print("\n*********************\n")
for i in range (1,6):
    for j in range (5,0,-1) :
        print (j , end =" ")
        j+=1
    i+=1
    print ("")
print("\n*********************\n")
for i in range (1,6):
    for j in range (1,i+1) :
        print (j , end =" ")
        j+=1
    i+=1
    print ("")
print("\n*********************\n")
for i in range (1,6):
    for j in range (5,5-i,-1) :
        print (j , end =" ")
        j+=1
    i+=1
    print ("")
print("\n*********************\n")

        