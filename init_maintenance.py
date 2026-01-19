import os
import csv
from taxonomy_config import TAXONOMY


ROOT_DIR = "data_v2"


def create_meta_file(path, node_data, parent_id):
    # Метаданные (описание папки) можно перезаписывать смело, это структура
    meta_path = os.path.join(path, "_meta.csv")
    with open(meta_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Type", "Parent_ID", "Description"])
        writer.writerow([node_data['id'], node_data['name'], node_data['type'], parent_id, node_data.get('description', "")])


def safe_create_index_file(path):
    # А вот index.csv трогать нельзя, если он есть!
    index_path = os.path.join(path, "index.csv")
    if not os.path.exists(index_path):
        with open(index_path, mode='w', newline='', encoding='utf-8') as file:
            pass
        return True # Создал новый
    return False # Пропустил существующий


def build_structure_safe(base_path, structure, parent_id="ROOT"):
    created_count = 0
    for folder_name, node_data in structure.items():
        current_path = os.path.join(base_path, folder_name)
        
        # 1. Создаем папку, если нет
        if not os.path.exists(current_path):
            os.makedirs(current_path)
            created_count += 1
            print(f"➕ Добавлена новая папка: {folder_name}")
        
        # 2. Всегда обновляем паспорт (вдруг мы поменяли описание в конфиге)
        create_meta_file(current_path, node_data, parent_id)
        
        # 3. Создаем таблицу ТОЛЬКО если её нет
        if safe_create_index_file(current_path):
            # Если файл новый, можно сразу прогнать update_headers (опционально)
            pass 


        # Рекурсия
        if "children" in node_data:
            created_count += build_structure_safe(current_path, node_data["children"], parent_id=node_data['id'])
            
    return created_count


def main():
    print("🛡️ ЗАПУСК РЕЖИМА 'MAINTENANCE' (БЕЗОПАСНОЕ ОБНОВЛЕНИЕ)...")
    if not os.path.exists(ROOT_DIR):
        print("❌ База не найдена. Сначала запустите init_genesis.py!")
        return


    new_folders = build_structure_safe(ROOT_DIR, TAXONOMY)
    
    if new_folders == 0:
        print("✅ Структура актуальна. Новых папок не добавлено.")
        print("ℹ️ Метаданные (_meta.csv) обновлены.")
    else:
        print(f"✨ Структура обновлена. Добавлено папок: {new_folders}")


if __name__ == "__main__":
    main()