def add(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def subtract(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        total -= i
    return total



def multiplication(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total



def division(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        if i == 0:
            return "Error! Cannot divide by zero."
        total /= i
    return total



def modulus(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        if i == 0:
            return "Error! Cannot divide by zero."
        total %= i
    return total



def get_power(numbers, power):
    result = []
    for i in numbers:
        result.append(i**power)
    return result





    

