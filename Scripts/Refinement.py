import deepl
import csv

# This script translates a list of English terms into Dutch using DeepL's translation service. It applies a custom glossary to ensure certain terms are translated according to specified expert-provided translations.

# Input:
# - 'Homosaurus_english_prefLabel.csv': A CSV file containing the list of terms to be translated. 
# - 'experts_tokens_dutch.csv': A CSV file with expert-provided English-Dutch term translations.
# - 'Method_B.csv': A CSV file with a list of terms that should be included in the custom glossary.
# 
# Output: 'refined_DeepL_translations.csv': A CSV file containing the translated terms.

# To have a different CSV file as the input change the name 'Homosaurus_english_prefLabel.csv' in line 32. If it's in a different language change the "EN" in lines 42 and 50,
# and make sure that the CSV file with the experts' translations corresponds to the change in language.
# To have a different file be the expert-provided translations change the name 'experts_tokens_dutch.csv' in line. 
# Also, if your expert translations are in a different language change the "NL" in lines 43 and 50 to the preferred language
# To have a different set of tokens being used change the name 'Method_B.csv' in line

# To run this code, you need to change the text "DEEPL_API_KEY" in line 16 to include the DeepL API key you retrieve from your own DeepL account
YOUR_API_KEY = "DEEPL_API_KEY"

# Create a DeepL translator object
translator = deepl.Translator(YOUR_API_KEY)

# Load the CSV files into lists
def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader]

# Load the Homosaurus_english_prefLabel, expert tokens and Method files
input_terms = [row[0] for row in load_csv('Homosaurus_english_prefLabel.csv')]
experts_tokens = load_csv('experts_tokens_dutch.csv')
method_b_terms = [row[0] for row in load_csv('Method_B.csv')]

# Filter the glossary to include only the tokens that are in Method_B
glossary_dict = {row[0]: row[1] for row in experts_tokens if row[0] in method_b_terms}

# Create a glossary using DeepL
glossary = translator.create_glossary(
    name="CustomGlossary",
    source_lang="EN",
    target_lang="NL",
    entries=glossary_dict
)

# Translate terms, applying the glossary where necessary
translated_terms = []
for term in input_terms:
    translated_word = translator.translate_text(term, source_lang="EN", target_lang="NL", glossary=glossary).text
    translated_terms.append(translated_word)

# Save the translated terms to a CSV file
with open('refined_DeepL_translations.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for term in translated_terms:
        writer.writerow([term])

print("Translation completed and saved to refined_DeepL_translations.csv")

