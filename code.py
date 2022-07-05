
#IF/ELSE syntax 
age = 2 
name = "auguste"

if age >= 18:
    print("You can vote")
elif name == "auguste":
    print("cool cohort")
else:
    print("You are too young")



# more

can_vote = True if age >= 18 else False
print(can_vote)

# while 

i = 0 
while i < 3:
    print(f"Hello has been printed {i + 1} times")
    i += 1

# With input ity always be a string (pyth2 it would be integer)
name = input("what's your name please?")
print(name)





