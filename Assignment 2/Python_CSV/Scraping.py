#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


csv_wiki = requests.get ("https://en.wikipedia.org/wiki/Comma-separated_values")
soup = BeautifulSoup(csv_wiki.text, 'html.parser')


# In[5]:


ths=soup.find(id='Example')
table = ths.findNext('pre').text
table


# In[6]:


f = open('car.csv','w')
f.write(table)
f.close()


# In[7]:


import pandas as pd
pd.read_csv('car.csv')

