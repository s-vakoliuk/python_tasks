# Cтворити порожній список users_list = []

# Створити меню в якому потрібно реалізувати:
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню

# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = [] # порожній список users_list

while True:
    print("1) додававання нового юзера)")
    print("2) вивід всіх юзерів")
    print("3) вивід всіх юзерів за віком")
    print("4) видалення юзера по id")
    print("5) заміна статуса юзера на протилежний")
    print("6) вихід з меню")

    choice = input('Зробіть вибір: ')

    if choice == '1':
        user = {}  # порожня бібліотека user
        print("Введіть дані користувача:")

        id = int(input("Введіть свій id: "))
        name = str(input("Введіть своє ім'я: "))
        age = int(input("Введіть свій вік: "))
        status = bool(input("Введіть свій статус: "))

        user = {'id': id,
                'name': name,
                'age': age,
                'status': status,
                }

        users_list.append(user) # додати словник (користувача) user до списку users_list

        repeat= input("Додати дані наступного користувача? Якщо так введіть 1, якщо ні 0: ")
        if repeat == "1":
            choice == "1"
        elif repeat == "0":
            print(users_list)
            continue

    elif choice == '2':
        for item in users_list:
            print(item)

    elif choice == '3':
        name = input('Введіть вік користувача: ')
        for item in users_list:
            if item['age'] == age:
                print(item)


    elif choice == '4':
        id = input('Введіть id користувача для видалення: ')
        for item in range(len(users_list)):
            if item['id'] == id:
                del users_list[item]

        print(users_list)

    elif choice == '5':
        status = input('Введіть status користувача для видалення: ')
        for item in range(len(users_list)):
            if users_list[item] == status['true']:
                users_list[item] = 'false'

        print(users_list)

    elif choice == '6':
        break