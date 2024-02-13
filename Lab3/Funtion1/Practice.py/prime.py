num=int(input())
check = False
if num == 1:
    print(num, "no")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            check = True
            break
    else:
        print("yes")

    

        