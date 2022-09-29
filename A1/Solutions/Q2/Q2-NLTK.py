import nltk
nltk.download('punkt')


def list_printer(my_list):
    print(f"Number of elements inside list: {len(my_list)}")
    for element in my_list:
        print(element)


if __name__ == '__main__':
    text = open('Q2-input.txt').read()
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    print("-----Words in text-----")
    list_printer(words)

    print("\n-----Sentences in text-----")
    list_printer(sentences)
