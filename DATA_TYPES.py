#Example 1
#Print the data type of the variable x:

x = 5
print(type(x))


# 2 example 


x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

# 3 example
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview


#EX-1  ans:int
x = "Hello World"
print(type(x))


#EX-2 ans:str
x = "Hello World"
print(type(x))
 
#EX-3 ans:float
x = 20.5
print(type(x))

#EX-4 ans:list
x = ["apple", "banana", "cherry"]
print(type(x))

#EX-5 ans:tuple
x = ("apple", "banana", "cherry")
print(type(x))

#EX-6 ans:dict
x = {"name" : "John", "age" : 36}
print(type(x)) 
#EX-7 ans:bool
x = True
print(type(x))

