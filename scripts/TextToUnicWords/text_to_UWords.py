import pandas as pd
import re
from googletrans import Translator
import concurrent.futures
import httpcore

def translate_word(word, translator):
    """
    Translates a single word from Hebrew to Russian.
    """
    try:
        result = translator.translate(word, src='he', dest='ru')
        return word, result.text
    except httpcore._exceptions.ReadTimeout:
        return word, "Translation unavailable"
    except Exception:
        return word, "Translation unavailable"

def main():
    # Source text for processing
    text = """
    ... (ваш текст) ...
    """
    
    # Remove non-Hebrew characters
    cleaned_text = re.sub(r'[^א-ת\s]', '', text)
    words = cleaned_text.split()
    
    # Get unique words
    unique_words = set(words)
    print(f'Found {len(unique_words)} unique Hebrew words.')
    
    translator = Translator()
    translations = {}
    
    # Translate words concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_word = {executor.submit(translate_word, word, translator): word for word in unique_words}
        for future in concurrent.futures.as_completed(future_to_word):
            word, translation = future.result()
            translations[word] = translation
    
    # Prepare data for DataFrame
    unique_words_list = list(translations.keys())
    translations_list = list(translations.values())
    
    new_data = {
        "he": ["he"] * len(unique_words_list),
        "ru": ["ru"] * len(unique_words_list),
        "he_word": unique_words_list,
        "ru_translation": translations_list
    }
    
    new_df = pd.DataFrame(new_data)
    print('DataFrame created.')
    
    # Save to CSV
    output_path = 'output_data/unique_words.csv'
    new_df.to_csv(output_path, index=False, header=False, encoding='utf-8-sig')
    print(f'CSV file saved at: {output_path}')
    
    # Add headers to CSV file
    with open(output_path, 'r+', encoding='utf-8-sig') as file:
        content = file.read()
        file.seek(0, 0)
        file.write("he,ru,he,ru\n" + content)
    print('Headers added to CSV file.')

if __name__ == "__main__":
    main()