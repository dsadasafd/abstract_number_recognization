#!/usr/bin/env python
# coding: utf-8

# In[70]:


data_file = open("C:\\Users\\Administrator\\Desktop\\mnist_dataset\\mnist_train_100.csv","r")
data_list = data_file.readlines()
data_file.close


# In[71]:


len(data_list)


# In[97]:


data_list[0]


# In[98]:


import numpy
import matplotlib.pyplot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[99]:


all_values = data_list[0].split(',')
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
matplotlib.pyplot.imshow(image_array, cmap='Greys',interpolation='None')


# In[92]:


# scale input to range 0.01 to 1.00
scale_input = numpy.asfarray(all_values[1:])/255.0*0.99+0.01
print(scale_input)


# In[94]:


targets = numpy.zeros(10)+0.01
targets[int(all_values[0])]=0.99
targets


# In[101]:


a=range(3)
print(a)


# In[102]:


type(a)


# In[ ]:




