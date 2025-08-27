import first
import second

# my_module/main.py

# lets use the functions in the first.py file
print("=== math functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets us the functions in the second.py file

print("\n=== string functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'python' =",second.reverse_string("python"))
print("Character count in sentence =",second.count_character("python modules are powerful"))
print("Word count in sentence  =",second.count_words("python modules are powerful"))
