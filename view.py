import datetime

def input_to_find():
    return input('Введите информацию для поиска: ')


def choose_mode():
    return input('-------------------------------------------------------------\
----------------------------------------------------------------------------\n\
"1" - Ввод новых заметок, \
"2" - Поиск заметки, \
"3" - Вывести всю базу заметок, \
"4" - Редактирование заметки, \
"5" - Удаление заметки, \
"6" - Выход из программы \
\nВыберите комманду: ')


def new_note(id):
    head_note = input('Введите заголовок заметки: ')
    note = input('Введите заметку: ')
    date = datetime.datetime.now()

    return f'{id};{head_note};{note};{date}'


def show_found(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)

def show_all_info(base):
    print(base)


def get_base():
    with open('data.csv', "r") as file:
        return file.read()


def input_id():
    return int(input('Введите id заметки: '))


def input_edit_command():
    command = int(input('"1" - Изменить заголовок заметки\
    "2" - Изменить заметку\
    \n Введите комманду: '))

    input_info = ''
    if command == 1: input_info = input('Введите новый заголовок заметки: ')
    if command == 2: input_info = input('Введите новую заметку: ')

    return [command, input_info]