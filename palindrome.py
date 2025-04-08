words = ['madam', 'hello', 'racecar',
         'world', 'level']

for word in words:
    if word == word[::-1]:
        print(f"{word} is a palindrome")
