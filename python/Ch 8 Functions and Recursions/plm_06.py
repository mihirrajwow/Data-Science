def convert(inch):
    return inch * 2.54

i=int(input("Enter length in inches: "))
print(f"{i} inches = {convert(i)} centimetres.")