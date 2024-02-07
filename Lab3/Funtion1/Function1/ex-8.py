def spy_game(nums):
    d = list(map(str,filter(lambda x: x==0 or x==7,nums)))
    f= ''.join(d)
    if '007' in f:
        print(True)
    else:
        print(False)