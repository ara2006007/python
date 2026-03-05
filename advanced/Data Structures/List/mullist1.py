x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(type(x))
print (x[0][0])
print (x[0][1])
print (x[0][2])
print()
i=0
j=0
for i in range (len(x)):    
    for j in range (len(x)):
        print (x[i][j],end=" ")
    print()
    