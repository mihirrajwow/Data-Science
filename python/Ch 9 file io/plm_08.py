with open('this.txt') as f:
    content = f.read()
with open('this_copy.txt','w') as c:
    c.write(content)
