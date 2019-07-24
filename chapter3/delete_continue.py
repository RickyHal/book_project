#delete_continue.py
#!/usr/bin/env python3
var = 10
while var > 0:
    var = var -1
    if var == 5 or var == 8:
        continue
    print ('当前值 :', var)
