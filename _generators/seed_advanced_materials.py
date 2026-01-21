import os
import csv
import random

BASE_DIR = os.path.join("data_v2", "04_MATERIALS")

PATHS = {
    "POLYMERS_COMMODITY":   os.path.join(BASE_DIR, "Polymers", "Commodity", "index.csv"),
    "POLYMERS_ENGINEERING": os.path.join(BASE_DIR, "Polymers", "Engineering", "index.csv"),
    "ELASTOMERS":           os.path.join(BASE_DIR, "Polymers", "Elastomers", "index.csv"),
    "COMPOSITES":           os.path.join(BASE_DIR, "Composites", "index.csv"),
    "CERAMICS_TECH":        os.path.join(BASE_DIR, "Ceramics", "Technical", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Properties", "Chemical_Formula", "Req_Resource", "Req_Process", 
    "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", 
    "Impact_Map", "External_Data_Link"
]

# 1. МАССОВЫЕ ПЛАСТИКИ
COMMODITY_RESINS = [
    {"code": "PE_HD", "name": "HDPE", "density": 0.95, "feed": "RES-FUEL_GAS_NGL", "era": "ERA-05_ELECTRICAL", "desc": "High density polyethylene. Pipes, containers."},
    {"code": "PP_HOMO", "name": "Polypropylene", "density": 0.90, "feed": "RES-FUEL_GAS_NGL", "era": "ERA-05_ELECTRICAL", "desc": "Fatigue resistant. Hinges, bumpers."},
    {"code": "PVC_RIGID", "name": "PVC (Rigid)", "density": 1.40, "feed": "RES-FUEL_GAS_NGL", "era": "ERA-04_INDUSTRIAL", "desc": "Construction pipes, profiles."},
    {"code": "PS_GP", "name": "Polystyrene", "density": 1.05, "feed": "RES-FUEL_NAPHTHA", "era": "ERA-05_ELECTRICAL", "desc": "Brittle, clear. Packaging."},
]

# 2. ИНЖЕНЕРНЫЕ ПЛАСТИКИ
ENGINEERING_RESINS = [
    {"code": "PA66", "name": "Nylon 66", "temp": 260, "feed": "RES-FUEL_NAPHTHA", "era": "ERA-05_ELECTRICAL", "desc": "High strength, low friction. Gears."},
    {"code": "PC_OPT", "name": "Polycarbonate", "temp": 150, "feed": "RES-FUEL_NAPHTHA", "era": "ERA-05_ELECTRICAL", "desc": "Impact resistant, transparent. Lenses."},
    {"code": "PEEK", "name": "PEEK", "temp": 340, "feed": "RES-FUEL_NAPHTHA", "era": "ERA-06_DIGITAL", "desc": "Ultra-performance. Aerospace replacement for metal."},
    {"code": "ABS_HI", "name": "ABS", "temp": 105, "feed": "RES-FUEL_NAPHTHA", "era": "ERA-05_ELECTRICAL", "desc": "Tough, shiny. Consumer electronics housings."},
]

# 3. ЭЛАСТОМЕРЫ
ELASTOMERS = [
    {"code": "RUBBER_NBR", "name": "Nitrile Rubber (NBR)", "app": "Oil Seals", "era": "ERA-04_INDUSTRIAL"},
    {"code": "RUBBER_EPDM", "name": "EPDM Rubber", "app": "Weather Seals", "era": "ERA-05_ELECTRICAL"},
    {"code": "SILICONE", "name": "Silicone Rubber", "app": "High Temp/Medical", "era": "ERA-05_ELECTRICAL"},
]

# 4. КОМПОЗИТЫ
COMPOSITES = [
    {"code": "FR4_EPOXY", "name": "FR-4 (Glass/Epoxy)", "mat": "Epoxy + Glass Fiber", "era": "ERA-05_ELECTRICAL", "desc": "Standard PCB substrate."},
    {"code": "CFRP_AERO", "name": "Carbon Fiber (Aerospace)", "mat": "Epoxy + Carbon", "era": "ERA-06_DIGITAL", "desc": "High strength-to-weight ratio."},
    {"code": "GFRP_STRUCT", "name": "Fiberglass (Structural)", "mat": "Polyester + Glass", "era": "ERA-05_ELECTRICAL", "desc": "Boat hulls, tanks."},
]

# 5. ТЕХНИЧЕСКАЯ КЕРАМИКА
CERAMICS = [
    {"code": "ALUMINA_96", "name": "Alumina 96% (Al2O3)", "prop": "Insulator", "era": "ERA-05_ELECTRICAL", "desc": "Chip substrates, spark plugs."},
    {"code": "SILICON_CARBIDE", "name": "Silicon Carbide (SiC)", "prop": "Hardness/Heat", "era": "ERA-06_DIGITAL", "desc": "Brakes, armor, semiconductors."},
    {"code": "ZIRCONIA_TZP", "name": "Zirconia (TZP)", "prop": "Toughness", "era": "ERA-06_DIGITAL", "desc": "Dental, knives, bearings."},
]

def generate_polymers(source_list, category_type):
    rows = []
    for p in source_list:
        base_syn = 2.0 if category_type == "ENG" else 1.0
        if p['code'] == "PEEK": base_syn = 5.0
        
        row = {
            "ID": f"MAT-POLY_{p['code']}",
            "Name": p['name'],
            "Description": p['desc'],
            "Era": p['era'],
            "Predecessor_ID": "MAT-RUBBER_NATURAL",
            "Status": "ACTIVE",
            "Syntropy_Score": base_syn,
            "Catalytic_Potential": 10.0 * base_syn,
            "Structural_Pattern": "POLYMER_CHAIN",
            "Properties": f"{{'Feedstock': '{p['feed']}'}}",
            "Chemical_Formula": "C-H Chain",
            "Req_Resource": p['feed'],
            "Req_Process": "PROC-SYN_POLYMERIZATION_STANDARD",
            "Invention_Reason": "SOC-NEED_LIGHTWEIGHT",
            "Social_Context": "MKT-MATERIALS",
            "Drawbacks": "Microplastics", "Side_Effects": "Ocean Pollution",
            "Impact_Map": "FAC-MFG_PLASTIC:FEED:+10",
            "External_Data_Link": "NULL"
        }
        rows.append(row)
    return rows

def generate_elastomers():
    rows = []
    for e in ELASTOMERS:
        row = {
            "ID": f"MAT-ELAST_{e['code']}",
            "Name": e['name'],
            "Description": f"Elastomer for {e['app']}.",
            "Era": e['era'],
            "Predecessor_ID": "MAT-RUBBER_NATURAL",
            "Status": "ACTIVE",
            "Syntropy_Score": 3.0,
            "Catalytic_Potential": 5.0,
            "Structural_Pattern": "CROSS_LINKED_NET",
            "Properties": "{'Elasticity': 'High'}",
            "Chemical_Formula": "Polymer",
            "Req_Resource": "RES-FUEL_NAPHTHA",
            "Req_Process": "PROC-SYN_POLYMERIZATION_STANDARD",
            "Invention_Reason": "SOC-NEED_SEALING",
            "Social_Context": "MKT-AUTO",
            "Drawbacks": "Aging", "Side_Effects": "None",
            "Impact_Map": "PART-SEAL_ORING:MAKE:+100",
            "External_Data_Link": "NULL"
        }
        rows.append(row)
    return rows

def generate_composites():
    rows = []
    for c in COMPOSITES:
        row = {
            "ID": f"MAT-COMP_{c['code']}",
            "Name": c['name'],
            "Description": c['desc'],
            "Era": c['era'],
            "Predecessor_ID": "MAT-STL_1010_HR_US__001",
            "Status": "ACTIVE",
            "Syntropy_Score": 8.0,
            "Catalytic_Potential": 50.0,
            "Structural_Pattern": "FIBER_MATRIX",
            "Properties": f"{{'Matrix': '{c['mat']}'}}",
            "Chemical_Formula": "Composite",
            "Req_Resource": "RES-FUEL_NAPHTHA;RES-MIN_SILICA",
            # ИСПРАВЛЕНО: Добавлен суффикс _STANDARD
            "Req_Process": "PROC-MOLD_COMPOSITE_LAYUP_STANDARD", 
            "Invention_Reason": "SOC-NEED_PERFORMANCE",
            "Social_Context": "MKT-AEROSPACE",
            "Drawbacks": "Hard to Recycle", "Side_Effects": "None",
            "Impact_Map": "ASSY-AIRCRAFT:ENABLE:+100",
            "External_Data_Link": "NULL"
        }
        rows.append(row)
    return rows

def generate_ceramics():
    rows = []
    for c in CERAMICS:
        row = {
            "ID": f"MAT-CER_{c['code']}",
            "Name": c['name'],
            "Description": c['desc'],
            "Era": c['era'],
            "Predecessor_ID": "MAT-CER_CLAY_BRICK",
            "Status": "ACTIVE",
            "Syntropy_Score": 6.0,
            "Catalytic_Potential": 100.0,
            "Structural_Pattern": "CRYSTAL_IONIC",
            "Properties": f"{{'Key_Prop': '{c['prop']}'}}",
            "Chemical_Formula": c['code'].split('_')[0],
            "Req_Resource": "RES-MIN_BAUXITE" if "ALUMINA" in c['code'] else "RES-MIN_SILICA",
            # ИСПРАВЛЕНО: SYN -> TRE (так как Sintering в Treatment)
            "Req_Process": "PROC-TRE_SINTERING_STANDARD", 
            "Invention_Reason": "SOC-NEED_HEAT_RESISTANCE",
            "Social_Context": "MKT-TECH",
            "Drawbacks": "Brittle", "Side_Effects": "High Energy Cost",
            "Impact_Map": "PART-IC_PKG:ENABLE:+100",
            "External_Data_Link": "NULL"
        }
        rows.append(row)
    return rows

def main():
    print("🧪 Генерация Продвинутых Материалов (Polymers, Composites, Ceramics)...")
    tasks = {
        "POLYMERS_COMMODITY": generate_polymers(COMMODITY_RESINS, "COM"),
        "POLYMERS_ENGINEERING": generate_polymers(ENGINEERING_RESINS, "ENG"),
        "ELASTOMERS": generate_elastomers(),
        "COMPOSITES": generate_composites(),
        "CERAMICS_TECH": generate_ceramics()
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
    print(f"✅ Материалы v2.0: Создано {total} видов.")

if __name__ == "__main__":
    main()