# list_find_adult_1.py
#!/usr/bin/env python3
age = [12, 6, 30, 52, 3, 42, 8, 18]
adult = [item for item in age if item >= 18]
adult.sort()
print(adult)
