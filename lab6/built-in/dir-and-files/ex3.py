import os
path = input("Enter path: ")
#C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date as example

if os.path.exists(path):
    print(path)
    print("Filename of the given path: ", os.path.basename(path))
    print("Directory portion of the given path: ", os.path.dirname(path))
else:
    print("The path do not exist")