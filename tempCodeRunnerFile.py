def power(numbers, pow):
    total = numbers[0]
    for i in numbers:
        total = i**pow
    print(total)

num = [100, 50]
p = 2

power(num, p)

