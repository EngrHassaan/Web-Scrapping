#!/usr/bin/env python
# coding: utf-8

# In[66]:


#First of all import the module requests to get the url of the website
import requests as req


# In[67]:


#Getting the data with the help of "get" function
url=req.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
url


# In[68]:


#Import BeautifulSoup from the package "bs4" in order to get the data from a website
from bs4 import BeautifulSoup


# In[72]:


#Here we've got all the data in text form from the website (Html Parser)
soup=BeautifulSoup(url.text,'html.parser')
soup


# In[55]:


#Here We have find all the required tags of html and stored the result in "results"
results=soup.find_all('span',attrs={'class':'short-desc'})
results[0]


# In[60]:


#We have stored all the data in the list "records" in order to form the different columns to get the data clean
records=[]
for result in results:
    date=result.find('strong').text[0:-1]+', 2020'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-2]
    url=result.find('a')['href']
    records.append([date,lie,explanation,url])
    
    


# In[61]:


#Data have stored separately in the form of a list
records


# In[59]:


#Import the module pandas to get the data in the tabular form and we've given them different names accordingly
import pandas as pd
df=pd.DataFrame(records,columns=['Date','Lie','Explanation','URL'])
df


# In[49]:


#Finally We have stored the data or exported in csv format and now this dataset can be use for data analysis 
df.to_csv('Record', index=False, encoding= "utf-8")

