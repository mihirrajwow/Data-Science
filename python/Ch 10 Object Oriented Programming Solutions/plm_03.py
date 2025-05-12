class sample:
    a = "Mihir"

obj = sample()
obj.a = "Vikky" # Changes the instance attribute
print(sample.a)
print(obj.a)

# sample.a = "Vikky"
# print(sample.a) ## Changes the class attribute