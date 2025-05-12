myDict={
    "key" : "value",
    "Furious" : "In a very quick manner (faster than fast)",
    "Mihir" : "A genius",
    "Marks" : [1,2,5],
    "anotherDict" : {'mihir': 'Player'}
}
print(myDict['Furious'])
print(myDict['Mihir'])
print(myDict['Marks'])

myDict['Marks']=[99,99,99,99] # Dictionary is mutable
print(myDict['Marks'])

print(myDict['anotherDict']['mihir'])