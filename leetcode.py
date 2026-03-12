x = 121

if str(x) == str(x)[::-1]:
    print(True)
else:
    print(False)

nums = [1,1,2]

nums = list(set(nums))
print(nums)

n = 5

a = 1
b = 1

for i in range(n):
    a, b = b, a+b

print(a)