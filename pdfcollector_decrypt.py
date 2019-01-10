#! python3
# chapter13 practice

import os, re, PyPDF2


def pdfcheck(filename):
    print(filename)
    return

path = '.'
Pdfext = '.pdf'

# os.walk() to get pdf file in folders under path
pdffiles = []
for currrentDir, dirs, files in os.walk(path):
    #print('current path is ' + os.path.abspath(currrentDir))
    #for dir in dirs:
    #    print('ディレクトリ' + dir)
    for file in files:
        if file.endswith('.pdf'):
            #print('ファイル ' + file)
            pdffiles.append(os.path.abspath(file))
            
for pdf in pdffiles:
    pdfcheck(pdf)


# isencrypt = false then ...
# password = input(), then decript w password

# write with new name original filename and "decrypt".pdf
