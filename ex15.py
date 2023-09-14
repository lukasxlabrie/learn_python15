#tells python tp save user input for later use
from sys import argv

#tells python that the input will be used for "filename"
script, filename = argv

#prints a meassge
txt = open(filename)

#calls a fucntion on txt called "read"
print(f"Here's your file {filename}:")
print(txt.read())

#the rest of the srcipt is nore of the same
print("Type The filename again:")
file_again =input("> ")

txt_again = open(file_again)

print(txt_again.read())