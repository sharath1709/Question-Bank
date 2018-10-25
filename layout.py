import types

from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal

def extract_text_from_pdf(pdf_path):
	document = open(pdf_path, 'rb')
	rsrcmgr = PDFResourceManager()
	laparams = LAParams()
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	text = ''
	file = open("trace.txt", "w")
	for page in PDFPage.get_pages(document):
		interpreter.process_page(page)
		layout = device.get_result()
		printTree(file, layout, 0)
		# print(layout)
		# type(layout)
		for element in layout:
			# print(type(element))
			# print(isinstance(element, basestring))
			# print(element)
			# print(element.get_text())
			# text = text + element.get_text()
			if isinstance(element, LTTextBoxHorizontal):
				# print(element.get_text())
				text = text + element.get_text()

	if text:
		return text

def printTree(file, tree, numTabs):
	for x in range(0, numTabs):
		file.write('\t')
	# file.write(str(type(tree)) + str(tree) + "\n")
	# file.write(str(type(tree)))
	file.write(str(tree))
	file.write('\n')
	# if isinstance(tree, basestring) or not hasattr(tree, '__iter__'):
	# 	# for x in range(0, numTabs):
	# 	# 	file.write('\t')
	# 	if tree.get_text() == u'\u2022':
	# 		# file.write(tree.get_text() + "\n")
	# 		file.write(str(tree))
	# 	# file.write("{[" + str(tree) + "]}\n")
	# 	file.write('\n')
	# if isinstance(tree, LTTextLineHorizontal):
	# 	for x in range(0, numTabs):
	# 		file.write('\t')
	# 	file.write(tree.get_text().encode('utf8') + '\n')
	# el
	if not hasattr(tree, '__iter__'):
		return
	else:
		# file.write('\n')
		for node in tree:
			printTree(file, node, numTabs + 1)

if __name__ == '__main__':
	print(extract_text_from_pdf('/home/nagendra/CS490-RnD/samples/final-solutions.pdf'))