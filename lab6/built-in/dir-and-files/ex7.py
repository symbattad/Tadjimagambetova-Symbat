file1 = "C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date"
file2 = "C:\Users\symba\Tadjimagambetova-Symbat\Lab4\w3school\date"
with open (file1, 'r') as src:
    with open (file2, 'w') as copy:
        for i in src:
            copy.write(i)