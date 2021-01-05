
# Problem 1

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print('FIFA')
    elif number % 3 == 0:
        print('FI')
    elif number % 5 == 0:
        print('FA')
    else:
        print(number)

