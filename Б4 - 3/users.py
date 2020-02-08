import json
import os
# Модуль os позволяет взаимодействовать с операционной системой - узнавать/менять
# файловую структуру, переменные среды, узнавать имя и права пользователя и др. 
# Программа, использующая переменные и функции модуля os, переносима с одной
# операционной системы на другую, так как os умеет учитывать особенности каждой ОС.
import uuid

DATA_FILE_PATH = "users.json"  # в этой переменной будем хранить путь к JSON документу

def read():
    """читает json док с диска"""
    # проверяем наличие файла на диске
    if not os.path.exists(DATA_FILE_PATH):
        # возвращаем пустой список, если файл еще не создан
        return []
    # открываем файл на чтение
        with open(DATA_FILE_PATH) as fd:
        # загружаем JSON документ
            users = json.load(fd)
    # возвращаем список пользователей

        return users

def save(users):
    """
  		Сохраняет список пользователей users в JSON файле на диск
     """


# открываем файл на запись
with open(DATA_FILE_PATH, "w") as fd:
    # сохраняем список пользователей на диск
            json.dump(users, fd, ensure_ascii=True)

def main():
    """
  	Осуществляет взаимодействие с пользователем и обрабатывает пользовательский ввод
  	"""
    # читаем список сохранённых пользователей
users_list = read()

print("привет! я запишу Ваши данные!")
    # запрашиваем у пользователя данные
first_name = input("Enter your first name:")
last_name = input("Enter your sir name:")
email = input("Enter your email:")
    # генерируем идентификатор пользователя и сохраняем его строковое представление
user_id = str(uuid.uuid4())
    # создаем словарь пользователя
user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    # добавляем нового пользователя в список всех пользователей
users_list.append(user)
    # сохраняем список пользователей
save(users_list)
print("Thanks, the data is saved!")


if __name__ == "__main__":
    main()
#рабочий файл users1.py
