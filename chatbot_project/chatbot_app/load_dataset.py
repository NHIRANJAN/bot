import os
import pandas as pd

def load_dataset():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'Book1.xlsx')  # Update the file name

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the XLSX file
        df = pd.read_excel(file_path)  # Use pd.read_excel for XLSX files
        # Process the data as needed
        print(df.head())
        print(df)  # Example: print the first few rows of the DataFrame
    else:
        print("File 'Book1.xlsx' not found.")

if __name__ == "__main__":
    load_dataset()
