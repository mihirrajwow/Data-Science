
f = open('F:\python\Ch 9 file io\sample.txt')

# Reads first line
data = f.readline() 
print(data)

# Reads second line
data = f.readline() 
print(data)

# Reads third line
data = f.readline() 
print(data)

# Reads fourth line... and so on...
data = f.readline() 
print(data)
f.close()