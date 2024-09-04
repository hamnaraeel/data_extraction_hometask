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
df['sex'] = df['sex'].str.strip()
df['income'] = df['income'].str.strip()

# Filter based on sex and income for analysis
ml = df[df.sex == 'Male']
ml1 = df[(df.sex == 'Male') & (df.income == '>50K')]
fm = df[df.sex == 'Female']
fm1 = df[(df.sex == 'Female') & (df.income == '>50K')]
df1 = df[df.income == '>50K']

# Check the total rate of people with high income
if len(df) == 0:
    print('No data found in the dataset.')
elif len(df1) == 0:
    print('No people with high income found in the dataset.')
else:
    print('The rate of people with high income is: ', int(len(df1)) / float(len(df)) * 100, '%.')
    
# Check the rate of men with high income
if len(ml) == 0:
    print('No men found in the dataset.')
elif len(ml1) == 0:
    print('No men with high income found in the dataset.')
else:
    print('The rate of men with high income is: ', int(len(ml1)) / float(len(ml)) * 100, '%.')
    
# Check the rate of women with high income
if len(fm) == 0:
    print('No women found in the dataset.')
elif len(fm1) == 0:
    print('No women with high income found in the dataset.')
else:
    print('The rate of women with high income is: ', int(len(fm1)) / float(len(fm)) * 100, '%.')


