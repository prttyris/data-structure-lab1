first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))

if first_num < second_num:
    print(f"The first number {first_num} is less than to the second number {second_num}")
elif first_num > second_num:
    print(f"The first number {first_num} is greater than the second number {second_num}")
else:
    print(f"The first number {first_num} is equal to the second number {second_num}")