#! python3
# chapter13 practice

import os, re, PyPDF2


def pdfcheck(filename,filepass):
    print(filename)
    pdffile = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdffile)
    if pdfReader.isEncrypted:
        pdffile.close()
        
    else:
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfWriter.encrypt(filepass)
        pathfile = os.path.split(filename)
        #os.chdir(pathfile[0])
        #正規表現でファイル名加工
        newpdffile = open(os.path.join(pathfile[0],'encrypted_' + pathfile[1]),'wb')
        pdfWriter.write(newpdffile)
        pdffile.close()
        newpdffile.close()
    return

path = '.'
Pdfext = '.pdf'

pdfpassword = input('pdfpassword to set:')

# os.walk() to get pdf file in folders under path
pdffiles = []
for currrentDir, dirs, files in os.walk(path):
    #print('current path is ' + os.path.abspath(currrentDir))
    #for dir in dirs:
    #    print('ディレクトリ' + dir)
    for file in files:
        if file.endswith('.pdf'):
            fullpathfilename = os.path.join(currrentDir,file)
            pdffiles.append(fullpathfilename)

for targetfile in pdffiles:
    pdfcheck(targetfile,pdfpassword)

