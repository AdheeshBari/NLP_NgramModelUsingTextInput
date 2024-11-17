# NLP_NgramModelUsingTextInput
This script generates N-Grams from text and calculates their frequencies.

This Python script uses the NLTK library to tokenize input text, generate N-Grams (contiguous sequences of n words), and compute their frequencies.
Steps:
1. Setup and Download: The script ensures the necessary NLTK data (punkt for word tokenization) is downloaded.
2. N-Gram Generation Function: 
    The function generate_ngrams(text, n):
        Tokenizes the input text into individual words using nltk.word_tokenize.
        Generates N-Grams using nltk.util.ngrams, which creates tuples of n consecutive tokens.
        Counts N-Grams using collections.Counter to store the frequency of each N-Gram.
3. User Input:
    Value of N: The user specifies the number of words in each N-Gram.
    Text Input: The user provides the text to be processed.
4. Output:
    Displays each N-Gram as a tuple along with its frequency.
Notes: N-Gram Choice: Higher values of N result in longer sequences, capturing context but reducing overlap.
Applications:
    Text Analysis: Extracting frequently used phrases or patterns.
    Language Modeling: Building predictive text models.
