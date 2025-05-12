# Creating an empty set
b=set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(3)
b.add(3) # Adding a value repeatedly does not changes a set
b.add((6,7,8))

## Accessing Elements
# b.add({4:5}) # Cannot add lists or dictionary to sets
print(b)

## Length of the set 
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(3) # Removes 3 from the set b
# b.remove(13) # Throws a error while trying to remove 13 (which was not in the set b)
print(b)

print(b.pop())
print(b)