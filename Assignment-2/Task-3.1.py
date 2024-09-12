from collections import Counter
import csv
import re

# Read the merged text file
with open("./data/task_1_merged_txt.txt", "r", encoding="utf-8") as file:
    text_data = file.read()

# Tokenize and count word occurrences (excluding punctuation)
words = re.findall(r'\b\w+\b', text_data.lower())
word_counts = Counter(words)  # initlize counter

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Save to CSV
with open("./data/top_30_common_words.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Word", "Count"])
    writer.writerows(top_30_words)

print("Top 30 common words saved to './data/top_30_common_words.csv'")
