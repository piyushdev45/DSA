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

  
class fruit:
  def __init__(self,name,color,flavour):
    self.name=name
    self.color=color
    self.flavour=flavour
  def taste(self):
    print(f" i am eating {self.color} {self.name} which taste is {self.flavour}")
f1=fruit("apple","red","tart")
f2=fruit("banana","yellow","sweet")
f1.taste()
f2.taste()
 
def findMax(nums):
    return max(nums)

print(findMax([3, 5, 1, 9, 2]))
def sumOfDigits(n):
    return sum(map(int, str(n)))

print(sumOfDigits(12346))

list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in list] 
if squared_list:
    print(squared_list) 
else:    print("The list is empty.")    

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))

nums = [1, 2, 3, 4, 5]
rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])

print(rev)
