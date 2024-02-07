def my_shape(x):
    if x=="rectangle":
        a=12
        b=11
        result=a*b
    elif x=="triangle":
        a=12
        b=11
        result=(a*b)/2
    elif x=="square":
        a=12
        result=a*a
    print(result)
        
x="rectangle"
my_shape(x)