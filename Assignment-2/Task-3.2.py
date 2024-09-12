from transformers import AutoTokenizer
from collections import Counter


def get_top_30_tokens(text_file_path):

    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

    # Read the merged text file
    with open(text_file_path, "r", encoding="utf-8") as file:
        text_data = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text_data)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    # Return the top 30 tokens
    return top_30_tokens


# Usage example:
text_file_path = "./data/task_1_merged_txt.txt"
top_30_tokens = get_top_30_tokens(text_file_path)

# Display top 30 tokens
print("Top 30 tokens:", top_30_tokens)
