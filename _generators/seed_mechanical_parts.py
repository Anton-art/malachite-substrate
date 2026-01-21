import os
import csv
import math

BASE_DIR = os.path.join("data_v2", "07_ARTIFACTS", "Parts_Mechanical")

PATHS = {
    "FASTENERS": os.path.join(BASE_DIR, "Fasteners", "index.csv"),
    "BEARINGS":  os.path.join(BASE_DIR, "Bearings", "index.csv"),
    "GEARS":     os.path.join(BASE_DIR, "Gears", "index.csv"),
    "SEALS":     os.path.join(BASE_DIR, "Seals", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Properties", "Req_Material", "Req_Process", "Impact_Map", 
    "Invention_Reason", "Social_Context", "Bill_of_Materials", "Potential_Realization_Rate"
]

def generate_fasteners():
    rows = []
    sizes = ["M6", "M8", "M10", "M12"]
    lengths = [20, 40, 60, 100]
    for s in sizes:
        for l in lengths:
            if l > 80: continue
            rows.append({
                "ID": f"PART-BOLT_HEX_{s}x{l}_88",
                "Name": f"Hex Bolt {s}x{l}mm (8.8)",
                "Description": "High tensile bolt for through-holes.",
                "Era": "ERA-04_INDUSTRIAL",
                "Predecessor_ID": "PART-RIVET",
                "Status": "ACTIVE",
                "Syntropy_Score": 2.0,
                "Catalytic_Potential": 1.0,
                "Structural_Pattern": "HELICAL_HEADED",
                "Properties": f"{{'Size': '{s}', 'Length': '{l}mm', 'Grade': '8.8'}}",
                "Req_Material": "MAT-STL_1045_CD_US__001", 
                "Req_Process": "PROC-MACH_THREAD_ROLLING_STANDARD",
                "Impact_Map": "ASSY-GENERIC:CLAMP:+1",
                "Invention_Reason": "SOC-NEED_FIXATION",
                "Social_Context": "MKT-HARDWARE",
                "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
            })
        for l in lengths:
            rows.append({
                "ID": f"PART-STUD_THREADED_{s}x{l}_88",
                "Name": f"Threaded Stud {s}x{l}mm",
                "Description": "Headless rod. For blind holes or dual-nut flanges.",
                "Era": "ERA-04_INDUSTRIAL",
                "Predecessor_ID": "NULL",
                "Status": "ACTIVE",
                "Syntropy_Score": 2.5,
                "Catalytic_Potential": 2.0,
                "Structural_Pattern": "HELICAL_ROD",
                "Properties": f"{{'Size': '{s}', 'Length': '{l}mm', 'Type': 'Full Thread'}}",
                "Req_Material": "MAT-STL_1045_CD_US__001",
                "Req_Process": "PROC-MACH_THREAD_ROLLING_STANDARD",
                "Impact_Map": "ASSY-ENGINE:ASSEMBLE:+10",
                "Invention_Reason": "SOC-NEED_PRECISION_ASSEMBLY",
                "Social_Context": "MKT-AUTOMOTIVE",
                "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
            })
        rows.append({
            "ID": f"PART-NUT_HEX_{s}_8",
            "Name": f"Hex Nut {s} (Cl.8)",
            "Description": "Standard hex nut.",
            "Era": "ERA-04_INDUSTRIAL",
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": 2.0,
            "Catalytic_Potential": 1.0,
            "Structural_Pattern": "HELICAL_INTERNAL",
            "Properties": f"{{'Size': '{s}', 'Pitch': 'Standard'}}",
            "Req_Material": "MAT-STL_1045_HR_US__001",
            "Req_Process": "PROC-MACH_THREAD_ROLLING_STANDARD",
            "Impact_Map": "PART-BOLT_HEX:LOCK:+10;PART-STUD_THREADED:LOCK:+10",
            "Invention_Reason": "SOC-NEED_FIXATION",
            "Social_Context": "MKT-HARDWARE",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
        })
        rows.append({
            "ID": f"PART-WASHER_FLAT_{s}",
            "Name": f"Flat Washer {s}",
            "Description": "Load distribution washer.",
            "Era": "ERA-04_INDUSTRIAL",
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": 1.5,
            "Catalytic_Potential": 0.5,
            "Structural_Pattern": "TORUS_FLAT",
            "Properties": f"{{'ID': '{s}', 'Type': 'Flat'}}",
            "Req_Material": "MAT-STL_1010_HR_US__001",
            "Req_Process": "PROC-DEF_STAMPING_STANDARD",
            "Impact_Map": "PART-NUT_HEX:PROTECT:+5",
            "Invention_Reason": "SOC-NEED_DURABILITY",
            "Social_Context": "MKT-HARDWARE",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
        })
    return rows

def generate_bearings():
    rows = []
    series = [
        {"code": "608", "name": "Skate Bearing", "id": 8, "od": 22, "load": "Low"},
        {"code": "6204", "name": "Motor Bearing", "id": 20, "od": 47, "load": "Medium"},
        {"code": "6309", "name": "Heavy Bearing", "id": 45, "od": 100, "load": "High"}
    ]
    for b in series:
        rows.append({
            "ID": f"PART-BEARING_BALL_{b['code']}_ZZ",
            "Name": f"Ball Bearing {b['code']}-ZZ",
            "Description": f"Deep groove ball bearing. ID:{b['id']}mm.",
            "Era": "ERA-04_INDUSTRIAL",
            "Predecessor_ID": "PART-BUSHING_BRONZE",
            "Status": "ACTIVE",
            "Syntropy_Score": 15.0,
            "Catalytic_Potential": 20.0,
            "Structural_Pattern": "CONCENTRIC_ROTATION",
            "Properties": f"{{'ID': '{b['id']}mm', 'OD': '{b['od']}mm', 'Shield': 'Metal'}}",
            "Req_Material": "MAT-STL_52100_VAC_ARC",
            "Req_Process": "PROC-MACH_GRIND_PRECISION",
            "Impact_Map": "SCI-LAW_FRICTION:REDUCE:+100",
            "Invention_Reason": "SOC-NEED_EFFICIENCY",
            "Social_Context": "MKT-AUTOMOTIVE",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.95
        })
    return rows

def generate_gears():
    rows = []
    modules = [1.0, 2.0, 4.0]
    teeth = [12, 24, 48, 96]
    for m in modules:
        for t in teeth:
            pd = m * t
            rows.append({
                "ID": f"PART-GEAR_SPUR_M{int(m)}_T{t}",
                "Name": f"Spur Gear M{m} T{t}",
                "Description": f"Involute gear. Pitch Dia: {pd}mm.",
                "Era": "ERA-04_INDUSTRIAL",
                "Predecessor_ID": "PART-GEAR_WOODEN",
                "Status": "ACTIVE",
                "Syntropy_Score": 5.0,
                "Catalytic_Potential": 10.0,
                "Structural_Pattern": "RADIAL_SYMMETRY",
                "Properties": f"{{'Module': '{m}', 'Teeth': '{t}', 'PD': '{pd}mm'}}",
                "Req_Material": "MAT-STL_1045_HR_US__001",
                "Req_Process": "PROC-MACH_MILL_PRECISION",
                "Impact_Map": "ASSY-GEARBOX:ENABLE:+10",
                "Invention_Reason": "SOC-NEED_TORQUE",
                "Social_Context": "MKT-MACHINERY",
                "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.98
            })
    return rows

def generate_seals():
    rows = []
    sizes = [10, 20, 50, 100]
    for s in sizes:
        rows.append({
            "ID": f"PART-SEAL_ORING_NBR_{s}MM",
            "Name": f"O-Ring NBR {s}mm",
            "Description": "Nitrile rubber sealing ring.",
            "Era": "ERA-05_ELECTRICAL",
            "Predecessor_ID": "MAT-LEATHER_GASKET",
            "Status": "ACTIVE",
            "Syntropy_Score": 3.0,
            "Catalytic_Potential": 5.0,
            "Structural_Pattern": "TORUS",
            "Properties": f"{{'Diameter': '{s}mm', 'Material': 'NBR'}}",
            "Req_Material": "MAT-RUBBER_SYNTHETIC",
            "Req_Process": "PROC-MOLD_INJECTION_STANDARD", # <--- FIXED (MOLD)
            "Impact_Map": "ASSY-HYDRAULICS:ENABLE:+10",
            "Invention_Reason": "SOC-NEED_SAFETY",
            "Social_Context": "MKT-SPARES",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
        })
    return rows

def main():
    print("⚙️ Генерация Механической Номенклатуры (Professional Grade)...")
    tasks = {"FASTENERS": generate_fasteners(), "BEARINGS": generate_bearings(), "GEARS": generate_gears(), "SEALS": generate_seals()}
    total = 0
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        total += len(data)
    print(f"✅ Механика обновлена: {total} деталей.")

if __name__ == "__main__":
    main()
