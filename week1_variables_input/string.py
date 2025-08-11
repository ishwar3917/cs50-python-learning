# Ask user for their name 
# name is the variable use to store input
name = input("What is your name : ")

# Say hello to user 
# There are 2 ways to print Hello user 
# 1st is 

# name = name.strip().capitalize()
# print("Hello, " + name)


# how to split name 
first , last = name.split(" ")
print(f"Hello, {first} ")

# #2nd is 
# print("Hello,", name)

# # Both print works the same but 2nd method is mostly used 

# print("Hello,",end = " ")
# print(name)

# # how to use double quutes inside the parantheses

# print('Hello , "friend" ')
# print('Hello , \"friend\"')

# # Fromat string or F string 
# print(f"Hello, {name}")