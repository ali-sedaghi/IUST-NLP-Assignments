import csv
import re
import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from wordcloud import WordCloud


nltk.download('stopwords')


def remove_whitespaces(string):
    string = string.replace('\n', ' ').replace('\t', ' ')
    string = re.sub(' +', ' ', string)
    return string


stop_words = set(stopwords.words('english'))
def remove_stopwords(string_tokens):
    new_string = ''
    for token in string_tokens:
        if not (token in stop_words):
            new_string += token + ' '
    return new_string[:-1]


def remove_short_words(string_tokens):
    new_string = ''
    for token in string_tokens:
        if len(token) >= 3:
            new_string += token + ' '
    return new_string[:-1]


porter_stemmer = PorterStemmer()
def stemmer(string_tokens):
    new_string = ''
    for token in string_tokens:
        new_string += porter_stemmer.stem(token) + ' '
    return new_string[:-1]


tokenizer = TreebankWordTokenizer()
def my_tokenize(string):
    return tokenizer.tokenize(string)


def generate_word_cloud(all_words):
    word_cloud = WordCloud(
        width=720, height=720,
        background_color='white',
        stopwords=stop_words,
        min_font_size=10
    ).generate(all_words)

    plt.figure(figsize=(16, 16), facecolor=None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('word_cloud.png')


def generate_trends_chart(trends, counts=10):
    my_dict = Counter(trends)
    my_list = [(k, v) for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)]
    my_list = my_list[:counts]
    x, y = zip(*my_list)

    plt.figure(figsize=(20, 8), facecolor=None)
    plt.bar(x, y)
    plt.xlabel('trend')
    plt.ylabel('counts')
    plt.tight_layout(pad=0)
    plt.savefig('trends_chart.png')


def preprocess(t):
    # Step 1
    t = remove_whitespaces(t)
    # Step 2
    t = t.lower()
    # Step 3
    t = re.sub('@[^ ]*', '', t)
    # Step 4
    t = re.sub('[^a-z\s]+', '', t)
    # Step 5
    tokens = my_tokenize(t)
    # Step 6
    t = remove_stopwords(tokens)
    # Step 7
    tokens = my_tokenize(t)
    t = remove_short_words(tokens)
    # Step 8
    tokens = my_tokenize(t)
    t = stemmer(my_tokenize(t))
    return t


def step_test(indexes):
    file = open('tweets.csv', encoding='utf-8')
    csv_reader = csv.reader(file)
    tweets = [row[0] for row in csv_reader]
    tweets = [tweets[i] for i in indexes]
    file.close()

    for tweet in tweets:
        t = tweet
        # Step 1
        t = remove_whitespaces(t)
        # Step 2
        t = t.lower()
        # Step 3
        t = re.sub('@[^ ]*', '', t)
        # Step 4
        t = re.sub('[^a-z\s]+', '', t)
        # Step 5
        tokens = my_tokenize(t)
        # Step 6
        t = remove_stopwords(tokens)

        # Step 7
        tokens = my_tokenize(t)
        t = remove_short_words(tokens)
        print(f"------\n{t}\n------")

        # Step 8
        tokens = my_tokenize(t)
        t = stemmer(my_tokenize(t))
        print(f"------\n{t}\n------")


# if __name__ == '__main__':
#     indexes = [4, 11, 12]
#     step_test(indexes)


if __name__ == '__main__':
    file = open('tweets.csv', encoding='utf-8')
    csv_reader = csv.reader(file)
    tweets = [row[0] for row in csv_reader]
    file.close()

    new_tweets_str = ''
    new_tweets = []
    all_trends = []
    for tweet in tweets:
        t = tweet
        t = preprocess(t)

        new_tweets_str += t + ' '
        new_tweets.append([tweet, t])
        all_trends += re.findall('#[^\s]*', tweet)
    print("Preprocessing finished.")

    with open('tweets_new.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_tweets)
    print("New CSV file generated.")

    generate_word_cloud(new_tweets_str[:-1])
    print("Word cloud generated.")

    generate_trends_chart(all_trends)
    print("Trends chart generated.")
