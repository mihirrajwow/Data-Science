# Use open function to read the content of a file
# file = open('fileName.ext','mode')
# f = open('sample.txt','r')
f = open('F:\python\Ch 9 file io\sample.txt') # by default the mode is 'r'
# data = f.read()
data = f.read(5) # reads first 5 characters from the file
print(data)
f.close()