name = input("Введите три имени тех которых вы хотите пригласить: ")
inviteList = [name]

while True:
    option = input("Хотите кого-то пригласить еще yes/no: ")
    if option == "yes":
        newName = input("Введите имя приглашенного: ")
        inviteList = [name + ' ' + newName]
    elif option == "no":
        break
for n in inviteList:
    print(n)