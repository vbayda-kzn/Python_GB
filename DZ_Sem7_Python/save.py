# модуль сохранения текущей версии Справочника

import names

def save_data():
    if names.data !=[]:
        with open ("tel.txt", 'w', encoding="utf-8") as f:
            data_str = ""
            for i in names.data:
                row = " ".join(i)
                data_str += row + "\n"
            f.write(data_str)
            print("Изменения Справочника сохранены.")
    else: 
        print("Справочник пуст или не был загружен - сохранять нечего.")
    
        

