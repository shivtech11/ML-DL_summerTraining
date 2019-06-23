#!/usr/bin/env python
# coding: utf-8

# <font size=5>2D Lists</font>

# <p>We use lists to store data like in arrays, but what if we want to store, say arrays as elements in an array? How do we make a list of lists maybe? This is where 2D lists come in.</p>
# <p>Two dimensional array is an array within an array. It is an array of arrays. In this type of array the position of an data element is referred by two indices instead of one. So it represents a table with rows an dcolumns of data. In the below example of a two dimensional array, observer that each array element itself is also an array.</p>
# <p>The data elements in two dimesnional arrays can be accessed using two indices. One index referring to the main or parent array and another index referring to the position of the data element in the inner array. If we mention only one index then the entire inner array is printed for that index position. </p>

# In[17]:


# Declaring a 2D array
myArr = np.array([[1,2],[3,4]])

# Taking input into a 2D array
str = input().strip().split(" ")
n = int(str[0])
m = int(str[1])
l = [int(i) for i in input().strip().split(" ")]

out = []
for i in range(n):
    out.append([])
    for j in range(m):
        out[i].append(l[i*m+j])
        
print(out)

# The above work done in a single line.
out2 = [[l[i*m+j] for j in range (m)] for i in range (n)]
print(out2)


# <font size=5>Wave Print</font>

# <p>The problem of wave print is an important one to know and understand. Given a 2D list, how can you print a wave pattern? That is, you need to print the list elements which form a wave pattern in the list.</p>
# <p>We rationalize that since the wave is to be printed in an up-and-down fashion, we traverse downwards for even iterations and upwards for odd iterations. The code for the problem is given below.</p>

# In[18]:


n = len(out2)
m = len(out2[0])

for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            print(out2[i][j],end=" ")
    else:
        i = n - 1
        while(i>=0):
            print(out2[i][j],end=" ")
            i = i - 1
            


# <font size=5>Importing Modules</font>

# <p>To use various functionalities in Python, it is very difficult and cumbersome to write code for each from scratch. Hence, we use in-built modules for ease of work.</p>
# </p>If we are importing a module with a big name, we can import it as a shortcut as well. Note that we have to use the name to import further functions from it, or an error will be displayed.</p>

# In[2]:


import pandas as pd         # Writing pandas everywhere is cumbersome, so we've imported it as pd.
from pandas import read_csv # if you import like this, then you don't need to write pd.read_csv() to call it, you can simply 
                            # write read_csv() and use it.
from pandas import *        # This has imported everything in the pandas module.


# <font size=5>Numpy</font>

# <p>Arrays in Python are a bit slow as compared to other languages. This is because unlike in other languages, elements in Python arrays are not stored compactly, rendering Python arrays ineffective in terms of speed. This problem is solved by using Numpy, a library in Python.</p>p>
# Note that elements in numpy arrays have to be of the same type unlike in lists. We can insert, perform slicing and access elements in numpy arrays just the same as in lists.
# </p>

# In[2]:


import numpy as np # importing Numpy
l = [1,2,3]
arr = np.array(l) # converted list to numpy array

myArr = np.ones((1,3))
print(myArr)


# <font size=5>Numpy Operations</font>

# <p>NumPy’s array class is called ndarray. Let us take a look at some common numpy operations.</p>
# <ol><li>ndarray.ndim:
#     the number of axes (dimensions) of the array.</li><li>
# ndarray.shape:
# the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.</li><li>
# ndarray.size:
# the total number of elements of the array. This is equal to the product of the elements of shape.</li><li>
# ndarray.dtype:
# an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.</li>
# </ol>

# In[3]:


myArr = np.array([1,2,3,4,5])

emptyArr = np.empty((1,2)) # initializes a numpy array with no values
print(myArr + 4) # This would have given an error in case of a list but not for a numpy array.

print(np.max(myArr)) # Prints the maximum element in myArr

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[8,9]])
print(a1.dot(a2)) # computes dot product

a = np.arange(15).reshape(3, 5)

print(a.shape)

print(a.ndim)

print(a.dtype.name)

print(a.itemsize)

print(a.size)

print(type(a))

