# single quotes
# name = 'Ada'
# print(name)

# #Double quotes
# greeting = "Hello"
# print(greeting)

#tripple quotes (for multi_line strings)
# story = ''' once upon a time ,
# there was a coder named Ada. '''
# print(story)


# #string with numbers and symbols
# password = "p@ssw0rd123"

#indexing
# word = "python"
# print(word[0])  # p 
# print(word[-1]) # n

#slicing
# word = "python"
# print(word[0:4])   # pyth
# print(word[2:])    # thon        it counts after 2
# print(word[:3])    #pyt       it counts 3 letters 
# print(word[::4])     # pto  start and stop in p then count 4 letter after p 
# print(word[::-1])  # nohtyp  start and stop in n then count -1  


# concatenation
# a = "Hello"
# b = "World"
# print(a + " " + b) # hello world

# Repetition
# word = "Hi! "
# print(word * 3) # Hi! Hi! Hi! 

# string searching & checking
# text = "python programming"
# print("python" in text)  # true
# print("Java" not in text) # true


# find() / rfind()
# text = "Hello world"
# print(text.find("o")) # 4
# print(text.rfind("o"))  # 7

# index()/ rindex()
# (like find() but raises an error if not found)
# text = "Hello world"
# print(text.index("world")) # 6

# # startswith()/ endswith()
filename = "data.csv"
print(filename.startswith("data")) # true
print(filename. endswith(".csv")) # true