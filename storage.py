import json
import os
def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)
    print(f"Directory '{directory_name}' created successfully.")
create_directory('data')

path = os.path.realpath(__file__)
main_dir = os.path.dirname(path)
data_dir = os.path.join(main_dir, 'data')

def save_data(data_list, file_name):
    dictionary_list = [item.to_dict() for item in data_list]
    with open(f'{data_dir}{file_name}', 'w', encoding='utf-8') as file:
        json.dump(dictionary_list, file, indent=4)
    
def load_data(file_name, class_type):
    try:
        with open(f'{data_dir}{file_name}', 'r', encoding='utf-8') as file:
            data_list = json.load(file)
            obj_list = [class_type(**item) for item in data_list]
        return obj_list
    except FileNotFoundError:
        return []  

