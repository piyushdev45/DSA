arr = [1, 2, 3, 4, 5]

for i in arr:
    print(i)
    arr = [10, 20, 30, 40]
total = 0

for i in arr:
    total += i

print("Sum:", total) 

arr = list(map(int, input("Enter numbers: ").split()))
print(arr)
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)
arr = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)