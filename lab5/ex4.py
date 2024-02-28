import re
string = "i dont know what to say"
pattern = r"([A-Z]{1}+[a-z]*)"
x = re.findall(pattern, string)
print(x)