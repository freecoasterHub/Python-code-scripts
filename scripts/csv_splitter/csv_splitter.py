import csv
import os

# Define file paths
input_file = 'input_data/Hebrew_Numerals.csv'
output_dir = 'output_data/Automotive_terms'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def clean_row(row):
    """
    Removes empty elements from a row.
    """
    return [element for element in row if element]

def main():
    # Read the input CSV file
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))
        
        header = reader[0]
        data = reader[1:]

        # Clean each row
        cleaned_data = [clean_row(row) for row in data if any(row)]

        # Split data into chunks of 11 lines each
        chunk_size = 11
        for i in range(0, len(cleaned_data), chunk_size):
            chunk = cleaned_data[i:i + chunk_size]
            
            # Define the output file path
            output_file = os.path.join(output_dir, f'Automotive_terms_{i // chunk_size + 1}.csv')
            
            # Write the chunk to a new CSV file
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                # Write the header
                writer.writerow(header)
                # Write the cleaned chunk
                writer.writerows(chunk)

    print("Files have been cleaned, split, and saved successfully.")

if __name__ == "__main__":
    main()