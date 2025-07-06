#!/usr/bin/env python
# coding: utf-8

# # **Automatidata project**
# **Course 2 - Get Started with Python**

# Welcome to the Automatidata Project!
# 
# You have just started as a data professional in a fictional data consulting firm, Automatidata. Their client, the New York City Taxi and Limousine Commission (New York City TLC), has hired the Automatidata team for its reputation in helping their clients develop data-based solutions.
# 
# The team is still in the early stages of the project. Previously, you were asked to complete a project proposal by your supervisor, DeShawn Washington. You have received notice that your project proposal has been approved and that New York City TLC has given the Automatidata team access to their data. To get clear insights, New York TLC's data must be analyzed, key variables identified, and the dataset ensured it is ready for analysis.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # Course 2 End-of-course project: Inspect and analyze data
# 
# In this activity, you will examine data provided and prepare it for analysis.  This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>    
# 
# **The purpose** of this project is to investigate and understand the data provided.
#   
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings. 
# <br/>  
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation 
# * Prepare to understand and organize the provided taxi cab dataset and information.
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities.
# 
# * Compile summary information about the data to inform next steps.
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into specific variables.
# 
# 
# <br/> 
# Follow the instructions and answer the following questions to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 
# 

# # **Identify data types and relevant variables using Python**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: **Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided taxi cab information? 

# **Response:**
# To prepare for understanding and organizing the taxi cab data, I would first identify the purpose of the dataset, the format of the data, review the columns and data types, check for missing values, anomalies or outliers, group related information (like trip details and fare data), and outline key questions to guide the analysis.

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: **Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Build dataframe**
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Create a pandas dataframe for data learning, and future exploratory data analysis (EDA) and statistical activities.
# 
# **Code the following,**
# 
# *   import pandas as `pd`. pandas is used for buidling dataframes.
# 
# *   import numpy as `np`. numpy is imported with pandas
# 
# *   `df = pd.read_csv('Datasets\NYC taxi data.csv')`
# 
# **Note:** pair the data object name `df` with pandas functions to manipulate data, such as `df.groupby()`.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[1]:


#Import libraries and packages listed above

import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
# 1. `df.head(10)`
# 2. `df.info()`
# 3. `df.describe()`
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the `df.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 2:** When reviewing the `df.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values?

# **Response Question 1** There are 18 variables where the first one is unnamed. In terms of data types, we have 8 floats, 7 integers and 3 objects.No null values. All the variables are not numeric because 3 variables are objects(tpep_pickup_datetime,tpep_dropoff_datetime are in string format and store_and_fwd_flag is in categorie).
# 
# **Response Question 2** Based on the describe() output, I observe that some variables like fare_amount and total_amount have unexpected minimum/maximum values. Fare amount of $999.99, Negative values for fare amount and trip distance of 33 miles are questionables. Tip amount and tolls amount have high standard deviations, which might indicate outliers or data entry errors. 

# In[2]:


df.head(10)


# In[2]:


df.info()


# In[3]:


df.describe()


# In[ ]:


#==> ENTER YOUR CODE HERE


# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# 
# **Question 2:** Sort by your second variable (`total_amount`), are any values unusual?
# 
# **Question 3:** Are the resulting rows similar for both sorts? Why or why not?

# **Response:**
# 
# **Question 1:**  The values align with our earlier data discovery, where we noticed that the longest rides are approximately 33 miles. #The values seems reasonable based on typical taxi usage in large city like New York
# 
# **Question 2:** Yes, the first two values are significantly higher than the others. # Yes,the $1200.29 value at the top looks unusually high for a typical taxi fare.
# 
# **Question 3:** The most expensive rides are not necessarily the longest ones. # No, the resulting rows are not always similar because trip_distance and total_amount can vary independently. 
# # Additional charges like tips, tolls, and fees affect the total amount, so the longest trips aren't always the most expensive.

# In[4]:


# Sort the data by trip distance from maximum to minimum value
df_trip_distance = df.sort_values(by='trip_distance', ascending=False)
df_trip_distance.head(10)


# In[5]:


# Sort the data by total amount and print the top 20 values
df_total_amount = df.sort_values(by='total_amount', ascending=False)['total_amount']
df_total_amount.head(20)


# In[6]:


# Sort the data by total amount and print the bottom 20 values
df_total_amount.tail(20)


# In[7]:


# How many of each payment type are represented in the data?
df['payment_type'].value_counts()


# According to the data dictionary, the payment method was encoded as follows:
# 
# 1 = Credit card  
# 2 = Cash  
# 3 = No charge  
# 4 = Dispute  
# 5 = Unknown  
# 6 = Voided trip

# In[8]:


# What is the average tip for trips paid for with credit card?
average_tip_cc = df[df['payment_type'] == 1]['tip_amount'].mean()

# What is the average tip for trips paid for with cash?
average_tip_cash = df[df['payment_type'] == 2]['tip_amount'].mean()
print('average_tip_cc:', average_tip_cc)
print('average_tip_cash:', average_tip_cash)


# In[9]:


# How many times is each vendor ID represented in the data?
df['VendorID'].value_counts()


# In[10]:


# What is the mean total amount for each vendor?

df.groupby('VendorID').mean(numeric_only= True)[['total_amount']]


# In[11]:


# Filter the data for credit card payments only
credit_card = df[df['payment_type']==1]

# Filter the credit-card-only data for passenger count only
credit_card['passenger_count'].value_counts()


# In[12]:


# Calculate the average tip amount for each passenger count (credit card payments only)

credit_card.groupby(['passenger_count'])[['tip_amount']].mean()


# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: **Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project. 
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: **Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.
# 

# ### **Given your efforts, what can you summarize for DeShawn and the data team?**
# 
# *Note for Learners: Your notebook should contain data that can address Luana's requests. Which two variables are most helpful for building a predictive model for the client: NYC TLC?*

# **Response**
# 
# **What I did**:
# 1-Filtered the dataset for credit card payments only (using payment_type == 1).
# 
# 2-Analyzed tip behavior by calculating the average tip amount based on passenger count.
# 
# 3-Counted vendor representation to understand which vendors appear most often.
# 
# **Key Findings**:
# - The average tip amount increases slightly with higher passenger counts.
# - Vendor ID 1 and 2 are both frequently represented in the data, suggesting a balanced usage across vendors.
# 
# **2 variables for a predictive model**:
# trip_distance is strongly correlated with total_amount and likely tip_amount.
# total_amount is positively correlated with tip amount. Generally, a higher total amount is associated with a higher tip.

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
