# Changed 'cStringIO' to 'io' - change was initiated in Py3
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import time 

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    # Changed from 'file' to 'open' - change was initiated in Py3
    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

def convertMultiple(pdfDir, txtDir):
    #if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    counter = 0
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        startTime = time.time()
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text.encode('utf8').decode('ascii', 'ignore')) #write text to text file
            counter += 1 
        print(counter, pdf, (time.time() - startTime))

pdfDir = "/Users/collinlyou/Desktop/Supreme_Court_Cases/2000/"
txtDir = "/Users/collinlyou/Desktop/Supreme_Court_Cases/2000/2000_txt/"
convertMultiple(pdfDir, txtDir)

