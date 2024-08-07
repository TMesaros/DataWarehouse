import pandas as pd

# Define the file path for input and output
input_file_path = r'C:\OMS Masters program\CS 6400\Phase 3\school data\Product - Copy.tsv'
output_file_path = r'C:\OMS Masters program\CS 6400\Phase 3\school data\ProductCategory.tsv'

# Attempt to read the TSV file into a DataFrame
try:
    # Read the TSV file into a DataFrame
    df = pd.read_csv(input_file_path, sep='\t')
    
    # Select only the 'employeeID' and 'districts_assigned' columns
    df = df[['PID', 'categories']]
    
    # Perform the transformation: split 'districts_assigned' and explode
    df['categories'] = df['categories'].str.split(',')
    df = df.explode('categories')
    
    # Rename columns to 'employeeID' and 'district'
    df.columns = ['PID', 'CategoryName']
    
    # Save the result to a new TSV file
    df.to_csv(output_file_path, sep='\t', index=False)
    
    print(f'Transformation complete. The output file is saved as {output_file_path}.')
    
except FileNotFoundError:
    print(f"Error: The file at {input_file_path} was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file at {input_file_path} is empty.")
except pd.errors.ParserError:
    print(f"Error: There was an issue parsing the file at {input_file_path}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")