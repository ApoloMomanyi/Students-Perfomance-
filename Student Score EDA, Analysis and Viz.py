#!/usr/bin/env python
# coding: utf-8

# In[112]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Reading the data 

# In[86]:


data=pd.read_csv("C:/Users/HP/Downloads/StudentsPerformance.csv")
data.head()


# In[87]:


# Checking the rows and columns in the dataframe
data.shape


# In[89]:


#Checking th individual Columns
data.columns


# In[90]:


"""
Checking for the datatypes and see if all
are in the correct datatype i.e numeric values with 
either int or float dtype
"""
data.dtypes


# In[91]:


"""
Checking for missing values and see what I can do with them
either fill or drop them
"""
data.isnull().sum()
# We do not have null values in our df data


# In[92]:


"""
Renaming the files to look appealing and uniform
Remember when to use inplace=True is only when you do not assign as
data=dat.rename(...
else use inplace=True
Remember to make a copy when assigning
"""
data=data.rename(columns={"gender":"Gender","race/ethnicity":"Race/Ethnicity",
                      "parental level of education":"Parents_EducationLevel",
                     "lunch":"Lunch_Program","test preparation course":"Test_PreparationCourse",
                    "math score":"Math_Score","reading score":"Reading_Score","writing score":"Writing_Score"}).copy()
data.head()


# In[93]:


# checking on any duplicates in the dataframe
data.loc[data.duplicated()]


# In[95]:


"""
This is unnecessary here because we have many students from each gender
there is a possibility of duplication for each subset
""" 
y=data.loc[data.duplicated(subset=["Gender"])]
y.head()


# In[96]:


data.head()
# Our data is now some how clean and presentable 
# to enable us draw some insights 


# # Data Analysis and Visualization

# In[97]:


"""
Creating a bar graph showing how students from various races
averagely perform in the three test
"""
data.groupby("Race/Ethnicity")[["Math_Score","Reading_Score","Writing_Score"]].mean().plot(kind="bar",figsize=[5,5])
plt.xlabel("Race/Ethnicity")
plt.ylabel("Score")
plt.suptitle("Race/Ethnicity and Score")
plt.show()

# You can see students from ethnicity E performed averagely well in all subjects 


# In[98]:


#checking the average score by gender
data.groupby("Gender")[["Math_Score","Reading_Score","Writing_Score"]].mean()


# In[113]:


# Finding the average scores for the three subjects
data[["Math_Score","Reading_Score","Writing_Score"]].mean()


# In[114]:


#You can as well use this inbuilt pandas function
data.describe()


# In[101]:


# Showing how females prepare for the exams
y=data[data["Gender"]=="female"]["Test_PreparationCourse"].agg(pd.Series.mode)
print(y)
#Most female students did not complete preparations for the exams


# In[102]:


#checking the average score by parental Education level
data.groupby("Parents_EducationLevel")[["Math_Score","Reading_Score","Writing_Score"]].mean()
#students whose parents have masters degree performed well in all subjects
#With exemplarly performance in reading and writing


# In[103]:


data.groupby("Test_PreparationCourse")[["Math_Score","Reading_Score","Writing_Score"]].mean()
#Students who completed the preparation performed well in all the subjects


# In[104]:


data.groupby("Lunch_Program")[["Math_Score","Reading_Score","Writing_Score"]].mean()
#Students with a standard lunch program performed well in all the subjects


# In[115]:


data[data["Gender"]=='female'][["Reading_Score","Writing_Score"]].plot(kind="scatter",
                     x="Reading_Score",y="Writing_Score",stacked=False)
plt.suptitle("Relationship between writing and reading score for females")
plt.savefig("png")
plt.show()
# This shows a high postive correlation between writing and reading scores for female students 


# In[111]:


data[data["Gender"]=='male'][["Math_Score","Writing_Score"]].plot(kind="scatter",
                     x="Math_Score",y="Writing_Score",stacked=False)
# This shows a high postive correlation between writing and Math scores for Male students 


# In[ ]:




