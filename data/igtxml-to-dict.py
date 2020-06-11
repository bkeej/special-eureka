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

# Can't use this because the gls section of this corpus is fucked.
# def get_morph_gloss(xmlfile):
# 	tree = ET.parse(corpus_dir + xmlfile)
# 	root = tree.getroot()

# 	morph_gloss = []

# 	for phrase in root.findall('./body/morphemes/phrase'):
# 		try:
# 			morph_list = phrase.findall('morph')
# 			gloss_list = root.find("./body/gloss/phrase[@phrase_ref='" + phrase.get('phrase_ref') + "']").findall('gls')

# 			morph_gloss = morph_gloss + list(zip(morph_list,gloss_list))
# 		except AttributeError:
# 			continue

# 	return morph_gloss

def get_morphs(xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()

	morph_list = []

	for phrase in root.findall('./body/morphemes/phrase'):
		morph_list = morph_list + phrase.findall('morph')

	return morph_list

def get_pos(word,xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()
	
	try:
		pos = root.find("./body/postags/phrase/pos[@morph_ref='" + word.get('morph_id') + "']").get('text')
	except AttributeError:
		return ['err','err']

	return [word.get('text'), pos]



def main():

	with open("pos.csv", "w") as csvfile:
		writer = csv.writer(csvfile)

		n = 1
	
		for xmlfile in xml_files:

			print("processing " + str(n) + " of 21: " + xmlfile)

			n = n + 1

			for m in get_morphs(xmlfile):
				mp = get_pos(m,xmlfile)
				mp[0] = ''.join(list(filter(lambda ch: ch not in " +.!¡¿?-,", mp[0])))
				mp[1] = mp[1].upper()
				writer.writerow(mp)
		
if __name__ == '__main__':
	main() 
