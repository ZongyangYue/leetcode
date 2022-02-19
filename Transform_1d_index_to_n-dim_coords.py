# Transform 1-d index into n-dimensional coordinates
# example: 1-d array of length 12 reshaped into shape(2, 2, 3):
# [
#  [[1,2, 3],
#  [4, 5, 6]],
#  [[7,8, 9],
#  [10, 11, 12]] 
# ] 

#shape = [2, 2, 3]
# 8 -> (1, 0, 2)
# 5 -> (0, 1, 2)

#shape: [d1, d2, ..., dm]
#index: 1-d index

#output: coordinates, len = len(shape)

#algorithm:
# d = (d1, d2, d3)
#x = index // (d2 * d3)
#y = (index // d3) % d2
#z = index % d3

#generalized algorithm
#coord[1,...,m]
#coord[m] = index % shape[m]
#coord[m-1] = index//shape[m] % shape[m-1]
#coord[m-2] = (index//(shape[m] * shape[m-1]))% shape[m-2]
#...
#coord[1] = index // (shape[m] * ... * shape[2])
def factorial(start, shape):
  ans = 1
  for i in range(start, len(shape)):
    ans *= shape[i]
  return ans
  
def transform(shape, index):
  len_coord = len(shape)
  coord = [0] * len_coord
  #i iterate from (m-1, m-2, ..., 0)
  for i in reversed(range(len_coord)):
    # if i == len_coord-1:
    #   coord[i] = index % shape[i]
    # elif i == 0:
    #   coord[i] = index // factorial(i+1, shape)
    # else:
    coord[i] = (index // (factorial(i+1, shape))) % shape[i]
  return coord

print(transform([2, 2, 3], 8)) #output [1, 0, 2]
print(transform([2, 2, 3], 5)) #output [0, 1, 2]
