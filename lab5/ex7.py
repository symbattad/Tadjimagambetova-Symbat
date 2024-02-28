import re
string = "dfghjkl"
x = re.sub(r'_\w', lambda match: match.group(0).replace('_', '').upper(),string)
print(x)