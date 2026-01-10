import csv
import os
import glob

# --- КОНФИГУРАЦИЯ ---
SOURCE_DIR = "data"
DEST_DIR = "data_v2"

# 1. КАРТА МИГРАЦИИ (Куда отправлять объекты по их Типу/Префиксу)
DESTINATION_MAP = {
    # --- 01 SCIENCE ---
    "DISCOVERY": "01_SCIENCE/Physics",
    "LAW": "01_SCIENCE/Physics",
    "THEORY": "01_SCIENCE/Physics",
    "BIO": "01_SCIENCE/Biology",
    
    # --- 02 DESIGN ---
    "STANDARD": "02_DESIGN/Standards",
    "METHOD": "02_DESIGN/Methods",
    "BLUEPRINT": "02_DESIGN/Blueprints",
    
    # --- 03 RESOURCES ---
    "RESOURCE": "03_RESOURCES/Minerals",
    "MINERAL": "03_RESOURCES/Minerals",
    "CROP": "03_RESOURCES/Biosphere",
    "SEED": "03_RESOURCES/Biosphere",
    
    # --- 04 MATERIALS ---
    "ELEMENT": "04_MATERIALS/Chemicals",
    "COMPOUND": "04_MATERIALS/Chemicals",
    "MATERIAL": "04_MATERIALS/Construction",
    "ALLOY": "04_MATERIALS/Metals/Ferrous",
    "TEXTILE": "04_MATERIALS/Textiles",
    "FUEL": "04_MATERIALS/Energy_Carriers",
    
    # --- 05 INFRASTRUCTURE ---
    "MACHINE": "05_INFRASTRUCTURE/Machines",
    "TOOL": "05_INFRASTRUCTURE/Hand_Tools",
    "ENVIRONMENT": "05_INFRASTRUCTURE/Facilities",
    "FACTORY": "05_INFRASTRUCTURE/Facilities",
    
    # --- 06 PROCESSES ---
    "PROCESS": "06_PROCESSES/Transformation",
    "TECHNIQUE": "06_PROCESSES/Transformation",
    
    # --- 07 ARTIFACTS ---
    "COMPONENT": "07_ARTIFACTS/Standard_Parts",
    "PART": "07_ARTIFACTS/Custom_Parts",
    "ASSEMBLY": "07_ARTIFACTS/Assemblies",
    "PRODUCT": "07_ARTIFACTS/Products",
    "VEHICLE": "07_ARTIFACTS/Products",
    "WEAPON": "07_ARTIFACTS/Products",
    "STRUCTURE": "07_ARTIFACTS/Products",
    "INVENTION": "07_ARTIFACTS/Products",
    
    # --- 08 SOCIETY ---
    "NEED": "08_SOCIETY/Needs",
    "ORDER": "08_SOCIETY/Orders",
    "SOCIETY": "08_SOCIETY/Markets",
    "ORGANIZATION": "08_SOCIETY/Markets",
    "ECONOMY": "08_SOCIETY/Markets",
    "INSTITUTION": "08_SOCIETY/Markets"
}

# 2. КАРТА ЗАВИСИМОСТЕЙ (Как раскидывать родителей по колонкам)
PREFIX_TO_COLUMN = {
    "SCI": "Req_Science", "PHYS": "Req_Science", "MATH": "Req_Science", "BIO": "Req_Science",
    "DES": "Req_Design", "STD": "Req_Design",
    "RES": "Req_Resource", "MIN": "Req_Resource", "CROP": "Req_Resource", "ELEM": "Req_Material", "F": "Req_Resource", "S": "Req_Infrastructure",
    "MAT": "Req_Material", "CHEM": "Req_Material", "FUEL": "Req_Material", "PRIM": "Req_Material",
    "IND": "Req_Infrastructure", "MACH": "Req_Infrastructure", "TOOL": "Req_Infrastructure", "ENV": "Req_Infrastructure",
    "PROC": "Req_Process", "METH": "Req_Process",
    "COMP": "Req_Artifact", "AUTO": "Req_Artifact", "DIG": "Req_Artifact", "MECH": "Req_Artifact", "WAR": "Req_Artifact", "ELEC": "Req_Artifact", "AV": "Req_Artifact",
    "SOC": "Req_Society", "ECON": "Req_Society", "INST": "Req_Society"
}

