import csv
from random import shuffle
from collections import defaultdict
from averged_perceptron import AveragedPerceptron
from perceptron_tagger import PerceptronTagger


data_file = '../data/clean/pos_phrase-cleaned-status-rev.csv'

model_file = 'usp_pos_model'


def test_sentence(sent):
    f = open('log.txt', 'a')
    f.write(str(sent) + '\n\n')

    START = ['-START-', '-START2-']
    END = ['-END-', '-END2-']
    prev, prev2 = START

    words = sent[0]
    tags = sent[1]
    context = START + words + END

    hit = 0

    miss = 0

    for i, word in enumerate(words):
        feat = trainer._get_features(i, word, context, prev, prev2)
        y = tags[i]

        if word == 'x':
            y_hat = 'COM'

        elif word == 't':
            y_hat = 'INC'

        elif word == 'r':
            y_hat = 'E3'

        elif word == 'j':
            y_hat = 'E3'

        elif word == 'taq':
            y_hat = 'PL'

        else:
            # y_hat = "ERR"
            y_hat = tester.predict(feat)

        # y_hat = tester.predict(feat)

        f.write('morph:' + word + '\n')
        f.write('actual:' + y + '\n')
        f.write('predicted:' + y_hat + '\n\n')

        if y == y_hat:
            hit = hit + 1
        else:
            miss = miss + 1

    f.close()

    return [hit,miss]




sentences = []

with open(data_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        words = []
        tags = []
        for cell in line:
            cells = cell.split()
            words.append(cells[0])
            tags.append(cells[1])
        sentences.append((words,tags))

total_n = len(sentences)

test_n = (round(len(sentences) * .30))

train_n = total_n - test_n

shuffle(sentences)

print('Number of sentences in corpus:', total_n, '\n')

train = sentences[:train_n]

print('Sampling', len(train), 'training sentences.\n')

test = sentences[train_n:]

print('Sampling', len(test), 'testing sentences.\n')

print('Training averaged perceptron part of speech tagger.\n')

trainer = PerceptronTagger()
trainer.train(train, save_loc = model_file)

print('Model pickled and saved to', model_file, '\n')

tester = AveragedPerceptron()
tester.load(model_file)

print('Testing', model_file, 'on', len(test), 'test sentences.\n')

print('Number of classes:', len(tester.classes), '\n')

print('Classes:', tester.classes, '\n')

hit = 0
miss = 0
f = open('log.txt','w')
f.close()

for sentence in test:
    result = test_sentence(sentence)
    hit = hit + result[0]
    miss = miss + result[1]

print('Accuracy:', hit / (hit + miss))
