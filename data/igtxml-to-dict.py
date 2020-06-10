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

def get_morph_gloss(xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()

	morph_gloss = []

	for phrase in root.findall('./body/morphemes/phrase'):
		try:
			morph_list = phrase.findall('morph')
			gloss_list = root.find("./body/gloss/phrase[@phrase_ref='" + phrase.get('phrase_ref') + "']").findall('gls')

			morph_gloss = morph_gloss + list(zip(morph_list,gloss_list))
		except AttributeError:
			continue

	return morph_gloss


def main():

	# print(len(get_gloss('1.xml')))
	print(get_morph_gloss('3.xml'))

if __name__ == '__main__':
	main() 
