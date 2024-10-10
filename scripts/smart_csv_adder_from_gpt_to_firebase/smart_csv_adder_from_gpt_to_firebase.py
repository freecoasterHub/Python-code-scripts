import pandas as pd

# User-defined translations
translations = {
    "דוושת בלם": "Brake pedal",
    "דוושת גז": "Gas pedal",
    "מזגן רכב": "Car air conditioner",
    # ... (other pairs of translations)
}

# Words to exclude if duplicates are found
additional_words = [
    "מְכוֹנִית",
    "גַלגַל",
    # ... (other words)
]

def create_csv(output_path):
    """
    Creates a CSV file with translations, excluding specified words.
    """
    # Create a list of unique words, excluding additional words
    unique_words_list = [word for word in translations.keys() if word not in additional_words]
    translations_list = [translations[word] for word in unique_words_list]
    
    # Prepare data for DataFrame
    new_data = {
        "he": ["he"] * len(unique_words_list),
        "ru": ["ru"] * len(unique_words_list),
        "he_word": unique_words_list,
        "ru_translation": translations_list
    }
    
    # Create DataFrame
    new_df = pd.DataFrame(new_data)
    
    # Save DataFrame to CSV
    new_df.to_csv(output_path, index=False, header=False, encoding='utf-8')
    
    # Add headers to CSV file
    with open(output_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write("he,ru,he,ru\n" + content)
    
    print(f"CSV file successfully created at: {output_path}")

if __name__ == "__main__":
    output_path = 'output_data/new_auto_words.csv'
    create_csv(output_path)