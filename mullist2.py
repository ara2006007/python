x = [
    [],
    ["Ara", 87, 98, 78, 90],
    ["Ava", 77, 58, 48, 80],
    ["Aca", 85, 48, 98, 45],
    ["Mra", 87, 98, 78, 90],
    ["Ari", 82, 58, 74, 70]
]
def grade(ava):
    if ava>=75 :
        return"A"
    elif ava>=65:
        return"B"
    elif ava>=55:
        return"C"
    elif ava>=45:
        return"S"
    else :
        return"F"
        
        
y = [["Student Name","Maths", "Science", "English", "ICT", "Total", "Average"]]
for i in range(1, len(x)):
    total=0
    avg=0
    for j in range (4): 
        total += int((x[i][j+1]))
    avg = total / 4
    k=grade(avg)
    y.append([x[i][0],x[i][1],x[i][2],x[i][3],x[i][4] ,total, avg,k])
for row in y:
    for item in row:
        print(item, end='\t') 
    print() 
