
# 1 example 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#2 example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# 3 example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# 4 example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)