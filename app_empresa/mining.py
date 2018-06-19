import PyPDF2
from PyPDF2 import PdfFileReader
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
pdf = open("DOEAL-EXEC.pdf", 'rb')
readerObj = PdfFileReader(pdf)
print "PDF Reader Object is:", readerObj
print "Details of open open-revolution book"
print "Number of pages:", readerObj.getNumPages()
print "Title:", readerObj.getDocumentInfo().title
print "Author:", readerObj.getDocumentInfo().author

# for i in range(0, readerObj.getNumPages()):
page = readerObj.getPage(20)
content = page.extractText()
listas = content
t = word_tokenize(content)
print t
# for i in range(len(t)):
#     if t[i].encode('cp1252').count("CONTRA") > 0:
#         print t[i]

