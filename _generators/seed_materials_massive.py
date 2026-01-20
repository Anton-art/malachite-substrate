import os
import csv
import random


# Целевая папка
TARGET_DIR = os.path.join("data_v2", "04_MATERIALS", "Metals", "Ferrous", "Carbon_Steels")
TARGET_FILE = os.path.join(TARGET_DIR, "index.csv")


# Заголовки (v4.0)
HEADERS = [
    "ID", "Name", "Description", 
    "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", 
    "Drawbacks", "Side_Effects", "Impact_Map",
    "Properties", "External_Data_Link",
    "Chemical_Formula", "Req_Resource", "Req_Process"
]


# База марок
BASE_GRADES = [
    {"code": "1010", "c": 0.10, "app": "Auto bodies", "base_yield": 180},
    {"code": "1018", "c": 0.18, "app": "Shafts", "base_yield": 310},
    {"code": "1020", "c": 0.20, "app": "General", "base_yield": 295},
    {"code": "1030", "c": 0.30, "app": "Machinery", "base_yield": 340},
    {"code": "1040", "c": 0.40, "app": "Crankshafts", "base_yield": 415},
    {"code": "1045", "c": 0.45, "app": "Gears", "base_yield": 450},
    {"code": "1050", "c": 0.50, "app": "Springs", "base_yield": 490},
    {"code": "1060", "c": 0.60, "app": "Blades", "base_yield": 540},
    {"code": "1080", "c": 0.80, "app": "Wire", "base_yield": 580},
    {"code": "1095", "c": 0.95, "app": "Knives", "base_yield": 600},
]


# Обработка
CONDITIONS = [
    {"suffix": "HR", "name": "Hot Rolled", "yield_mod": 1.0, "energy_cost": 1.0},
    {"suffix": "CD", "name": "Cold Drawn", "yield_mod": 1.2, "energy_cost": 1.4},
    {"suffix": "ANN", "name": "Annealed", "yield_mod": 0.8, "energy_cost": 1.2},
    {"suffix": "NORM", "name": "Normalized", "yield_mod": 1.1, "energy_cost": 1.3},
    {"suffix": "Q_T", "name": "Quenched & Tempered", "yield_mod": 1.5, "energy_cost": 2.2},
]


MANUFACTURERS = ["US_Steel", "ArcelorMittal", "Nippon", "Baowu", "POSCO", "Tata", "Thyssen", "Nucor", "Severstal", "JFE"]


def generate_row(grade, cond, mfg, index):
    unique_id = f"MAT-STL_{grade['code']}_{cond['suffix']}_{mfg[:3].upper()}_{index:03d}"
    
    # Физика
    yield_strength = int(grade['base_yield'] * cond['yield_mod'] * random.uniform(0.98, 1.02))
    tensile = int(yield_strength * 1.5)
    hardness = int(yield_strength / 3.2)
    
    props = (f"{{'Yield': '{yield_strength} MPa', 'Tensile': '{tensile} MPa', "
             f"'Hardness': 'HB {hardness}', 'Density': '7.85 g/cm3'}}")


    # --- РАСЧЕТ СИНТРОПИИ ---
    # Мы поощряем высокую прочность, так как она позволяет делать детали легче (экономия материи).
    # Формула: (Прочность^1.1) / Энергия. Нелинейность дает бонус качеству.
    benefit = (yield_strength / 100.0) ** 1.1
    cost = cond['energy_cost']
    syntropy = round(benefit / cost, 2)


    # --- РАСЧЕТ КАТАЛИЗА ---
    catalytic = 5.0
    if grade['c'] > 0.6: catalytic += 10.0 # Инструменты создают другие вещи
    if cond['suffix'] == "CD": catalytic += 5.0 # Точность важна для машин
    if cond['suffix'] == "Q_T": catalytic += 8.0 # Высоконагруженные узлы


    # --- ПАТТЕРН (Исправленная логика) ---
    # Определяем микроструктуру на основе обработки и углерода
    if cond['suffix'] == "Q_T":
        pattern = "MICROSTRUCTURE_MARTENSITE_TEMPERED" # Самая прочная
    elif cond['suffix'] == "ANN":
        pattern = "MICROSTRUCTURE_SPHEROIDITE" # Самая мягкая
    elif cond['suffix'] == "NORM":
        pattern = "MICROSTRUCTURE_FINE_PEARLITE"
    elif grade['c'] > 0.8:
        pattern = "MICROSTRUCTURE_PEARLITE_CEMENTITE" # Хрупкая, твердая
    else:
        pattern = "MICROSTRUCTURE_FERRITE_PEARLITE" # Стандартная


    return {
        "ID": unique_id,
        "Name": f"AISI {grade['code']} - {cond['name']} ({mfg})",
        "Description": f"Carbon steel {grade['c']}% C. {cond['name']}.",
        "Era": "ERA-04_INDUSTRIAL",
        "Predecessor_ID": "MAT-IRON_PUDDLED",
        "Status": "ACTIVE",
        "Syntropy_Score": syntropy,
        "Catalytic_Potential": catalytic,
        "Structural_Pattern": pattern,
        "Invention_Reason": "SOC-NEED_STRENGTH",
        "Social_Context": "MKT-GLOBAL_CONSTRUCTION",
        "Drawbacks": "Rusts; Heavy",
        "Side_Effects": "CO2 emissions",
        "Impact_Map": "FAC-MACHINERY:ENABLE:+10",
        "Properties": props,
        "External_Data_Link": "NULL",
        "Chemical_Formula": f"Fe, C:{grade['c']}%, Mn:0.6%",
        "Req_Resource": "RES-ORE_IRON_HEMATITE;RES-COAL_COKE",
        "Req_Process": "PROC-MET_SMELTING_BF_STANDARD"
    }


def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)


    print("🚀 Генерация стали (v4.1 Fixed Logic)...")
    rows = []
    for grade in BASE_GRADES:
        for cond in CONDITIONS:
            for mfg in MANUFACTURERS:
                for batch in range(1, 3): 
                    rows.append(generate_row(grade, cond, mfg, batch))


    with open(TARGET_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)


    print(f"✅ Создано {len(rows)} строк в {TARGET_FILE}")


if __name__ == "__main__":
    main()