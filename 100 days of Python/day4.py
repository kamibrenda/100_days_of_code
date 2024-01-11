#multiply a number by 8 if its an even number and by 9 if otherwise
def simple_multiplication(number):
    if number % 2 == 0:
        result = number * 8
    else:
        result = number * 9
    return result