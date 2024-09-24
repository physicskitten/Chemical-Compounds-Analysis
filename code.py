# 1. Chemical Formula Parser:
# Write a Python function capable of parsing chemical formulas such as "H2O", "NaCl", or "CF4". Your function should accurately count the occurrences of each element and return a dictionary with the element symbols as keys and their corresponding counts as values.

import re  # for matching patterns in strings

def parse_chemical_formula(formula):
    """
    Parses a chemical formula and returns a dictionary with element symbols as keys and their corresponding counts as values.
    
    Args:
        formula (str): The chemical formula as a string (e.g., 'H2O', 'NaCl').
    
    Returns:
        dict: A dictionary where keys are element symbols and values are their counts.
    """
    pattern = r'([A-Z][a-z]*)(\d*)'  # defines a regular expression pattern,
    # matches a capital letter followed by zero or more lowercase letters to represent symbol
    elements = re.findall(pattern, formula)  # Find all element-count pairs in the formula

    # Dictionary
    element_counts = {}

    for element, count in elements:
        if count == '':  # If no count, assume it is 1
            count = 1
        else:
            count = int(count)
        # If element already exists in dictionary, update its count
        if element in element_counts:
            element_counts[element] += count
        else:
            element_counts[element] = count

    return element_counts

# Trial runs!
formulas = ["H2O", "NaCl", "CF4", "FCN", "CH2NH"]  # Various sample formulas for testing

for formula in formulas:
    result = parse_chemical_formula(formula)
    print(f"{formula} has: {result}")  #yay  # Print result for each formula

formula = str(input("Enter a chemical formula: "))  # Allow user input for testing additional formulas
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
print(df)  # Print the initial dataset
print(df.info())  # Information about the dataset, including data types and missing values
print(df.describe())  # Summary statistics for numerical columns

#calculate the percentage of missing values in each column
missing_percentage = df.isnull().mean() * 100  # Calculate percentage of missing values
print("Percentage of Missing Values in Each Column: \n", missing_percentage)

# The majority of columns have 0% missing values however, the column 'ionisation_potential' has approximately 59.72% missing values, indicating a significant portion of values are missing. 
# Handling missing values in 'ionisation_potential' may be necessary before analysis but due to this being such a large percentage of the data, excluding these points may also be too limiting. 
# Ionization potential might be missing values because: obtaining accurate ionization potential values can be challenging due to experimental limitations or some compounds may lack ionization potential data altogether.
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)
print(df)  # Print dataset after duplicates are removed

# Correlation matrix
correlation_matrix = df.iloc[:, 3:].corr() # taking away index, formula and names that can be observed from the excel sheet
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Annotate the heatmap with values
plt.title('Correlation Matrix')
plt.show()

# Find empty columns or columns with all zero values
empty_columns = df.columns[(df == 0).all()]  # Identify columns that are completely empty or contain only zeros
print("Empty columns or columns with all zero values:", empty_columns)

df.drop(empty_columns, axis=1, inplace=True)  # remove empty columns
correlation_matrix = df.iloc[:, 3:].corr()  # Recalculate correlation matrix after removing empty columns

# Plot the new correlation matrix after dropping empty columns
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)  # Set vmin and vmax for color range
plt.title('Correlation Matrix After Removing Empty Columns')
plt.show()

# By adding vmax and vmin, all blue and red values are for negative and positive correlation respectively, thus aiding in data visualization. Since the correlation matrix is symmetrical along the diagonal, I have decided to omit the upper triangle to avoid repeating information.

# Enhanced correlation matrix plot with upper triangle omitted for better clarity
plt.figure(figsize=(20, 10))
mask = np.triu(np.ones_like(df.corr(numeric_only=True)))  # Mask to remove the upper triangle
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', mask=mask, annot=True, vmin=-1, vmax=1)  # Masked heatmap
plt.title('Correlation Matrix with Masked Upper Triangle')  # Add a title for clarity
plt.show()
