import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer


nltk.download('wordnet')
nltk.download('omw-1.4')


if __name__ == '__main__':
    # Part B
    print("-----Stemming-----")
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    text = open('../Q4/AlbertEinstein.txt', mode='r', encoding='utf-8').read()
    tokens = TreebankWordTokenizer().tokenize(text)
    for i in [2, 10, 18, 19, 21, 22, 42]:
        w = tokens[i]
        print(f"Index {i}: {w}")
        print(f"Porter stem: {porter.stem(w)}")
        print(f"Lancaster stem: {lancaster.stem(w)}")
        print()

    # Part C
    print("-----Lemmatization-----")
    lemmatizer = WordNetLemmatizer()
    words = ["Waves", "fishing", "rocks", "was", "corpora", "better", "ate", "broken"]
    for w in words:
        print(f"{w} ---> {lemmatizer.lemmatize(w)}")
