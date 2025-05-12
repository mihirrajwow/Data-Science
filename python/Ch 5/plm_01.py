userDict={
    "pankha":"Fan",
    "dabba":"Container",
    "pratha":"Tradition",
}
print("Options are: ",list(userDict.keys()))
a=input("Enter the Hindi Word\n")

# print("The meaning of your word is: ",userDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is: ",userDict.get(a))