numbers=input(" ")
def get_max(numbers):
    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    print(max)  
get_max(numbers)