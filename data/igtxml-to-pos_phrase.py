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


def get_morphs(xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()

	morph_list = []

	for phrase in root.findall('./body/morphemes/phrase'):
		morph_list.append(phrase.findall('morph'))

	morph_list = [x for x in morph_list if x != []]

	return morph_list

def get_pos(morphlist,xmlfile):
	tree = ET.parse(corpus_dir + xmlfile)
	root = tree.getroot()
	
	pos_list = []

	for morph in morphlist:

		try:
			pos = root.find("./body/postags/phrase/pos[@morph_ref='" + morph.get('morph_id') + "']").get('text')
		except AttributeError:
			pos = 'err'

		m = ''.join(list(filter(lambda ch: ch not in " +.!¡¿?-,", morph.get('text'))))
		p = pos.upper()

		pos_list.append(m + ' ' + p)

	return pos_list



def main():

	# for xmlfile in ['1.xml']:

	# 	mor = get_morphs(xmlfile)
	# 	for i in mor:
	# 		pos = get_pos(i, xmlfile)
	# 		print(pos)

	with open("pos_list.csv", "w") as csvfile:
		writer = csv.writer(csvfile)

		n = 1
	
		for xmlfile in xml_files:

			print("processing " + str(n) + " of 21: " + xmlfile)

			n = n + 1

			for m in get_morphs(xmlfile):
				poses = get_pos(m,xmlfile)
				writer.writerow(poses)
		
if __name__ == '__main__':
	main()
