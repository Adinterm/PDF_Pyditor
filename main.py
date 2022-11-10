from PyPDF2 import PdfWriter, PdfReader
pages_to_delete = [3] # page numbering starts from 0
infile = PdfReader(str(input('filename 1 : ')), 'rb')
infile2 = PdfReader(str(input('filename 2 : ')))
output = PdfWriter()

for i in range(len(infile.pages) ):
    if i not in pages_to_delete:
        p = infile._get_page(i)
        output.add_page(p)
output.add_page(infile2._get_page(0))

with open(str(input('output filename : ')), 'wb') as f:
    output.write(f)
