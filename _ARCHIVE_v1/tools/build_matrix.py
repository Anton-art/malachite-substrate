import os
import csv
import json
import sys

# Настройки
DATA_DIR = "data"
OUTPUT_FILE = "malachite_graph.json"

# Цвета для консоли
C_OK = '\033[92m'
C_WARN = '\033[93m'
C_FAIL = '\033[91m'
C_END = '\033[0m'

def parse_list(cell_data):
    """Превращает строку 'ID1;ID2' в список"""
    if not cell_data or cell_data.strip() == "NULL":
        return []
    return [x.strip() for x in cell_data.split(';') if x.strip()]

def build():
    print(f"🏗️  Запуск Матричного Сборщика...")
    
    nodes = {}
    categories = {}
    
    # 1. Сканируем папки (Рекурсивно)
    for root, dirs, files in os.walk(DATA_DIR):
        
        # А. Читаем паспорт папки (_meta.csv)
        if "_meta.csv" in files:
            meta_path = os.path.join(root, "_meta.csv")
            try:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cat_id = row['ID']
                        categories[cat_id] = {
                            "id": cat_id,
                            "name": row['Name'],
                            "type": "CATEGORY", # Или GROUP/BASE
                            "parent_id": row['Parent_ID'],
                            "description": row['Description']
                        }
            except Exception as e:
                print(f"{C_FAIL}Ошибка в {meta_path}: {e}{C_END}")

        # Б. Читаем объекты (index.csv)
        if "index.csv" in files:
            index_path = os.path.join(root, "index.csv")
            try:
                with open(index_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    
                    # Определяем ID текущей папки (чтобы привязать объекты к ней)
                    current_folder_id = "UNKNOWN"
                    if "_meta.csv" in files:
                        # Перечитываем meta быстро, чтобы взять ID
                        with open(os.path.join(root, "_meta.csv"), 'r', encoding='utf-8') as mf:
                            current_folder_id = next(csv.DictReader(mf))['ID']

                    for row in reader:
                        node_id = row['ID']
                        
                        # Собираем все требования в один словарь
                        requirements = {
                            "science": parse_list(row.get('Req_Science', '')),
                            "design": parse_list(row.get('Req_Design', '')),
                            "resource": parse_list(row.get('Req_Resource', '')),
                            "material": parse_list(row.get('Req_Material', '')),
                            "infrastructure": parse_list(row.get('Req_Infrastructure', '')),
                            "process": parse_list(row.get('Req_Process', '')),
                            "artifact": parse_list(row.get('Req_Artifact', '')),
                            "society": parse_list(row.get('Req_Society', '')) # Старое имя колонки
                        }
                        
                        # Собираем плоский список родителей для проверки связей
                        all_parents = []
                        for req_list in requirements.values():
                            all_parents.extend(req_list)

                        nodes[node_id] = {
                            "id": node_id,
                            "name": row['Name'],
                            "description": row.get('Description', ''),
                            "type": "OBJECT",
                            "folder_category_id": current_folder_id, # Связь с папкой
                            "level": row.get('Level', 'SPECIFIC'),
                            "requirements": requirements,
                            "all_parents_flat": all_parents
                        }
            except Exception as e:
                print(f"{C_FAIL}Ошибка в {index_path}: {e}{C_END}")

    print(f"📊 Найдено категорий (папок): {len(categories)}")
    print(f"📊 Найдено объектов: {len(nodes)}")

    # 2. Валидация (Проверка связей)
    print(f"\n🔍 Проверка целостности...")
    missing_links = 0
    
    for node_id, node in nodes.items():
        for parent in node['all_parents_flat']:
            # Родитель может быть Объектом ИЛИ Категорией
            if parent not in nodes and parent not in categories:
                print(f"{C_WARN}[MISSING] {node['name']} ({node_id}) требует --> {parent} (не найдено){C_END}")
                missing_links += 1

    # 3. Сохранение
    full_graph = {
        "meta": {"version": "2.0", "status": "Matrix Ontology"},
        "categories": list(categories.values()),
        "nodes": list(nodes.values())
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(full_graph, f, indent=2, ensure_ascii=False)

    if missing_links == 0:
        print(f"\n{C_OK}✅ УСПЕХ! Граф собран без ошибок.{C_END}")
    else:
        print(f"\n{C_WARN}⚠️ Граф собран, но найдено {missing_links} битых ссылок.{C_END}")
    print(f"📁 Результат: {OUTPUT_FILE}")

if __name__ == "__main__":
    build()