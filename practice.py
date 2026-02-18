n = 5
for i in range(1,n+1):
    print(" "*(n-i) + (2*i-1)*"*")

n = int(input("enter your number"))
for i in range(1,11):
  print(n,"*",i,"=",n*i)


for i in range(1,101):
  if i%3==0 and i%5!=0:
    print(i)

