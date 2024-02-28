import re
f = r'[A-Z][a-z]*'
capitals = "apai postavt eful pzz"
x = re.findall(f, capitals)
print(x)