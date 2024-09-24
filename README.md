# Chemical Formula Parser & Data Analysis Tool

## Overview

This project contains two main functionalities:

1. **Chemical Formula Parser**: A Python function that parses chemical formulas (such as H₂O, NaCl, or CF₄), counting the occurrences of each element and returning a dictionary.  
2. **Data Analysis Task**: A set of data analysis techniques applied to a dataset (`dataset_quantemol.csv`). This analysis includes data cleaning, identifying missing values, removing duplicates, and visualizing correlations using a heatmap.

## Features

### 1. Chemical Formula Parser
- Parses a chemical formula and returns a dictionary of elements with their counts.
- Uses regular expressions to detect element symbols and their quantities.
- Supports user input to parse any chemical formula.

### 2. Data Analysis Task
- Reads a dataset (`dataset_quantemol.csv`) and performs various data cleaning tasks.
- Calculates missing value percentages for each column.
- Removes duplicates to ensure data integrity.
- Visualizes the correlation matrix between numerical features using Seaborn heatmaps.
    - First heatmap: A standard correlation matrix.
    - Second heatmap: A correlation matrix after removing columns with only zero values.
    - Third heatmap: A correlation matrix with the upper triangle masked to remove redundant information.
- Handles empty or zero-filled columns by removing them before analysis.
- Displays heatmaps, with the option to mask the upper triangle for clarity.

## Files

- **`chemical_formula_parser.py`**: Contains the function `parse_chemical_formula()` to parse chemical formulas and output element counts as a dictionary.
- **`data_analysis.py`**: Includes all steps for reading the dataset, cleaning it, calculating missing values, and generating visualizations.
- **`dataset_quantemol.csv`**: The dataset used for the data analysis task (this file must be present in the project directory).
- **`README.md`**: Project documentation.
