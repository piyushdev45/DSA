# list1 = [45,65,48,2,4,5,2]
# list2 = []
# for i in list1:
#     if i%2==0:
#       list2.append(i)
#     else:
#        list2.append("none")
# print(list2)
# for i in range(1,11):
#   print(i) 
# n = 5
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# list1 = [45,65,48,2,4,5,2]
# for i in list1:   
#     if i%2==0:
#       print(i)
#     else:
#        print("none")    

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# top, bottom = 0, len(matrix) - 1
# left, right = 0, len(matrix[0]) - 1

# while top <= bottom and left <= right:
    
#     # left → right
#     for i in range(left, right + 1):
#         print(matrix[top][i], end=" ")
#     top += 1

#     # top → bottom
#     for i in range(top, bottom + 1):
#         print(matrix[i][right], end=" ")
#     right -= 1

#     if top <= bottom:
#         # right → left
#         for i in range(right, left - 1, -1):
#             print(matrix[bottom][i], end=" ")
#         bottom -= 1

#     if left <= right:
#         # bottom → top
#         for i in range(bottom, top - 1, -1):
#             print(matrix[i][left], end=" ")
#         left += 1


if __name__ == "__main__":
    a = [[5,6,9],[2,3,6]]
    m = [ [4,5,6],[2,3,7]]

    dd = [[a[i][j] + m[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    print("Aura addition:\n",dd)  