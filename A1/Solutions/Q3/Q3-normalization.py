import nltk
import re

nltk.download('words')
english_dict = set(nltk.corpus.words.words())


def normalize_word(word):
    if word in english_dict:
        return word
    new_word = re.compile(r'(\w*)(\w)\2(\w*)').sub(r'\1\2\3', word)
    if new_word == word:
        return new_word
    return normalize_word(new_word)


if __name__ == '__main__':
    samples = open('Q3-input.txt').read().split('\n')
    for sample in samples:
        correct_form = normalize_word(str(sample))
        print(f"{sample} ------> {correct_form}")
