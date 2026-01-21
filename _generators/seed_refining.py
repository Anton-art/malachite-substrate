import os
import csv
import random


# =================================================================================
# НАСТРОЙКИ
# =================================================================================
BASE_DIR = os.path.join("data_v2", "03_RESOURCES", "Hydrocarbons")
INFRA_DIR = os.path.join("data_v2", "05_INFRASTRUCTURE", "Energy_Grid") # Для электричества


PATHS = {
    "CRUDE":    os.path.join(BASE_DIR, "Crude_Oil", "index.csv"),
    "FUELS":    os.path.join(BASE_DIR, "Refined_Products", "index.csv"),
    "COAL":     os.path.join(BASE_DIR, "Coal", "index.csv"),
    "GAS":      os.path.join(BASE_DIR, "Natural_Gas", "index.csv"),
    "ELECTRIC": os.path.join(INFRA_DIR, "Electricity", "index.csv")
}


HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "Impact_Map", 
    "Properties", "External_Data_Link", "Renewable", "Location", 
    "Extraction_Method", "Reserves_Estimate", "Energy_Density_J_kg", 
    "Scarcity_Score", "Knowledge_Completeness", "Hidden_Potential_Hypothesis", "Potential_Realization_Rate"
]


# =================================================================================
# ДАННЫЕ (СЫРЬЕ)
# =================================================================================


CRUDE_TYPES = [
    {"code": "BRENT", "name": "Brent Crude", "sulfur": 0.37, "api": 38, "loc": "North Sea", "yield_diesel": 0.2, "yield_gas": 0.3},
    {"code": "URALS", "name": "Urals Crude", "sulfur": 1.30, "api": 31, "loc": "Russia", "yield_diesel": 0.3, "yield_gas": 0.2},
    {"code": "WTI",   "name": "WTI Crude",   "sulfur": 0.24, "api": 40, "loc": "USA", "yield_diesel": 0.15, "yield_gas": 0.4},
    {"code": "ARAB_LIGHT", "name": "Arab Light", "sulfur": 1.8, "api": 33, "loc": "Saudi Arabia", "yield_diesel": 0.25, "yield_gas": 0.25}
]


REFINED_PRODUCTS = [
    {"code": "GASOLINE_95", "name": "Gasoline (RON 95)", "j_kg": 46400000, "era": "ERA-05_ELECTRICAL", "app": "Light Vehicles"},
    {"code": "DIESEL_ULSD", "name": "Diesel (ULSD)",     "j_kg": 45600000, "era": "ERA-04_INDUSTRIAL", "app": "Heavy Trucks, Ships"},
    {"code": "KEROSENE_JET_A1", "name": "Jet Fuel A-1",  "j_kg": 43000000, "era": "ERA-05_ELECTRICAL", "app": "Aviation"},
    {"code": "NAPHTHA",     "name": "Naphtha Feedstock", "j_kg": 44000000, "era": "ERA-05_ELECTRICAL", "app": "Plastics Production"},
    {"code": "HEAVY_FUEL_OIL", "name": "Bunker Fuel",    "j_kg": 40000000, "era": "ERA-04_INDUSTRIAL", "app": "Large Ships"},
    {"code": "BITUMEN",     "name": "Bitumen/Asphalt",   "j_kg": 38000000, "era": "ERA-04_INDUSTRIAL", "app": "Roads"}
]


# =================================================================================
# ГЕНЕРАТОРЫ
# =================================================================================


def generate_crude():
    rows = []
    for c in CRUDE_TYPES:
        # Генерируем партии
        for i in range(1, 6):
            real_sulfur = c['sulfur'] * random.uniform(0.9, 1.1)
            syn = round(10.0 / (1 + real_sulfur), 2) # Меньше серы = лучше
            
            rows.append({
                "ID": f"RES-FUEL_OIL_{c['code']}_BATCH_{i:02d}",
                "Name": f"{c['name']} (Batch {i})",
                "Description": f"Crude oil. API: {c['api']}. Sulfur: {real_sulfur:.2f}%.",
                "Era": "ERA-04_INDUSTRIAL",
                "Predecessor_ID": "RES-BIO_ANCIENT_FOREST",
                "Status": "ACTIVE",
                "Syntropy_Score": syn,
                "Catalytic_Potential": 50.0, # Нефть создает цивилизацию
                "Structural_Pattern": "HYDROCARBON_MIX",
                "Invention_Reason": "NATURE",
                "Social_Context": "MKT-ENERGY",
                "Drawbacks": "CO2 Emissions", "Side_Effects": "Geopolitics", 
                "Impact_Map": "PROC-SYN_REFINING:FEED:+100",
                "Properties": f"{{'API': '{c['api']}', 'Sulfur': '{real_sulfur:.2f}%'}}",
                "External_Data_Link": "NULL",
                "Renewable": "FALSE", "Location": c['loc'], "Extraction_Method": "Drilling",
                "Reserves_Estimate": "Finite", "Energy_Density_J_kg": 45000000,
                "Scarcity_Score": 0.4, "Knowledge_Completeness": 0.99,
                "Hidden_Potential_Hypothesis": "None", "Potential_Realization_Rate": 1.0
            })
    return rows


