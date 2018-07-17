import re

fileinput = open('Tax Invoice Multiple Extract.txt', 'r')
fileoutput = open('Tax Invoice Consolidated Report.txt', 'w')

totalInvoice = 0

for line in fileinput:
	xval = re.findall('^Attention: (\S+\s\S+)',line)
	if xval:
		xvalSTR = ''.join(xval)
		print(xvalSTR)

	xval = re.findall('^Invoice Date: (\S+\S+)',line)
	if xval:
		xvalSTR = ''.join(xval)
		print(xvalSTR)
		
	xval = re.findall('^Invoice Number: (\S+\S+)',line)
	if xval:
		xvalSTR = ''.join(xval)
		print(xvalSTR)
		
	xval = re.findall('^Total AUD: (\S+\S+)',line)
	if xval:
		xvalSTR = ''.join(xval)
		print(xvalSTR)
		print('-------------------')
		totalInvoice = totalInvoice + float(xvalSTR)

print('Total Invoice Amount : ${:0,.2f}'.format(totalInvoice))
fileinput.close()
fileoutput.close()