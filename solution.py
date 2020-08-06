#!/usr/bin/env python
# coding: utf-8

# # Introduction
# This is a test for seeing how well you can get around doing some basic statistical analyses on a dataset similar to the those that you would see while working at Carta.
# 
# In this analysis, you are assuming the role of a data scientist assigned the goal of understanding the usage of surgical supplies for different procedures and surgeons. You have been given a dataset of the supplies that are used for each surgical case, and also a second dataset which gives you the price of each of the items used in surgery. The dataset encompasses the last month of surgeries at your hospital.
# 
# ## The Goal
# Your goal is to answer the following questions:
# 
#  1. How many of each item were used over the last month?
#  2. What is the average number of items used for each procedure? 
#  3. What is the average total cost of supplies for each procedure?
# 
# ### Total Item Usage
# The output for 1) should look like a table with the following columns:
# 
# Item Name || Total Number of Items Used
# 
# ### Average Items per Procedure
# The output for 2) should be a table with the following columns:
# 
# Procedure Name || Average Number of Items Used per Case
# 
# ### Average Cost per Procedure
# The output for 3) should be a table with the following columns:
# 
# Procedure Name || Average Total Cost of Items Used per Case
# 
# # Dataset Overview
# Here is an explanation of the dataset you have been given:
# 
# ## hospital-supply-usage.csv
# 
# ```
# case_id: A unique identifier for a single surgical case
# primary_surgeon: The surgeon on the case
# primary_procedure: The name of the procedure that was performed
# item_name: The name of the item used
# item_id: A unique id for each item
# number_used: The number of items used
# number_wasted: The number of items wasted
# ```
# 
# ## pricing.csv
# ```
# item_id: A unique identifier for the item (will match item_id in the hospital-supply-usage.csv dataset)
# price: The price of the item
# ```
# 
# # Sending your solution
# Once you're done, export your solution to a python file (File > Download as > Python), and send it to matt@carta.healthcare.
# 
# Feel free to reach out if you have questions along the way!

# In[3]:


import numpy as np
import pandas as pd
from carta_interview import Datasets, get_data_file

USAGE_FILENAME = get_data_file(Datasets.SUPPLY_USAGE)
PRICING_FILENAME = get_data_file(Datasets.PRICING)


# In[17]:


usage_df = pd.read_csv(USAGE_FILENAME)
pricing_df = pd.read_csv(PRICING_FILENAME)


# In[18]:


usage_df


# In[19]:


pricing_df


# # Task 1

# In[21]:


usage_df.groupby(['item_name'])['number_used'].agg('sum').to_frame().reset_index().rename(columns={'item_name': 'Item Name', 'number_used': 'Total Number of Items Used'})


# # Task 2

# In[26]:


summed = usage_df.groupby(['primary_procedure', 'case_id']).agg(sum_per_case=('number_used', 'sum'))
avarage_items_used = summed.groupby(['primary_procedure'])['sum_per_case'].agg('mean')
found = avarage_items_used.reset_index().rename(columns={'primary_procedure': 'Procedure Name', 'sum_per_case': 'Average Number of Items Used per Case'})
found


# In[34]:


# Task 3


# In[35]:


dfp = pd.merge(usage_df, pricing_df, how='inner', on='item_id')
dfp['total_price'] = dfp['number_used'] * dfp['price']
result = dfp.groupby(['primary_procedure', 'case_id']).agg(total_cost_per_case=('total_price', 'sum')).groupby('primary_procedure')['total_cost_per_case'].agg('mean')
result.reset_index().rename(columns={'primary_procedure': 'Procedure Name', 'total_cost_per_case': 'Average Total Cost of Items Used per Case'})


# In[ ]:




