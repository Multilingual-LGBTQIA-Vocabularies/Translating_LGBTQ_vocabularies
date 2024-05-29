import deepl
import csv

YOUR_API_KEY = "5fd103b7-510a-d088-5bad-f2b5a6261af7:fx"

# Create a DeepL translator object
translator = deepl.Translator(YOUR_API_KEY)

# Open the CSV file to be translated
with open("input.csv", "r", encoding="utf-8") as f:
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