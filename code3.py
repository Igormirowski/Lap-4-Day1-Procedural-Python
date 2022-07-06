fridge = ["hummus", "celery", "cucumner", "cucumber"]

def first_letter(item):
    return item[0]

# Normal way print first letter of each in fridge
for elt in fridge:
    print(first_letter(elt))


# Map way

initials = map(first_letter, fridge)
print(initials)

# for elt in initials:
#     print(elt)

# return in a list  LIST COMPREHENTION
initials3 = [item[0] for item in fridge]
print("initials3", initials3)

# lambda 
initials4 = [lambda item:item[0], fridge]
print("4", initials4)

# map with lambda
initials5 = map(lambda item:item[0], fridge)

print(initials5)
