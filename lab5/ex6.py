import re

txt=input("enter text")
x = re.sub("[,. ]",":",txt)
print(x)