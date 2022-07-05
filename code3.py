fridge = ["hummus", "celery", "cucumner", "cucumber"]

def first_letter(item):
    return item[0]

# Normal way print first letter of each in fridge
for elt in fridge:
    print(first_letter(elt))


# Map way

initials = map(first_letter, fridge)
print(initials)

for elt in initials:
    print(elt)

# return in a list 
initials3 = [item[0] for item in fridge]
print("initials3", initials3)
