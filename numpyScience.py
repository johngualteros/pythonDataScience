import numpy as np

x = np.array([1, 2, 3, 4])

arrayMultidimensional = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# return the number of dimensions of the array
print(arrayMultidimensional.ndim)
# return the total number of elements in the array
print(arrayMultidimensional.size)
# return the tuple of elements saved in each dimension of the array
print(arrayMultidimensional.shape)

x = np.append(x, 40)
x = np.delete(x, 0)
x = np.sort(x)

x = np.arange(2, 10, 3)

# if only have 1 argument is the total elements in one list
z = x.reshape(3, 2)

# CONDITIONS

i = np.arange(1, 10)
print(i[i < 4])

print(i[(i > 5) & (i % 2 == 0)])

print(i.sum())

print(np.mean(i))
print(np.median(i))
print(np.var(i))
print(np.std(i))
