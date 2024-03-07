import string
#C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date
for i in string.ascii_uppercase:
    with open(f'{i}.txt', 'w') as file:
        file.write(f'{i}')

file.close()