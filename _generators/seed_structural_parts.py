import os
import csv
import random

BASE_DIR = os.path.join("data_v2", "07_ARTIFACTS", "Parts_Structural")

PATHS = {
    "PROFILES": os.path.join(BASE_DIR, "Profiles", "index.csv"),
    "HOUSINGS": os.path.join(BASE_DIR, "Housings", "index.csv"),
    "WHEELS":   os.path.join(BASE_DIR, "Wheels", "index.csv"),
    "CHASSIS":  os.path.join(BASE_DIR, "Chassis", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Properties", "Req_Material", "Req_Process", "Impact_Map", 
    "Invention_Reason", "Social_Context", "Bill_of_Materials", "Potential_Realization_Rate"
]

def generate_profiles():
    rows = []
    sizes = [20, 30, 40, 80]
    for s in sizes:
        rows.append({
            "ID": f"PART-PROFILE_TSLOT_{s}x{s}_AL",
            "Name": f"Alu Profile {s}x{s}mm T-Slot",
            "Description": "Extruded aluminum modular framing.",
            "Era": "ERA-05_ELECTRICAL",
            "Predecessor_ID": "PART-BEAM_WOODEN",
            "Status": "ACTIVE",
            "Syntropy_Score": 4.0,
            "Catalytic_Potential": 20.0,
            "Structural_Pattern": "EXTRUSION_CONSTANT",
            "Properties": f"{{'Size': '{s}mm', 'Material': '6063 Aluminum'}}",
            "Req_Material": "MAT-AL_6061_T6",
            "Req_Process": "PROC-DEF_EXTRUSION_AL_STANDARD", # <--- FIXED
            "Impact_Map": "FAC-MACH_CNC:BUILD:+10",
            "Invention_Reason": "SOC-NEED_MODULARITY",
            "Social_Context": "MKT-AUTOMATION",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 1.0
        })
    rows.append({
        "ID": "PART-PROFILE_IBEAM_STEEL_HEAVY",
        "Name": "Steel I-Beam (Heavy)",
        "Description": "Structural support beam.",
        "Era": "ERA-04_INDUSTRIAL",
        "Predecessor_ID": "NULL",
        "Status": "ACTIVE",
        "Syntropy_Score": 2.0,
        "Catalytic_Potential": 5.0,
        "Structural_Pattern": "I_SECTION",
        "Properties": "{'Standard': 'IPE 200'}",
        "Req_Material": "MAT-STL_1010_HR_US__001",
        "Req_Process": "PROC-DEF_ROLLING_STANDARD",
        "Impact_Map": "ASSY-UNIT_CHASSIS_STEEL:CONSTRUCT:+100",
        "Invention_Reason": "SOC-NEED_STRENGTH",
        "Social_Context": "MKT-CONSTRUCTION",
        "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 1.0
    })
    return rows

def generate_housings():
    rows = []
    rack_units = [1, 2, 4]
    for u in rack_units:
        rows.append({
            "ID": f"PART-CASE_STEEL_{u}U",
            "Name": f"Server Chassis {u}U",
            "Description": "19-inch rackmount enclosure.",
            "Era": "ERA-05_ELECTRICAL",
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": 2.5,
            "Catalytic_Potential": 10.0,
            "Structural_Pattern": "BOX_ENCLOSURE",
            "Properties": f"{{'Height': '{u}U', 'Material': 'SECC Steel'}}",
            "Req_Material": "MAT-STL_1010_CD_US__001",
            "Req_Process": "PROC-DEF_STAMPING_STANDARD",
            "Impact_Map": "ASSY-SERVER:PROTECT:+10",
            "Invention_Reason": "SOC-NEED_PROTECTION",
            "Social_Context": "MKT-IT",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 1.0
        })
    rows.append({
        "ID": "PART-CASE_NEMA_IP67",
        "Name": "Industrial Control Box IP67",
        "Description": "Waterproof electrical enclosure.",
        "Era": "ERA-05_ELECTRICAL",
        "Predecessor_ID": "NULL",
        "Status": "ACTIVE",
        "Syntropy_Score": 3.0,
        "Catalytic_Potential": 5.0,
        "Structural_Pattern": "SEALED_BOX",
        "Properties": "{'Rating': 'IP67', 'Material': 'Polycarbonate/Steel'}",
        "Req_Material": "MAT-POLY_ABS_HI",
        "Req_Process": "PROC-MOLD_INJECTION_STANDARD", # <--- FIXED
        "Impact_Map": "FAC-MACH_CNC:CONTROL:+10",
        "Invention_Reason": "SOC-NEED_SAFETY",
        "Social_Context": "MKT-INDUSTRIAL",
        "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 1.0
    })
    return rows

def generate_wheels():
    rows = []
    wheels = [
        {"code": "CASTER_50MM", "name": "Swivel Caster 50mm", "app": "Furniture/Carts", "mat": "MAT-POLY_PA66"},
        {"code": "CAR_R16", "name": "Car Wheel R16", "app": "Passenger Vehicle", "mat": "MAT-AL_6061_T6"},
        {"code": "TRUCK_22", "name": "Heavy Truck Wheel", "app": "Logistics", "mat": "MAT-STL_1045_HR_US__001"}
    ]
    for w in wheels:
        obj_id = "PART-WHEEL_TRUCK" if w['code'] == "TRUCK_22" else f"PART-WHEEL_{w['code']}"
        rows.append({
            "ID": obj_id,
            "Name": w['name'],
            "Description": f"Wheel assembly for {w['app']}.",
            "Era": "ERA-04_INDUSTRIAL",
            "Predecessor_ID": "PART-WHEEL_WOODEN",
            "Status": "ACTIVE",
            "Syntropy_Score": 5.0,
            "Catalytic_Potential": 10.0,
            "Structural_Pattern": "ROTATING_ASSEMBLY",
            "Properties": f"{{'Application': '{w['app']}'}}",
            "Req_Material": f"{w['mat']};MAT-ELAST_RUBBER_NBR",
            "Req_Process": "PROC-ASS_MANUAL_STANDARD", # <--- FIXED (GEN -> ASS)
            "Impact_Map": "SOC-LOGISTICS:MOVE:+100",
            "Invention_Reason": "SOC-NEED_MOBILITY",
            "Social_Context": "MKT-AUTO",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 1.0
        })
    return rows

def generate_chassis():
    rows = []
    rows.append({
        "ID": "ASSY-UNIT_CHASSIS_STEEL",
        "Name": "Truck Ladder Frame",
        "Description": "Heavy duty steel chassis.",
        "Era": "ERA-04_INDUSTRIAL",
        "Predecessor_ID": "NULL",
        "Status": "ACTIVE",
        "Syntropy_Score": 4.0,
        "Catalytic_Potential": 10.0,
        "Structural_Pattern": "LADDER_FRAME",
        "Properties": "{'Type': 'Ladder', 'Material': 'Steel Channel'}",
        "Req_Material": "NULL",
        "Req_Process": "PROC-JOIN_WELD_ARC_STANDARD",
        "Impact_Map": "PROD-VEH_TRUCK:SUPPORT:+100",
        "Invention_Reason": "SOC-NEED_STRENGTH",
        "Social_Context": "MKT-AUTO",
        "Bill_of_Materials": "PART-PROFILE_IBEAM_STEEL_HEAVY:2;PART-BOLT_HEX_M12x60_88:50",
        "Potential_Realization_Rate": 1.0
    })
    rows.append({
        "ID": "ASSY-UNIT_CHASSIS_MONOCOQUE",
        "Name": "Car Monocoque",
        "Description": "Stamped steel unibody.",
        "Era": "ERA-05_ELECTRICAL",
        "Predecessor_ID": "ASSY-UNIT_CHASSIS_STEEL",
        "Status": "ACTIVE",
        "Syntropy_Score": 6.0,
        "Catalytic_Potential": 15.0,
        "Structural_Pattern": "SHELL_STRUCTURE",
        "Properties": "{'Type': 'Unibody'}",
        "Req_Material": "MAT-STL_1010_CD_US__001",
        "Req_Process": "PROC-JOIN_WELD_SPOT_STANDARD", # <--- FIXED
        "Impact_Map": "PROD-VEH_CAR:SUPPORT:+100",
        "Invention_Reason": "SOC-NEED_SAFETY",
        "Social_Context": "MKT-AUTO",
        "Bill_of_Materials": "NULL",
        "Potential_Realization_Rate": 1.0
    })
    return rows

def main():
    print("🏗️ Генерация Структурных Компонентов v2.0 (Profiles & Chassis)...")
    tasks = {"PROFILES": generate_profiles(), "HOUSINGS": generate_housings(), "WHEELS": generate_wheels(), "CHASSIS": generate_chassis()}
    total = 0
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        total += len(data)
    print(f"✅ Структура создана: {total} объектов.")

if __name__ == "__main__":
    main()
