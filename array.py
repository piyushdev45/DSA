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