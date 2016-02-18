from sys import argv
#so when we run this, "python ex15.py ex.txt" ex15.py=script ex.txt=filename
script, filename = argv
#stating the varible txt and opening the file. This creates a "FILE OBJECT" THINK OF IT AS A TAPE DRIVE YOU CAN MOVE AROUND IN IT AND READ IT BUT THE FILE IS NOT THE CONTENTS.
txt = open(filename)
#this prints the file name
print "Here's your file %r:" % filename
#this prints the files contents
print txt.read()
txt.close()
#this prints the string within ""
print "Type the filename again:"
#this sets the variable file_again to the input from the raw input commad
file_again = raw_input(">")
#this takes the varible file_again which we just typed in and opens the file and asigns the contents to the varible txt_again
txt_again = open(file_again)
#this prints the contents of the file by doing the read() command on txt_again
print txt_again.read()
txt_again.close()
