with open('log.txt') as l:
    content = l.read()#.lower()

if "python" in content.lower():
    print("Yes, python is present.")
else:
    print("No, python is not present.")