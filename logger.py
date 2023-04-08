import csv
import os.path


def get_base():
    if os.path.exists('data.csv') == False:
        return 'Не найдено'
    else:
        with open('data.csv', "r", encoding='utf-8') as file:
            return file.read()


def update_base(new_base):
    new_base_csv = [i.split(';') for i in new_base]

    with open('data.csv', 'w', encoding='utf-8', newline ='') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\r')
        writer.writerows(new_base_csv)


def add_note(note):
    try:
        with open('data.csv', 'a', encoding='utf-8', newline ='') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerows([note.split(';')])
    except FileNotFoundError:
        with open('data.csv', 'w', encoding='utf-8', newline ='') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerows([note.split(';')])

