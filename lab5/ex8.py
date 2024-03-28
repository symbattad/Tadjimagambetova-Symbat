import re
f = r'[A-Z][a-z]*'
capitals = "apai postavt ful pzz"
x = re.findall(f, capitals)
print(x)