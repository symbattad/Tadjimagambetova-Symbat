import re
txt  = "abbabbaabaab"
x = re.findall("ab*", txt)
print(x)