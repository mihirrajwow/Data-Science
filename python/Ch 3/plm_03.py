st="This is a string with double  spaces"

# Finding double spaces
doubleSpaces=st.find("  ")
print(doubleSpaces)

# Replacing double spaces with single spaces
st=st.replace("  "," ")
print(st)