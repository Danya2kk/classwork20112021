import random
import os

def printOption(choice):
    choice = int(input("Какую дверь хотите открыть? "))
    return

def doors(fight, heroPower):
    a = random.randint(1, 2)
    if a == 1:
        print("Вы нашли артефакт вам дается +", artifacts, " очков к силе, поздравляю!")
        heroPower += artifacts
        print("Теперь ваша сила составляет", heroPower + artifacts, "очков")

    elif a == 2:
        print("Вы наткнулись на монстра силой", monsterPower, "очков. Приготовтесь к битве")
        if heroPower >= monsterPower:
            print("Поздравляю вы победили монстра, но вы потратили очки силы. Теперь ваша сила составляет", heroPower - monsterPower, "очков")
            heroPower -= monsterPower
        elif heroPower <  monsterPower:
            print("Увы, но вы проиграли эту битву. Вы проиграли")




heroPower = 25
artifacts = random.randint(10, 80)
monsterPower = random.randint(5, 100)
newPower = 25

print("Добро пожаловать в игру! Вы находитесь в круглом зале с 10 дверями, вам предстоит сделать выбор, какую же дверь открыть? "
      "Помните за дверью могут быть монтсры, с которыми вам предстоит сразиться или артефакты, которые помогут вам в прохождении! Удачи!!!")









