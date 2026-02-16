# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)

# ADD ELEMENT IN SET 
fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)

#REMOVE ELEMENT 
animals = {"dog", "cat", "cow"}

animals.remove("cat")     # Error if element not found
animals.discard("lion")   # No error if element not found

print(animals)

#CONDITIONAL STATEMENT IN SET
nums = {10, 20, 30}

if 20 in nums:
    print("20 is present")

# LOOPS IN SET
subjects = {"Math", "Science", "English"}

for sub in subjects:
    print(sub)
# SET OPERATION 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
