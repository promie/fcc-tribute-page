import PyPDF2

pdf_file = open('Tax Invoice 1.pdf', 'rb')
fileoutput = open('Tax Invoice Single Extract.txt', 'w')

pdfReader = PyPDF2.PdfFileReader(pdf_file)
pageObj = pdfReader.getPage(0)
textoutput = pageObj.extractText()

fileoutput.write(textoutput)
fileoutput.close()

print('Done')