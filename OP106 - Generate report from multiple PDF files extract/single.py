import PyPDF2

pdf_file = open('Tax Invoice 1.pdf', 'rb')
fileOutput = open('Tax Invoice Single Extract.txt', 'w')

pdfReader = PyPDF2.PdfFileReader(pdf_file)
pageObj = pdfReader.getPage(0)
textOutput = pageObj.extractText()

fileOutput.write(textOutput)
fileOutput.close()

print('The file write from PDF to a text file is complete!')