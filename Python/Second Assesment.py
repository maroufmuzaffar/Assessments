# -*- coding: utf-8 -*-
"""Python2nd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TNf6YAB8w6N89reNwGRo3U56X_yRxzaE

Q1:calculate and print the minimum maximum,sum,mean and standard deviation of an array
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Minimum: ", np.min(arr))
print("Maximum: ", np.max(arr))
print("Sum: ", np.sum(arr))
# Calculate and print the mean standard deviation
print("Mean: ", np.mean(arr))
print("Standard Deviation: ", np.std(arr))

#Q2:
# health_data = np.array([[160, 70, 30],    
                        [165, 65, 35],   
                        [170, 75, 40]])  
                        import numpy as np
def normalize_data(data):
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)
    normalized_data = (data - means) / stds
    return normalized_data
health_data = np.array([[160, 70, 30],
                        [165, 65, 35],
                        [170, 75, 40]])
normalized_health_data = normalize_data(health_data)

print(normalized_health_data)

#QNO3

import numpy as np

def calculate_average_last_three_subjects(scores):
    last_three_subjects = scores[:, -3:]  
    exempt_mask = last_three_subjects != -1  
    non_exempt_scores = np.where(exempt_mask, last_three_subjects, 0)  
    non_exempt_count = 

np.sum(exempt_mask, axis=1)  
    total_scores = np.sum(non_exempt_scores, axis=1)  
    averages = np.where(non_exempt_count > 0, total_scores / non_exempt_count, 0)
    return averages
scores = np.array([[80, 75, 90, -1, 85],
                   [70, 65, -1, 80, 75],
                   [85, 90, 95, 88, 92]])
# Calculate average scores for the last three subjects
averages = 
calculate_average_last_three_subjects(scores)

print("Average scores for the last three subjects for each student:")
print(averages)


#QNO4
import numpy as np
start_temp = 15
end_temp = 25
num_measurements = 24
temperature_readings = np.linspace(start_temp, end_temp, num_measurements)

print(temperature_readings)
QNO5

import numpy as np

def moving_average(data, window_size):
    weights = np.ones(window_size) / window_size
    return np.convolve(data, weights, mode='valid')

daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])

# Define the window size
window_size = 5
moving_avg = moving_average(daily_closing_prices, window_size)

print("Moving average over a window of 5 days:")
print(moving_avg)

#Q6
import numpy as np
mean = [0, 0]
cov = [[1, 0.5], [0.5, 2]]

samples = np.random.multivariate_normal(mean, cov, 100)

print(samples)

#Q8:
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:")
print(array)
#  filter out numbers greater than 5
filtered_array = array[array > 5]
print("Filtered Array:")
print(filtered_array)

#QNO15
student_data = [
    {"StudentID": 1, "Subject": "Math", "Grade": 88},
    {"StudentID": 2, "Subject": "Science", "Grade": 92},
    {"StudentID": 3, "Subject": "History", "Grade": 85},
    {"StudentID": 4, "Subject": "Math", "Grade": 87},
    {"StudentID": 5, "Subject": "Science", "Grade": 90},
    {"StudentID": 6, "Subject": "History", "Grade": 82},
    {"StudentID": 7, "Subject": "Math", "Grade": 85},
    {"StudentID": 8, "Subject": "Science", "Grade": 91},
    {"StudentID": 9, "Subject": "History", "Grade": 84},
    {"StudentID": 10, "Subject": "Math", "Grade": 89}
]

subject_data = {}
for student in student_data:
    subject = student["Subject"]
    grade = student["Grade"]
    if subject not in subject_data:
        subject_data[subject] = {"total_grade": grade, "count": 1}
    else:
        subject_data[subject]["total_grade"] += grade
        subject_data[subject]["count"] += 1
for subject, data in subject_data.items():
    average_grade = data["total_grade"] / data["count"]
    print(f"The average grade for {subject} is {average_grade:.2f}")

#Q13
import pandas as pd

data = [
    {"TeamID": 1, "GamesPlayed": 10, "Wins": 7},
    {"TeamID": 2, "GamesPlayed": 10, "Wins": 6},
    {"TeamID": 3, "GamesPlayed": 10, "Wins": 8},
    {"TeamID": 4, "GamesPlayed": 10, "Wins": 5},
    {"TeamID": 5, "GamesPlayed": 10, "Wins": 9},
    {"TeamID": 6, "GamesPlayed": 10, "Wins": 6},
    {"TeamID": 7, "GamesPlayed": 10, "Wins": 7},
    {"TeamID": 8, "GamesPlayed": 10, "Wins": 4},
    {"TeamID": 9, "GamesPlayed": 10, "Wins": 9},
    {"TeamID": 10, "GamesPlayed": 10, "Wins": 5}
]

df = pd.DataFrame(data)
df['WinPercentage'] = df['Wins'] / df['GamesPlayed']
strengths = df[df['WinPercentage'] > 0.5]
weaknesses = df[df['WinPercentage'] <= 0.5]
print("Strengths:")
print(strengths)

print("\nWeaknesses:")
print(weaknesses)

#Q11

import pandas as pd

# Given data
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data)
fruit_df = df[df['Category'] == 'Fruit']e
average_price = fruit_df['Price'].mean()
result = fruit_df[(fruit_df['Price'] > average_price) & (fruit_df['Promotion'] == False)]
# Print the result
print(result)


#QNO9

import numpy as np 


properties_matrix = np.array([[1, 2, 3], 
                               [4, 5, 6], 
                               [7, 8, 9]])

determinant = np.linalg.det(properties_matrix)
print("Determinant of the matrix:")
print(determinant)

Q#NO10:

import pandas as pd
data = {
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales': [70000, 50000, 30000, 40000, 60000]
}
df = pd.DataFrame(data)
department_group = df.groupby('Department')
total_sales_per_department = department_group['Sales'].sum()

each department
num_salespersons_per_department = department_group['Salesperson'].count()
average_sales_per_salesperson = total_sales_per_department / num_salespersons_per_department

ranked_departments = average_sales_per_salesperson.sort_values(ascending=False)

print("Average sales per salesperson in each department:")
print(average_sales_per_salesperson)
print("\nRanking of departments based on average sales:")

print(ranked_departments)

QNO11

import pandas as pd

# Given data
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data)
fruit_products = df[df['Category'] == 'Fruit']
average_price_fruit = fruit_products['Price'].mean()
above_average_price_fruit = fruit_products[fruit_products['Price'] > average_price_fruit]
potential_candidates = above_average_price_fruit[~above_average_price_fruit['Promotion']]

print("Potential candidates for future promotions in the Fruit category:")
print(potential_candidates)

#QNO14
import pandas as pd
data = {
    'CustomerID': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Date': ['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30', '2021-05-31', 
             '2021-06-30', '2021-07-31', '2021-08-31', '2021-09-30'],
    'PurchaseAmount': [200, 150, 300, 250, 500, 350, 400, 450, 550],
    'LoyaltyProgramSignUp': ['2021-03-01'] * 9
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['LoyaltyProgramSignUp'] = pd.to_datetime(df['LoyaltyProgramSignUp'])
df['DaysSinceSignUp'] = (df['Date'] - df['LoyaltyProgramSignUp']).dt.days
df['BeforeSignUp'] = df['DaysSinceSignUp'] < 0
customer_metrics = df.groupby('CustomerID').agg(
    BeforeSignUp=('BeforeSignUp', 'sum'), 
    PurchaseCount=('PurchaseAmount', 'count'), 
    TotalPurchaseAmount=('PurchaseAmount', 'sum')
)
print(customer_metrics)


#Q7: END OF TIME








