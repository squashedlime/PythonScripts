#importing the libaries
from sys import argv
#nameing the variables unpacking them into argv
script, input_file = argv
#function print_all with variable f
def print_all(f):
    print f.read()
#function rewind with variable f
def rewind(f):
    f.seek(0)
#function print_a_line with 2 variables         
def print_a_line(line_count, f):
    print line_count, f.readline()
#setting current_file variable to open(input_file) which opens input_file   
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
#this is the function we defined above
rewind(current_file)

print "Let's print three lines:"
#sets the line number
current_line = 1
#takes the above function and puts in the two variables
print_a_line(current_line, current_file)
#incrediments the line number
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


