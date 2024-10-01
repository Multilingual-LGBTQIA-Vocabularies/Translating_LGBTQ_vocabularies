import deepl
import csv

# This script translates text in a CSV file from one language to another using the DeepL API.
# It reads the input CSV file, translates each cell's text, and writes the translated text to an output CSV file.

# Input: A CSV file named 'input.csv' containing the text to be translated.
# Output:A CSV file named 'output.csv' containing the translated text in the user's preffered language.

# To change the language that the Homosaurus_english_prefLabel.csv will be translated the user needs to change the 'NL' in line 35, according to the language they want.

# To translate a different file the user needs to change the name 'Homosaurus_english_prefLabel.csv' in line 21.

# To run this code, you need to change the text "DEEPL_API_KEY" in line 15 to include the DeepL API key you retrieve from your own DeepL account
YOUR_API_KEY = "DEEPL_API_KEY"

# Create a DeepL translator object
translator = deepl.Translator(YOUR_API_KEY)

# Open the CSV file to be translated
with open("Homosaurus_english_prefLabel.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Create a new CSV file to store the translated text
    i=0
    with open("output.csv", "w", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)

        # Iterate over the rows of the input CSV file
        for row in reader:
            # Translate each row of text
            translated_row = []
            for word in row:
                # To choose the language change "NL" to "SV" for Swedish, "FR" for French, "ES" for Spanish, etc.
                translated_word = translator.translate_text(word, target_lang="NL")
                translated_row.append(translated_word)

            # Write the translated row to the output CSV file
            writer.writerow(translated_row)
            i=i+1
            print(i)