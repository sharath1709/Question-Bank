# Question-Bank
A python2 based tool to extract questions from question paper pdf file.
The tool creates a basic splitting of question paper and makes an annotation box around the question for a given pdf file.
This annotated pdf then can be manually adjusted using foxit reader for any corrections to be made.
It extracts the questions and corresponding images(if any) and stores them as a latex string, for any annotated pdf.

Usage:
To create an annotated pdf from the question paper. This creates an annotated pdf in the same directory.
  python2 splitter.py <pdf-file> 0
To extract the text and images from the annotated pdf.
  python2 splitter.py <annotated-pdf-file> 1
This creates a text file containing the latex format of the extracted questions.
It also creates a folder with all the referenced images.
