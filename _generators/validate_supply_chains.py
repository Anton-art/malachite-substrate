import os
import csv
import sys
from collections import defaultdict

# =================================================================================
# НАСТРОЙКИ
# =================================================================================

ROOT_DIR = "data_v2"

# Колонки, которые содержат ссылки на другие ID
DEPENDENCY_COLUMNS = [
    "Req_Resource", 
    "Req_Material", 
    "Req_Process", 
    "Bill_of_Materials", 
    "Req_Infrastructure",
    "Predecessor_ID",
    "Power_Source"
]

# =================================================================================
# ЛОГИКА
# =================================================================================

def load_database(root_path):
    """Загружает все ID и их имена в память."""
    db_index = {} # {ID: Name}
    file_map = {} # {ID: FilePath}
    
    print(f"📂 Сканирование базы данных в {root_path}...")
    
    count = 0
    for dirpath, _, filenames in os.walk(root_path):
        if "index.csv" in filenames:
            path = os.path.join(dirpath, "index.csv")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if "ID" in row and row["ID"]:
                            obj_id = row["ID"].strip()
                            db_index[obj_id] = row
                            file_map[obj_id] = path
                            count += 1
            except Exception as e:
                print(f"⚠️ Ошибка чтения {path}: {e}")
                
    print(f"✅ Загружено объектов: {count}")
    return db_index, file_map

def validate_links(db_index, file_map):
    """Проверяет все связи на существование."""
    print("🔗 Проверка производственных цепочек...")
    
    missing_links = defaultdict(list) # {Missing_ID: [Who_Needs_It, ...]}
    total_links = 0
    broken_links = 0
    
    for obj_id, data in db_index.items():
        for col in DEPENDENCY_COLUMNS:
            if col in data:
                val = data[col]
                # Пропускаем пустые значения и NULL
                if not val or val == "NULL" or val == "":
                    continue
                
                # 1. Разделяем списки по точке с запятой (например "ID1;ID2")
                raw_targets = [t.strip() for t in val.split(';') if t.strip()]
                
                for target in raw_targets:
                    # 2. FIX: Отсекаем суффиксы количеств (например "PART-BOLT:5" -> "PART-BOLT")
                    clean_target = target.split(':')[0].strip()
                    
                    total_links += 1
                    
                    # Игнорируем ссылки на внешние системы (пока) или абстракции
                    if clean_target not in db_index:
                        broken_links += 1
                        # Записываем, кто ссылается, чтобы найти ошибку
                        missing_links[clean_target].append(f"{obj_id} ({col})")

    return missing_links, total_links, broken_links

def print_report(missing_links, total, broken):
    print("\n" + "="*60)
    print("📊 ОТЧЕТ МАТЕМАТИКА ГРАФОВ (SUPPLY CHAIN AUDIT)")
    print("="*60)
    
    if total == 0:
        print("⚠️ Связей не обнаружено. База данных состоит из изолированных атомов.")
        return

    health = ((total - broken) / total) * 100
    print(f"Всего связей проверено: {total}")
    print(f"Битых ссылок:           {broken}")
    print(f"Целостность Графа:      {health:.2f}%")
    
    if broken == 0:
        print("\n✅ ИДЕАЛЬНО. Все производственные цепочки замкнуты.")
    else:
        print("\n❌ ОБНАРУЖЕНЫ РАЗРЫВЫ ЦЕПОЧЕК (ТОП-15 ОТСУТСТВУЮЩИХ):")
        print("(Эти объекты нужны, но их нет в базе)")
        print("-" * 60)
        
        # Сортируем по количеству зависимостей (самые нужные - вверху)
        sorted_missing = sorted(missing_links.items(), key=lambda x: len(x[1]), reverse=True)
        
        for missing_id, requesters in sorted_missing[:15]:
            print(f"🔴 {missing_id:<35} (Требуется в {len(requesters)} местах)")
            # Показываем пару примеров, кто требует
            examples = ", ".join(requesters[:2])
            if len(requesters) > 2: examples += ", ..."
            print(f"   ↳ Кто ищет: {examples}")
            print()
            
        if len(sorted_missing) > 15:
            print(f"... и еще {len(sorted_missing) - 15} отсутствующих ресурсов.")

    print("="*60)
    print("💡 РЕКОМЕНДАЦИЯ:")
    if health < 50:
        print("Система фрагментирована. Срочно нужны генераторы для отсутствующих ресурсов.")
    elif health < 90:
        print("Хорошая структура, но есть пробелы. Заполните недостающие звенья.")
    else:
        print("Система стабильна.")

if __name__ == "__main__":
    if not os.path.exists(ROOT_DIR):
        print(f"❌ Ошибка: Папка {ROOT_DIR} не найдена.")
    else:
        db, fmap = load_database(ROOT_DIR)
        if db:
            missing, tot, brk = validate_links(db, fmap)
            print_report(missing, tot, brk)