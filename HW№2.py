account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

users = [user1, user2, user3, user4]
accounts = [account1, account2, account3, account4]

task_1 = input("Введите ключ (name или account):").lower()

try:
    print(f"значение ключа {task_1} для юзера 1 = {user1[task_1]}")
    print(f"значение ключа {task_1} для юзера 2 = {user2[task_1]}")
    print(f"значение ключа {task_1} для юзера 3 = {user3[task_1]}")
    print(f"значение ключа {task_1} для юзера 4 = {user4[task_1]}")

except:
    print('Введенный ключ не найден')
user_key = int(input('Введите порядковый номер:'))
try:
    print(f"Данные по юзеру № {user_key}: \n"
          f"Имя: {users[user_key-1]['name']} \n"
          f"Возраст: {users[user_key-1]['age']} \n"
          f"Аккаунт: {accounts[user_key-1]['login']} \n"
          f"Пароль: {accounts[user_key-1]['password']}")
except:
    print('Пользователь с указанным номером не найден')

task_3 = int(
    input('Введите номер пользователя которого хотите переместить в конец:'))
print('Список до изменеия:')
print(users)
print(f"Ползователь с именем{users[task_3-1]['name']} перемещен в конец")
element = users.pop(task_3-1)
users.append(element)
print('Список после изменеия:')
print(users)
lenght = len(users)
midAge = (user1['age']+user2['age']+user3['age']+user4['age'])/lenght
print(f"Средний возраст пользователей: {midAge}")
