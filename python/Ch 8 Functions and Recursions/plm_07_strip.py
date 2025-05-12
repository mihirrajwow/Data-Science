def remove_and_strip(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this="    Mihir is a good       "
n = remove_and_strip(this,"Mihir")
print(n)
# print(this)
# print(this.strip())