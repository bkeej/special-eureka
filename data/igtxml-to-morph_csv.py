import os
import csv 
import xml.etree.ElementTree as ET 

#
# Files and Directories
#

corpus_dir = 'uspanteko_corpus_xml/'

xml_files = os.listdir(corpus_dir)


#
# Parsers
#

# def match_morphs(word,morph):
# 	if word.get('wd_id') in morph.get('morph_id'):
# 		return(morph.get('text'))


# def parse_word(word,root):
# 	for phrase in root.findall('./body/morphemes/phrase'):
# 		if phrase.get('phrase_ref') in word.get('wd_id'):
# 			print(phrase.get('phrase_ref'), word.get('wd_id'))
# 			# morphs = phrase.findall('morph')
# 			# print(morphs)
# 			break
# 	# return list(map(lambda x: match_morphs(word, x), morphs))

def get_words(xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()

	word_list = []

	for phrase in root.findall('./body/phrases/phrase'):
		word_list = word_list + phrase.findall('word')
	
	return word_list


#
# Main
#

def main():
	
	xmlfile = '1.xml'
	for w in get_words(xmlfile):
		print(w.get('text'))

if __name__ == '__main__':
	main() 