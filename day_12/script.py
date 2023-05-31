# Sys Module
# The sys module provides functions and variables used to manipulate different parts of the Python runtime environment
# Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
# Example of a script.py file:
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# Now to check how this script works I wrote in command line:
# python script.py Asabeneh 30DaysOfPython
# The result:
# Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
# Some useful sys commands:
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version