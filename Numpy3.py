#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


arr1 = np.array([1,2,3,4,5])
arr1


# In[4]:


type(arr1)


# In[5]:


arr2 = np.array([[1,2,3],[4,5,6]])
arr2


# In[6]:


arr3 = np.zeros((2,3))
arr3


# In[7]:


arr4 = np.ones((3,3))
arr4


# In[8]:


arr5 = np.identity(5)


# In[9]:


arr5


# In[10]:


arr6 = np.arange(5,16,2)
arr6


# In[11]:


arr7 = np.linspace(10,20,10)
arr7


# In[12]:


arr8 = arr7.copy()
arr8


# In[13]:


lista = range(100)
liasta


# In[ ]:


arr11 = np.arange(100)


# In[ ]:


import sys


# In[14]:


print(sys.getsizeof(87)*len(lista))


# In[15]:


print(arr11.itemsize*arr11.size)


# In[16]:


import time


# In[ ]:





# In[17]:


x = range(10000000)
y = range(10000000,20000000)
start_time = time.time()
c = [(x,y) for x,y in zip(x,y)]

print(time.time() - start_time)


# In[18]:


a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start_time = time.time()
c = a+b

print(time.time() - start_time)


# In[19]:


arr12 = np.arange(24).reshape(6,4)
arr12


# In[20]:


arr12[:,1:3]


# In[21]:


arr12[2:4,1:3]


# In[22]:


arr12[4:6,2:]


# In[23]:


for i in arr12:
    print(i)


# In[24]:


for i in np.nditer(arr12):
    print(i)


# In[25]:


arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])


# In[26]:


arr1 - arr2


# In[27]:


arr1*arr2


# In[28]:


arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])


# In[29]:


arr1-arr2


# In[30]:


arr1*arr2


# In[31]:


arr1*2


# In[32]:


arr2>3


# In[33]:


arr3 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)


# In[34]:


arr3.dot(arr4)


# In[35]:


arr1.dot(arr2)


# In[36]:


arr1.dot(arr3)


# In[ ]:


arr4


# In[ ]:


arr4.max(axis=0)


# In[ ]:


arr4.min(axis=1)


# In[37]:


arr4.sum()


# In[38]:


arr4.median()


# In[39]:


arr4.std()


# In[40]:


np.sin(arr4)


# In[41]:


np.median(arr4)


# In[42]:


np.exp(arr4)


# In[43]:


(/converts, higher, dim, arrays, to, lower, dimensions)


# In[44]:


arr4.ndim


# #### 

# In[45]:


arr4.ndim


# In[46]:


arr4.ravel()


# In[47]:


arr4.transpose()


# In[48]:


arr3


# In[49]:


arr5 = np.arange(12,18).reshape(2,3)


# In[50]:


arr5


# In[51]:


np.hstack((arr3,arr5))


# In[52]:


np.vstack((arr3,arr5))


# In[53]:


arr3


# In[55]:


np.hsplit(arr3,3)


# In[56]:


np.vsplit(arr3,2)


# In[ ]:




