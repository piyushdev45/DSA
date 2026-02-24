a=[[4,5,6],[3,4,5]]
b=[[2,3,4],[6,7,8]]
result_mul =[[0 for _ in range (len(b[0]))]for _ in range (len(a))]
for j in range (len(b[0])):
  for i in range(len(a)):
    for k in range(len(b)):
      result_mul[i][j]+=a[i][k]*b[k][j]
print("multiplication:\n",result_mul)