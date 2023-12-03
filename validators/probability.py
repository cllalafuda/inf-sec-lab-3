def probability_validator(string):
    try:
        number = float(string)
    except ValueError:
        return False
    if number <= 0 or number >= 1:
        return False
    return True
