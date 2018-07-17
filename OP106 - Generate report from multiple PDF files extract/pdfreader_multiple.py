import PyPDF2
import glob

fileoutput = open('Tax Invoice Multiple Extract.txt', 'w')

for filename in glob.glob('*.pdf'):
	pdf_file = open(filename, 'rb')

	pdfReader = PyPDF2.PdfFileReader(pdf_file)
	pageObj = pdfReader.getPage(0)
	textoutput = pageObj.extractText()

	fileoutput.write(textoutput)

fileoutput.close()
print('Done')
