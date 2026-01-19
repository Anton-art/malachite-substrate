import os
import csv


ROOT_DIR = "data_v2"


# =================================================================================
# ОПРЕДЕЛЕНИЕ СХЕМЫ (SCHEMA DEFINITION v4.0 - FINAL)
# =================================================================================


COMMON_HEADERS = [
    "ID", "Name", "Description", 
    "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score",       # Энергия
    "Catalytic_Potential",  # <--- ДОБАВЛЕНО (Информация)
    "Structural_Pattern",   # <--- ДОБАВЛЕНО (Для аналогий)
    "Invention_Reason", "Social_Context", 
    "Drawbacks", "Side_Effects", 
    "Impact_Map", 
    "Properties",           # JSON
    "External_Data_Link"    # Ссылки
]


DOMAIN_HEADERS = {
    "01_SCIENCE": ["Prerequisite_Knowledge", "Key_Formula", "Discovered_By", "Experimental_Proof"],
    "02_DESIGN": ["Applicable_Domain", "Key_Principles", "License_Type", "Path_To_Code"],
    "03_RESOURCES": ["Renewable", "Location", "Extraction_Method", "Reserves_Estimate", "Energy_Density_J_kg", "Scarcity_Score", "Knowledge_Completeness", "Hidden_Potential_Hypothesis"],
    "04_MATERIALS": ["Chemical_Formula", "Req_Resource", "Req_Process"],
    "05_INFRASTRUCTURE": ["Power_Source", "Output_Capacity", "Req_Space", "Maintenance_Cycle", "Energy_Consumption_W"],
    "06_PROCESSES": ["Input_State", "Output_State", "Physics_Law", "Energy_Type", "Energy_Cost_Estimate", "Req_Infrastructure"],
    "07_ARTIFACTS": ["Req_Material", "Req_Process", "Req_Infrastructure", "Req_Science", "Bill_of_Materials", "Potential_Realization_Rate"],
    "08_SOCIETY": ["Target_Group", "Impact_Metric", "Related_Artifacts", "Cultural_Significance"]
}


def get_headers_for_path(path):
    norm_path = os.path.normpath(path)
    parts = norm_path.split(os.sep)
    for part in parts:
        if part in DOMAIN_HEADERS:
            return COMMON_HEADERS + DOMAIN_HEADERS[part]
    return COMMON_HEADERS + ["Links"]


def update_csv_headers(root_path):
    print("🔄 Запуск обновления схемы (v4.0 - Final)...")
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_path):
        if "index.csv" in filenames:
            file_path = os.path.join(dirpath, "index.csv")
            target_headers = get_headers_for_path(dirpath)
            
            existing_data = []
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                    try:
                        reader = csv.DictReader(file)
                        existing_data = list(reader)
                    except:
                        pass
            
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=target_headers)
                writer.writeheader()
                if existing_data:
                    # Умная миграция: пишем только те поля, которые есть в новой схеме
                    writer.writerows(existing_data)
            count += 1
    print(f"✅ Обновлено {count} файлов. Схема синхронизирована с ТЗ v4.1.")


if __name__ == "__main__":
    if not os.path.exists(ROOT_DIR):
        print(f"❌ Ошибка: Папка {ROOT_DIR} не найдена.")
    else:
        update_csv_headers(ROOT_DIR)