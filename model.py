
def serch_note(base, find):
    base = base.split('\n')
    serch = True
    result = []
    for i in base:
        if str(find) in i:
            result.append(i)
            serch = False
    if serch:
        result.append(f'Заметка |{find}| не найдена')
    return result


def create_id(base):
    if base == 'Не найдено': 
        return 1
    else:
        previous_id = base.split(';')[-4][-1]
        next_id = int(previous_id) + 1
        return next_id


def edit_note(base, find_item, new_info):
    base = base.split('\n')
    index = 0
    for i in base:
        index += 1
        if find_item in i:
            note = i
            break
    new_note = note.split(';')
    new_note[new_info[0]] = new_info[1]
    new_note = ';'.join(new_note)
    base[index-1] = new_note
    base.remove(base[len(base)-1])
    return base


def del_note(base, result):
    base = base.split('\n')
    base.remove(result)
    base.remove(base[len(base)-1])
    return base
    

