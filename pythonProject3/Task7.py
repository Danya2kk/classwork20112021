numbers = [123, 523, 936]

for num in numbers:
    print(num)

user_number = int(input("Введите число из трёх цифр: "))

if user_number in numbers:
    print(numbers.index(user_number))
else:
    print("That is not in the list")



