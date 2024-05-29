import csv
from fuzzywuzzy import fuzz
import Levenshtein


# Read the two CSV files into lists
output_dutch = []
with open("output_dutch.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    output_dutch.append(row[0])

prefLabel = []
with open("prefLabel.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    prefLabel.append(row[0])

# Create a new list to store the similarity score for each word
similarity_scores_r = []
similarity_scores_j = []


# Iterate over the words in the output_dutch list and calculate the similarity score for each word
for word in output_dutch:
  max_similarity_score = 0
  for label in prefLabel:
    similarity_score = fuzz.ratio(word, label)
    if similarity_score > max_similarity_score:
        max_similarity_score = similarity_score
  similarity_scores_r.append(max_similarity_score)

# Function to calculate Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

# Iterate over the words in the output_dutch list and calculate the similarity score for each word using Jaccard similarity
for word in output_dutch:
    max_similarity_score = 0
    word_set = set(word)
    for label in prefLabel:
        label_set = set(label)
        similarity_score = jaccard_similarity(word_set, label_set)
        if similarity_score > max_similarity_score:
            max_similarity_score = similarity_score
    similarity_scores_j.append(max_similarity_score)

#calculate the Levenshtein distance between two words.
def min_levenshtein_distance(word1, word2):
    return Levenshtein.distance(word1, word2)

#calculate the minimum Levenshtein distance between a word and a list of labels.
def calculate_min_distance(word, labels):
    min_distance = float('inf')
    for label in labels:
        distance = min_levenshtein_distance(word, label)
        min_distance = min(min_distance, distance)
    return min_distance

#calculate the minimum Levenshtein distance for each word in output_dutch, and store the results in the min_distances list.
min_distances = []
for word in output_dutch:
    min_distance = calculate_min_distance(word, prefLabel)
    min_distances.append(min_distance)

# Count the number of words in the similarity_scores list with a similarity score greater than or equal to 0.8
number_of_matched_words_r = sum(score >= 90 for score in similarity_scores_r)
number_of_matched_words_j = sum(score >= 0.9 for score in similarity_scores_j)
number_of_matched_words_ld = sum(score <= 2 for score in min_distances)

counter_r = [0] * 10
counter_j = [0] * 10
counter_ld = [0] * 10

# Calculate matches (total2=exact matches) with ratio algorithm
total2 = 0
for score in similarity_scores_r:
    index = score // 10  # Determine the index in counter_r
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

print("RATIO algorithm")
for i, count in enumerate(counter_r):
    print(f"Count in range {i * 10}-{(i + 1) * 10}: {count} terms")

print("Jaccard Similarity")
for i, count in enumerate(counter_j):
    range_start = i / 10
    range_end = (i + 1) / 10 if i < 9 else 1
    print(f"Count in range {range_start:.1f}-{range_end:.1f}: {count} terms")

print("Levenshtein distance")
for i, count in enumerate(counter_ld):
    print(f"With distnce {i} there are: {count} terms")



# Print the number of exact words
print(f"Number of exact words with the Jaccard similarity: {total1} terms")
print(f"Number of exact words with the Ratio Algorithm: {total2} terms")