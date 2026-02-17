list1 = [45,65,48,2,4,5,2]
list2 = []
for i in list1:
    if i%2==0:
      list2.append(i)
    else:
       list2.append("none")
print(list2)