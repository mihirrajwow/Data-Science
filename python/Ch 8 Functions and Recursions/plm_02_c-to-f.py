def convert(celcius):
    fahrenhite = (celcius * 9/5) + 32
    return fahrenhite

cel=int(input("Enter temperature in celcius: "))
far=convert(cel)
print(f"Temperature in Fahrenhite is {far}")