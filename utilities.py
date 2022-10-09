import json


def load_candidates(file_name):
    """
    Загрузка данных кандидатов из файла
    """
    with open(file_name, 'r', encoding='utf-8') as file:    # открытие файла
        data = json.load(file)                              # загрузка данных

    return data


def get_person(dat_cand):
    """
    Вывод данных одного кандидата
    """
    return f'  Имя кандидата - {dat_cand["name"]}\n  {dat_cand["pk"]}\n  {dat_cand["skills"]}\n'


def get_all(data):
    """
    Вывод данных списка кандидатов
    """
    main_page = ''  # инициализация строки
    cand_numb = len(data) - 1           # количество кандидатов - 1
    for i, dat in enumerate(data):
        main_page += get_person(dat)
        if i < cand_numb:               # последний CR не выводится согласно условию ДЗ
            main_page += '\n'

    return main_page


def get_by_pk(pk, data):
    """
    Выбор кандидата по его pk, предполагается, что pk - уникален
    """
    for dat in data:
        if int(dat.get('pk')) == pk:
            return True, get_person(dat)
    return False, f'Нет кандидатов с pk={pk}'


def get_by_skill(skill_name, data):
    """
    Выбор кандидатов по их навыку
    """
    # Инициализация массива словарей с кандидатами
    candidats = []

    for dat in data:
        if skill_name.upper() in dat.get('skills').upper():
            candidats.append(dat)
            continue
    if len(candidats) == 0:
        return f'Нет кандидатов с навыком \"{skill_name}\"'
    return get_all(candidats)       # вывод списка кандидатов
