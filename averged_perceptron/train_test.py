import csv
from collections import defaultdict
from averged_perceptron import AveragedPerceptron
from perceptron_tagger import PerceptronTagger


file = "../data/clean/pos_phrase-cleaned.csv"

sentences = []

with open(file, "r") as csv_file:
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

print("Number of sentences in corpus:", total_n, '\n')

print("Sampling", train_n, 'training sentences.\n')

print("Sampling", test_n, 'testing sentences.\n')


# trainer = PerceptronTagger()
# trainer.train(sentences, save_loc = "usp_pos_model")








# import csv
# from collections import defaultdict
# from averged_perceptron import AveragedPerceptron

# file = "../data/clean/pos_phrase-cleaned.csv"

# sentences = []

# with open(file, "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for line in csv_reader:
#         words = []
#         tags = []
#         for cell in line:
#             cells = cell.split()
#             words.append(cells[0])
#             tags.append(cells[1])
#         sentences.append((words,tags))

# def _get_features(i, word, context, prev, prev2):
#     '''Map tokens into a feature representation, implemented as a
#     {hashable: float} dict. If the features change, a new model must be
#     trained.
#     '''
#     def add(name, *args):
#         features[' '.join((name,) + tuple(args))] += 1

#     i += len(START)
#     features = defaultdict(int)
#     # It's useful to have a constant feature, which acts sort of like a prior
#     add('bias')
#     add('i suffix', word[-3:])
#     add('i pref1', word[0])
#     add('i-1 tag', prev)
#     add('i-2 tag', prev2)
#     add('i tag+i-2 tag', prev, prev2)
#     add('i word', context[i])
#     add('i-1 tag+i word', prev, context[i])
#     add('i-1 word', context[i-1])
#     add('i-1 suffix', context[i-1][-3:])
#     add('i-2 word', context[i-2])
#     add('i+1 word', context[i+1])
#     add('i+1 suffix', context[i+1][-3:])
#     add('i+2 word', context[i+2])
#     return features

# START = ['-START-', '-START2-']
# END = ['-END-', '-END2-']

# prev, prev2 = START
# # for words, tags in sentences:
# #     context = START + words + END

# #     for i, word in enumerate(words):
# #         print(_get_features(i, word, context, prev, prev2))
# #         prev2 = prev
# #         prev = tags[i]


# percep = AveragedPerceptron()
# percep.load("usp_pos_model")



# words = sentences[0][0]
# tags = sentences[0][1]
# context = START + words + END

# # print(words)
# # print(tags)

# for i, word in enumerate(words):
#     morphs = []
#     morphs.append((word,_get_features(i, word, context, prev, prev2)))
#     prev2 = prev
#     prev = tags[i]

#     for word, feat in morphs:
#         print("morph:", word)
#         print("prediction:", percep.predict(feat) + '\n')


# # print(type(percep.weights[2]))