import re
import requests
from collections import Counter
from modules.stop_words import stop_words_list

# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
url = 'https://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
# print(response)
# print(response.status_code)

url_content = response.text                                                               # Store url text content in a variable
url_content = url_content.lower()                                                         # Convert everything to lowercaps
stop_words = stop_words_list()                                                            # Call English stop words module
main_words = " ".join([word for word in url_content.split() if word not in stop_words])   # Remove stop words
clean_text = re.sub(r'[^\w\s]', '', main_words)                                           # Remove punctuation
clean_text = re.findall(r'[a-zA-Z]+', clean_text)                                         # Find complete words

word_count = dict(Counter(clean_text))                                                    # Count words and create a dictionary
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)          # Sort word count by descending order

print(f"Top 10 most common words in Romeo and Juliet: {sorted_word_count[:10]}")          # Print out top 10 most common words