num = input()

if num.isdigit():
    print(f'You have written a positive number: {num}!')
elif float(num) % 1 != 0:
    print(f'You have written a positive decimal number: {num}!')
elif (float(num) < 0) % 1 != 0:
    print(f'You have written a negative decimal number: {num}!')
else:
    print(f'You have written a negative number: {num}!')
