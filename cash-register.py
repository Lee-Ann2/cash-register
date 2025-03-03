def change(due, paid):
    if paid < due:
        raise ValueError(f'amount paid should be greater than amount due')
        
        denominations = {'R200': 20000, 'R100': 10000, 'R50': '5000', 'R20': 2000, 'R10': 1000, 'R5': 500, 'R2': 200, 'R1': 100, '50c': 50, '20c': 20, '10c': 10, '5c': 5}