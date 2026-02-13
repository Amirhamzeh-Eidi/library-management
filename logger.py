import os
from storage import data_dir


def show_history():
    data = read_txt('history.txt')
    if data:
        return data
    else:
        return '' 

def save_txt(file_name, data):
    with open(f'{data_dir}{file_name}', 'a', encoding='utf-8') as f:
        f.write(f'{data}\n')

def read_txt(file_name):
    try:
        with open(f'{data_dir}{file_name}', 'r', encoding='utf-8') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        return ''