def generate_refined():
    rows = []
    for p in REFINED_PRODUCTS:
        # Синтропия топлива зависит от плотности энергии
        syn = round(p['j_kg'] / 10000000.0, 2)
        
        rows.append({
            "ID": f"RES-FUEL_{p['code']}",
            "Name": p['name'],
            "Description": f"Refined product. Application: {p['app']}.",
            "Era": p['era'],
            "Predecessor_ID": "RES-FUEL_OIL_BRENT", # Ссылка на абстрактную нефть
            "Status": "ACTIVE",
            "Syntropy_Score": syn,
            "Catalytic_Potential": 20.0,
            "Structural_Pattern": "HYDROCARBON_CHAIN",
            "Invention_Reason": "SOC-NEED_MOBILITY",
            "Social_Context": "MKT-COMMODITIES",
            "Drawbacks": "Pollution", "Side_Effects": "None",
            "Impact_Map": f"SOC-LOGISTICS:ENABLE:+100",
            "Properties": f"{{'Energy': '{p['j_kg']} J/kg'}}",
            "External_Data_Link": "NULL",
            "Renewable": "FALSE", "Location": "Refinery", "Extraction_Method": "Distillation",
            "Reserves_Estimate": "Dependent on Crude", "Energy_Density_J_kg": p['j_kg'],
            "Scarcity_Score": 0.1, "Knowledge_Completeness": 1.0,
            "Hidden_Potential_Hypothesis": "None", "Potential_Realization_Rate": 1.0
        })
    return rows


def generate_coal_gas():
    # Упрощенная генерация для угля и газа (чтобы не ломать старые связи)
    rows_coal = []
    rows_gas = []
    
    # Уголь
    rows_coal.append({
        "ID": "RES-COAL_BITUMINOUS", "Name": "Thermal Coal", "Era": "ERA-04_INDUSTRIAL",
        "Syntropy_Score": 2.0, "Catalytic_Potential": 10.0, "Structural_Pattern": "CARBON_MATRIX",
        "Energy_Density_J_kg": 24000000, "Properties": "{'Ash': '10%'}",
        "Predecessor_ID": "RES-BIO_ANCIENT_FOREST", "Status": "ACTIVE",
        "Invention_Reason": "NATURE", "Social_Context": "MKT-ENERGY", "Impact_Map": "FAC-GEN_COAL:BURN:+100",
        "Drawbacks": "High CO2", "Side_Effects": "Smog", "External_Data_Link": "NULL",
        "Renewable": "FALSE", "Location": "Global", "Extraction_Method": "Mining",
        "Reserves_Estimate": "Huge", "Scarcity_Score": 0.1, "Knowledge_Completeness": 1.0,
        "Hidden_Potential_Hypothesis": "None", "Potential_Realization_Rate": 1.0
    })
    
    # Газ
    rows_gas.append({
        "ID": "RES-FUEL_GAS_METHANE", "Name": "Natural Gas (Methane)", "Era": "ERA-05_ELECTRICAL",
        "Syntropy_Score": 5.0, "Catalytic_Potential": 30.0, "Structural_Pattern": "CH4",
        "Energy_Density_J_kg": 55000000, "Properties": "{'Clean': 'Yes'}",
        "Predecessor_ID": "RES-BIO_ANCIENT_FOREST", "Status": "ACTIVE",
        "Invention_Reason": "NATURE", "Social_Context": "MKT-ENERGY", "Impact_Map": "FAC-GEN_GAS:BURN:+100",
        "Drawbacks": "Leaks", "Side_Effects": "Greenhouse Gas", "External_Data_Link": "NULL",
        "Renewable": "FALSE", "Location": "Global", "Extraction_Method": "Drilling",
        "Reserves_Estimate": "Large", "Scarcity_Score": 0.2, "Knowledge_Completeness": 1.0,
        "Hidden_Potential_Hypothesis": "Hydrogen Source", "Potential_Realization_Rate": 1.0
    })
    
    return rows_coal, rows_gas


def main():
    print("🛢️ Генерация Нефтепереработки (Refining Complex)...")
    
    coal, gas = generate_coal_gas()
    
    tasks = {
        "CRUDE": generate_crude(),
        "FUELS": generate_refined(),
        "COAL": coal,
        "GAS": gas
    }
    
    total = 0
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        total += len(data)
            
    print(f"✅ Энергетика обновлена: {total} видов топлива (включая Дизель, Керосин, Нафту).")


if __name__ == "__main__":
    main()