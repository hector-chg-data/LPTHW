from sys import argv as argumentos_terminal

script, input_fie = argumentos_terminal

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the whole file:\n")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)






