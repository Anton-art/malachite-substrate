import os
import csv
import sys

BASE_DIR = "data_v2"

def find_object(target_id):
    for root, dirs, files in os.walk(BASE_DIR):
        if "index.csv" in files:
            file_path = os.path.join(root, "index.csv")
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                for row in rows:
                    if row['ID'] == target_id:
                        return file_path, row, reader.fieldnames, rows
    return None, None, None, None

def explode_object(target_id):
    print(f"💥 Попытка развернуть объект '{target_id}' в папку...")
    
    source_file, row_data, headers, all_rows = find_object(target_id)
    
    if not source_file:
        print(f"❌ Ошибка: Объект '{target_id}' не найден.")
        return

    parent_dir = os.path.dirname(source_file)
    new_folder_path = os.path.join(parent_dir, target_id)

    if os.path.exists(new_folder_path):
        print(f"⚠️ Папка '{new_folder_path}' уже существует.")
        return

    print(f"   📍 Найден в: {source_file}")
    print(f"   📂 Создаем папку: {new_folder_path}")
    
    os.makedirs(new_folder_path)

    # Создаем _meta.csv
    meta_path = os.path.join(new_folder_path, "_meta.csv")
    with open(meta_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Type", "Parent_ID", "Description"])
        
        parent_meta_path = os.path.join(parent_dir, "_meta.csv")
        parent_id = "UNKNOWN"
        if os.path.exists(parent_meta_path):
            with open(parent_meta_path, 'r', encoding='utf-8') as pm:
                try: parent_id = next(csv.DictReader(pm))['ID']
                except: pass

        writer.writerow([
            row_data['ID'], row_data['Name'], "ASSEMBLY", parent_id, row_data['Description']
        ])

    # Создаем index.csv
    index_path = os.path.join(new_folder_path, "index.csv")
    with open(index_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

    # Удаляем из старого файла
    with open(source_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for r in all_rows:
            if r['ID'] != target_id:
                writer.writerow(r)

    print(f"✅ Успех! Объект '{target_id}' превращен в папку.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python tools/explode.py <ID>")
    else:
        explode_object(sys.argv[1])