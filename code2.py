# create array with square values 

li = [1, 2, 3, 4, 5]

new_li = []
for i in li:
    new_li.append(i**2)

# list comprehention

print(new_li)

new_li2 = [i**2 for i in li] # this line in equivalent to lines 6 and 7 !!!!!
print(new_li2)



# Add to list multiple values  
li.extend([6,7,8])
print(li)




