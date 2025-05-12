# # comment="I make a lot of money online. You can click this link to buy now and subscribe this prmeium feature."
# comment=input("Enter the comment:\n")
# # keywords={"make a lot of money","buy now","subscribe this","click this"}
# c1=comment.find("make a lot of money")
# c2=comment.find("buy now")
# c3=comment.find("subscribe this")
# c4=comment.find("click this")
# if(c1>0 or c2>0 or c3>0 or c4>0):
#     print("It's a SPAM!")
# else:
#     print("It's NOT a spam!")
# # print(c1,c2,c3,c4)

text=input("Enter the text:\n")
spam=False

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscrine this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")