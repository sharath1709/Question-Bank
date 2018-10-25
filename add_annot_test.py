import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

from PyPDF2.generic import (
	DictionaryObject,
	NumberObject,
	FloatObject,
	NameObject,
	TextStringObject,
	ArrayObject
)

# x1, y1 starts in bottom left corner
def createHighlight(x1, y1, x2, y2, meta, color = [1, 1, 0]):
	newHighlight = DictionaryObject()

	newHighlight.update({
		# NameObject("/P"): parent,
		NameObject("/F"): NumberObject(4),
		NameObject("/Type"): NameObject("/Annot"),
		NameObject("/Subtype"): NameObject("/Square"),

		NameObject("/T"): TextStringObject(meta["author"]),
		NameObject("/Contents"): TextStringObject(meta["contents"]),

		NameObject("/C"): ArrayObject([FloatObject(c) for c in color]),
		NameObject("/Rect"): ArrayObject([
			FloatObject(x1),
			FloatObject(y1),
			FloatObject(x2),
			FloatObject(y2)
		]),
		# NameObject("/Subj"): TextStringObject("Rectangle"),
		# NameObject("/RD"): ArrayObject([FloatObject(0), FloatObject(0), FloatObject(0), FloatObject(0)]),
		# NameObject("/QuadPoints"): ArrayObject([
		# 	FloatObject(x1),
		# 	FloatObject(y2),
		# 	FloatObject(x2),
		# 	FloatObject(y2),
		# 	FloatObject(x1),
		# 	FloatObject(y1),
		# 	FloatObject(x2),
		# 	FloatObject(y1)
		# ]),
	})

	return newHighlight

def addHighlightToPage(highlight, page, output):
	highlight_ref = output._addObject(highlight);

	if "/Annots" in page:
		page[NameObject("/Annots")].append(highlight_ref)
	else:
		page[NameObject("/Annots")] = ArrayObject([highlight_ref])

filename = sys.argv[1]
pdfInput = PdfFileReader(open(filename, "rb"))
pdfOutput = PdfFileWriter()

page1 = pdfInput.getPage(0)
# print(page1)
# annots = page1[NameObject("/Annots")]
# print(annots[0].getObject())
# print(annots[1].getObject())

highlight = createHighlight(400, 400, 800, 500, {
	"author": "nagendra",
	"contents": "Bla-bla-bla"
})

print(highlight)

addHighlightToPage(highlight, page1, pdfOutput)

pdfOutput.addPage(page1)

outputStream = open("output.pdf", "wb")
pdfOutput.write(outputStream)