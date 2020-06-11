import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pos_colnames = ['Morph', 'POS']
seg_colnames = ['Word', 'Morphs']

pos_df = pd.read_csv('pos.csv', names=pos_colnames, header=None)

print('pos.csv start shape:', pos_df.shape, '\n')

pos_df = pos_df[pos_df.POS != '???']
pos_df = pos_df[pos_df.POS != '***']
pos_df = pos_df[pos_df.Morph != '***']
pos_df = pos_df[pos_df.POS != 'ERROR']
pos_df = pos_df[pos_df.POS != 'err']

pos_df['POS'].replace('', np.nan, inplace=True)
pos_df['Morph'].replace('', np.nan, inplace=True)
pos_df.dropna(inplace=True)


pos_df = pos_df[pos_df.POS != 'PRONÃ§']
pos_df = pos_df[pos_df.POS != 'E3S?PERS']
pos_df = pos_df[pos_df.POS != "B'IK"]

print('Checking unique POS tags:\n', pos_df.POS.unique(), '\n')

print('pos.csv end shape:', pos_df.shape, '\n')

seg_df = pd.read_csv('segmented.csv', names=seg_colnames, header=None)

print('segmented.csv start shape:', seg_df.shape, '\n')

seg_df['Word'].replace('', np.nan, inplace=True)
seg_df['Morphs'].replace('', np.nan, inplace=True)
seg_df.dropna(inplace=True)



seg_df = seg_df[~seg_df.Word.str.contains("\*")]
seg_df = seg_df[~seg_df.Word.str.contains("\(")]
seg_df = seg_df[~seg_df.Word.str.contains("\[")]
seg_df = seg_df[~seg_df.Word.str.contains("\/")]

seg_df = seg_df[~seg_df.Morphs.str.contains("\*")]
seg_df = seg_df[~seg_df.Morphs.str.contains("\(")]
seg_df = seg_df[~seg_df.Morphs.str.contains("\[")]
seg_df = seg_df[~seg_df.Word.str.contains("\/")]

print('segmented.csv end shape:', seg_df.shape, '\n')

pos_df.to_csv('pos.csv')
seg_df.to_csv('segmented.csv')