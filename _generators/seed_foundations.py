import os
import csv

BASE_DIR = os.path.join("data_v2", "00_FOUNDATIONS")
PATHS = {
    "COMMODITIES": os.path.join(BASE_DIR, "Commodities", "index.csv"),
    "LEGACY":      os.path.join(BASE_DIR, "Legacy_Tech", "index.csv"),
    "INFRA_BASE":  os.path.join("data_v2", "05_INFRASTRUCTURE", "Base", "index.csv")
}
HEADERS = ["ID", "Name", "Description", "Era", "Predecessor_ID", "Status", "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern", "Invention_Reason", "Social_Context", "Impact_Map", "Properties", "External_Data_Link"]

DATA = {
    "COMMODITIES": [
        {"ID": "RES-ORE_IRON_HEMATITE", "Name": "Iron Ore (Generic)", "Era": "ERA-02_ENGINEERING", "Description": "Standard trade grade iron ore."},
        {"ID": "RES-ORE_COPPER_SULFIDE", "Name": "Copper Ore", "Era": "ERA-01_PRIMITIVE", "Description": "Source of copper."},
        {"ID": "RES-COAL_COKE", "Name": "Coking Coal", "Era": "ERA-04_INDUSTRIAL", "Description": "Fuel for blast furnaces."},
        {"ID": "RES-FUEL_OIL_BRENT", "Name": "Crude Oil (Benchmark)", "Era": "ERA-05_ELECTRICAL", "Description": "Global oil price benchmark."},
        {"ID": "RES-FUEL_GAS_NGL", "Name": "Natural Gas Liquids", "Era": "ERA-05_ELECTRICAL", "Description": "Feedstock for plastics."},
        {"ID": "RES-BIO_ANCIENT_FOREST", "Name": "Ancient Biomass", "Era": "ERA-01_PRIMITIVE", "Description": "Source of fossil fuels."},
        {"ID": "MAT-RUBBER_NATURAL", "Name": "Natural Rubber", "Era": "ERA-04_INDUSTRIAL", "Description": "Harvested latex."},
        {"ID": "RES-FIBER_COTTON", "Name": "Raw Cotton", "Era": "ERA-02_ENGINEERING", "Description": "Textile basis."},
        {"ID": "RES-MIN_LIMESTONE", "Name": "Limestone", "Era": "ERA-01_PRIMITIVE", "Description": "Flux and cement base."},
        {"ID": "RES-MIN_SILICA", "Name": "Silica Sand", "Era": "ERA-01_PRIMITIVE", "Description": "Glass and silicon base."},
        {"ID": "RES-MIN_BAUXITE", "Name": "Bauxite", "Era": "ERA-02_ENGINEERING", "Description": "Aluminum ore."},
        {"ID": "RES-FUEL_URANIUM", "Name": "Uranium-235", "Era": "ERA-05_ELECTRICAL", "Description": "Nuclear fuel."},
        {"ID": "ENV-SUNLIGHT", "Name": "Solar Irradiance", "Era": "ERA-01_PRIMITIVE", "Description": "Renewable energy source."},
        # НОВЫЕ ДОБАВЛЕНИЯ:
        {"ID": "MAT-AL_6061_T6", "Name": "Aluminum 6061-T6", "Era": "ERA-05_ELECTRICAL", "Description": "Structural aluminum alloy."},
        {"ID": "MAT-RUBBER_SYNTHETIC", "Name": "Synthetic Rubber", "Era": "ERA-04_INDUSTRIAL", "Description": "Petrochemical elastomer."},
        {"ID": "PART-TRANSISTOR_MOSFET", "Name": "Discrete MOSFET", "Era": "ERA-05_ELECTRICAL", "Description": "Basic transistor."},
        {"ID": "MAT-CER_CLAY_BRICK", "Name": "Clay Brick", "Era": "ERA-01_PRIMITIVE", "Description": "Fired clay."},
        {"ID": "MAT-CER_SILICON_CARBIDE", "Name": "Silicon Carbide", "Era": "ERA-06_DIGITAL", "Description": "Hard ceramic."},
        {"ID": "MAT-STL_52100_VAC_ARC", "Name": "Bearing Steel 52100", "Era": "ERA-04_INDUSTRIAL", "Description": "High hardness steel."},
    ],
    "LEGACY": [
        {"ID": "MAT-BRONZE_CAST", "Name": "Cast Bronze", "Era": "ERA-01_PRIMITIVE", "Description": "First alloy."},
        {"ID": "MAT-IRON_PUDDLED", "Name": "Puddled Iron", "Era": "ERA-03_SCIENTIFIC", "Description": "Wrought iron precursor."},
        {"ID": "PART-RIVET", "Name": "Industrial Rivet", "Era": "ERA-04_INDUSTRIAL", "Description": "Permanent fastener."},
        {"ID": "MECH-LOOM", "Name": "Power Loom", "Era": "ERA-03_SCIENTIFIC", "Description": "First automated machine."},
        {"ID": "PROC-HAND_CRAFT", "Name": "Manual Crafting", "Era": "ERA-01_PRIMITIVE", "Description": "Made by hand."},
        {"ID": "PROC-MASONRY", "Name": "Masonry", "Era": "ERA-01_PRIMITIVE", "Description": "Stone work."},
        {"ID": "FAC-WORKSHOP_MANUAL", "Name": "Manual Workshop", "Era": "ERA-02_ENGINEERING", "Description": "Pre-industrial shop."},
        {"ID": "FAC-STEAM_ENGINE", "Name": "Steam Engine", "Era": "ERA-03_SCIENTIFIC", "Description": "First prime mover."},
        {"ID": "FAC-WATER_WHEEL", "Name": "Water Wheel", "Era": "ERA-02_ENGINEERING", "Description": "Renewable power."},
        {"ID": "PROC-LOG_ANIMAL_CART", "Name": "Animal Transport", "Era": "ERA-01_PRIMITIVE", "Description": "Horse and cart."},
        {"ID": "PROC-LOG_STORAGE_SIMPLE", "Name": "Simple Storage", "Era": "ERA-01_PRIMITIVE", "Description": "Barns."},
        {"ID": "PART-RES_AXIAL", "Name": "Axial Resistor (Legacy)", "Era": "ERA-05_ELECTRICAL", "Description": "Old style component."},
        {"ID": "MAT-LEATHER_GASKET", "Name": "Leather Gasket", "Era": "ERA-02_ENGINEERING", "Description": "Precursor to O-Rings."},
        {"ID": "PART-WHEEL_WOODEN", "Name": "Wooden Wheel", "Era": "ERA-01_PRIMITIVE", "Description": "The original wheel."},
        {"ID": "PART-BEAM_WOODEN", "Name": "Wooden Beam", "Era": "ERA-01_PRIMITIVE", "Description": "Structural timber."},
        {"ID": "PART-GEAR_WOODEN", "Name": "Wooden Gear", "Era": "ERA-02_ENGINEERING", "Description": "Mill gear."},
        {"ID": "PART-BUSHING_BRONZE", "Name": "Bronze Bushing", "Era": "ERA-02_ENGINEERING", "Description": "Precursor to bearings."},
    ],
    "INFRA_BASE": [
        {"ID": "GRID-AC", "Name": "AC Power Grid", "Era": "ERA-05_ELECTRICAL", "Description": "Standard grid."},
        {"ID": "GRID-HV", "Name": "High Voltage Grid", "Era": "ERA-05_ELECTRICAL", "Description": "Industrial grid."},
        {"ID": "LOG-ROAD_DIRT", "Name": "Dirt Roads", "Era": "ERA-01_PRIMITIVE", "Description": "Basic logistics."},
    ]
}

def generate():
    print("🏛️ Генерация Фундамента (Commodities & Legacy)...")
    for key, items in DATA.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        try:
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(items)
            print(f"   - {key}: Записано {len(items)} объектов.")
        except Exception as e:
            print(f"❌ ОШИБКА записи {key}: {e}")
    print(f"✅ Фундамент успешно заложен.")

if __name__ == "__main__":
    generate()
