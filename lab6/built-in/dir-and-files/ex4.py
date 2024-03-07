import os
path = input("Enter path: ")
#C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date as example

with open (path, 'r') as file:
    count_lines = len(file.readlines())
    print("The number of lines in the given file is: ", count_lines)