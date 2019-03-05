def is_armstrong(number):
    magnitude = len(str(number))

    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** magnitude
        temp //= 10

    if sum == number:
        return True
        
    return False