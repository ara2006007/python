d={
    "name":"Ara",
    "age":20,
    "gender":"Male"
}
key=d.keys()
print(key)
value=d.values()
print(value)
items=d.items()
print(items)

for k in d.keys():
    print (k,d[k])
for k,i in d.items():
    print(k,i)
    
d1=d.copy()
d1["name"]="Thana"
print (d)
print(d1)