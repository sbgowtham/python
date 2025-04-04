s = "aabbccddeeffgg"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
else:
    print("None")
