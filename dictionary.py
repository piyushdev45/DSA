info={"name":"piyush sharma",
      "age":"19",
      "fav game ":"cricket"

}
print(info)
#nested dictionary 
info2 ={
    "name ":"piyush sharma ",
    "subject":{
        "chemistry":87,
        "math":78
    }
}
print(info2)
print(len(info))
print(len(list(info2)))
new_dict={"name":"abhinav","age":18}
info.update(new_dict)
print(info)
# apply conditional statement
f={"apple":2,"orange":3}
n=input("enter your fruit name")
if n in f:
  print("fruit found")
else:
  print("fruit not found")