#!/usr/bin/env python
# coding: utf-8

# ## ***Hey there! Just a heads-up: I'm not categorizing any queries as basic, intermediate, or advanced. That's like trying to fit a square peg in a round hole – everyone's perception is different! So, I'm leaving it up to you, dear reader, to decide what's basic or advanced. Personally, everything's advanced to me (😂). Let's keep it fun and flexible, shall we?***

# ### Introduction
# 
# SQL (Structured Query Language) is a powerful programming language used for managing and manipulating relational databases. It provides a standardized way to interact with databases, allowing users to perform various operations such as querying, updating, inserting, and deleting data.
# 
# Here's a brief introduction to SQL and its importance in data analysis:
# 
# ### What is SQL?
# 
# 1. **Structured Query Language**: SQL is a domain-specific language designed for managing and manipulating structured data in relational database management systems (RDBMS).
#   
# 2. **Declarative Language**: SQL is a declarative language, meaning users specify what data they want to retrieve or manipulate, rather than specifying how to retrieve it. This makes SQL easy to write and understand.
# 
# 3. **Standardized Language**: SQL is an ANSI/ISO standard language, ensuring consistency and portability across different database systems.
# 
# ### Importance in Data Analysis:
# 
# 1. **Data Retrieval**: SQL allows users to retrieve data from databases using SELECT statements. This is essential for data analysis as it enables users to extract relevant information for analysis.
# 
# 2. **Data Manipulation**: SQL provides commands like INSERT, UPDATE, and DELETE for manipulating data in databases. Data analysts use these commands to modify existing data or add new data as needed.
# 
# 3. **Data Aggregation**: SQL supports aggregation functions such as SUM, AVG, MIN, MAX, and COUNT, allowing analysts to summarize and aggregate data to derive insights.
# 
# 4. **Data Filtering and Sorting**: SQL enables users to filter and sort data based on specific criteria, facilitating data analysis by focusing on relevant subsets of data.
# 
# 5. **Data Joins**: SQL supports different types of joins (e.g., INNER JOIN, LEFT JOIN, RIGHT JOIN) to combine data from multiple tables. This is crucial for integrating data from different sources for analysis.
# 
# 6. **Data Transformation**: SQL can be used to transform data using functions like CASE statements, string functions, date functions, etc. This is useful for preparing data for analysis.
# 
# 7. **Data Integrity and Security**: SQL provides mechanisms for maintaining data integrity through constraints (e.g., primary keys, foreign keys) and enforcing security through user authentication and access control.
# 
# 8. **Scalability and Performance**: SQL databases are highly scalable and optimized for performance, allowing analysts to work with large datasets efficiently.
# 
# In summary, SQL is a fundamental tool for data analysis, providing powerful capabilities for retrieving, manipulating, and analyzing structured data stored in databases. It plays a crucial role in various data-related tasks, making it an essential skill for data analysts and professionals working with data.

# In[1]:


import sqlite3
import random
import string


# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a sample table for employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
''')

# Create a sample table for departments
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    name TEXT,
    budget REAL
)
''')

# Generate sample data for employees
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(6))

departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
salaries = [50000, 60000, 70000, 80000, 90000]

for i in range(100):
    name = generate_random_name()
    department = random.choice(departments)
    salary = random.choice(salaries)
    cursor.execute('''
    INSERT INTO employees (name, department, salary)
    VALUES (?, ?, ?)
    ''', (name, department, salary))

# Generate sample data for departments
for department in departments:
    budget = random.randint(100000, 500000)
    cursor.execute('''
    INSERT INTO departments (name, budget)
    VALUES (?, ?)
    ''', (department, budget))

conn.commit()


# ***There are various ways to achieve a desired result. Just as in life, the same principle applies to coding. Here is a simple example to illustrate this:😎***<br>
# ***I will show only two options in this query and not in the entire notebook. Or maybe I will give two options 😄. To prove me wrong, you have to read the entire notebook.😉***</br>
# ***So If you catch me goofing up or proving me wrong, I'll be thrilled! I love learning from my mistakes. So, if my query's acting up or my explanation's not quite hitting the mark, just shoot me a message on LinkedIn. Let's turn those whoopsies into 'Oh, cool, I learned something new!' moments!***</br>
# ***Here is the link:***  https://www.linkedin.com/in/deepak-koli-9b9a8426a/

