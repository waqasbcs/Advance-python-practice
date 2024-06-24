import PyPDF2

def pdfEncrypt(pdfFile):
    file = open(pdfFile, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()

    for pageNum in range(reader.numPages):
        writer.addPage(reader.getPage(pageNum))
    
    # Add a password
    writer.encrypt('yourPassword')

    encryptedPdf = open('securedMyPdf.pdf', 'wb')
    writer.write(encryptedPdf)
    encryptedPdf.close()
    print('File was encrypted successfully')

pdfEncrypt('myPdf.pdf')
