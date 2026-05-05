#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a1 = np.arange(8).reshape(2,4)
a2 = np.arange(8,16).reshape(2,4)

a1 + a2


# In[3]:


a5 = np.arange(3).reshape(1,3)
a6 = np.arange(12).reshape(4,3)

print(a5,a6)


# In[4]:


a5 + a6


# In[6]:


np.random.random()


# In[7]:


np.random.seed(1)
np.random.random()


# In[8]:


np.random.uniform(3,10)


# In[10]:


np.random.uniform(1,100,10).reshape(2,5)


# In[13]:


np.random.randint(1,10,15).reshape(3,5)


# In[15]:


a = np.random.randint(1,10,6)


# In[16]:


a


# In[17]:


np.max(a)


# In[18]:


np.min(a)


# In[20]:


a[np.argmax(a)]


# In[21]:


a[np.argmin(a)]


# In[22]:


np.argmin(a)


# In[23]:


a = np.random.randint(1,10,6)


# In[24]:


a


# In[25]:


a[a%2 == 1] = -1


# In[26]:


a


# In[33]:


a = np.random.randint(1,10,6)


# In[34]:


a


# In[35]:


out = np.where(a%2 == 1, -1, a)


# In[36]:


a


# In[37]:


out


# In[43]:


a = np.random.randint(1,50,10)


# In[44]:


a


# In[45]:


a = np.sort(a)
a


# In[46]:


np.percentile(a,25)


# In[48]:


np.percentile(a,99.8)


# In[ ]:




