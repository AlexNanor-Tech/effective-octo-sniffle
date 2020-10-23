#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn 


# # Load CSV into Memory 
# 
# data = pandas.read_csv('Downloads/uber-raw-data-apr14.txt') 
# data.tail()

# # Convert Column to Datetime and Add Columns 

# In[9]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[7]:


data.tail()


# In[10]:


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)


# In[11]:


data.tail()


# In[16]:


def get_weekday(dt): 
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt): 
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# # Analysis by Day

# In[23]:


hist(data.dom, bins = 30, rwidth = .8, range=(0.5, 30.5))
xlabel('Date of Month')
ylabel('Frequency')
title('Frequency of Rides Per DoM in Uber Data - April 2014')


# In[31]:


#for k, rows in data.groupby('dom'): 
#    print((k,rows))

def count_rows(rows): 
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[33]:


bar(range(1,31), by_date)


# In[34]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[36]:


bar(range(1,31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index); 
xlabel('Date of Month')
ylabel('Frequency')
title('Frequency of Rides Per DoM in Uber Data - April 2014')


# # Analysis by Hour

# In[37]:


hist(data.hour, bins = 24, range=(0.5, 24))


# # Analysis by Weekday 

# In[41]:


hist(data.weekday, bins = 7, range = [-.5, 6.5], rwidth=0.8, color='green')
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun '.split())


# # Cross-Analysis by Hour and Day of Week 

# In[48]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[50]:


seaborn.heatmap(by_cross)


# # Analysis by Latitude and Longitude 

# In[52]:


hist(data['Lat'], bins=100, range(40.5, 41))
("")


# In[53]:


hist(data['Lon'], bins=100);


# In[60]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color = 'g', alpha = .5); 
grid()
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='r', alpha = 0.5); 
grid()
legend()


# # Outline of Manhattan, NY

# In[73]:


figure(figsize=[40, 40])
plot(data['Lon'], data['Lat'],'.', ms = 1, color = 'r', alpha = .5 )
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:




