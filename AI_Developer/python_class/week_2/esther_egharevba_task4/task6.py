# Asking  user to enter a word
word = input("please enter a word: ")
print(len(word))


# Check if it is all uppercase, all lowercase, or title case.
print(f"uppercase: {word.isupper()}")
print(f"uppercase: {word.islower()}")
print(f"uppercase: {word.istitle()}")


# Reversing  the word using slicing.
print(word[: :-1])