# In[2]:


# Execute SQL query to select all columns from the employees table
cursor.execute('SELECT * FROM employees')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Display the fetched rows
for row in rows:
    print(row)


# In[3]:


import pandas as pd
pd.set_option("display.max_rows", None)
# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Example 1: SELECT and FROM
# Retrieve all columns from the employees table
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_all_employees = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("All Employees:")

df_all_employees


# 
# #### Execution Steps:
# 
# **Determine the Columns to Retrieve**:
#    - The query parser interprets the `SELECT *` part, meaning it needs to retrieve all columns from the specified table (`employees`).
# 
# **Identify the Data Source**:
#    - The query parser then looks at the `FROM employees` part to identify which table to query. 
# 
# **Access the Table**:
#    - The database engine accesses the `employees` table in the database. 
# 
# **Retrieve the Data**:
#    - The database engine retrieves all rows and all columns from the `employees` table.
# 
# **Return the Result**:
#    - The results (all columns for all rows) are returned and stored in the variable `rows`.
# 
# 
# 

# The following SQL query is used to retrieve the `name` and `department` columns from the `employees` table. The fetched rows are then displayed using a DataFrame for better visualization.

# In[4]:


# Example 2: SELECT specific columns
# Retrieve the names and departments of all employees
cursor.execute('SELECT name, department FROM employees')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_name_department = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nNames and Departments of All Employees:")

df_name_department


# #### Execution Steps:
# ***Query Parsing:***
# - The SQL query is parsed to understand which columns and table are being requested.
# 
# ***Determine the Columns to Retrieve:***
# - The SELECT name, department part indicates that only the name and department columns should be retrieved.
# 
# ***Identify the Data Source:***
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Access the Table:***
# - The database engine accesses the employees table to fetch the required data.
# 
# ***Retrieve the Data:***
# - The engine retrieves all rows but only the name and department columns from the employees table.
# 
# ***Return the Result:***
# - The result set (containing the name and department columns for all rows) is returned and stored in the variable rows.
# 
# 

# In[5]:


# Example 3: SELECT with WHERE
# Retrieve all employees in the 'Engineering' department
cursor.execute("SELECT * FROM employees WHERE department = 'Engineering'")
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_engineering = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nEmployees in Engineering Department:")

df_engineering


# The following SQL query is used to retrieve all columns from the `employees` table for employees who are in the 'Engineering' department. The fetched rows are then displayed using a DataFrame for better visualization.
# 
# #### Execution
# ***Query Parsing:***
# - The SQL query is parsed to understand the columns (* for all columns), table (employees), and the condition (department = 'Engineering').
# 
# ***Determine the Columns to Retrieve:***
# - Since * is used, the query will retrieve all columns from the employees table.
# 
# ***Identify the Data Source:***
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Apply the WHERE Clause:***
# - The WHERE department = 'Engineering' condition is applied to filter the rows.
# 
# ***Access the Table and Filter Data:***
# - The database engine accesses the employees table and filters the rows to include only those where the department is 'Engineering'.
# 
# ***Retrieve the Filtered Data:***
# - The engine retrieves all columns for the filtered rows.

# In[6]:


# Example 4: COUNT with WHERE
# Find out how many employees are in the 'Engineering' department
cursor.execute("SELECT COUNT(*) FROM employees WHERE department = 'Engineering'")
engineering_count = cursor.fetchone()[0]

# Print the count
print("\nNumber of employees in the Engineering department:", engineering_count)


# 
# The following SQL query is used to count the number of employees in the 'Engineering' department. The count is then displayed.
# 
# #### Execution
# 
# 
# The SQL query is parsed to understand the columns to retrieve (in this case, the count of rows), the table (employees), and the condition (department = 'Engineering').
# 
# ***Determine the Data Source:***
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Apply the WHERE Clause:***
# - The WHERE department = 'Engineering' condition is applied to filter the rows.
# 
# ***Access the Table and Filter Data:***
# - The database engine accesses the employees table and filters the rows to include only those where the department is 'Engineering'.
# 
# ***Aggregate Function (COUNT):***
# - The COUNT(*) function counts the number of rows that satisfy the WHERE condition.
# 
# ***Return the Result:***
# - The result (a single value representing the count of rows) is returned and stored in the variable engineering_count.

