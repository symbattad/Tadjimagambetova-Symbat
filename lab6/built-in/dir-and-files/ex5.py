import os
path = input("Enter path: ")
my_list = ["Divergent", "The Matrix", "The Hunger games"]
with open(path, 'w') as file:
    for element in my_list:
        file.write(str(element) + '\n')
        
print("List has been written to the file successfully.")