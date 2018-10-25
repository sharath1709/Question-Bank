from splitter import get_PDF_layout, get_text_from_box, get_pages_pdf2image, page_to_image, get_image_from_page
import poppler
import sys, urllib, os


if len(sys.argv) > 1:
	pdf_path = sys.argv[1]
layout = get_PDF_layout(pdf_path)
pages_pdf2image = get_pages_pdf2image(pdf_path)
document = poppler.document_new_from_file('file://%s' % \
    urllib.pathname2url(os.path.abspath(pdf_path)), None)
pages = document.get_n_pages()
annots = []
for i in range(pages):
	page = document.get_page(i)
	page_layout = layout[i]
	page_pdf2image = pages_pdf2image[i]
	page_to_image(page_pdf2image, 'images/'+str(i)+'.jpg')
	for ann in page.get_annot_mapping():
		# annots = annots + [ann.annot]
		annots = annots + [ann]
		print(get_text_from_box(page_layout, ann.area.x1, ann.area.x2, ann.area.y1, ann.area.y2))
		get_image_from_page(page_pdf2image, ann.area.x1, ann.area.x2, ann.area.y1, ann.area.y2, page_layout.bbox[2], page_layout.bbox[3])
	# anns = page.get_annot_mapping()
	# anns = []
	# ann.area.y1 = 0
	# ann.area.y2 = 10
	# print([method_name for method_name in dir(page) if callable(getattr(page, method_name))])
	# document.get_page(pages - 1).poppler_page_add_annot(ann.annot)
	# annots = annots + page.get_annot_mapping()
# print(annots)
# for ann in annots:
	# print(ann.area)
	# print(ann.area.x1)
	# print(ann.area.x2)
	# print(ann.area.y1)
	# print(ann.area.y2)
	# print(get_text_from_box(layout, ann.area.x1, ann.area.x2, ann.area.y1, ann.area.y2))
	# ann = ann.annot
	# print(ann.get_flags())
	# print(ann.get_color().green)
	# print(ann.get_modified())
	# print(ann.get_annot_type().value_name)
	# print(ann.get_annot_type().__dict__.keys())
	# print(ann.get_contents())
	# print([method_name for method_name in dir(ann) if callable(getattr(ann, method_name))])
# document.save('file://%s' % \
#     urllib.pathname2url(os.path.abspath('test.pdf')))