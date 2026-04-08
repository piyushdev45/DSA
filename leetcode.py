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

# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(isPrime(7))

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))

# def sumEven(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             total += i
#     return total

# print(sumEven(10))

# def twoSum(numbers, target):
#     left, right = 0, len(numbers) - 1
    
#     while left < right:
#         s = numbers[left] + numbers[right]
        
#         if s == target:
#             return [left + 1, right + 1]
#         elif s < target:
#             left += 1
#         else:
#             right -= 1

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length