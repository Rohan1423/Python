import numpy as np

# a = np.array([1,2,3,4]) # 1-d
# print(a)

# b = np.array([[0.5,1.2,3.5,2.2,3.4,5.6],[1.5,3.4,3.4,2.3,4.5,6.6]]) # 2-d
# print(b)

# # Get Dimensions
# print(a.ndim)
# print(b.ndim)

# # Get Shape 
# print(a.shape) # 1-d -> no. of elements
# print(b.shape) # 2 rows 3 cols

# # Get Type
# print(a.dtype)
# print(b.dtype)

# # Change Type
# c = np.array([1,2,3],dtype ="int32") # 1-d

# # Get Type
# print(c.dtype)

# # Get Size
# print(a.itemsize)
# print(b.itemsize)

# # Get Total Size
# print(a.nbytes)
# print(b.itemsize)

# # Accessing/Changing specific elements, rows, cols, etc

# # Get a specific element [r,c]
# print(a[1])
# print(b[1])
# print(b[0,0])
# print(b[0,-2]) # -ve indexing same as Lists

# # Get a specific row
# print(a[:])
# print(b[0,:])
# print(b[1,:])

# # Get a specific col
# print(a[1])
# print(b[:,0])
# print(b[1:,0])

# # Getting a little more fancy [startidx:endidx:stepsize]
# print(b[0,1:])
# print(b[0,1:3])
# print(b[0,1:4:2])
# print(b[0,-4:-1:2])

# # To Change Value
# a[1]=10
# print(a)

# b[1,5]=20.1
# print(b)

# b[:,2]=[5.3]
# print(b)

# b[:,2]=[4.4,3.3]
# print(b)

# # 3-d Example
# c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)

# # Get specific element (work outside in)
# print(c[0,1,1]) # 4
# print(c[:,0,:]) # [1,2] [5,6]
# print(c[:,0,0]) # [1 5]

# # replace
# c[:,1,:] = [9,10],[11,12] # it should be same dimension
# print(c)

# # Initializing different types of Arrays

# # ALl 0s matrix
# d = np.zeros((2,3))
# print(d)

# # ALl 1s matrix
# e = np.ones((4,2,2), dtype = 'int32')
# print(e)

# # Any other number
# f = np.full((2,2),99, dtype = 'float32')
# print(f)

# # Any other number (full_like)
# g = np.full_like(a,4) # it will take already built a shape
#                       # we can also write it as g = np.full(a.shape,4)  
# print(g)

# # Random decimal numbers
# h = np.random.rand(4,2)
# print(h)

# i = np.random.rand(4,2,3)
# print(i)

# j = np.random.random_sample(a.shape) # it will take already built a shape
# print(j)

# # Random Integer Values (low, high=None, size=None)
# k = np.random.randint(5, size = (2,2)) # 5 is the exclusive upper bond 
# print(k)

# l = np.random.randint(-2, 5, size = (2,2)) # 2 is inclusive the lower bond and 5 is exclusive the upper bond 
# print(l)

# # Identity Matrix -> Square Matrix
# m = np.identity(4)
# print(m)

# # Repeat an Array
# n = np.array([[1,2,3]])
# r1 = np.repeat(n,3,axis=0)
# print(r1)

# output = np.ones((5,5))
# print(output)

# z = np.zeros((3,3))
# print(z)

# z[1,1] = 9
# print(z)

# output[1:4,1:4] = z # first 1:4 means from 1st row to 3rd row second 1:4 means from 1st col to 3rd col 
# print(output)

# # Copying an array

# p = np.array([1,2,3])
# q = p # wrong this will update p value also when we will changhe q value
# q[0] = 100
# print(q)
# print(p)

# r = np.array([1,2,3])
# s = r.copy() # this is the correct way to copy
# s[0] = 100
# print(s)
# print(r)

# Element-wise Arithmetic Operations
t = np.array([1,2,3,4])
print(t)

t += 2
print(t)

u = t - 2
print(u)

u = t * 2
print(u)

u = t / 2
print(u)

u = t ** 2
print(u)

v = np.array([1,0,1,0])
u = t+v
print(u)

# Take the sin of all values
u = np.sin(t)
print(u)

# Take the cos of all values
u = np.cos(t)
print(u)

# Linear Algebra
v = np.ones((2,3))
print(v)

w = np.full((3,2),2)
print(w)

x = np.matmul(v,w)
print(x)

# Find Determinant
y = np.identity(3)
print(y)

z = np.linalg.det(y)
print(z)

# Statistics
stats = np.array([[1,2,3],[4,5,6]]) 
print(stats)

minimum = np.min(stats)
print(minimum)

maximum = np.max(stats)
print(maximum)

minimum = np.min(stats)
print(minimum)

minimum = np.min(stats,axis=1)
print(minimum)

maximum = np.max(stats,axis=0)
print(maximum)

sum = np.sum(stats)
print(sum)

sum = np.sum(stats,axis=1)
print(sum)

# Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,2,2)) # it will work until the shape is valid according to the total no. of elements 2x2x2 = 8
print(after)

# Vertically Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

result = np.vstack([v2,v1,v1,v2]) 
print(result) # [[5 6 7 8]
#                [1 2 3 4]
#                [1 2 3 4]
#                [5 6 7 8]]

# Horizontally Stacking Vectors
h1 = np.array([1,2,3,4])
h2 = np.array([5,6,7,8])

result = np.hstack([v2,v1,v1,v2]) # [5 6 7 8 1 2 3 4 1 2 3 4 5 6 7 8]
print(result)

# Load Data from File
filedata = np.genfromtxt('/Users/rohanchauhan/Desktop/Python/NumPy/data.txt',delimiter=',')  # automatically casted the data to float type
newdata = filedata.astype('int32')
print(filedata)
print(newdata)

# You can index with a list in NumPy
aa = np.array([1,2,3,4,5,6,7,8,9])
print(aa[[1,2,8]])

# Boolean Masking and Advanced Indexing
print(filedata>50) # this will check each data value in the file and return true/false for that
print(filedata[filedata>50]) # this will return only the values greater than 50
print(np.any(filedata>50,axis=0))
print(np.all(filedata>50,axis=0))
print((filedata > 50) & (filedata < 100))
print(~(filedata > 50) & (filedata < 100)) # ~ this means not