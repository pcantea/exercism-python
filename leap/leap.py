def is_leap_year(year):
    if (year % 4 == 0) & (year % 100 == 0):
        if year % 400 == 0:
            return True
        else:
                return False
    elif year % 4 == 0: 
        return True

    return False