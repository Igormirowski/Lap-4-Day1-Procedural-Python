# Filter Print all starting with C
fridge = ["hummus", "celery", "cucumner", "cucumber"]


def begins_with_c(item):
    return item[0] == 'c'


aisle_c = filter(begins_with_c, fridge)

print(aisle_c)

for item in aisle_c:
    print(item)
