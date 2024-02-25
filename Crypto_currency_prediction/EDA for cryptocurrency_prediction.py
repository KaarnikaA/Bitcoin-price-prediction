#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv(r"C:\Users\Kaarvin\Downloads\BTC-INR.csv")


# In[4]:


df


# In[6]:


df.shape


# In[8]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.isna().sum()


# In[12]:


sns.heatmap(df.isnull(),yticklabels=False,cmap='viridis')


# In[15]:


sns.distplot(df.Close)


# In[17]:


sns.boxplot(df.Close)


# In[19]:


data=pd.read_csv(r"C:\Users\Kaarvin\OneDrive\Documents\archive (1)[1]\all_currencies.csv")


# In[20]:


data


# In[22]:


data.shape


# In[23]:


data.describe()


# In[25]:


data.info()


# In[26]:


data.isna().sum()


# In[27]:


data["Market Cap"].head()


# In[28]:


data["Market Cap"]=data["Market Cap"].replace(np.nan,0)


# In[29]:


data["Market Cap"].head()


# In[31]:


data.tail(5)


# In[36]:


sns.scatterplot(data=data,y='Close',x='Open')


# In[40]:


sns.distplot(data['High'],bins=30)


# In[ ]:




