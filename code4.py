# Filter Print all starting with C
fridge = ["hummus", "celery", "cucumner", "cucumber"]


def begins_with_c(item):
    return item[0] == 'c'


aisle_c = filter(begins_with_c, fridge)

print(aisle_c)

for item in aisle_c:
    print(item)


## DICTIONARY 

dic1 = {'a': 1,'b': 2, 'c': 3 }

#see keys 
for elt in dic1:
    print(elt)

#see values
for elt in dic1.items():
    print(elt)

for(key, value) in dic1.items():
    print(f' key is {key} ad vaule is {value}')

# Multiply value by 2 (DICTIONARY COMPREHENTION) DOUBLE THE VALUE 

double_dic1 = {k:v*2 for (k, v) in dic1.items()}
print(double_dic1)
