import os
import csv
import random
import math

# =================================================================================
# НАСТРОЙКИ И ПУТИ
# =================================================================================
BASE_DIR = os.path.join("data_v2", "05_INFRASTRUCTURE")

PATHS = {
    "HEAVY":    os.path.join(BASE_DIR, "Facilities", "Heavy_Ind", "index.csv"),
    "MACHINES": os.path.join(BASE_DIR, "Machines", "CNC", "index.csv"),
    "GENERIC":  os.path.join(BASE_DIR, "Facilities", "Light_Ind", "index.csv"),
    "POWER":    os.path.join(BASE_DIR, "Facilities", "Energy", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Power_Source", "Output_Capacity", "Req_Space", "Maintenance_Cycle", "Energy_Consumption_W",
    "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "Impact_Map", 
    "Properties", "External_Data_Link"
]

# =================================================================================
# БАЗА ЗНАНИЙ
# =================================================================================

# Связь станка с процессом (для Impact_Map)
# ИСПРАВЛЕНО: Добавлены суффиксы _STANDARD
OP_TO_PROCESS = {
    "Turning": "PROC-MACH_TURN_STANDARD",
    "Milling": "PROC-MACH_MILL_STANDARD",
    "Drilling": "PROC-EXT_DRILLING_STANDARD",
    "Grinding": "PROC-MACH_GRIND_STANDARD",
    "Threading": "PROC-MACH_THREAD_ROLLING_STANDARD",
    "Forming": "PROC-DEF_STAMPING_STANDARD",
    "Additive": "PROC-ADD_FDM_STANDARD",
    "Assembly": "PROC-GEN_ASSEMBLY_STANDARD",
    "Cutting": "PROC-MACH_CUTTING_STANDARD"
}

MACHINE_TYPES = [
    {"code": "MACH_LATHE", "name": "Lathe", "op": "Turning", "base_era": "ERA-04_INDUSTRIAL", "complexity": 1.0},
    {"code": "MACH_MILL", "name": "Milling Machine", "op": "Milling", "base_era": "ERA-04_INDUSTRIAL", "complexity": 1.2},
    {"code": "MACH_DRILL", "name": "Drill Press", "op": "Drilling", "base_era": "ERA-04_INDUSTRIAL", "complexity": 0.8},
    {"code": "MACH_GRINDER", "name": "Surface Grinder", "op": "Grinding", "base_era": "ERA-04_INDUSTRIAL", "complexity": 1.1},
    {"code": "MACH_THREADER", "name": "Thread Roller", "op": "Threading", "base_era": "ERA-04_INDUSTRIAL", "complexity": 1.0},
    {"code": "MACH_PRESS", "name": "Hydraulic Press", "op": "Forming", "base_era": "ERA-04_INDUSTRIAL", "complexity": 1.5},
    {"code": "MACH_PRINTER_FDM", "name": "3D Printer (FDM)", "op": "Additive", "base_era": "ERA-06_DIGITAL", "complexity": 2.0},
    {"code": "MACH_ROBOT_ARM", "name": "Robotic Arm", "op": "Assembly", "base_era": "ERA-06_DIGITAL", "complexity": 3.0},
]

SIZES = [
    {"suffix": "MICRO", "name": "Lab/Desktop", "pwr_mod": 0.05, "cap_mod": 0.02, "space": "2m2", "volt": "110/220V", "prec_id": "FAC-WORKSHOP_MANUAL"},
    {"suffix": "STD",   "name": "Standard",    "pwr_mod": 1.0,  "cap_mod": 1.0,  "space": "15m2", "volt": "380V 3-Phase", "prec_id": "FAC-WORKSHOP_MANUAL"},
    {"suffix": "IND",   "name": "Industrial",  "pwr_mod": 5.0,  "cap_mod": 8.0,  "space": "50m2", "volt": "480V 3-Phase", "prec_id": "STD"},
    {"suffix": "GIGA",  "name": "Gigafactory", "pwr_mod": 50.0, "cap_mod": 120.0,"space": "500m2","volt": "HV Direct Feed", "prec_id": "IND"},
]

POWER_TYPES = [
    {"code": "COAL_PLANT", "name": "Coal Power Plant", "era": "ERA-04_INDUSTRIAL", "syn": -5.0, "fuel": "RES-COAL_BITUMINOUS", "waste": "High CO2", "desc": "Burns coal to generate steam."},
    {"code": "GAS_TURBINE", "name": "Gas Turbine Cycle", "era": "ERA-05_ELECTRICAL", "syn": 2.0, "fuel": "RES-FUEL_GAS_METHANE", "waste": "Med CO2", "desc": "Combusts natural gas."},
    {"code": "NUCLEAR_PWR", "name": "Nuclear Reactor (PWR)", "era": "ERA-05_ELECTRICAL", "syn": 50.0, "fuel": "RES-FUEL_URANIUM", "waste": "Nuclear Waste", "desc": "Splits uranium atoms."},
    {"code": "SOLAR_FARM", "name": "Solar PV Farm", "era": "ERA-06_DIGITAL", "syn": 20.0, "fuel": "ENV-SUNLIGHT", "waste": "None", "desc": "Captures sunlight."},
]

# =================================================================================
# ЛОГИКА
# =================================================================================

def calculate_mtbf(complexity, era_str):
    base_hours = 2000
    if "DIGITAL" in era_str: base_hours += 5000
    if "INTELLECTUAL" in era_str: base_hours += 20000
    return int(base_hours / max(complexity, 0.5))

def generate_machines():
    rows = []
    for m in MACHINE_TYPES:
        for s in SIZES:
            obj_id = f"FAC-{m['code']}" if s['suffix'] == "STD" else f"FAC-{m['code']}_{s['suffix']}"
            
            if s['prec_id'] == "STD": prec_id = f"FAC-{m['code']}"
            elif s['prec_id'] == "IND": prec_id = f"FAC-{m['code']}_IND"
            else: prec_id = s['prec_id']

            proc_link = OP_TO_PROCESS.get(m['op'], "PROC-GENERIC")
            boost = int(10 * s['cap_mod'])
            impact = f"{proc_link}:ENABLE:+{boost};SOC-GDP:GROWTH:+{int(boost/2)}"

            base_watts = 10000
            watts = int(base_watts * s['pwr_mod'])
            mtbf = calculate_mtbf(m['complexity'], m['base_era'])
            efficiency = (s['cap_mod'] * (mtbf/1000)) / max(s['pwr_mod'], 0.1)
            
            row = {
                "ID": obj_id,
                "Name": f"{s['name']} {m['name']}",
                "Description": f"{m['op']} unit. {s['name']} scale.",
                "Era": m['base_era'],
                "Predecessor_ID": prec_id,
                "Status": "ACTIVE",
                "Syntropy_Score": round(efficiency, 2),
                "Catalytic_Potential": 10.0 * m['complexity'],
                "Structural_Pattern": "MECHANICAL_KINEMATIC",
                "Power_Source": "GRID-AC",
                "Output_Capacity": f"{int(100 * s['cap_mod'])} ops/hr",
                "Req_Space": s['space'],
                "Maintenance_Cycle": f"Every {int(mtbf/10)} hours",
                "Energy_Consumption_W": watts,
                "Invention_Reason": "SOC-NEED_EFFICIENCY",
                "Social_Context": "MKT-MANUFACTURING",
                "Drawbacks": "Noise; Vibration",
                "Side_Effects": "Heat Generation",
                "Impact_Map": impact,
                "Properties": f"{{'Voltage': '{s['volt']}', 'MTBF': '{mtbf} hours'}}",
                "External_Data_Link": "NULL"
            }
            rows.append(row)
    return rows

def generate_power():
    rows = []
    for p in POWER_TYPES:
        scales = [("SMALL", 10), ("MAIN", 100), ("GIGA", 1000)]
        for suffix, mult in scales:
            mw = 50 * mult
            row = {
                "ID": f"FAC-GEN_{p['code']}_{suffix}",
                "Name": f"{p['name']} ({suffix})",
                "Description": f"{p['desc']} Output: {mw} MW.",
                "Era": p['era'],
                "Predecessor_ID": "FAC-STEAM_ENGINE",
                "Status": "ACTIVE",
                "Syntropy_Score": p['syn'],
                "Catalytic_Potential": 100.0 * mult,
                "Structural_Pattern": "ENERGY_SOURCE",
                "Power_Source": p['fuel'],
                "Output_Capacity": f"{mw} MW",
                "Req_Space": f"{10*mult} Hectares",
                "Maintenance_Cycle": "Continuous",
                "Energy_Consumption_W": -mw * 1000000,
                "Invention_Reason": "SOC-NEED_ENERGY",
                "Social_Context": "MKT-ENERGY_GRID",
                "Drawbacks": p['waste'],
                "Side_Effects": "Thermal Pollution",
                "Impact_Map": "GRID-ALL:ENERGIZE:+1000",
                "Properties": "{'Grid_Type': 'HV_AC'}",
                "External_Data_Link": "NULL"
            }
            rows.append(row)
    return rows

def generate_heavy():
    # ИСПРАВЛЕНО: Добавлены суффиксы _STANDARD к процессам
    base_heavy = [
        {"code": "BLAST_FURNACE", "name": "Blast Furnace", "cap": 5000, "proc": "PROC-MET_SMELTING_BF_STANDARD"},
        {"code": "EAF", "name": "Electric Arc Furnace", "cap": 2000, "proc": "PROC-MET_RECYCLING_STANDARD"},
        {"code": "ROLLING_MILL", "name": "Rolling Mill", "cap": 3000, "proc": "PROC-DEF_ROLLING_STANDARD"},
        {"code": "REFINERY", "name": "Oil Refinery", "cap": 10000, "proc": "PROC-SYN_REFINING_STANDARD"},
    ]
    rows = []
    for h in base_heavy:
        row = {
            "ID": f"FAC-{h['code']}",
            "Name": h['name'],
            "Description": "Heavy industrial facility.",
            "Era": "ERA-04_INDUSTRIAL",
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": 8.5,
            "Catalytic_Potential": 50.0,
            "Structural_Pattern": "CENTRALIZED_PLANT",
            "Power_Source": "GRID-HV", # Оставляем HV, это верно
            "Output_Capacity": f"{h['cap']} t/day",
            "Req_Space": "Industrial Zone",
            "Maintenance_Cycle": "Weekly",
            "Energy_Consumption_W": 50000000,
            "Invention_Reason": "SOC-NEED_SCALE",
            "Social_Context": "MKT-HEAVY_IND",
            "Drawbacks": "Pollution", "Side_Effects": "None", 
            "Impact_Map": f"{h.get('proc', 'PROC-GENERIC')}:ENABLE:+100",
            "Properties": "{'Zone': 'Heavy_Ind'}",
            "External_Data_Link": "NULL"
        }
        rows.append(row)
    return rows

def generate_generic():
    # ИСПРАВЛЕНО: Power_Source теперь GRID-AC
    return [{"ID": "FAC-GENERIC", "Name": "General Factory", "Era": "ERA-04_INDUSTRIAL", "Syntropy_Score": 1.0, "Catalytic_Potential": 5.0, "Structural_Pattern": "BOX", "Power_Source": "GRID-AC", "Output_Capacity": "N/A", "Req_Space": "Zone", "Maintenance_Cycle": "N/A", "Energy_Consumption_W": 50000, "Invention_Reason": "N/A", "Social_Context": "N/A", "Drawbacks": "N/A", "Side_Effects": "N/A", "Impact_Map": "N/A", "Properties": "{}", "External_Data_Link": "NULL", "Predecessor_ID": "NULL", "Status": "ACTIVE"}]

def main():
    print("🏭 Генерация Инфраструктуры v3.3 (Final Links)...")
    tasks = {"MACHINES": generate_machines(), "POWER": generate_power(), "HEAVY": generate_heavy(), "GENERIC": generate_generic()}
    total = 0
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        print(f"   - {key}: {len(data)} объектов.")
        total += len(data)
    print(f"✅ Инфраструктура обновлена. Всего объектов: {total}")

if __name__ == "__main__":
    main()