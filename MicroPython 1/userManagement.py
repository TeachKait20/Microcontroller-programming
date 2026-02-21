# for ESP32

import time

allUser = {
    "Oleg": "qwerty123!", 
    "Anna": "xxXX1234"
    }

def newUser(newUser, newPass):
    global allUser
    allUser[newUser] = newPass
    print("Пользователь", newUser, "добавлен")

def printUsers():
    if not allUser:
        print("_______________________________")
        print("Нет пользователей в системе")
        print("_______________________________")
        return
        
    print("Все пользователи:")
    print("_______________________________")
    for username, password in allUser.items():
        print(f"Имя: {username}")
        print(f"Пароль: {password}")
        print("---------------------------")
    print("_______________________________")

def main():
    while True:
        print("[1] - посмотреть всех пользователей")
        print("[2] - добавить пользователя")
        print("[3] - удалить пользователя")
        print("[4] - выход")

        answer = input("> ")

        if answer == "1":
            printUsers()

        elif answer == "2":
            newUserName = input("Введите имя пользователя: ")
            
            if newUserName in allUser:
                print("______________________________________")
                print("Такое имя пользователя уже существует")
                print("______________________________________")
            else:
                newPass = input("Введите пароль для пользователя: ")
                # надо проверить, что пароль больше 8-ми символов
                newUser(newUserName, newPass)
                print("_______________________________")
                print("Пользователь успешно создан")
                print("_______________________________")
        
        elif answer == "3":
            pass  # заглушка. дописать функцию удаления пользователей

        elif answer == "4":
            print("Выход из системы")
            print("Сохранение данных...")
            for i in "*" * 15:
                print(i, end="")
                time.sleep(0.5)
            print("Успешный выход")
            time.sleep(1)
            break

        else:
            print("Некорректный ответ.")

main()
