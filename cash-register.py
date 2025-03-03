def change(due, paid):
    if paid < due:
        raise ValueError(f'amount paid should be greater than amount due')
    