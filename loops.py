list1 = [45,65,48,2,4,5,2]
list2 = []
for i in list1:
    if i%2==0:
      list2.append(i)
    else:
       list2.append("none")
print(list2)
for i in range(1,11):
  print(i) 
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
for i in range(10):
    if i == 5:
        break
    print(i)