import os
import csv


# =================================================================================
# НАСТРОЙКИ
# =================================================================================
BASE_DIR = os.path.join("data_v2", "00_FOUNDATIONS")


PATHS = {
    "COMMODITIES": os.path.join(BASE_DIR, "Commodities", "index.csv"),
    "LEGACY":      os.path.join(BASE_DIR, "Legacy_Tech", "index.csv"),
    "INFRA_BASE":  os.path.join("data_v2", "05_INFRASTRUCTURE", "Base", "index.csv")
}


HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", "Impact_Map", "Properties", "External_Data_Link"
]

DATA = {
    "COMMODITIES": [
        # --- МЕТАЛЛЫ И ТОПЛИВО ---
        {"id": "RES-ORE_IRON_HEMATITE", "name": "Iron Ore (Generic Hematite)", "era": "ERA-02_ENGINEERING", "desc": "Standard trade grade iron ore."},
        {"id": "RES-ORE_COPPER_SULFIDE", "name": "Copper Ore (Chalcopyrite)", "era": "ERA-01_PRIMITIVE", "desc": "Source of copper and bronze."}, # <--- НОВОЕ (Бронзовый век)
        {"id": "RES-COAL_COKE", "name": "Coking Coal", "era": "ERA-04_INDUSTRIAL", "desc": "Fuel for blast furnaces."},
        {"id": "RES-FUEL_OIL_BRENT", "name": "Crude Oil (Benchmark)", "era": "ERA-05_ELECTRICAL", "desc": "Global oil price benchmark."},
        {"id": "RES-FUEL_GAS_NGL", "name": "Natural Gas Liquids", "era": "ERA-05_ELECTRICAL", "desc": "Feedstock for plastics."},
        
        # --- БИОСФЕРА И АГРО ---
        {"id": "RES-BIO_ANCIENT_FOREST", "name": "Ancient Biomass", "era": "ERA-01_PRIMITIVE", "desc": "Source of fossil fuels."},
        {"id": "MAT-RUBBER_NATURAL", "name": "Natural Rubber", "era": "ERA-04_INDUSTRIAL", "desc": "Harvested latex."},
        {"id": "RES-FIBER_COTTON", "name": "Raw Cotton", "era": "ERA-02_ENGINEERING", "desc": "Basis of early industrialization."}, # <--- НОВОЕ (Текстиль)
        
        # --- СТРОИТЕЛЬСТВО ---
        {"id": "RES-MIN_LIMESTONE", "name": "Limestone", "era": "ERA-01_PRIMITIVE", "desc": "Flux for steel and base for cement."}, # <--- НОВОЕ (Для цемента и стали)

       # --- СИРОТЫ ---
        {"id": "RES-COAL_BITUMINOUS", "name": "Bituminous Coal", "era": "ERA-04_INDUSTRIAL", "desc": "Thermal coal for power plants."},
        {"id": "RES-FUEL_GAS_METHANE", "name": "Methane", "era": "ERA-05_ELECTRICAL", "desc": "Natural gas fuel."},
        {"id": "RES-FUEL_URANIUM", "name": "Uranium-235", "era": "ERA-05_ELECTRICAL", "desc": "Nuclear fuel."},
        {"id": "ENV-SUNLIGHT", "name": "Solar Irradiance", "era": "ERA-01_PRIMITIVE", "desc": "Renewable energy source."},
    ],
    "LEGACY": [
        # --- МЕТАЛЛУРГИЯ ---
        {"id": "MAT-BRONZE_CAST", "name": "Cast Bronze", "era": "ERA-01_PRIMITIVE", "desc": "First alloy of civilization."}, # <--- НОВОЕ
        {"id": "MAT-IRON_PUDDLED", "name": "Puddled Iron", "era": "ERA-03_SCIENTIFIC", "desc": "Wrought iron precursor."},
        
        # --- МЕХАНИКА ---
        {"id": "PART-RIVET", "name": "Industrial Rivet", "era": "ERA-04_INDUSTRIAL", "desc": "Permanent fastener."},
        {"id": "MECH-LOOM", "name": "Power Loom", "era": "ERA-03_SCIENTIFIC", "desc": "First automated machine."}, # <--- НОВОЕ (Предок ЧПУ)
        
        # --- ПРОЦЕССЫ ---
        {"id": "PROC-HAND_CRAFT", "name": "Manual Crafting", "era": "ERA-01_PRIMITIVE", "desc": "Made by hand."},
        {"id": "PROC-MASONRY", "name": "Masonry", "era": "ERA-01_PRIMITIVE", "desc": "Stone and brick laying."}, # <--- НОВОЕ (Строительство)
        
        # --- ЭНЕРГИЯ И ЦЕХА ---
        {"id": "FAC-WORKSHOP_MANUAL", "name": "Manual Workshop", "era": "ERA-02_ENGINEERING", "desc": "Pre-industrial shop."},
        {"id": "FAC-STEAM_ENGINE", "name": "Steam Engine", "era": "ERA-03_SCIENTIFIC", "desc": "First prime mover."},
        {"id": "FAC-WATER_WHEEL", "name": "Water Wheel", "era": "ERA-02_ENGINEERING", "desc": "Renewable mechanical power."}, # <--- НОВОЕ (До пара)

       # --- СИРОТЫ ---
        {"id": "PROC-LOG_ANIMAL_CART", "name": "Animal Transport", "era": "ERA-01_PRIMITIVE", "desc": "Horse and cart logistics."},
        {"id": "PROC-LOG_STORAGE_SIMPLE", "name": "Simple Storage", "era": "ERA-01_PRIMITIVE", "desc": "Barns and cellars."},
    ],
    "INFRA_BASE": [
        {"id": "GRID-AC", "name": "AC Power Grid", "era": "ERA-05_ELECTRICAL", "desc": "Alternating Current distribution."},
        {"id": "GRID-HV", "name": "High Voltage Grid", "era": "ERA-05_ELECTRICAL", "desc": "Industrial power feed."},
        {"id": "LOG-ROAD_DIRT", "name": "Dirt Roads", "era": "ERA-01_PRIMITIVE", "desc": "Basic logistics."}, # <--- НОВОЕ
    ]
}

def generate():
    print("🏛️ Генерация Фундамента (Commodities & Legacy)...")
    for key, items in DATA.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        
        rows = []
        for item in items:
            rows.append({
                "ID": item['id'],
                "Name": item['name'],
                "Description": item['desc'],
                "Era": item['era'],
                "Predecessor_ID": "NULL",
                "Status": "ACTIVE",
                "Syntropy_Score": 1.0,
                "Catalytic_Potential": 5.0,
                "Structural_Pattern": "ROOT_NODE",
                "Invention_Reason": "FOUNDATION",
                "Social_Context": "HISTORY",
                "Impact_Map": "SOC-DEV:ENABLE:+1",
                "Properties": "{}",
                "External_Data_Link": "NULL"
            })
            
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)
            
    print(f"✅ Фундамент заложен ({len(DATA['COMMODITIES']) + len(DATA['LEGACY']) + len(DATA['INFRA_BASE'])} объектов).")


if __name__ == "__main__":
    generate()
