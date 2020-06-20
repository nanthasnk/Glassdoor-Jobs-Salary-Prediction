# Data Science Jobs Salary Prediction: Project Overview
- Created a [Web Application](https://ds-salary-prediction-app.herokuapp.com/) that estimates data science salaries in the USA to help data scientists negotiate their income when they get a job.
- The project aims to predict Data Scientist salary based on job descriptions
- Scraped over 1000 job descriptions from glassdoor using python and selenium
- Cleaned the data to extract salary, job_roles, skills required (Python, R, SQL, etc.) and other features
- Explored the data to understand the relationship of various features with the target (salary)
- Applied mean-encoding to categorical features
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to obtain the best model
- Built a web application using Streamlit Web API

# Motivation
*“You can lay the groundwork now so that when the crisis is over you have opened doors and rekindled relationships.”*<br>
The coronavirus (COVID-19) outbreak is causing widespread concern and economic hardship for consumers, businesses and communities across the globe. Being able to get a good job right now in the data science industry, with a salary proportionate to the skills they possess is important, and at the same time, much more different compared to more normal time. This Web Application powered by machine learning provides a means to help estimate the salary based on the skills of a person, as well as the company hiring them.

# Resources Used
**Python Version:** 3.7 </br>
**Packages Used:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Selenium, Streamlit, Pickle  </br>
**Web Framework:** `pip install -r requirements.txt` </br>
**Scrapper Article:**:https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 </br>
**Streamlit Productionization**:https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020

# Web Scraping
Tweaked the web Scraper to scrape 1000 job postings from glassdoor.com. Each job we got the following:
- Job Title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors
- Company Size
- Company Founded Date

# Data Cleaning
After scraping the data from glassdoor.com, I needed to clean it up so that it was usable for our analysis and model building. I made the following changes and created the following variables:
- Parsed numeric data out of salary estimate
- Removed rows without salary estimate
- Parsed company rating out of company text
- Made a new column for Company State
- Created a new column with a condition of whether the work was at the company headquarters
- Transformed company founded date into Age of company
- Created columns for various skills listed in the job description
  * Python
  * R
  * Excel
  * SQL
  * Tableau
  * PowerBI
  * Hadoop
  * AWS
  * Spark
- Created columns for simplified job title and Seniority
- Created column for description length

# EDA
Visually analysed the distributions of the data and the value counts for the various numerical and categorical variables. Below are a few highlights.

![Heat Map](/Images/HeatMap.png "HeatMap")

![Skills](/Images/skills.png "Skills Count")

![Skills1](/Images/skills1.png "Skills Count")

![Statewise Average Salary](/Images/statewise.PNG "Statewise Salary") ![Seniority wise Average Salary](/Images/Seniority.PNG "Seniority wise salary")

# Model Building
Built a dataframe for our model with relevant columns.

Transformed the categorical variables into dummy variables. In addition, the data is split into train and test set

Performed Regression analysis using Linear Regression, Lasso Regression and Random Forest.
  -**Multiple Linear Regression**- BaseLine for the model
  -**Lasso Regression**- As there was sparsity associated with categorical data, these models match well
  -**Random Forest**- Again, with the sparsity associated with the data, this model was chosen
  
 # Model Performance Comparison
 - **Linear Regession**: MAE ~ 26K
 - **Lasso Regession**: MAE ~ 25K
 - **Random Forest**: MAE ~ 23K
 - **After HyperParameter Tuning Random Forest**: MAE ~ 22K
 
 # Productionization
 In this step, a web application is built using Streamlit API and hosted on Heroku platform. The web application provides users options to choose values from a job listing and returns an estimated salary.
 
 # Conclusion
 An end-to-end machine learning project for predicting the Salary for Data Scientist Job was developed starting from the collection of data, data cleaning, exploratory data analysis, model building and model deployment.


 


