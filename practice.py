n = 5
for i in range(1,n+1):
    print(" "*(n-i) + (2*i-1)*"*")

n = int(input("enter your number"))
for i in range(1,11):
  print(n,"*",i,"=",n*i)


for i in range(1,101):
  if i%3==0 and i%5!=0:
    print(i)

def convertor(mass_val):
  gram_val=mass_val*1000
  print(f"{mass_val}kg is {gram_val}g")
convertor(3.5)

n= int(input("enter your number"))
if n%5==0:
  print("multiple of 5")
elif n%11==0:
  print("multiple of 11")
else:
  print("not multiple of 5 and 11")