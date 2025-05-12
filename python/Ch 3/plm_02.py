letter='''Dear <|NAME|>,
Greetings from MKG coding house. We are happy to tell you about your selection.
Your are selected!
Have a great day!
Thanks and regards,
Ajeeb
Date: <|DATE|>
'''
name=input("Enter your Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)