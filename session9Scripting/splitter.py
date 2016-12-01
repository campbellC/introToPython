from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
for doc1 in sys.argv[1:]:
    doc1 = str(doc1)
    input1 = PdfFileReader(open(doc1,"rb"))

    output1 = PdfFileWriter()
    output2 = PdfFileWriter()

    size = input1.getNumPages()

    for i in xrange(size):
        if i % 2 == 0:
            output1.addPage(input1.getPage(i))
        else:
            output2.addPage(input1.getPage(i))

    evenOutputStream = file(doc1[:-4] + "Even.pdf","wb")
    oddOutputStream = file(doc1[:-4] + "Odd.pdf","wb")
    output1.write(evenOutputStream)
    output2.write(oddOutputStream)

