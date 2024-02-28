import re
txt= "abbbabb"
x=re.findall("a.{2,3}b")
print(x)