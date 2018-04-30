from sys import argv as input_terminal
import subprocess as sp #Module for clearing screen

script, filename = input_terminal

print("Here's your file %r:" % filename)
print("\v---------------------------------")
txt = open(filename)
print(txt.read())

