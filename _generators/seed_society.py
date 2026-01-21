import os
import csv


BASE_DIR = os.path.join("data_v2", "08_SOCIETY")


PATHS = {
    "NEEDS":   os.path.join(BASE_DIR, "Humanity", "Needs", "index.csv"),
    "MARKETS": os.path.join(BASE_DIR, "Economics", "Markets", "index.csv")
}


HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Target_Group", "Impact_Metric", "Related_Artifacts", "Cultural_Significance",
    "Invention_Reason", "Social_Context", "Impact_Map", "Properties", "External_Data_Link"
]


# Эти ID уже используются в ваших генераторах как Invention_Reason
NEEDS = [
    {"id": "SOC-NEED_SURVIVAL", "name": "Survival", "era": "ERA-01_PRIMITIVE", "desc": "Food, water, shelter."},
    {"id": "SOC-NEED_SAFETY", "name": "Safety & Security", "era": "ERA-01_PRIMITIVE", "desc": "Protection from elements and threats."},
    {"id": "SOC-NEED_MOBILITY", "name": "Mobility", "era": "ERA-02_ENGINEERING", "desc": "Movement of people and goods."},
    {"id": "SOC-NEED_ENERGY", "name": "Energy Access", "era": "ERA-04_INDUSTRIAL", "desc": "Power for machines and heat."},
    {"id": "SOC-NEED_EFFICIENCY", "name": "Efficiency", "era": "ERA-04_INDUSTRIAL", "desc": "Doing more with less."},
    {"id": "SOC-NEED_CONNECTIVITY", "name": "Connectivity", "era": "ERA-05_ELECTRICAL", "desc": "Communication and information flow."},
    {"id": "SOC-NEED_COMPUTATION", "name": "Computation", "era": "ERA-06_DIGITAL", "desc": "Processing data and logic."},
    {"id": "SOC-NEED_INTELLIGENCE", "name": "Artificial Intelligence", "era": "ERA-07_INTELLECTUAL", "desc": "Autonomous cognitive tasks."},
    {"id": "SOC-NEED_EXPANSION", "name": "Space Expansion", "era": "ERA-07_INTELLECTUAL", "desc": "Multi-planetary existence."},
    # Специфические
    {"id": "SOC-NEED_FIXATION", "name": "Mechanical Fixation", "era": "ERA-02_ENGINEERING", "desc": "Holding things together."},
    {"id": "SOC-NEED_STRENGTH", "name": "Structural Strength", "era": "ERA-02_ENGINEERING", "desc": "Load bearing capacity."},
    {"id": "SOC-NEED_CONTROL", "name": "Control Systems", "era": "ERA-05_ELECTRICAL", "desc": "Regulation of flows and energy."}
]


MARKETS = [
    {"id": "MKT-GLOBAL", "name": "Global Market", "era": "ERA-04_INDUSTRIAL"},
    {"id": "MKT-ENERGY", "name": "Energy Market", "era": "ERA-04_INDUSTRIAL"},
    {"id": "MKT-AUTOMOTIVE", "name": "Automotive Market", "era": "ERA-05_ELECTRICAL"},
    {"id": "MKT-ELECTRONICS", "name": "Consumer Electronics", "era": "ERA-06_DIGITAL"},
    {"id": "MKT-CONSTRUCTION", "name": "Construction & Real Estate", "era": "ERA-02_ENGINEERING"},
    {"id": "MKT-AEROSPACE", "name": "Aerospace & Defense", "era": "ERA-06_DIGITAL"},
]


def generate():
    print("🌍 Генерация Общества (Needs & Markets)...")
    
    # 1. Needs
    rows_needs = []
    for n in NEEDS:
        rows_needs.append({
            "ID": n['id'], "Name": n['name'], "Description": n['desc'], "Era": n['era'],
            "Predecessor_ID": "NULL", "Status": "ACTIVE", "Syntropy_Score": 10.0,
            "Catalytic_Potential": 100.0, "Structural_Pattern": "HIERARCHY_NODE",
            "Target_Group": "Humanity", "Impact_Metric": "Quality of Life",
            "Invention_Reason": "EVOLUTION", "Social_Context": "CIVILIZATION",
            "Impact_Map": "NULL", "Properties": "{}", "External_Data_Link": "NULL"
        })
        
    # 2. Markets
    rows_mkts = []
    for m in MARKETS:
        rows_mkts.append({
            "ID": m['id'], "Name": m['name'], "Description": "Economic exchange system.", "Era": m['era'],
            "Predecessor_ID": "MKT-BARTER", "Status": "ACTIVE", "Syntropy_Score": 5.0,
            "Catalytic_Potential": 50.0, "Structural_Pattern": "NETWORK_EXCHANGE",
            "Target_Group": "Corporations", "Impact_Metric": "GDP",
            "Invention_Reason": "SOC-NEED_EFFICIENCY", "Social_Context": "CAPITALISM",
            "Impact_Map": "NULL", "Properties": "{}", "External_Data_Link": "NULL"
        })


    # Запись
    tasks = {"NEEDS": rows_needs, "MARKETS": rows_mkts}
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
            
    print(f"✅ Общество создано: {len(rows_needs)} потребностей, {len(rows_mkts)} рынков.")


if __name__ == "__main__":
    generate()