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

def get_words(xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()

	word_list = []

	for phrase in root.findall('./body/phrases/phrase'):
		word_list = word_list + phrase.findall('word')
	
	return word_list

def get_morphs(word,xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()
	word_morphs = [word.get('text')]
	for phrase in root.findall('./body/morphemes/phrase'):
		if phrase.get('phrase_ref') + "_" in word.get('wd_id'):
			morphs = phrase.findall('morph')
			for m in morphs:
				if word.get('wd_id') + "_" in m.get('morph_id'):
					word_morphs.append(m.get('text'))
			break
	return word(word_morphs)

#
# Main
#

def main():
	
	xmlfile = '1.xml'
	for w in get_words(xmlfile):
		get_morphs(w,xmlfile)

if __name__ == '__main__':
	main() 