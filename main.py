import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# reverse column order
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)

# alias employee number as ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)

# bin job titles into Executive or Not Executive
df_executive = pd.read_sql("""
    SELECT *, 
        CASE 
            WHEN jobTitle = 'President' 
                OR jobTitle = 'VP Sales' 
                OR jobTitle = 'VP Marketing' 
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# get length of last name
df_name_length = pd.read_sql("""
    SELECT length(lastName) AS name_length 
    FROM employees
""", conn)

# first two letters of job title
df_short_title = pd.read_sql("""
    SELECT substr(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)

# sum of rounded total prices
sum_total_price = pd.read_sql("""
    SELECT round(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn).sum().values

# format date as day, month, year
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
""", conn)

conn.close()