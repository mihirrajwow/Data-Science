myDict={
    "key" : "value",
    "Furious" : "In a very quick manner (faster than fast)",
    "Mihir" : "A genius",
    "Marks" : [1,2,5],
    "anotherDict" : {'mihir': 'Player'},
    1: 2
}

# DICTIONARY METHODS

print(myDict.keys()) # Prints the keys of the dictionary
print(myDict.values()) # Prints the values of the dictionary
print(type(myDict.keys()))
print(list(myDict.keys())) # Typecasting <class 'dict_keys'> to <class 'list'>
print(myDict.items()) # Prints the (key,value) for all contents of the dictionary
print(myDict)
updateDict={
    "Lovish":"Friend",
    "Nayka":"Friend",
    "Devishi":"Friend",
    "Shruti":"Friend",
    "Mihir":"Player"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get('Mihir')) # Prints value associated with key "Mihir"
print(myDict['Mihir']) # Prints value associated with key "Mihir"

# The difference between .get and [] syntax in Dictionaries?
print(myDict.get('Mihir4')) # Returns None as Mihir4 is not present in the dictionary
# print(myDict['Mihir4']) # Throws an Error as Mihir4 is not present in the dictionary