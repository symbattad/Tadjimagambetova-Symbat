import re

txt = input("Введите слово: ")
x = re.findall("a.*b", txt)
print(x)