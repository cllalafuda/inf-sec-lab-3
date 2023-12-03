def brute_speed_validator(string):
    try:
        number = float(string)
    except ValueError:
        return False
    if number <= 0:
        return False
    return True
