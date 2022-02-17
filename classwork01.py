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

user = {} # порожня бібліотека user
while True:
    id = int(input("Введіть свій id: "))
    name = str(input("Введіть своє ім'я: "))
    age = int(input("Введіть свій вік: "))
    status = bool(input("Введіть свій статус: "))

    print("Введіть дані наступного користувача")

    user={'id':id,
      'name':name,
      'age':age,
      'status':status,
      }

    # for user in range (3):
    users_list.append(user)
    if len(users_list)==4:
        break


print(users_list)