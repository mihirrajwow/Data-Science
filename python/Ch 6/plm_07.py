post=input("Enter a post:\n")
# post="Mihir is an excellent coder"
c=False
if "Mihir" in post:
    c=True
elif "mihir" in post:
    c=True
else:
    c=False
print(c)