# 1. Chemical Formula Parser:
# Write a Python function capable of parsing chemical formulas such as "H2O", "NaCl", or "CF4". Your function should accurately count the occurrences of each element and return a dictionary with the element symbols as keys and their corresponding counts as values.
import re  # for matching patterns in strings

def parse_chemical_formula(formula):
    pattern = r'([A-Z][a-z]*)(\d*)'  # defines a regular expression pattern,
    elements = re.findall(pattern, formula)  # matches a capital letter followed by zero or more lowercase letters to represent symbol

    # Dictionary
    element_counts = {}

    for element, count in elements:
        if count == '':
            count = 1
        else:
            count = int(count)
        if element in element_counts:
            element_counts[element] += count
        else:
            element_counts[element] = count

    return element_counts

# Trial runs!
formula = "H2O"
result = parse_chemical_formula(formula)
print( "H2O has: ", result)  #yay

formula = "NaCl"
result = parse_chemical_formula(formula)
print(result)

formula = "CF4"
result = parse_chemical_formula(formula)
print(result)

formula = "FCN"  # trial with 3 diff elements in a compound
result = parse_chemical_formula(formula)
print(result)

formula = "CH2NH"  #trial with reoccuring H in diff places in the compound
result = parse_chemical_formula(formula)
print(result)

formula = str(input())
result = parse_chemical_formula(formula)
print(result)

# 2. Data Analysis Task:
# Explore various aspects of the data ('dataset_quantemol.csv'). Your analysis should cover the following:
# Data Cleaning: Identify and address any missing or possibly erroneous data. Perform operations such as imputation or removal of duplicates to ensure data integrity.
# Data Exploration and Visualisation: Investigate the dataset's structure, features, and any notable patterns or trends. Utilise summary statistics, data visualisation, or other exploratory techniques to gain insights.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read csv
df = pd.read_csv("dataset_quantemol.csv")
print(df)
print(df.info())
print(df.describe())

#calculate the precentage of missing values in each value in each column
missing_precentage = df.isnull().mean() * 100
print("Precentage of Missing Values in Each Column: \n", missing_precentage)

# The majority of columns have 0% missing values however, the column 'ionisation_potential' has approximately 59.72% missing values, indicating a significant portion of values are missing. Handling missing values in 'ionisation_potential' may be necessary before analysis but due to this being such a large precentage of the data, exluding these points may also be too limiting. Isonisation potential might be missing values because: obtaining accurate ionization potential values can be challenging due to experimental limitations or some compounds may lack ionization potential data altogether.
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)
print(df)

# Correlation matrix
correlation_matrix = df.iloc[:, 3:].corr() # taking away index, formula and names that can be observed from the excel sheet
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Find empty columns or columns with all zero values
empty_columns = df.columns[(df == 0).all()]
print("Empty columns or columns with all zero values:", empty_columns)

df.drop(empty_columns, axis=1, inplace=True)  # remove empty columns
correlation_matrix = df.iloc[:, 3:].corr()  # excluding the first three columns (index, formula, species_name)

# Plot
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1) 
plt.title('Correlation Matrix')
plt.show()

# By adding vmax and vmin, all blue and red values are for negative and positive correlation respectively, thus aiding in data visualisation. Since the correlation matrix is symmetrical along the diagonal, I have decided to omit the upper triangle to avoid repeating information.

empty_columns = df.columns[(df == 0).all()]
df.drop(empty_columns, axis=1, inplace=True)
correlation_matrix = df.iloc[:, 3:].corr()
plt.figure(figsize=(20, 10))
mask = np.triu(np.ones_like(df.corr(numeric_only = True)))
sns.heatmap(df.corr(numeric_only = True), cmap='coolwarm', mask = mask, annot = True, vmin=-1, vmax=1)
print(plt.show())
