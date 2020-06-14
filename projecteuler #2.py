#!/usr/bin/env python
# coding: utf-8

# In[4]:


# here i attempt to create a list whose terms are the first few of fibonacci's famous sequence.
fib = 0
fiblist = [0, 1, 1, 2]
fibsum = 0


# In[5]:


while len(fiblist) < 4000:
    fiblist.append(fiblist[-1] + fiblist[-2])
    fib += 1
    if fiblist[-1] >= 4000000:
        break
print(fiblist)


# In[6]:


for e in fiblist:
    if e % 2 == 0:
        fibsum += e
print(fibsum)


# In[ ]:


# EUREKA!

