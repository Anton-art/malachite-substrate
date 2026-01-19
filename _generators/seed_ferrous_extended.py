import os
import csv
import random

# =================================================================================
# НАСТРОЙКИ
# =================================================================================
TARGET_PATH = os.path.join("data_v2", "03_RESOURCES", "Minerals", "Ferrous", "index.csv")

# Полный список заголовков. Теперь он точно совпадает с данными.
HEADERS = [
    "ID", "Name", "Description", 
    "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", 
    "Drawbacks", "Side_Effects", "Impact_Map",
    "Properties", "External_Data_Link",
    "Renewable", "Location", "Extraction_Method", "Reserves_Estimate", 
    "Energy_Density_J_kg", "Scarcity_Score", "Knowledge_Completeness", 
    "Hidden_Potential_Hypothesis", "Potential_Realization_Rate"
]

# =================================================================================
# ГЕОЛОГИЧЕСКИЕ ПРОФИЛИ (HARD FACTS)
# =================================================================================

MINERAL_TYPES = {
    "HEMATITE": {"pattern": "TRIGONAL_HEXAGONAL", "syn_base": 2.0, "desc": "High grade iron oxide (Fe2O3)."},
    "MAGNETITE": {"pattern": "ISOMETRIC_SPINEL", "syn_base": 2.5, "desc": "Magnetic iron oxide (Fe3O4)."},
    "GOETHITE": {"pattern": "ORTHORHOMBIC", "syn_base": 1.0, "desc": "Hydrated iron oxide."},
    "TACONITE": {"pattern": "SEDIMENTARY_BANDED", "syn_base": -1.0, "desc": "Hard rock, requires pelletizing."},
    "CHROMITE": {"pattern": "ISOMETRIC_SPINEL", "syn_base": 3.0, "desc": "Chrome ore."},
    "PYROLUSITE": {"pattern": "TETRAGONAL", "syn_base": 2.0, "desc": "Manganese ore."},
}

# Здесь мы прописываем ХИМИЮ каждого региона
DEPOSITS = [
    # AUSTRALIA (High Alumina issue)
    {"id": "AU_PILBARA", "name": "Pilbara Blend", "type": "HEMATITE", "loc": "Australia", "era": "ERA-06_DIGITAL", 
     "fe_avg": 61.5, "sio2_avg": 4.5, "al2o3_avg": 2.3, "p_avg": 0.08, "scarcity": 0.1},
    
    {"id": "AU_YANDI", "name": "Yandicoogina", "type": "GOETHITE", "loc": "Australia", "era": "ERA-06_DIGITAL", 
     "fe_avg": 58.0, "sio2_avg": 5.0, "al2o3_avg": 1.5, "p_avg": 0.06, "scarcity": 0.1},

    # BRAZIL (Clean, Low Impurities)
    {"id": "BR_CARAJAS", "name": "Carajas IOCG", "type": "HEMATITE", "loc": "Brazil", "era": "ERA-05_ELECTRICAL", 
     "fe_avg": 66.0, "sio2_avg": 1.5, "al2o3_avg": 1.0, "p_avg": 0.04, "scarcity": 0.15},

    # USA (High Silica Taconite)
    {"id": "US_MESABI", "name": "Mesabi Taconite", "type": "TACONITE", "loc": "USA", "era": "ERA-05_ELECTRICAL", 
     "fe_avg": 32.0, "sio2_avg": 45.0, "al2o3_avg": 0.5, "p_avg": 0.02, "scarcity": 0.1},

    # RUSSIA (Magnetite, requires enrichment)
    {"id": "RU_KMA", "name": "Kursk Concentrate", "type": "MAGNETITE", "loc": "Russia", "era": "ERA-05_ELECTRICAL", 
     "fe_avg": 65.0, "sio2_avg": 3.5, "al2o3_avg": 0.2, "p_avg": 0.01, "scarcity": 0.1},

    # AFRICA (Manganese & Chrome)
    {"id": "ZA_KALAHARI", "name": "Kalahari Mn", "type": "PYROLUSITE", "loc": "South Africa", "era": "ERA-04_INDUSTRIAL", 
     "fe_avg": 5.0, "sio2_avg": 4.0, "al2o3_avg": 0.5, "p_avg": 0.1, "scarcity": 0.4}, # Fe тут примесь
     
    {"id": "ZA_BUSHVELD", "name": "Bushveld Cr", "type": "CHROMITE", "loc": "South Africa", "era": "ERA-04_INDUSTRIAL", 
     "fe_avg": 15.0, "sio2_avg": 2.0, "al2o3_avg": 14.0, "p_avg": 0.01, "scarcity": 0.6},

    # SPACE (Pure but expensive)
    {"id": "FUT_PSYCHE", "name": "Asteroid Psyche", "type": "MAGNETITE", "loc": "Space", "era": "ERA-07_INTELLECTUAL", 
     "fe_avg": 90.0, "sio2_avg": 1.0, "al2o3_avg": 0.1, "p_avg": 0.0, "scarcity": 0.9},
]

