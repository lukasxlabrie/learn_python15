from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
file_again = input("> ")

print(txt.read())
file_again =input("> ")