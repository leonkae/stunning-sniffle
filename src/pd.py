import pandas as pd

numbers = pd.Series([1, 2, 3, 4, 5])
print(numbers)

ages = pd.Series([12, 13, 66], index=['Alice', 'Bob', 'Charlie'])
print(ages)
print("Alice's age:", ages['Alice'])

# Creating a DataFrame
people_data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

people_df = pd.DataFrame(people_data)
print(people_df)\
    
df = pd.read_csv("../data/exam_scores.csv")
print(df.head()) 
print(df.tail())
print(df.describe())