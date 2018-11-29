# findAdult.py
age = [12, 6, 30, 52, 3, 42, 8, 18]
adult = [item for item in age if item >= 18]
adult.sort()
print(adult)