def parse_parents(parents_str):
    if not parents_str or parents_str == "NULL": return []
    clean = parents_str.replace('[', '').replace(']', '').replace('"', '')
    return [p.strip() for p in clean.split(';') if p.strip()]

def get_destination(row):
    row_type = row['Type'].upper()
    for key, path in DESTINATION_MAP.items():
        if key in row_type:
            return path
    
    # Дополнительные проверки по ID
    row_id = row['ID'].upper()
    if row_id.startswith("BIO-"): return "01_SCIENCE/Biology"
    if row_id.startswith("CHEM-"): return "04_MATERIALS/Chemicals"
    if row_id.startswith("ELEM-"): return "04_MATERIALS/Chemicals"
    if row_id.startswith("AUTO-"): return "07_ARTIFACTS/Custom_Parts"
    if row_id.startswith("SOC-"): return "08_SOCIETY/Markets"
    
    return "07_ARTIFACTS/Standard_Parts"

def migrate():
    print("🚀 Начинаем миграцию в Матричную Структуру...")
    buffer = {}

    # Рекурсивный поиск CSV файлов во всех подпапках data/
    files = glob.glob(os.path.join(SOURCE_DIR, "**/*.csv"), recursive=True)
    
    for fpath in files:
        if "data_v2" in fpath: continue # Игнорируем новую папку если она внутри
        
        print(f"   Reading {os.path.basename(fpath)}...")
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if not row['ID'] or row['ID'].startswith('#'): continue
                    
                    dest_folder = get_destination(row)
                    
                    new_row = {
                        "ID": row['ID'],
                        "Name": row['Name'],
                        "Description": f"{row.get('Trigger', '')} | {row.get('Principle', '')}",
                        "Level": "SPECIFIC",
                        "Parent_Group": "NULL",
                        "Req_Science": [], "Req_Design": [], "Req_Resource": [],
                        "Req_Material": [], "Req_Infrastructure": [], "Req_Process": [],
                        "Req_Artifact": [], "Req_Society": []
                    }
                    
                    parents = parse_parents(row.get('Parents', ''))
                    for p in parents:
                        prefix = p.split('-')[0].upper()
                        target_col = "Req_Artifact"
                        for key, col in PREFIX_TO_COLUMN.items():
                            if prefix == key:
                                target_col = col
                                break
                        new_row[target_col].append(p)
                    
                    for k, v in new_row.items():
                        if isinstance(v, list):
                            new_row[k] = ";".join(v)
                    
                    if dest_folder not in buffer:
                        buffer[dest_folder] = []
                    buffer[dest_folder].append(new_row)
        except Exception as e:
            print(f"⚠️ Ошибка при чтении {fpath}: {e}")

    print("\n💾 Запись в новые папки...")
    headers = OBJ_HEADERS = [
        "ID", "Name", "Description", "Level", "Parent_Group", 
        "Req_Science", "Req_Design", "Req_Resource", "Req_Material", 
        "Req_Infrastructure", "Req_Process", "Req_Artifact", "Req_Society"
    ]

    for folder, rows in buffer.items():
        full_path = os.path.join(DEST_DIR, folder, "index.csv")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        file_exists = os.path.exists(full_path)
        with open(full_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_exists or os.stat(full_path).st_size == 0:
                writer.writeheader()
            writer.writerows(rows)
            print(f"   -> {folder}/index.csv ({len(rows)} items)")

    print("\n✅ Миграция завершена! Проверьте папку data_v2/")

if __name__ == "__main__":
    migrate()