# In[7]:


# INNER JOIN employees and departments
cursor.execute('''
SELECT employees.name, employees.department, employees.salary, departments.budget
FROM employees
JOIN departments ON employees.department = departments.name
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_joined = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("Employees and Their Department Budgets:")
print(df_joined)


# 
# 
# The following SQL query performs an INNER JOIN between the `employees` and `departments` tables to retrieve the names, departments, salaries of employees, and the corresponding department budgets. The fetched rows are then displayed using a DataFrame for better visualization.
# 
# #### Execution Steps:
# 
# ***Query Parsing:***
# - The SQL query is parsed to understand the columns to retrieve, the tables involved (employees and departments), and the join condition.
# 
# ***Determine the Data Sources:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# - The JOIN departments part tells the database engine to join the employees table with the departments table.
# 
# ***Apply the JOIN Condition:***</br>
# - The ON employees.department = departments.name condition is applied to match rows from the employees table with rows from the departments table where the department in the employees table matches the name in the departments table.
# 
# ***Combine Rows:***</br>
# - The database engine combines the rows from employees and departments that satisfy the join condition. This means for each employee, it finds the corresponding department budget from the departments table.
# 
# ***Select Columns:***</br>
# - The SELECT clause specifies which columns to retrieve from the combined rows: employees.name, employees.department, employees.salary, and departments.budget.
# 
# ***Return the Result:***</br>
# - The result set, containing the selected columns from the combined rows, is returned.

# In[8]:


# GROUP BY department to find average salary
cursor.execute('''
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_avg_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nAverage Salary by Department:")

df_avg_salary


# 
# The following SQL query calculates the average salary for each department in the `employees` table and groups the results by department. The fetched rows are then displayed using a DataFrame for better visualization.
# 
# 
# #### Execution Steps:
# 
# ***Query Parsing:***</br>
# - The SQL query is parsed to understand the columns to retrieve, the table involved (employees), and the grouping condition.
# 
# ***Determine the Data Source:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Group the Rows:***</br>
# - The GROUP BY department part tells the database engine to group the rows based on the department column. This means all rows with the same department value will be grouped together.
# 
# ***Apply Aggregate Function:***</br>
# - The AVG(salary) function calculates the average salary for each group of rows. The database engine computes the average salary for each department group.
# 
# ***Select Columns:***</br>
# - The SELECT department, AVG(salary) as avg_salary part specifies the columns to retrieve from the grouped rows: the department column and the calculated average salary with the alias avg_salary.
# 
# ***Return the Result:***
# - The result set, containing the department and the calculated avg_salary, is returned.
# 

# In[9]:


# GROUP BY department and use HAVING to filter average salary > 65000
cursor.execute('''
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING avg_salary > 65000
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_having = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nDepartments with Average Salary Greater Than $65,000:")
print(df_having)


# This query retrieves departments from the employees table, calculates the average salary for each department, and then filters the results to include only those departments with an average salary greater than $65,000.
# 
# #### Execution Steps:
# ***Query Parsing***:</br>
# - The SQL query is parsed to understand the columns to retrieve, the table involved (employees), the grouping condition (GROUP BY department), and the filtering condition on the aggregated data (HAVING avg_salary > 65000).
# 
# ***Determine the Data Source:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Group the Rows:***</br>
# - The GROUP BY department part tells the database engine to group the rows based on the department column. All rows with the same department value will be grouped together.
# 
# ***Apply Aggregate Function:***</br>
# - The AVG(salary) function calculates the average salary for each group of rows (each department). The database engine computes the average salary for each department group.
# 
# ***Apply HAVING Clause:***</br>
# - The HAVING avg_salary > 65000 clause filters the grouped results. Only those groups (departments) where the average salary is greater than $65,000 are included in the final result set.
# 
# ***Select Columns:***</br>
# - The SELECT department, AVG(salary) as avg_salary part specifies the columns to retrieve from the grouped rows: the department column and the calculated average salary with the alias avg_salary.
# 
# ***Return the Result:***</br>
# - The result set, containing the department and the calculated avg_salary for departments with an average salary greater than $65,000, is returned.

# In[10]:


# GROUP BY department to calculate total salary
cursor.execute('''
SELECT department, SUM(salary) as total_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_total_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nTotal Salary by Department:")
print(df_total_salary)


# This query retrieves the total salary for each department from the employees table by summing up the salaries of all employees within each department.
# 
# #### Execution Steps:
# ***Query Parsing:***</br>
# - The SQL query is parsed to understand the columns to retrieve, the table involved (employees), and the grouping condition (GROUP BY department).
# 
# ***Determine the Data Source:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Group the Rows:***</br>
# - The GROUP BY department part tells the database engine to group the rows based on the department column. All rows with the same department value will be grouped together.
# 
# ***Apply Aggregate Function:***</br>
# - The SUM(salary) function calculates the total salary for each group of rows (each department). The database engine computes the sum of the salaries for each department group.
# 
# ***Select Columns:***</br>
# - The SELECT department, SUM(salary) as total_salary part specifies the columns to retrieve from the grouped rows: the department column and the calculated total salary with the alias total_salary.
# 
# ***Return the Result:***</br>
# - The result set, containing the department and the calculated total_salary for each department, is returned.

# In[11]:


# GROUP BY department to find maximum salary
cursor.execute('''
SELECT department, MAX(salary) as max_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_max_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("Maximum Salary by Department:")
print(df_max_salary)


# This query retrieves the maximum salary for each department from the employees table.
# 
# #### Execution Steps:
# 
# ***Query Parsing:***</br>
# - The SQL query is parsed to understand the columns to retrieve, the table involved (employees), and the grouping condition (GROUP BY department).
# 
# ***Determine the Data Source:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Group the Rows:***</br>
# - The GROUP BY department part tells the database engine to group the rows based on the department column. All rows with the same department value will be grouped together.
# 
# ***Apply Aggregate Function:***</br>
# - The MAX(salary) function calculates the maximum salary for each group of rows (each department). The database engine finds the highest salary value within each department group.
# 
# ***Select Columns:***</br>
# - The SELECT department, MAX(salary) as max_salary part specifies the columns to retrieve from the grouped rows: the department column and the calculated maximum salary with the alias max_salary.
# 
# ***Return the Result:***</br>
# - The result set, containing the department and the calculated max_salary for each department, is returned.

# In[12]:


# GROUP BY department to find minimum salary
cursor.execute('''
SELECT department, MIN(salary) as min_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_min_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nMinimum Salary by Department:")
print(df_min_salary)


# This SQL query retrieves the minimum salary for each department from the employees table.
# 
# #### Execution Steps:
# 
# ***Query Parsing:***</br>
# - The SQL query is parsed to understand the columns to retrieve, the table involved (employees), and the grouping condition (GROUP BY department).
# 
# ***Determine the Data Source:***</br>
# - The FROM employees part tells the database engine to fetch the data from the employees table.
# 
# ***Group the Rows:***</br>
# - The GROUP BY department part tells the database engine to group the rows based on the department column. All rows with the same department value will be grouped together.
# 
# ***Apply Aggregate Function:***</br>
# - The MIN(salary) function calculates the minimum salary for each group of rows (each department). The database engine finds the lowest salary value within each department group.
# 
# ***Select Columns:***</br>
# - The SELECT department, MIN(salary) as min_salary part specifies the columns to retrieve from the grouped rows: the department column and the calculated minimum salary with the alias min_salary.
# 
# ***Return the Result:***</br>
# - The result set, containing the department and the calculated min_salary for each department, is returned.

# In[13]:


# GROUP BY department to count number of employees
cursor.execute('''
SELECT department, COUNT(*) as num_employees
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_count_employees = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nNumber of Employees by Department:")
print(df_count_employees)


# This SQL query counts the number of employees in each department from the employees table.
# 
# #### Execution Steps:
# 
# ***Query Parsing:***</br>
# - The SQL query is parsed to identify the columns to retrieve, the primary table involved (employees), and the grouping condition (GROUP BY department).
# 
# ***Determine Data Source:***</br>
# - The FROM employees part specifies that the data will be retrieved from the employees table.
# 
# ***Grouping:***</br>
# - The GROUP BY department clause tells the database engine to group the rows based on the department column.
# 
# ***Counting:***</br>
# - The COUNT(*) function calculates the number of rows in each group (each department), effectively counting the number of employees in each department.
# 
# ***Selecting Columns:***</br>
# - The SELECT department, COUNT(*) as num_employees part specifies the columns to retrieve from the grouped rows: the department column and the count of employees with the alias num_employees.
# 
# ***Result Set:***</br>
# - The result set contains each department and the count of employees in that department.

# In[14]:


# Fetch salaries grouped by department
cursor.execute('''
SELECT department, 
       ROUND(STDDEV(salary), 2) AS stddev_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for calculation
df_stddev_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nStandard Deviation of Salaries by Department:")
print()
print(df_stddev_salary)


# ***Oopsie***</br>
# ***well this happens in life also 😂***

# In[15]:


# Fetch salaries grouped by department
cursor.execute('''
SELECT department, 
       AVG(salary) AS avg_salary,
       ROUND(SQRT(AVG(salary * salary) - AVG(salary) * AVG(salary)), 2) AS stddev_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for calculation
df_stddev_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nStandard Deviation of Salaries by Department:")
print()
print(df_stddev_salary)


# ***Again Oopsies***</br>
# ***Same day, another oopsie! Whether it's a predictable blunder or a surprise one, who knows?😂*** 

# In[ ]:


# Fetch salaries grouped by department
cursor.execute('''
SELECT department, 
       AVG(salary) AS avg_salary,
       ROUND(AVG(salary * salary) - AVG(salary) * AVG(salary), 2) AS variance,
       ROUND(SQRT(ABS(AVG(salary * salary) - AVG(salary) * AVG(salary))), 2) AS stddev_salary
FROM employees
GROUP BY department
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for calculation
df_stddev_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nStandard Deviation of Salaries by Department:")
print()
print(df_stddev_salary)


# ***Have to use python function now 😉***

# In[ ]:


# Fetch salaries grouped by department
cursor.execute('''
SELECT department, salary
FROM employees
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for calculation
df_salaries = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Calculate standard deviation of salaries in each department
df_stddev_salary = df_salaries.groupby('department').agg({'salary': 'std'}).reset_index()
df_stddev_salary.columns = ['department', 'stddev_salary']

# Display the DataFrame
print("\nStandard Deviation of Salaries by Department:")
print()
print(df_stddev_salary)


# The reason I used a Python function is because I couldn't utilize "std" and "sqrt" functions directly within the SQL command. Hence, I opted for Python instead. However, if you require the SQL query, here it is along with its execution steps.
# 
# ***SELECT department,</br> 
#        ROUND(STDDEV(salary), 2) AS stddev_salary</br>
# FROM employees</br>
# GROUP BY department;***</br>
# 
# The SQL query provided calculates the standard deviation of salaries for each department. Here's how the execution works step by step:
# #### Execution
# ***SELECT clause:***</br>
# - It specifies the columns to be retrieved in the result set. In this case, it selects the department column and the rounded standard deviation of the salary column as stddev_salary.
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data. Here, it's the employees table.
# 
# ***GROUP BY clause:***</br>
# - It groups the rows that have the same value in the department column into summary rows. Each group represents a unique department.
# 
# ***STDDEV function:***</br>
# - This is an aggregate function that computes the standard deviation of a set of values. It calculates the dispersion or variability of the salary values within each department group.
# 
# ***ROUND function:***</br>
# - It rounds the standard deviation values to two decimal places, making the output more readable.
# 
# ***Result set:***</br>
# - The query returns a result set with two columns: department and stddev_salary, where each row represents a department and its corresponding standard deviation of salaries
# 
# 
# 
# 
# 
# 
# 
# ***SELECT department,</br> 
#        AVG(salary) AS avg_salary,</br>
#        ROUND(AVG(salary * salary) - AVG(salary) * AVG(salary), 2) AS variance,</br>
#        ROUND(SQRT(ABS(AVG(salary * salary) - AVG(salary) * AVG(salary))), 2) AS stddev_salary</br>
# FROM employees</br>
# GROUP BY department;***</br>
# </br>
# The SQL query  provided calculates not only the average salary (avg_salary) for each department but also the variance and standard deviation of salaries within each department. Here's how the execution works step by step:
# #### Execution
# 
# ***SELECT clause:***</br>
# - It specifies the columns to be retrieved in the result set. In this case, it selects the department column, the average salary (AVG(salary)), the variance (ROUND(AVG(salary * salary) - AVG(salary) * AVG(salary), 2) AS variance), and the standard deviation (ROUND(SQRT(ABS(AVG(salary * salary) - AVG(salary) * AVG(salary))), 2) AS stddev_salary).
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data. Here, it's the employees table.
# 
# ***GROUP BY clause:***</br>
# - It groups the rows that have the same value in the department column into summary rows. Each group represents a unique department.
# 
# ***AVG function:***</br>
# - This is an aggregate function that computes the average of a set of values. It calculates the average salary for each department.
# 
# ***Variance calculation:***</br>
# - The expression AVG(salary * salary) - AVG(salary) * AVG(salary) calculates the variance of salaries within each department. It subtracts the square of the average salary from the average of the squares of salaries.
# 
# ***ROUND function (Variance):***</br>
# - It rounds the variance values to two decimal places, making the output more readable.
# 
# ***SQRT function:***</br>
# - This function calculates the square root of a given value. Here, it computes the square root of the absolute value of the variance to obtain the standard deviation.
# 
# ***ROUND function (Standard Deviation):***</br>
# - It rounds the standard deviation values to two decimal places, making the output more readable.
# 
# ***Result set:***</br>
# - The query returns a result set with four columns: department, avg_salary, variance, and stddev_salary, where each row represents a department and its corresponding average salary, variance, and standard deviation of salaries.

# In[ ]:


# Subquery in SELECT clause
cursor.execute('''
SELECT name,
       (SELECT SUM(salary) FROM employees WHERE department = departments.name) as total_salary
FROM departments
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_total_salary_dept = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("Total Salary Spent on Employees by Department:")
print(df_total_salary_dept)


# The SQL query contains a subquery within the SELECT clause. 
# #### Execution
# 
# ***SELECT clause:***</br>
# - It specifies the columns to be retrieved in the result set. In this case, it selects the name column from the departments table and a subquery that calculates the total salary spent on employees in each department.
# 
# ***Subquery:***</br>
# - The subquery (SELECT SUM(salary) FROM employees WHERE department = departments.name) calculates the total salary for each department. It sums up the salary column from the employees table where the department matches the name of the department in the outer query.
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data. Here, it's the departments table.
# 
# ***Result set:***</br>
# - The query returns a result set with two columns: name (department name) and total_salary, where each row represents a department and its corresponding total salary spent on employees.
# 
# 

# In[ ]:


# Subquery in WHERE clause
cursor.execute('''
SELECT name, department, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_high_earners = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nEmployees Earning More Than Average Salary in Their Department:")
print(df_high_earners)


# The SQL query uses a subquery in the WHERE clause to filter employees earning more than the average salary in their respective departments.
# 
# #### Execution
# ***Subquery in WHERE clause:***</br>
# - The subquery (SELECT AVG(salary) FROM employees WHERE department = e.department) calculates the average salary for each department. It selects the average salary from the employees table where the department matches the e.department from the outer query.
# 
# ***Main query:***</br>
# - It selects the name, department, and salary columns from the employees table, aliased as e.
# 
# ***WHERE clause:***</br>
# - The condition salary > (SELECT AVG(salary) FROM employees WHERE department = e.department) filters the rows where the salary of an employee is greater than the average salary of their respective department.
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data, which is the employees table, aliased as e.
# 
# ***Result set:***</br>
# - The query returns a result set containing the names, departments, and salaries of employees who earn more than the average salary in their respective departments.

# In[17]:


# Common Table Expression (CTE)
cursor.execute('''
WITH dept_budgets AS (
    SELECT department, SUM(budget) as total_budget
    FROM departments
    GROUP BY department
)
SELECT department, total_budget
FROM dept_budgets
WHERE total_budget = (SELECT MAX(total_budget) FROM dept_budgets)
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_highest_budget = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nDepartment(s) with the Highest Total Budget:")
print(df_highest_budget)


# In[16]:


# Window Function (ROW_NUMBER())
cursor.execute('''
SELECT name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as row_number
FROM employees
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_row_number = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nRow Number of Employees Within Their Department (Ordered by Salary):")
print(df_row_number)


# This SQL query employs a window function, specifically the ROW_NUMBER() function, to assign a row number to each employee within their respective department. The row number is determined based on the descending order of their salary within each department.
# 
# 
# #### Execution:
# 
# ***Window Function (ROW_NUMBER()):***</br> 
# - The ROW_NUMBER() function assigns a unique sequential integer to each row within its partition.</br> 
# In this query:</br>
#    1. The PARTITION BY department clause partitions the result set into groups based on the department column.</br>
#    2. The ORDER BY salary DESC clause orders the rows within each partition by salary in descending order.</br>
# 
# ***Main query:***</br>
# - It selects the name, department, and salary columns from the employees table.
# 
# ***Window Function Usage:***</br>
# - The ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) expression computes a row number for each row within its partition, where the partition is defined by the department, and the rows are ordered by salary in descending order within each partition.
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data, which is the employees table.
# 
# ***Result set:***</br>
# - The query returns a result set containing the names, departments, salaries, and row numbers of employees within their departments, ordered by salary in descending order within each department.

# In[18]:


# Window Function (Running Total with SUM() OVER())
cursor.execute('''
SELECT name, department, salary,
       SUM(salary) OVER (PARTITION BY department ORDER BY salary ASC) as running_total
FROM employees
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_running_total = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nRunning Total of Salaries Within Each Department (Ordered by Salary):")
print(df_running_total)


# #### Execution
# ***Window Function (SUM() OVER()):***</br>
# - The SUM() function computes the running total of the salary column within each partition.</br>
# In this query:</br>
# 
#    1. The PARTITION BY department clause partitions the result set into groups based on the department column.
#    2. The ORDER BY salary ASC clause orders the rows within each partition by salary in ascending order.
# 
# ***Main query:***</br>
# - It selects the name, department, and salary columns from the employees table.
# 
# ***Window Function Usage:***</br>
# - The SUM(salary) OVER (PARTITION BY department ORDER BY salary ASC) expression computes the running total of salaries within each department, where the partition is defined by the department, and the rows are ordered by salary in ascending order within each partition.
# 
# ***FROM clause:***</br>
# - It specifies the table from which to retrieve the data, which is the employees table.
# 
# ***Result set:***</br>
# - The query returns a result set containing the names, departments, salaries, and running totals of salaries within each department, ordered by salary in ascending order within each department.

# In[19]:


# Create a connection to the database (use the same database 'example.db')
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Corrected Common Table Expression (CTE) query
cursor.execute('''
WITH dept_salaries AS (
    SELECT department, SUM(salary) as total_salary
    FROM employees
    GROUP BY department
)
SELECT department, total_salary
FROM dept_salaries
WHERE total_salary = (SELECT MAX(total_salary) FROM dept_salaries);
''')
rows = cursor.fetchall()

# Convert the fetched data into a DataFrame for better display
df_highest_salary = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Display the DataFrame
print("\nDepartment(s) with the Highest Total Salary:")
print(df_highest_salary)

# Close the connection
conn.close()


# 
# The query calculates and retrieves the department(s) with the highest total budget by first summing budgets per department and then selecting the maximum total budget.
# #### Execution Steps
# 
# 1. **CTE Execution**:
#    - The database first executes the CTE part of the query.
#    - It scans the `departments` table and groups the rows by the `department` column.
#    - It calculates the sum of the `budget` for each department, resulting in a temporary result set (`dept_budgets`) with columns `department` and `total_budget`.
# 
# 2. **Subquery Execution**:
#    - The subquery `SELECT MAX(total_budget) FROM dept_budgets` is executed next.
#    - This subquery scans the `dept_budgets` CTE to find the maximum value of `total_budget`.
# 
# 3. **Main Query Execution**:
#    - The main query then executes, using the result of the subquery to filter the `dept_budgets` CTE.
#    - It selects the department(s) whose `total_budget` matches the maximum value found by the subquery.
#    - The result is a set of rows with the department(s) having the highest total budget and their respective budget values.

# ***Phew! We've reached the finish line! If you dig my vibe, feel free to slide into my DMs and give me a virtual high-five! Let's keep the momentum going and motivate me to churn out more notebooks. Sure, I might not have written a gazillion notebooks😂 (yet!), but hey, gotta start somewhere, right?😉 Who knows, maybe the next one will be the 'Notebook of the Century' (or at least Notebook of the Week?) Let's keep the laughter and learning rolling!😎***
# 
# ***Here is the link:*** https://www.linkedin.com/in/deepak-koli-9b9a8426a/
