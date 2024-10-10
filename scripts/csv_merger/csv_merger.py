import os
import pandas as pd

def combine_csv_files(input_directory, output_file):
    """
    Combines multiple CSV files into one and removes duplicates based on the third column.
    """
    combined_df = pd.DataFrame()
    
    # Iterate over all CSV files in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_directory, filename)
            df = pd.read_csv(file_path)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    # Remove duplicates based on the third column
    if len(combined_df.columns) >= 3:
        combined_df.drop_duplicates(subset=combined_df.columns[2], inplace=True)
    else:
        print("Warning: Not enough columns to drop duplicates based on the third column.")

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved to {output_file}")

if __name__ == "__main__":
    # Specify the input directory and output file
    input_directory = 'input_data/verbs'  # Replace with your input directory
    output_file = 'output_data/combined_verbs.csv'  # Replace with your desired output file

    # Execute the combine function
    combine_csv_files(input_directory, output_file)