import os
import csv

# Настройка путей
# Мы предполагаем, что скрипт запускается из корня проекта
BASE_DIR = "data_v2"

# 1. Определение Структуры и ID
# Формат: "Путь/К/Папке": ("ID_Узла", "Описание")
TAXONOMY = {
    "01_SCIENCE": ("BASE-SCI", "Fundamental Laws and Knowledge"),
    "01_SCIENCE/Physics": ("DOM-PHYS", "Study of Matter and Energy"),
    "01_SCIENCE/Chemistry": ("DOM-CHEM", "Study of Substances"),
    "01_SCIENCE/Biology": ("DOM-BIO", "Study of Life"),
    "01_SCIENCE/Mathematics": ("DOM-MATH", "Logic and Numbers"),
    "01_SCIENCE/Sociology": ("DOM-SOC", "Study of Society"),
    
    "02_DESIGN": ("BASE-DES", "Information, Standards, and Methods"),
    "02_DESIGN/Standards": ("CAT-STD", "ISO, GOST, DIN Standards"),
    "02_DESIGN/Blueprints": ("CAT-BLUE", "Technical Drawings and Schematics"),
    "02_DESIGN/Methods": ("CAT-METH", "Algorithms and methodologies"),
    
    "03_RESOURCES": ("BASE-RES", "Raw Natural Resources"),
    "03_RESOURCES/Minerals": ("CAT-MIN", "Ores and Stones"),
    "03_RESOURCES/Hydrocarbons": ("CAT-OIL", "Oil, Gas, Coal"),
    "03_RESOURCES/Biosphere": ("CAT-BIO_RES", "Plants and Animals"),
    "03_RESOURCES/Environment": ("CAT-ENV", "Water, Air, Sun"),
    
    "04_MATERIALS": ("BASE-MAT", "Processed Substances"),
    "04_MATERIALS/Metals": ("CAT-METAL", "Conductive hard materials"),
    "04_MATERIALS/Metals/Ferrous": ("GRP-FERROUS", "Iron-based metals"),
    "04_MATERIALS/Metals/NonFerrous": ("GRP-NONFERR", "Copper, Aluminum, etc."),
    "04_MATERIALS/Polymers": ("CAT-POLY", "Plastics and Rubbers"),
    "04_MATERIALS/Chemicals": ("CAT-CHEM", "Acids, Gases, Solvents"),
    "04_MATERIALS/Construction": ("CAT-CONST", "Concrete, Wood, Glass"),
    "04_MATERIALS/Textiles": ("CAT-TEXT", "Fabrics and Leather"),
    "04_MATERIALS/Energy_Carriers": ("CAT-FUEL", "Fuel and Electricity"),
    
    "05_INFRASTRUCTURE": ("BASE-INFRA", "Tools, Machines, and Facilities"),
    "05_INFRASTRUCTURE/Machines": ("CAT-MACH", "Powered manufacturing equipment"),
    "05_INFRASTRUCTURE/Hand_Tools": ("CAT-TOOL", "Manual instruments"),
    "05_INFRASTRUCTURE/Facilities": ("CAT-FAC", "Buildings and Environments"),
    "05_INFRASTRUCTURE/Computing_HW": ("CAT-COMP_HW", "Servers and Computers"),
    
    "06_PROCESSES": ("BASE-PROC", "Actions and Technologies"),
    "06_PROCESSES/Transformation": ("CAT-TRANS", "Changing shape (Cutting, Casting)"),
    "06_PROCESSES/Synthesis": ("CAT-SYNTH", "Chemical/Bio creation"),
    "06_PROCESSES/Assembly": ("CAT-ASSY", "Joining parts"),
    "06_PROCESSES/Logistics": ("CAT-LOG", "Moving things"),
    
    "07_ARTIFACTS": ("BASE-ART", "Engineered Components and Products"),
    "07_ARTIFACTS/Standard_Parts": ("CAT-STD_PART", "Bolts, Bearings, Resistors"),
    "07_ARTIFACTS/Custom_Parts": ("CAT-CUST_PART", "Unique components"),
    "07_ARTIFACTS/Assemblies": ("CAT-ASSY_PART", "Complex nodes (Engines)"),
    "07_ARTIFACTS/Products": ("CAT-PROD", "Finished Goods"),
    
    "08_SOCIETY": ("BASE-SOC", "Social and Economic Context"),
    "08_SOCIETY/Needs": ("CAT-NEED", "Human necessities"),
    "08_SOCIETY/Orders": ("CAT-ORD", "Specific requests"),
    "08_SOCIETY/Markets": ("CAT-MKT", "Economic structures")
}

# Заголовки для объектов (Матричная система)
OBJ_HEADERS = [
    "ID", "Name", "Description", 
    "Level", "Parent_Group", 
    "Req_Science", "Req_Design", "Req_Resource", 
    "Req_Material", "Req_Infrastructure", "Req_Process", 
    "Req_Artifact", "Req_Society"
]

def create_taxonomy():
    print(f"🌳 Создание Таксономии (Папки как Узлы) в {BASE_DIR}...")

    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    for path, (node_id, desc) in TAXONOMY.items():
        # 1. Создаем физический путь
        full_path = os.path.join(BASE_DIR, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        
        # 2. Определяем ID Родителя
        parent_dir = os.path.dirname(path)
        parent_id = "NULL"
        if parent_dir in TAXONOMY:
            parent_id = TAXONOMY[parent_dir][0]
        
        # 3. Создаем _meta.csv (Паспорт папки)
        meta_path = os.path.join(full_path, "_meta.csv")
        with open(meta_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Type", "Parent_ID", "Description"])
            node_name = os.path.basename(path)
            node_type = "BASE" if parent_id == "NULL" else ("CATEGORY" if "CAT-" in node_id else "GROUP")
            writer.writerow([node_id, node_name, node_type, parent_id, desc])
            
        # 4. Если это конечная папка, создаем index.csv для объектов
        is_leaf = True
        for other_path in TAXONOMY.keys():
            if other_path != path and other_path.startswith(path):
                is_leaf = False
                break
        
        if is_leaf:
            index_path = os.path.join(full_path, "index.csv")
            if not os.path.exists(index_path):
                with open(index_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(OBJ_HEADERS)

    print("✅ Таксономия построена. Скелет Графа готов.")

if __name__ == "__main__":
    create_taxonomy()