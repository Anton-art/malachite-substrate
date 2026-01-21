import os
import csv
import random

# =================================================================================
# НАСТРОЙКИ
# =================================================================================
BASE_DIR = os.path.join("data_v2", "07_ARTIFACTS", "Assemblies")

PATHS = {
    "MECHANICAL": os.path.join(BASE_DIR, "Mechanical_Systems", "index.csv"),
    "ELECTRONIC": os.path.join(BASE_DIR, "Electronic_Systems", "index.csv"),
    "VEHICLES":   os.path.join(BASE_DIR, "Vehicles", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Properties", "Req_Material", "Req_Process", "Impact_Map", 
    "Invention_Reason", "Social_Context", "Bill_of_Materials", "Potential_Realization_Rate"
]

# =================================================================================
# КОНСТРУКТОРСКОЕ БЮРО (LOGIC CORES)
# =================================================================================

class EngineeringBureau:
    def __init__(self):
        self.buffer = []

    def create_artifact(self, category, code, name, era, desc, bom_dict, process, pattern, syn_bonus=1.0):
        # Формируем BOM строку
        bom_str = ";".join([f"{k}:{v}" for k, v in bom_dict.items()])
        
        base_syn = 5.0 * syn_bonus
        
        row = {
            "ID": code,
            "Name": name,
            "Description": desc,
            "Era": era,
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": round(base_syn, 2),
            "Catalytic_Potential": 50.0 * syn_bonus,
            "Structural_Pattern": pattern,
            "Properties": "{}",
            "Req_Material": "NULL",
            "Req_Process": process,
            "Impact_Map": "SOC-STANDARD_OF_LIVING:RAISE:+10",
            "Invention_Reason": "SOC-NEED_COMPLEXITY",
            "Social_Context": "MKT-GLOBAL",
            "Bill_of_Materials": bom_str,
            "Potential_Realization_Rate": 0.95
        }
        self.buffer.append((category, row))
        return code

# =================================================================================
# ГЕНЕРАТОРЫ СИСТЕМ
# =================================================================================

def build_powertrains(bureau):
    # --- УРОВЕНЬ 3: УЗЛЫ ---
    piston_id = bureau.create_artifact(
        "MECHANICAL", "ASSY-SUB_PISTON_GROUP", "Piston Group (Steel)", "ERA-04_INDUSTRIAL",
        "Piston, rings, pin and connecting rod.",
        {
            "MAT-STL_1045_HR_US__001": 2,   
            "PART-BOLT_HEX_M8x40_88": 2     
        }, 
        "PROC-ASS_MANUAL_STANDARD", "MECHANICAL_LINKAGE"
    )

    # --- УРОВЕНЬ 4: АГРЕГАТЫ ---
    engines = [
        {"cyl": 4, "name": "Inline-4 Engine", "power": "150HP"},
        {"cyl": 8, "name": "V8 Engine", "power": "400HP"},
        {"cyl": 12, "name": "V12 Engine", "power": "700HP"}
    ]

    engine_ids = []
    for e in engines:
        bolts_needed = e['cyl'] * 10 
        
        e_id = bureau.create_artifact(
            "MECHANICAL", f"ASSY-UNIT_ICE_{e['cyl']}CYL", e['name'], "ERA-05_ELECTRICAL",
            f"Internal Combustion Engine. {e['power']}.",
            {
                piston_id: e['cyl'],
                "MAT-STL_1045_HR_US__001": 50, 
                "PART-BOLT_HEX_M8x40_88": bolts_needed 
            },
            "PROC-ASS_HEAVY_STANDARD", "POWER_SOURCE", syn_bonus=2.0
        )
        engine_ids.append(e_id)
    
    return engine_ids

def build_computers(bureau):
    # --- УРОВЕНЬ 3: ПЛАТЫ ---
    motherboard_id = bureau.create_artifact(
        "ELECTRONIC", "ASSY-SUB_MOTHERBOARD_ATX", "ATX Motherboard", "ERA-06_DIGITAL",
        "Main circuit board with chipset.",
        {
            "ASSY-CPU_x86_14NM": 1, 
            "PART-RES_0402_10kOHM": 120,
            "PART-RES_0603_1kOHM": 50      
        },
        "PROC-ASS_PRECISION_STANDARD", "CIRCUIT_LOGIC", syn_bonus=5.0
    )

    # --- УРОВЕНЬ 4: СЕРВЕРЫ ---
    server_id = bureau.create_artifact(
        "ELECTRONIC", "ASSY-UNIT_SERVER_RACKMOUNT", "1U Server Node", "ERA-06_DIGITAL",
        "High density compute node.",
        {
            motherboard_id: 1,
            "PART-CASE_STEEL_1U": 1        
        },
        "PROC-ASS_PRECISION_STANDARD", "COMPUTE_NODE", syn_bonus=10.0
    )
    return server_id

def build_vehicles(bureau, engine_ids):
    # --- УРОВЕНЬ 5: ИЗДЕЛИЯ ---
    # Ищем ID двигателя V8 в списке созданных
    try:
        v8_id = next(e for e in engine_ids if "8CYL" in e)
    except StopIteration:
        print("⚠️ ОШИБКА: Двигатель V8 не найден. Пропускаем создание грузовика.")
        return

    bureau.create_artifact(
        "VEHICLES", "PROD-VEH_TRUCK_HEAVY", "Heavy Duty Truck", "ERA-05_ELECTRICAL",
        "Logistics transport vehicle.",
        {
            v8_id: 1,
            "ASSY-UNIT_CHASSIS_STEEL": 1, 
            "PART-WHEEL_TRUCK": 6         
        },
        "PROC-ASS_HEAVY_STANDARD", "TRANSPORT_SYSTEM", syn_bonus=20.0
    )

# =================================================================================
# MAIN
# =================================================================================

def main():
    print("🏗️ Запуск Конструкторского Бюро (Parametric Assembly)...")
    bureau = EngineeringBureau()
    
    # 1. Строим двигатели и ЗАПОМИНАЕМ их ID
    engine_ids = build_powertrains(bureau)
    
    # 2. Строим компьютеры
    build_computers(bureau) 
    
    # 3. Строим машины, ПЕРЕДАВАЯ им ID двигателей
    build_vehicles(bureau, engine_ids)
    
    # 4. Запись
    grouped = {"MECHANICAL": [], "ELECTRONIC": [], "VEHICLES": []}
    for cat, row in bureau.buffer:
        grouped[cat].append(row)
        
    for key, rows in grouped.items():
        if not rows: continue
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)
            
    print(f"✅ Сборки созданы: {len(bureau.buffer)} уникальных узлов и агрегатов.")

if __name__ == "__main__":
    main()


