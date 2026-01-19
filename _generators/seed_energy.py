import os
import csv
import random


# Базовые пути (из таксономии)
BASE_RES = os.path.join("data_v2", "03_RESOURCES", "Hydrocarbons")
PATHS = {
    "OIL": os.path.join(BASE_RES, "Crude_Oil", "index.csv"),
    "COAL": os.path.join(BASE_RES, "Coal", "index.csv"),
    "GAS": os.path.join(BASE_RES, "Natural_Gas", "index.csv")
}


HEADERS = ["ID", "Name", "Description", "Era", "Predecessor_ID", "Status", "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern", "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "Impact_Map", "Properties", "External_Data_Link", "Renewable", "Location", "Extraction_Method", "Reserves_Estimate", "Energy_Density_J_kg", "Scarcity_Score", "Knowledge_Completeness", "Hidden_Potential_Hypothesis"]


# Данные с типами
FUELS = [
    # OIL
    {"type": "OIL", "code": "BRENT", "name": "Brent Crude", "base_j": 45e6, "sulfur": 0.37, "api": 38, "loc": "North Sea"},
    {"type": "OIL", "code": "URALS", "name": "Urals Crude", "base_j": 42e6, "sulfur": 1.30, "api": 31, "loc": "Russia"},
    {"type": "OIL", "code": "WTI", "name": "WTI Crude", "base_j": 46e6, "sulfur": 0.24, "api": 40, "loc": "USA"},
    {"type": "OIL", "code": "ARAB_LIGHT", "name": "Arab Light", "base_j": 44e6, "sulfur": 1.80, "api": 33, "loc": "Saudi Arabia"},
    
    # COAL
    {"type": "COAL", "code": "ANTHRACITE", "name": "Anthracite", "base_j": 32e6, "sulfur": 0.6, "ash": 5, "loc": "China"},
    {"type": "COAL", "code": "BITUMINOUS", "name": "Thermal Coal", "base_j": 24e6, "sulfur": 1.5, "ash": 15, "loc": "Australia"},
    {"type": "COAL", "code": "LIGNITE", "name": "Lignite", "base_j": 15e6, "sulfur": 3.0, "ash": 30, "loc": "Germany"},


    # GAS (Новое!)
    {"type": "GAS", "code": "METHANE", "name": "Natural Gas (Dry)", "base_j": 55e6, "sulfur": 0.0, "co2_factor": 0.5, "loc": "Qatar"},
    {"type": "GAS", "code": "SHALE_GAS", "name": "Shale Gas", "base_j": 53e6, "sulfur": 0.1, "co2_factor": 0.6, "loc": "USA"},
]


def generate_row(fuel, batch_num):
    # Флуктуации
    j_var = random.uniform(0.95, 1.05)
    real_j = int(fuel['base_j'] * j_var)
    
    # Расчет Синтропии
    # Газ (55 МДж) лучше Нефти (45 МДж) лучше Угля (24 МДж).
    # Штраф за серу и золу.
    penalty = 1.0
    if fuel['type'] == "OIL": penalty = 1 + fuel['sulfur']
    if fuel['type'] == "COAL": penalty = 1 + fuel['sulfur'] + (fuel['ash'] / 10.0)
    
    syntropy = round((real_j / 1e7) / penalty, 2)
    
    # Свойства JSON
    props = f"{{'Energy': '{real_j/1e6:.1f} MJ/kg'}}"
    if fuel['type'] == "OIL": props += f", 'Sulfur': '{fuel['sulfur']}%', 'API': '{fuel['api']}'"
    if fuel['type'] == "COAL": props += f", 'Ash': '{fuel['ash']}%', 'Sulfur': '{fuel['sulfur']}%'"
    
    return {
        "ID": f"RES-FUEL_{fuel['code']}_BATCH_{batch_num:03d}",
        "Name": f"{fuel['name']} #{batch_num}",
        "Description": f"{fuel['type']} source from {fuel['loc']}.",
        "Era": "ERA-05_ELECTRICAL",
        "Predecessor_ID": "RES-BIO_ANCIENT_FOREST",
        "Status": "ACTIVE",
        "Syntropy_Score": syntropy,
        "Catalytic_Potential": 50.0 if fuel['type'] == "OIL" else 20.0, # Нефть дает пластик (Катализ!)
        "Structural_Pattern": "HYDROCARBON_CHAIN" if fuel['type'] != "COAL" else "CARBON_MATRIX_IMPURE",
        "Energy_Density_J_kg": real_j,
        "Scarcity_Score": 0.4,
        "Properties": props,
        "Impact_Map": "FAC-POWER:ENABLE:+100;ENV-CLIMATE:DAMAGE:-50",
        "Invention_Reason": "Nature", "Social_Context": "MKT-ENERGY",
        "Drawbacks": "CO2", "Side_Effects": "Warming",
        "External_Data_Link": "NULL", "Renewable": "FALSE",
        "Location": fuel['loc'], "Extraction_Method": "Drilling/Mining",
        "Reserves_Estimate": "Finite", "Knowledge_Completeness": 0.95,
        "Hidden_Potential_Hypothesis": "None"
    }


def main():
    # Буферы для разных файлов
    buffers = {"OIL": [], "COAL": [], "GAS": []}
    
    for fuel in FUELS:
        for i in range(1, 11): # 10 партий
            row = generate_row(fuel, i)
            buffers[fuel['type']].append(row)
            
    # Запись в 3 разных файла
    for ftype, rows in buffers.items():
        path = PATHS[ftype]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)
        print(f"✅ {ftype}: Записано {len(rows)} строк в {path}")


if __name__ == "__main__":
    main()