#collecting 5 nigerian stateentered by the user.
state1 = input("Enter a state: ")
state2 = input("Enter a state: ")
state3 = input("Enter a state: ")
state4 = input("Enter a state: ")
state5 = input("Enter a state: ")
Nigeria_state = state1, state2, state3, state4, state5
five_states =tuple(Nigeria_state)
print(five_states[0])
print(five_states[-1])

# checking if lagos is in the tuple
print("lagos" in five_states)
print(len(five_states))