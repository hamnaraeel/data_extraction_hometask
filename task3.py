import pandas as pd

# Load the data file into a DataFrame
data = pd.read_csv('adult.data', header=None)

# Now, create the DataFrame from the loaded data
df = pd.DataFrame(data)

# Assign the column names manually
df.columns = [
    'age', 'type_employer', 'fnlwgt', 'education', 'education_num', 
    'marital', 'occupation', 'relationship', 'race', 'sex', 
    'capital_gain', 'capital_loss', 'hr_per_week', 'country', 'income'
]

# Clean up any leading or trailing spaces in the data
df['race'] = df['race'].str.strip()
df['income'] = df['income'].str.strip()

# Filter for white people
white_people = df[df.race == 'White']

# Filter for white people with income <=50K (as an approximation for < 20K)
white_low_income = white_people[white_people.income == '<=50K']

# Calculate the count of low-income white individuals
white_low_income_count = len(white_low_income)

# Calculate the total number of white people
total_white_people_count = len(white_people)

# Calculate the percentage of white people with low income
if total_white_people_count > 0:
    white_low_income_percentage = (white_low_income_count / total_white_people_count) * 100
else:
    white_low_income_percentage = 0

# Output the result
if white_low_income_count == 0:
    print('No white people with low income (<= 50K) found in the dataset.')
else:
    print(f'The number of white people with low income (<= 50K) is: {white_low_income_count}')
    print(f'The percentage of white people with low income (<= 50K) is: {white_low_income_percentage:.2f}%')
