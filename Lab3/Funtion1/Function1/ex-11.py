def palindrome(word):
    word = word.lower() 
    if word[::-1] == word:
        print("Yes! Word is palindrome.")
    else:
        print("Nope")

palindrome("Madam")