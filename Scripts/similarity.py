import csv
from fuzzywuzzy import fuzz
import Levenshtein

# This script compares words in two CSV files (output_dutch.csv and prefLabel.csv) in a case-insensitive manner using three different algorithms:
# 1. Fuzzy string matching with the Ratio algorithm (using fuzzywuzzy).
# 2. Jaccard similarity.
# 3. Levenshtein distance.
# The script calculates similarity scores and writes the results to three separate CSV files.

# Input:
# Two CSV files:
# 1. output_dutch.csv - A list of our translated terms.
# 2. prefLabel.csv - A list of the Dutch Homosaurus preflabels.

# Output:
# Three CSV files with similarity results:
# 1. similarity_results_ratio.csv - Results using the Ratio algorithm.
# 2. similarity_results_jaccard.csv - Results using Jaccard similarity.
# 3. similarity_results_levenshtein.csv - Results using Levenshtein distance.
# Also, the script prints the following information to the console:
# 1. Count of terms in different similarity score ranges for the Ratio algorithm.
# 2. Count of terms in different similarity score ranges for Jaccard similarity.
# 3. Count of terms in different distance ranges for Levenshtein distance.
# 4. Number of exact matches found using the Jaccard similarity.
# 5. Number of exact matches found using the Ratio algorithm.

# If the user wants to compare different files they need to change the "output_dutch_methodB_semi-manual.csv" in line 33 and the "prefLabel.csv" in line 39


# Read the two CSV files into lists
output_dutch = []
with open("output_dutch_methodB_semi-manual.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    output_dutch.append(row[0].lower())  # Convert to lowercase

prefLabel = []
with open("prefLabel.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    prefLabel.append(row[0].lower())  # Convert to lowercase

# Create lists to store the results
similarity_scores_r = []
similarity_scores_j = []
min_distances = []
results_ratio = []
results_jaccard = []
results_levenshtein = []


# Iterate over the words in the output_dutch list and calculate the similarity score for each word using the Ratio algorithm
for word in output_dutch:
  max_similarity_score_r = 0
  best_label_r = ''
  for label in prefLabel:
    similarity_score = fuzz.ratio(word, label)
    if similarity_score > max_similarity_score_r:
        max_similarity_score_r = similarity_score
        best_label_r = label
  similarity_scores_r.append(max_similarity_score_r)
  results_ratio.append((word, max_similarity_score_r, best_label_r))

# Function to calculate Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

# Iterate over the words in the output_dutch list and calculate the similarity score for each word using Jaccard similarity
for word in output_dutch:
    max_similarity_score_j = 0
    best_label_j = ''
    word_set = set(word.split())  # Split the term into a set of words
    for label in prefLabel:
        label_set = set(label.split())  # Split the preflabel into a set of words
        similarity_score = jaccard_similarity(word_set, label_set)
        if similarity_score > max_similarity_score_j:
            max_similarity_score_j = similarity_score
            best_label_j = label
    similarity_scores_j.append(max_similarity_score_j)
    results_jaccard.append((word, max_similarity_score_j, best_label_j))

#calculate the Levenshtein distance between two words.
def min_levenshtein_distance(word1, word2):
    return Levenshtein.distance(word1, word2)

#calculate the minimum Levenshtein distance between a word and a list of labels.
def calculate_min_distance(word, labels):
    min_distance = float('inf')
    best_label_ld = ''
    for label in labels:
        distance = min_levenshtein_distance(word, label)
        if distance < min_distance:
            min_distance = distance
            best_label_ld = label
    return min_distance, best_label_ld

#calculate the minimum Levenshtein distance for each word in output_dutch, and store the results in the min_distances list.
min_distances = []
for word in output_dutch:
    min_distance, best_label_ld = calculate_min_distance(word, prefLabel)
    min_distances.append(min_distance)
    results_levenshtein.append((word, min_distance, best_label_ld))

# Write the results to CSV files
with open("similarity_results_ratio.csv", "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Word", "Max Similarity Score (Ratio)", "Best Label (Ratio)"])
    for result in results_ratio:
        writer.writerow(result)

with open("similarity_results_jaccard.csv", "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Word", "Max Similarity Score (Jaccard)", "Best Label (Jaccard)"])
    for result in results_jaccard:
        writer.writerow(result)

with open("Levenshtein_distance_results.csv", "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Word", "Min Distance (Levenshtein)", "Best Label (Levenshtein)"])
    for result in results_levenshtein:
        writer.writerow(result)

# initialize counters for different similarity score ranges
counter_r = [0] * 10
counter_j = [0] * 10
counter_ld = [0] * 10

# Calculate matches (total2=exact matches) with ratio algorithm
total2 = 0
for score in similarity_scores_r:
    index = score // 10 # Determine the index in counter_r
    if index < 10:
        counter_r[index] += 1
    else:
        counter_r[9] += 1
        total2 += 1

# Calculate matches (total1=exact matches) with Jaccard similarity
total1 = 0
# Iterate through the similarity_scores_j list and count scores in each range
for score in similarity_scores_j:
    if score == 1.0:
        counter_j[-1] += 1  # If the score is 1, count it in the last range
        total1 += 1
    else:
        index = int(score * 10)  # Determine the index in counter_j
        if 0 <= index < 10:
            counter_j[index] += 1

# Calculate matches with Levenshtein distance
for score in min_distances:
    if score < 9:
        counter_ld[score] += 1
    else:
        counter_ld[9] += 1

# Print results summary for Ratio algorithm
print("RATIO algorithm")
for i, count in enumerate(counter_r):
    print(f"Count in range {i * 10}-{(i + 1) * 10}: {count} terms")

# Print results summary for Jaccard similarity
print("Jaccard Similarity")
for i, count in enumerate(counter_j):
    range_start = i / 10
    range_end = (i + 1) / 10 if i < 9 else 1
    print(f"Count in range {range_start:.1f}-{range_end:.1f}: {count} terms")

# Print results summary for Levenshtein distance
print("Levenshtein distance")
for i, count in enumerate(counter_ld):
    print(f"With distance {i} there are: {count} terms")



# Print the number of exact words
print(f"Number of exact words with the Jaccard similarity: {total1} terms")
print(f"Number of exact words with the Ratio Algorithm: {total2} terms")