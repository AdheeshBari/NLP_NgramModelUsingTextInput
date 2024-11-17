import nltk
from nltk.util import ngrams
from collections import Counter

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')

def generate_ngrams(text, n):
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    
    # Generate N-Grams
    n_grams = ngrams(tokens, n)
    
    # Count the frequency of each N-Gram
    ngram_counts = Counter(n_grams)
    
    return ngram_counts

if __name__ == "__main__":
    # Input for the number of N-Grams
    n = int(input("Enter the value of N for N-Grams: "))
    
    # Input for the text
    text_input = input("Enter the text: ")
    
    # Generate N-Grams and their counts
    ngram_counts = generate_ngrams(text_input, n)
    
    # Output the N-Grams and their frequencies
    print("\nGenerated N-Grams and their Frequencies:")
    for ngram, count in ngram_counts.items():
        print(f"{ngram}: {count}")
