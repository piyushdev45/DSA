# x = 121

# if str(x) == str(x)[::-1]:
#     print(True)
# else:
#     print(False)

# nums = [1,1,2]

# nums = list(set(nums))
# print(nums)

# n = 5

# a = 1
# b = 1

# for i in range(n):
#     a, b = b, a+b

# print(a)

# def fizzBuzz(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result

# print(fizzBuzz(15))

# def findMin(nums):
#     return min(nums)

# print(findMin([3, 1, 7, 2]))

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isPrime(7))