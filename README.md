# Ultra-simple version
word = input("Enter word: ")
print(' '.join(format(ord(c), '08b') for c in word))
