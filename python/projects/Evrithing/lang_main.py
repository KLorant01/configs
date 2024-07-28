import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow
import random
import json
import pickle
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import edit_distance

stemmer = LancasterStemmer()


def autocorrect_sentence(sentence):
    sentence_tokens = word_tokenize(sentence.lower())
    corrected_tokens = []

    word_list = nltk.corpus.words.words()

    for token in sentence_tokens:
        closest_match = min(word_list, key=lambda x: edit_distance(token, x))
        corrected_tokens.append(closest_match)

    corrected_sentence = " ".join(corrected_tokens)
    return corrected_sentence


file = open("intents.json", "r")
data = json.load(file)
file1 = open("jason_settings.json", "r")
settings = json.load(file1)

retrain = int(settings["retrain"])

try:
    if retrain == 1:
        raise SyntaxError("nothing")
    with open("model_data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    with open("model_data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    if retrain == 1:
        raise SyntaxError("nothing")
    model.load("Lang_Model/model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=7, show_metric=True)
    model.save("Lang_Model/model.tflearn")


def bag_of_words(s, wordss):
    bag = [0 for _ in range(len(wordss))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(wordss):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def chat(text):
    inp = text
    res = model.predict([bag_of_words(inp, words)])[0]
    res_index = np.argmax(res)
    tag = labels[res_index]

    if res[res_index] > 0.7:
        for tg in data["intents"]:
            if tg["tag"] == tag:
                resp = tg["responses"]

        return random.choice(resp), tag, res[res_index]
    else:
        return "I don't understand the question or task, try again.", None, res[res_index]


def chat_by_tag(tag):
    for tg in data["intents"]:
        if tg["tag"] == tag:
            resp1 = tg["responses"]
    try:
        return random.choice(resp1)
    except:
        return None
