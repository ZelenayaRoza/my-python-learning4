HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечать все добавленные задачи. 
"""
tasks = []

command = input('Введите команду: ')
while command:
    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите название задачи: ')
        tasks.append(task)
        print('Задача добавлена')
    elif command == 'show':
        print(tasks)
    else:
        print('Неизвестная команда')
        break  
