
a = input("Введите любимое блюдо: ")
b = input("Введите любимое блюдо: ")
c = input("Введите любимое блюдо: ")
d = input("Введите любимое блюдо: ")

dishes = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
}
for dish in dishes:
    print(dish)

x = input("Какое блюдо хотите удалить? ")
dishes.pop(x)
for i in sorted(dishes):
    print(i)

