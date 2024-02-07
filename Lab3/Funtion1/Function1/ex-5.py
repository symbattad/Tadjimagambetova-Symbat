def print_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[:i] + s[i+1:]
            print_permutations(rem, prefix + s[i])
user_string = "abcd" 
print_permutations(user_string)