import os
from collections import Counter

# Define the path to the book
book_path = os.path.join("books", "Frankenstein.txt")

# Open and read the book
with open(book_path, 'r') as file:
    content = file.read()
words = content.split()

# Print the content of the book

print(f"Number of words: {len(words)}")

def count_characters(text):
    text = text.lower()
    return Counter(text)

# Example usage
char_count = count_characters(content)
print(char_count)

# Generate report
def generate_report(content, words, char_count):
    report = []
    report.append("Book Report")
    report.append("=" * 40)
    report.append(f"Total number of words: {len(words)}")
    report.append(f"Total number of characters: {sum(char_count.values())}")
    report.append("\nCharacter Frequency:")
    for char, count in char_count.items():
        report.append(f"{char}: {count}")
    return "\n".join(report)

# Print the report
report = generate_report(content, words, char_count)
print(report)
