import sys
import splitter

filename = sys.argv[1]
# filename = raw_input("File Name: ")
layout = splitter.get_PDF_layout(filename)
outfile = open('out.txt', 'w')
splitter.print_layout(outfile, layout, 0)
# splitter.print_layout_tree(outfile, layout, 0)
splitter.print_layout_bytestream(sys.stdout, layout[2], 0)