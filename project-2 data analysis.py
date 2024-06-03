#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)


# In[2]:


df


# In[3]:


# 1.display the top 10 rows
df.head(10)


# In[4]:


#2. check last 10 rows
df.tail(10)


# In[5]:


# Gettin the inforamtion about our dataset(like no of rows and no of columns)
df.info()


# In[6]:


df.describe()


# In[7]:


#check the null values in dataset
df.columns


# In[8]:


df.isnull()


# In[9]:


df.isnull().sum()


# In[10]:


#find the shape of the dataset
df.shape


# In[ ]:





# In[19]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)


# In[20]:


df=df.drop(["Id","Notes","Agency","Status"],axis=1)
print(df)


# In[ ]:





# In[23]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)


# In[24]:


df=df.drop(["Id","Notes","Agency","Status"],axis=1,inplace=True)
print(df)


# In[ ]:





# In[26]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)


# In[27]:


df.describe(include="all")


# In[28]:


#find occurence of the Employee names (top 5)
df.columns


# In[29]:


df["EmployeeName"]


# In[31]:


df["EmployeeName"].count()


# In[33]:


df["EmployeeName"].value_counts()


# In[34]:


df["EmployeeName"].value_counts().head()


# In[ ]:





# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)


# In[3]:


df.columns


# In[4]:


df["JobTitle"].str.contains("captain")


# In[11]:


df[df["JobTitle"].str.contains("Captain")]


# In[7]:


df[df["JobTitle"].str.contains("captain",case=False)]


# In[10]:


len(df[df["JobTitle"].str.contains("captain",case=False)])


# In[12]:


#findthe all employee names from fire department
df["JobTitle"]


# In[13]:


df["JobTitle"]=="FIRE DEPARTMENT"


# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("Downloads//Salaries.csv")
print(df)
df[df["JobTitle"]=="FIRE DEPARTMENT"]


# In[5]:


df["JobTitle"].nunique()


# In[6]:


df["JobTitle"].str.contains("Fire ", case=False)


# In[7]:


df[df["JobTitle"].str.contains("fire",case=False)]


# In[8]:


#find the max min and and avg basepay
df["BasePay"].describe()


# In[11]:


#replace 'not provided' in employeeNam
df['EmployeeName'].replace('Not provided',np.NaN)


# In[12]:


df["EmployeeName"]=df['EmployeeName'].replace('Not provided',np.NaN)
print(df["EmployeeName"])


# In[13]:


#drop the  rows having 5 missing values
df.isnull().sum(axis=1)==5


# In[14]:


df[df.isnull().sum(axis=1)==5]


# In[15]:


df.drop(df[df.isnull().sum(axis=1)==5],axis=0)


# In[17]:


df.drop(df[df.isnull().sum(axis=1)==5].index,axis=0)


# In[19]:


df.drop(df[df.isnull().sum(axis=1)==5].index,axis=0,inplace=True)


# In[27]:


#find job title of albert pardine
df[df["EmployeeName"]=='ALBERT PARDINI']['JobTitle']


# In[29]:


#how much albert pardini make (include Benifits)
df[df["EmployeeName"]=="ALBERT PARDINI"]["TotalPayBenefits"]


# In[30]:


#display the name of the person having the highesst Basepay
df.columns


# In[31]:


df["BasePay"].max()


# In[33]:


df["BasePay"].max()==df["BasePay"]


# In[34]:


df[df["BasePay"].max()==df["BasePay"]]["EmployeeName"]


# In[36]:


#find the avg BasePay of all employee per year
df.groupby("Year")


# In[39]:


df.groupby("Year").mean()


# In[40]:


#find the average BasePay of all Employee per JobTitle
df.groupby("JobTitle").mean()['BasePay']


# In[41]:


#find avg basepay of employee having job title accountant
df['JobTitle']=="ACCOUNTANT"


# In[43]:


df[df["JobTitle"]=="ACCOUNTANT"]['BasePay'].mean()


# In[44]:


#find top 5 most  common jobs
df["JobTitle"].value_counts().head()


# In[ ]:




