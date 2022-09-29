from nltk.tokenize import TreebankWordTokenizer, RegexpTokenizer
from nltk.tokenize import WhitespaceTokenizer, WordPunctTokenizer
from collections import Counter


class Tokenize:
    def __init__(self, path):
        self.text = open(path, mode='r', encoding='utf-8').read()

    def treebank_word_tokenizer(self):
        return TreebankWordTokenizer().tokenize(self.text)

    def regexp_tokenizer(self, pattern, gaps=True):
        return RegexpTokenizer(pattern, gaps=gaps).tokenize(self.text)

    def whitespace_tokenizer(self):
        return WhitespaceTokenizer().tokenize(self.text)

    def word_punct_tokenizer(self):
        return WordPunctTokenizer().tokenize(self.text)


def get_types_count(tokens):
    tokens_dict = Counter(tokens)
    return len(tokens_dict.items())


if __name__ == '__main__':
    tokenize = {
        'AlbertEinstein.txt': None,
        'Shahnameh.txt': None,
        'ShortSampleEnglish.txt': None,
        'ShortSamplePersian.txt': None,
    }

    # Init Tokenize classes
    for path in tokenize.keys():
        tokenize[path] = Tokenize(path)

    # Part C
    print("-----TreebankWordTokenizer-----")
    paths = tokenize.keys()
    for path in paths:
        tokens = tokenize[path].treebank_word_tokenizer()
        print(path)
        print(f"Tokens count: {len(tokens)}")
        print(f"Types count: {get_types_count(tokens)}")
        print()

    # Part D
    print("-----RegexpTokenizer-----")

    path = 'ShortSampleEnglish.txt'
    tokens = tokenize[path].regexp_tokenizer(pattern='\s+|\.')
    print(f"{path} tokens:")
    print(tokens)

    path = 'ShortSamplePersian.txt'
    tokens = tokenize[path].regexp_tokenizer(pattern='\s+|\.')
    print(f"\n{path} tokens:")
    print(tokens)

    path = 'AlbertEinstein.txt'
    tokens = tokenize[path].regexp_tokenizer(pattern='[0-9]', gaps=False)
    print(f"\n{path} tokens:")
    print(tokens)

    # Part E
    print("\n-----WhitespaceTokenizer-----")
    path = 'ShortSampleEnglish.txt'
    tokens = tokenize[path].whitespace_tokenizer()
    print(f"{path} tokens:")
    print(tokens)

    # Part F
    print("\n-----WordPunctTokenizer-----")
    path = 'ShortSampleEnglish.txt'
    tokens = tokenize[path].word_punct_tokenizer()
    print(f"{path} tokens:")
    print(tokens)
