import logger
import model
import view


def control_edit_note():
    base = logger.get_base()
    head = view.input_to_find()
    result = model.serch_note(base, head)
    view.show_found(result)
    if 'не найден' not in result[0] and len(base.split('\n')) > 1:
        find = str(view.input_id()) + ';' + head
        update = model.edit_note(base, find, view.input_edit_command())
        logger.update_base(update)

    elif 'не найден' not in result[0]:
        result = base.split('\n')[0]
        update = model.edit_note(result)
        logger.update_base(update)


def control_del_note():
    base = logger.get_base()
    head = view.input_to_find()
    result = model.serch_note(base, head)
    view.show_found(result)
    if 'не найден' not in result[0] and len(base.split('\n')) > 1:
        find = str(view.input_id()) + ';' + head
        result = model.serch_note(base, find)[0]
        update = model.del_note(base, result)
        logger.update_base(update)
    elif 'не найден' not in result[0]:
        result = base.split('\n')[0]
        update = model.del_note(base, result)
        logger.update_base(update)


def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':     # Добавление
            id = model.create_id(logger.get_base())
            note = view.new_note(id)
            logger.add_note(note)

        elif mode == '2':   # Поиск
            head = view.input_to_find()
            base = logger.get_base()
            result = model.serch_note(base, head)
            view.show_found(result)

        elif mode == '3':   # Вывод базы
            base = logger.get_base()
            view.show_all_info(base)

        elif mode == '4':   # Редактирование
            control_edit_note()

        elif mode == '5':   # Удаление заметки
            control_del_note()

        elif mode == '6':   # Выход из программы
            return False

        else:
            return 'Неккоретная команда'