#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})


# In[3]:


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})


# In[4]:


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


# In[5]:


pd.Series([1, 2, 3, 4, 5])


# In[6]:


pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


# In[7]:


import pandas as pd
pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")


# In[8]:


pd.DataFrame ({'Apples' : [30] , 'Bananas' : [21]} , index = ['0'])


# In[11]:


fruits = pd.DataFrame ({'Apples' : [30] , 'Bananas' : [21]} , index = ['0'])


# In[23]:


df = pd.DataFrame ({'Apples' :['35' , '41'] ,
               'Bananas' :  ['21' , '34']} , 
              index=['2017 Sales' , '2018 Sales'])
print(df)


# In[21]:


import pandas as pd

df = pd.DataFrame({'Apples': ['35', '41'],
                   'Bananas': ['21', '34']},
                  index=['2017 Sales', '2018 Sales'])

print(df)


# In[24]:


import pandas as pd

ingredients = pd.Series({
    'Flour': '4 cups',
    'Milk': '1 cup',
    'Eggs': '2 large',
    'Spam': '1 can'
}, name='Dinner')

print(ingredients)


# In[25]:


animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals


# In[ ]:




