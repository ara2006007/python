d=[("name", "Seelan"),("age", 39),("gender", "male")]
data=dict(d)
data["nic"]=200621401188
print (data)
data.update({"nic":34080998,"age":40} )
del data["name"]
print (data)
d=[("name", "Seelan"),("age", 39),("gender", "male")]
data["nic"]=200621401188
data=dict(d)
data.pop("age")
print (data)
d=[("name", "Seelan"),("age", 39),("gender", "male")]
data["nic"]=200621401188
data=dict(d) 
data.popitem()
print (data)
d=[("name", "Seelan"),("age", 39),("gender", "male")]
data["nic"]=200621401188
data=dict(d)
data.clear()
print (data)
