def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
for j in squares(a,b):
    print(j)