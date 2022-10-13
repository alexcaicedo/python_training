import re
import string
import spacy
import numpy as np
from modules.stop_words import stop_words_list
from collections import Counter

def lowercaps_text(text):
    lowercaps_text = text.lower()
    return lowercaps_text

def remove_stop_words(text, stop_words):
    main_words_text = " ".join([word for word in text.split() if word not in stop_words])
    return main_words_text

def remove_unicode(text):
    text_encode = text.encode("ascii", errors="ignore")
    return text_encode

def remove_punctuation(text):
    punct = set(string.punctuation)
    no_punct_text = "".join([ch for ch in text if ch not in punct])
    return no_punct_text

def check_text_similarity(filepath_a, filepath_b):
    """
    Function that takes two text files and returns the top 10 most used words and their similarity rate.

    Args:
        - filepath_a: Path of file a (first file). --> Type str object.
        - filepath b: Path of file b (second file). --> Type str object.
    
    Returns:
        - top_10_a: Top 10 most used words in text a. --> Type List object.
        - top_10_b: Top 10 most used words in text b. --> Type List object.
        - sr: Similarity Rate. --> Type numpy.float64 object.
    """

    # Read files
    with open(filepath_a, "r") as file_a:
        content_a = file_a.read()
    
    with open(filepath_b, "r") as file_b:
        content_b = file_b.read()
    
    # Clean content of each file
    content_a = lowercaps_text(content_a)
    content_b = lowercaps_text(content_b)

    content_a = remove_punctuation(content_a)
    content_b = remove_punctuation(content_b)

    # Remove stop words from each text
    stop_words = stop_words_list()
    content_a = remove_stop_words(content_a, stop_words)
    content_b = remove_stop_words(content_b, stop_words)

    # Match complete words using a RegEx pattern
    word_list_a = re.findall(r'[a-zA-Z]+', content_a) # ==> Returns a list obj.
    word_list_b = re.findall(r'[a-zA-Z]+', content_b) # ==> Returns a list obj.

    # Combine words from lists to form content back again
    content_a = " ".join([word for word in word_list_a])
    content_b = " ".join([word for word in word_list_b])

    # # Count the frequency of the words
    word_count_a = dict(Counter(word_list_a))
    word_count_b = dict(Counter(word_list_b))

    # Sort the word count by descending order
    sorted_word_count_a = sorted(word_count_a.items(), key=lambda x: x[1], reverse=True)
    sorted_word_count_b = sorted(word_count_b.items(), key=lambda x: x[1], reverse=True)

    top_10_a = sorted_word_count_a[:10]
    top_10_b = sorted_word_count_b[:10]

    # Load the Spacy model
    nlp = spacy.load("en_core_web_md")

    # Obtain tokens from both texts
    tokens_a = nlp(content_a)
    tokens_b = nlp(content_b)

    # Calculate similarity rate between texts
    sr = np.round(tokens_a.similarity(tokens_b), 4)
    
    return top_10_a, top_10_b, sr