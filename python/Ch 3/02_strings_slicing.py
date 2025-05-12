greeting="Good Morning, "
name="Mihir"
# print(type(name))

# Concatenating two Strings
c=greeting+name
print(c)

# Indexing
print(name[4])
# name[3] = "d" --> DOES NOT WORK

# String_Slicing
print(name[0:3])
print(name[0:4])
print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:4]

# Negative_Indices
d=name[-4:-1] # is same as name[1:4]
print(d)

# Slicing_With_Skip_Value
n="RikshiGamingRKG"
e=n[0::2]
f=n[0::3]
g=n[0::4]
print(e,f,g)