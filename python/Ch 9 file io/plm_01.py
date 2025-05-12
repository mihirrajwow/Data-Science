# with open('poems.txt') as p:
#     t = p.read()

# if 'twinkle' in t:
#     print("Yes, twinkle is present.")
# else:
#     print("No, twinkle is not present")

f = open('poems.txt')
t = f.read()

if 'twinkle' in t:
    print("Yes, twinkle is present.")
else:
    print("No, twinkle is not present.")
f.close()