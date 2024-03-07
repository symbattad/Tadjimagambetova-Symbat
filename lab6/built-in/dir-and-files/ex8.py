import os
path = input("Enter path for your file: ")
#C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File successfully deleted!")
else:
    print("File not found!")