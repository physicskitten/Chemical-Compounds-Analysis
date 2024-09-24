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
    # Regular expression to capture element symbols and their counts
    pattern = r'([A-Z][a-z]*)(\d*)'
    elements = re.findall(pattern, formula)  # Find all element-count pairs in the formula

    element_counts = {}  # Dictionary to hold element symbols and their counts

    for element, count in elements:
        # Default count is 1 if no number is provided
        count = int(count) if count else 1
        
        # Add the element to the dictionary or update its count if it already exists
        element_counts[element] = element_counts.get(element, 0) + count

    return element_counts

# Trial runs
formulas = ["H2O", "NaCl", "CF4", "FCN", "CH2NH"]

for formula in formulas:
    result = parse_chemical_formula(formula)
    print(f"{formula} has: {result}")

# Allow input from the user to test other formulas
user_formula = str(input("Enter a chemical formula: "))
result = parse_chemical_formula(user_formula)
print(f"{user_formula} has: {result}")

# 2. Data Analysis Task:
# Explore various aspects of the data ('dataset_quantemol.csv'). Your analysis should cover the following:
# Data Cleaning: Identify and address any missing or possibly erroneous data. Perform operations such as imputation or removal of duplicates to ensure data integrity.
# Data Exploration and Visualisation: Investigate the dataset's structure, features, and any notable patterns or trends. Utilise summary statistics, data visualisation, or other exploratory techniques to gain insights.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("dataset_quantemol.csv")
print("Initial Dataset Preview:\n", df.head())
print("\nDataset Information:\n")
df.info()  # Provides an overview of the dataset structure
print("\nDataset Summary Statistics:\n", df.describe())  # Summary statistics for numerical columns

# Calculate the percentage of missing values in each column
missing_percentage = df.isnull().mean() * 100
print("\nPercentage of Missing Values in Each Column: \n", missing_percentage)

# Comment on missing values:
# The column 'ionisation_potential' has approximately 59.72% missing values.
# Given the high percentage, we need to decide how to handle it, either through imputation or careful exclusion.

# Remove duplicates to ensure no repeated data
df.drop_duplicates(inplace=True)
print("\nDataset After Removing Duplicates:\n", df)

# Visualize the correlation matrix for numerical columns (excluding first three, which are non-numerical)
correlation_matrix = df.iloc[:, 3:].corr()  # Exclude non-numerical columns (index, formula, names)
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Identify and remove empty columns or columns with all zero values
empty_columns = df.columns[(df == 0).all()]
print("Empty columns or columns with all zero values:", empty_columns)

df.drop(empty_columns, axis=1, inplace=True)  # Remove empty columns

# Re-calculate the correlation matrix after removing zero-value columns
correlation_matrix = df.iloc[:, 3:].corr()  # Exclude first three non-numerical columns
plt.figure(figsize=(20, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)  # Set vmin and vmax for color range
plt.title('Correlation Matrix After Removing Empty Columns')
plt.show()

# Enhanced correlation matrix visualization: mask the upper triangle to avoid redundancy
plt.figure(figsize=(20, 10))
mask = np.triu(np.ones_like(df.corr(numeric_only=True)))  # Mask to remove upper triangle
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', mask=mask, annot=True, vmin=-1, vmax=1)
plt.title('Correlation Matrix with Masked Upper Triangle')
plt.show()
