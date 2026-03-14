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

num = 121
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
s = "PyThOn ProGRamMing"

upper = 0
lower = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print("Upper:", upper)
print("Lower:", lower)
nums = [1,2,3,4,5]
k = 2

k = k % len(nums)

nums = nums[-k:] + nums[:-k]

print(nums)

from itertools import permutations

nums = [1,2,3]

perm = permutations(nums)

for i in perm:
    print(i)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c1 = Car("Toyota", "Fortuner")
c1.show_details()

n= input("enter your name ")
d=int(input("enter your age"))
print("name:",n)
print("age:",d)


import random 
def generate_random_number(start, end):
    return random.randint(start, end)
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
random_number = generate_random_number(start, end)
print(f"Generated random number between {start} and {end}: {random_number}")


class client:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if self.age < 18:
            print("client is minor")
        else:
                print("client is major")    
c1=client("john",17)
c2=client("doe",25) 
    
