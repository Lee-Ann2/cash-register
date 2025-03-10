def change(due, paid):
    if paid < due:
        raise ValueError(f'amount paid should be greater than amount due')
        
    denominations = {200: 20000, 100: 10000, 50: 5000, 20: 2000, 10: 1000, 5: 500, 2: 200, 1: 100, 50: 50, 20: 20, 10: 10, 5: 5}
    changeDictionary = {}
    changeLeft = paid - due

    for denomination, value in denominations.items():
        if changeLeft >= value:
            count = changeLeft // value
            changeDictionary[denomination] = count
            changeLeft -= count * value
    return changeDictionary

total = change(1222, 2000)
print(total)