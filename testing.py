def subtract(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        total -= i
    return

num = [100, 120]
subtract(num) 


def multiplication(numbers):
    total = 1
    for i in numbers:
        total *= i
    print(total)
num = [100, 120]
multiplication(num)


def division(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        total /= i
    print(total)

num = [100, 20]
division(num)





def modulus(numbers):
    total = numbers[0]
    for i in numbers[1:]:
        total %= i
    print(float(total))

num = [100, 3]
modulus(num)



def power(numbers, pow):
    total = numbers[0]
    for i in numbers:
        total = i**pow
    print(total)

num = [100, 50]
p = 2

power(num, p)