# =================================================================================
# ЛОГИКА
# =================================================================================

def calculate_syntropy(fe, sio2, al2o3, mineral_base, scarcity, loc):
    # Формула: База + (Железо/10) - (Вредные примеси)
    # Глинозем (Al2O3) вреднее Кремнезема (SiO2) для доменной печи
    score = mineral_base + (fe / 20.0) - (sio2 / 10.0) - (al2o3 / 5.0)
    
    if scarcity > 0.5: score -= 1.0 # Штраф за редкость
    if "Space" in loc: score = -5.0 # Пока недоступно
    
    return round(score, 2)

def generate_rows():
    rows = []
    
    for dep in DEPOSITS:
        mineral = MINERAL_TYPES[dep['type']]
        
        # Генерируем 10 партий для каждого месторождения (Симуляция 10 лет работы)
        batches = 10 if "Space" not in dep['loc'] else 1
        
        for i in range(batches):
            # 1. Симуляция флуктуаций (Геологический шум)
            fe = round(dep['fe_avg'] * random.uniform(0.98, 1.02), 2)
            sio2 = round(dep['sio2_avg'] * random.uniform(0.9, 1.1), 2)
            al2o3 = round(dep['al2o3_avg'] * random.uniform(0.9, 1.1), 2)
            p = round(dep['p_avg'] * random.uniform(0.8, 1.2), 3)
            
            # 2. Расчеты
            syn = calculate_syntropy(fe, sio2, al2o3, mineral['syn_base'], dep['scarcity'], dep['loc'])
            
            # Катализ
            cat = 10.0
            if dep['type'] in ["CHROMITE", "PYROLUSITE"]: cat = 50.0
            if "Space" in dep['loc']: cat = 1000.0

            # 3. Сборка JSON свойств
            main_element = "Fe"
            main_val = fe
            if dep['type'] == "CHROMITE": 
                main_element = "Cr2O3"
                main_val = 42.0 * random.uniform(0.95, 1.05)
            if dep['type'] == "PYROLUSITE":
                main_element = "Mn"
                main_val = 38.0 * random.uniform(0.95, 1.05)

            props = (f"{{'{main_element}': '{main_val:.2f}%', "
                     f"'SiO2': '{sio2}%', 'Al2O3': '{al2o3}%', 'P': '{p}%'}}")

            # 4. Impact Map
            impact = "MAT-STEEL:ENABLE:+10"
            if al2o3 > 2.0: impact += ";FAC-BLAST_FURNACE:DAMAGE:-2"
            if "Space" in dep['loc']: impact = "SOC-EXPANSION:ENABLE:+100"

            row = {
                "ID": f"RES-ORE_{dep['id']}_BATCH_{i+1:02d}",
                "Name": f"{dep['name']} (Batch {2020+i})",
                "Description": f"{mineral['desc']} {dep['loc']}. {main_element}: {main_val:.1f}%.",
                "Era": dep['era'],
                "Predecessor_ID": "NULL",
                "Status": "DORMANT" if "Space" in dep['loc'] else "ACTIVE",
                
                "Syntropy_Score": syn,
                "Catalytic_Potential": cat,
                "Structural_Pattern": mineral['pattern'],
                "Scarcity_Score": dep['scarcity'],
                "Knowledge_Completeness": 0.2 if "Space" in dep['loc'] else 0.99,
                "Potential_Realization_Rate": 0.95,
                "Hidden_Potential_Hypothesis": "None",
                
                "Invention_Reason": "Nature",
                "Social_Context": "MKT-GLOBAL_TRADE",
                "Drawbacks": f"High Alumina" if al2o3 > 2.0 else "None",
                "Side_Effects": "Tailings",
                "Impact_Map": impact,
                
                "Properties": props,
                "External_Data_Link": "NULL",
                
                "Renewable": "FALSE",
                "Location": dep['loc'],
                "Extraction_Method": "Open-pit",
                "Reserves_Estimate": "Huge",
                "Energy_Density_J_kg": 0
            }
            rows.append(row)
            
    return rows

def main():
    if not os.path.exists(os.path.dirname(TARGET_PATH)):
        os.makedirs(os.path.dirname(TARGET_PATH))
        
    print(f"🚀 Генерация ГЕОЛОГИЧЕСКИ ТОЧНОЙ базы руд (v5.1)...")
    data = generate_rows()
    
    # extrasaction='ignore' - это защита от падения, если в row есть лишние поля
    with open(TARGET_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)
        
    print(f"✅ Успешно создано {len(data)} записей.")
    print("   - Данные соответствуют реальным профилям примесей (Al2O3, SiO2, P).")

if __name__ == "__main__":
    main()