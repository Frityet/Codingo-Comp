# Uncomment the code below and fix the bug as described in the question.
# Underneath the fixed code, describe what the initial issue was and how
# you fixed it.

file = open("new_file.txt", "r")
name = input("Please enter a first name: ")
file.write(name)
file.close()
age = input("Please enter a last name: ")
file.write(age)
