from random import randint


class Counter:
    def __init__(self):
        self.__counter = randint(10, 100)
        print("Число сгенерировано.")

    def increase(self, value):
        self.__counter = self.__counter + value
        print("Мы увеличим число на", value)

    def decrease(self, value):
        self.__counter = self.__counter - value
        print("Мы уменьшим число на", value)

    def count(self):
        return self.__counter


count = Counter()

while True:
    option = input("Нажмите + для увеличения, - для уменьшения, q для выхода из счетчика ")
    if option == '+':
        count.increase(randint(0, 10))
        print("Результат",count.count())
    elif option == '-':
        count.decrease(randint(0, 10))
        print("Результат", count.count())
    elif option == 'q':
        print("Результат", count.count())
        break
    else:
        print("Введена неверная команда")
