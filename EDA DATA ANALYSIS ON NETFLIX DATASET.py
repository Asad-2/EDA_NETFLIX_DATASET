#!/usr/bin/env python
# coding: utf-8

# ![download.png](attachment:download.png)
# 
# The netflix dataset has the information of tv shows and movies 

# In[1]:


import numpy as np #numeric maths
import pandas as pd # use for data prepration 


# In[2]:


#df = pd.read_csv(r"‪C:\Users\HP\Documents\netflix_titles.csv")
df = pd.read_csv(r"C:\Users\HP\Documents\netflix_titles.csv", encoding='latin1')
# or
#df = pd.read_csv(r"C:\Users\HP\Documents\netflix_titles.csv", encoding='cp1252')
df


# ### Get some info about the dataset
# 
# 1 head()
# 2 tail()
# 3 shape

# In[3]:


df.head(10) #show the top 5 rows


# In[4]:


df.tail(10) #show the last 5 rows


# In[5]:


df.shape  #total number of rows and total number of columns


# In[6]:


df.size #total number of element in the dataset


# In[7]:


df.columns  # tell the all names of columns


# In[8]:


df.dtypes              # to show the data type of each column


# In[9]:


df.info() # to show index columns data types of each columns 


# ## Task 1: Is there is any duplicate record in the dataset ? if yes then remove the duplicate steps 

# In[10]:


df.head()


# In[11]:


df.shape


# In[12]:


df[df.duplicated()]


# In[13]:


df.drop_duplicates(inplace = True)


# In[14]:


df[df.duplicated()]


# In[15]:


df.shape


# ## Task 2 Is there is any null values is any columns? Show with heat map 

# ### isnull()

# In[15]:


df.head()


# In[16]:


df.isnull()                               # to show where null values is present 


# In[17]:


df.isnull().sum()


# ## heat-map (seaborn)

# In[21]:


import seaborn as sns                                   # to import sea born libarary


# In[20]:


sns.heatmap(df.isnull())


# ## Q1. For blood and water what is the show id and who is the director of the show
# 
# ### isin()

# In[18]:


df.head()


# In[27]:


df[df['title'].isin(['Blood & Water'])]


# In[33]:


df[df['title'].str.contains('Blood & Water')]


# ## Q2. In which year highest number of tv shows & Movies were released? Show with Bar chart 
# 
# ### dtype()

# In[22]:


df.dtypes


# ### to_datetime 

# In[27]:


df['Date_N'] = pd.to_datetime(df['date_added'])


# In[29]:


df.head()


# ### dt.year.value_counts()

# In[31]:


df['Date_N'].dt.year.value_counts()  #it counts the all occurrence of individual year in date columns


# ### Bar Graph

# In[33]:


df['Date_N'].dt.year.value_counts().plot(kind='bar')


# # Q3. how many types of tv shows and movies in this dataset

# ### Groupby()

# In[35]:


df.head()


# In[36]:


df.groupby('type').type.count()  #To group all unique items of column and show their count 


# ### Countplot()

# In[44]:


print(df['type'].unique())
sns.countplot(x='type', data=df)    # To show the count of all unique values of any column in the form of bar graph 


# # Q4 Show all the movies that were released in year 2000

# ## Creating new column

# In[45]:


df.head()


# In[55]:


df [(df['type'] == 'Movie') & (df['release_year']==2000)]


# # Q5. Show only the title of all tv shows that were released in us only 

# In[56]:


df.head(4)


# In[61]:


df [(df['type']== 'TV Show') & (df['country'] == 'United States')]


# In[64]:


df  [(df['type']== 'TV Show') & (df['country'] == 'United States')] ['title'] 


# In[65]:


df  [(df['type']== 'TV Show') & (df['country'] == 'United States')] ['director'] 


# ## Q6 Show Top 10 director who gives the higest number of TV shows & Movie on netflix 

# ### values_count() 

# In[67]:


df['director'].value_counts().head(10)


# ### Q7 Show all the records , where type is movie and listed_in is comedies or country is united kingdom

# ### Filtering with And and Or operator 

# In[70]:


df.head()


# In[71]:


df [(df['type'] == 'Movie') & (df['listed_in'] == 'Comedies')] 


# In[72]:


df [(df['type'] == 'Movie') & (df['listed_in'] == 'Comedies') | (df['country']== 'United Kingdom')] 


# # Q8 In how many movies/Shows , Tom cruise were cast ?
# 

# In[73]:


df.head()


# In[90]:


df [df['cast'] == 'Tom Cruise']


# In[92]:


df[df['cast'].str.contains('Tom Cruise')]


# In[95]:


df_new = df.dropna()


# In[96]:


df_new.head()


# In[98]:


df_new[df_new['cast'].str.contains('Tom Cruise')]


# # Q9 What are the different rating by netflix?

# ### nunique()

# In[99]:


df['rating'].nunique()


# ### unique()

# In[100]:


df['rating'].unique()


# # Q10 how many movies got the 'tv-14' rating in canada 

# In[104]:


df[(df['type']=='Movie') & (df['rating']=='TV-14')].shape


# In[105]:


df[(df['type']=='Movie') & (df['rating']=='TV-14') & (df['country'] == 'Canada')]


# # Q11 How many tv shows got the R rating , after year 2018

# In[106]:


df.head()


# In[107]:


df[(df['type']=='TV Show') & (df['rating']=='R')]


# In[108]:


df[(df['type']=='TV Show') & (df['rating']=='R') & (df['release_year'] > 2018)]


# # Q12 maximum duration of movie show on netflix

# In[110]:


df.head(2)


# In[111]:


df.duration.unique()


# In[115]:


df.duration.dtypes


# In[125]:


df[['minutes' , 'unit']] = df['duration'].str.split(' ',expand = True)


# In[126]:


df.head(2)


# In[127]:


df['minutes']


# # Q13 which country has the highest number of tv shows

# In[130]:


df.head(3)


# In[131]:


df_tvshow = df[df['type'] == 'TV Show']


# In[132]:


df_tvshow.head(2)


# In[133]:


df_tvshow.country.value_counts()


# In[134]:


df_tvshow.country.value_counts().head(1)


# # 14 How can we sort dataset by year

# In[137]:


df.sort_values(by='release_year')


# In[138]:


df.sort_values(by='release_year' ,ascending = False)


# # Q15 Find all the instance where:
# 
# ## type is movie and listed_in is drama
# 
# ### or
# 
# ## Type is tv show ad listed_in is kids tv

# In[142]:


df [(df['type']=='Movie') & (df['listed_in'] == 'Dramas')].head(5)


# In[147]:


df [(df['type']=='Movie') & (df['listed_in'] =="Documentaries")].head(5)


# In[149]:


df[(df['type']=='Movie') & (df['listed_in'] == 'Dramas') | (df['type']=='Movie') & (df['listed_in'] =="Documentaries")]


# In[ ]:




