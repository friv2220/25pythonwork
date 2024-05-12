def getMoneySpent(keyboards, drives, b):
    maxmount = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard+drive<=b:
                maxmount = max(maxmount, keyboard=drive)
    return maxmount