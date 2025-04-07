logs = ['login', 'view', 'view', 
        'logout', 'login', 'login', 'logout']

for i in range(1, len(logs)):
    if logs[i] == logs[i - 1]: 
        print(f"Consecutive duplicate found: "
              f"{logs[i]} at positions {i-1} & {i}")
