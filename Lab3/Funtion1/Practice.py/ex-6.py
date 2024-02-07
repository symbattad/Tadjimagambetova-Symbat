def get_max(numbers):
    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    print(max)
            
numbers=[9,8,8]
get_max(numbers)



def get_min(numbers):
    min=numbers[0]
    for i in numbers:
        if i<min:
            min=i
    print(min)
            
numbers=[9,8,7]
get_min(numbers)


