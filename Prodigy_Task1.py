#!/usr/bin/env python
# coding: utf-8

# In[23]:


import csv
import statistics as stat
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


bank=pd.read_csv('bank-full.csv')


# In[3]:


bank.head(5)


# In[4]:


bank.columns


# In[5]:


bank['age']


# In[6]:


age=bank['age']


# In[7]:


print(age)


# In[8]:


mean=stat.mean(age)


# In[9]:


sd=stat.stdev(age)


# In[10]:


print("Mean : ",mean ," S.D. : ",sd)


# In[11]:


plt.hist(age)


# In[12]:


plt.plot(age)


# In[13]:


plt.plot(age,norm.pdf(age,mean,sd))


# In[14]:


bank.hist()


# In[20]:


bank.corr()


# In[26]:


sns.heatmap(bank.corr())


# In[28]:


sns.scatterplot(x='age',y='balance',data=bank)


# In[ ]:




