subjects=["Eng","Tam","Sinh"]
print(subjects)
print (type(subjects))
print(subjects[0])
print(subjects[-1])
subjects[0]="german"
print (subjects)
subjects.append("Japanese")
print (subjects)
print (len(subjects))
for i in subjects:
    print (i)
print ("**********************")
    
i=0
while i<len(subjects):
    print(subjects[i])
    i+=1
print ("**********************")



for i in subjects:
    n=subjects.index(i)
    sub=input(f"Please give your sub you want to change for {n+1} : ")
    
    subjects[n]=sub
  
print (subjects)