import os
from pprint import pprint as pp


def get_cook_book(file_name):
    cook_book = {}
    temp_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if line != '\n':
                temp_list.append(line.replace('\n', ''))
            else:
                cook_book[temp_list[0]] = generate_dict(temp_list[2::])
                temp_list.clear()
    return cook_book


def generate_dict(raw_list: list):
    ingredients = []
    for line in raw_list:
        ingredient = line.split(' | ')
        ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
    return ingredients


def get_shop_list_by_dishes(dishes_list: list, number_of_person: int):
    ingredients = {}
    cook_book = get_cook_book('recipes.txt')
    for dish in dishes_list:
        for ingredient in cook_book[dish]:
            ingredients[ingredient['ingredient_name']] = {
                'measure': ingredient['measure'],
                'quantity': ingredient['quantity'] * number_of_person
            }
    return ingredients


def sorted_files(files: list):
    d = {}
    l = []
    for file in files:
        with open(file, 'r') as f:
            d[file] = len(f.readlines())
            l.append(f.readlines())
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1])
    return list_d


def merging_files(files: list):
    list_d = sorted_files(files)
    for i in list_d:
        with open('result.txt', 'a') as f:
            f.writelines(i[0] + '\n')
            f.writelines(str(i[1]) + '\n')
            for file_name, file_len in list_d:
                with open(file_name) as f_r:
                    f.writelines(f_r.readlines())
            f.writelines('\n')


pp(get_cook_book('recipes.txt'))
pp(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
merging_files(['1.txt', '2.txt', '3.txt'])