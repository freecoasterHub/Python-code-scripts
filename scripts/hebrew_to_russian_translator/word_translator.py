import csv
from googletrans import Translator

def translate_phrases(phrases, src_lang='he', dest_lang='ru'):
    """
    Translates a list of phrases from source language to destination language.
    """
    translator = Translator()
    translations = []
    for phrase in phrases:
        translated = translator.translate(phrase, src=src_lang, dest=dest_lang).text
        translations.append((phrase, translated))
    return translations

def save_translations_to_csv(translations, output_csv):
    """
    Saves translations to a CSV file with the specified structure.
    """
    header = ["he", "ru", "he", "ru"]  # Header as per the required structure
    rows = [header] + [["Hebrew", "Russian", he, ru] for he, ru in translations]
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"CSV file successfully saved to {output_csv}")

if __name__ == "__main__":
    # List of phrases in Hebrew
    hebrew_phrases = [
        "ראשי", "עובר ושב", "כרטיסי אשראי", "פיקדונות וחסכונות", "מטבע חוץ",
        "ריכוז יתרות", "החשבון שלי", "השותף", "יצירת קשר", "הגדרות", "תפריט",
        "כחול", "אפור"
    ]
    
    # Translate phrases
    translations = translate_phrases(hebrew_phrases)
    
    # Save translations to CSV
    output_csv = 'output_data/output_phrases.csv'
    save_translations_to_csv(translations, output_csv)