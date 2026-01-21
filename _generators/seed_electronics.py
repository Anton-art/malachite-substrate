import os
import csv
import math

BASE_DIR = os.path.join("data_v2", "07_ARTIFACTS", "Electronics")

PATHS = {
    "SEMICON":    os.path.join(BASE_DIR, "Semiconductors", "index.csv"),
    "PASSIVE":    os.path.join(BASE_DIR, "Passive", "index.csv"),
    "IC":         os.path.join(BASE_DIR, "Integrated_Circuits", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Properties", "Req_Material", "Req_Process", "Impact_Map", 
    "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", 
    "External_Data_Link", "Req_Infrastructure", "Req_Science", 
    "Bill_of_Materials", "Potential_Realization_Rate"
]

RESISTOR_VALUES = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
MULTIPLIERS = [1, 10, 100, 1000, 10000, 100000, 1000000]
PACKAGES = ["0201", "0402", "0603", "0805", "1206"]

NODES = [
    {"nm": 180, "era": "ERA-05_ELECTRICAL", "trans_density": 1, "cost": 1},
    {"nm": 90,  "era": "ERA-06_DIGITAL",    "trans_density": 4, "cost": 2},
    {"nm": 45,  "era": "ERA-06_DIGITAL",    "trans_density": 16, "cost": 4},
    {"nm": 14,  "era": "ERA-06_DIGITAL",    "trans_density": 64, "cost": 10},
    {"nm": 5,   "era": "ERA-07_INTELLECTUAL","trans_density": 256, "cost": 50},
]

ARCHITECTURES = ["x86", "ARM", "RISC-V"]

def format_resistor_name(ohms):
    if ohms >= 1000000:
        val = ohms / 1000000
        return f"{int(val)}M" if val.is_integer() else f"{val:.1f}M"
    elif ohms >= 1000:
        val = ohms / 1000
        return f"{int(val)}k" if val.is_integer() else f"{val:.1f}k"
    else:
        return str(int(ohms))

def generate_passives():
    rows = []
    for pkg in PACKAGES:
        for mult in MULTIPLIERS:
            for val in RESISTOR_VALUES:
                ohms = val * mult
                name_val = format_resistor_name(ohms)
                size_bonus = 5.0 if pkg == "0201" else 1.0
                syn = 2.0 * size_bonus
                row = {
                    "ID": f"PART-RES_{pkg}_{name_val}OHM",
                    "Name": f"Resistor {name_val}Ω {pkg}",
                    "Description": f"Thick film resistor. Package {pkg}.",
                    "Era": "ERA-05_ELECTRICAL",
                    "Predecessor_ID": "PART-RES_AXIAL",
                    "Status": "ACTIVE",
                    "Syntropy_Score": syn,
                    "Catalytic_Potential": 5.0,
                    "Structural_Pattern": "PASSIVE_DAMPENER",
                    "Properties": f"{{'Resistance': '{ohms} Ohm', 'Package': '{pkg}', 'Power': '0.1W'}}",
                    "Req_Material": "MAT-CER_ALUMINA_96;RES-ORE_COPPER_SULFIDE", 
                    "Req_Process": "PROC-SYN_POLYMERIZATION_STANDARD",
                    "Impact_Map": "ASSY-PCB:ENABLE:+1",
                    "Invention_Reason": "SOC-NEED_CONTROL",
                    "Social_Context": "MKT-ELECTRONICS",
                    "Drawbacks": "None", "Side_Effects": "Heat", "External_Data_Link": "NULL",
                    "Req_Infrastructure": "FAC-GENERIC",
                    "Req_Science": "SCI-LAW_OHM",
                    "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
                }
                rows.append(row)
    return rows

def generate_semicon():
    rows = []
    sizes = [200, 300, 450]
    for s in sizes:
        row = {
            "ID": f"PART-WAFER_SI_{s}MM",
            "Name": f"Silicon Wafer {s}mm",
            "Description": "Monocrystalline silicon substrate.",
            "Era": "ERA-05_ELECTRICAL",
            "Predecessor_ID": "NULL",
            "Status": "ACTIVE",
            "Syntropy_Score": 10.0,
            "Catalytic_Potential": 100.0,
            "Structural_Pattern": "CRYSTAL_LATTICE",
            "Properties": f"{{'Diameter': '{s}mm', 'Purity': '99.9999999%'}}",
            "Req_Material": "RES-MIN_SILICA",
            "Req_Process": "PROC-SYN_CRYSTAL_GROWTH_STANDARD",
            "Impact_Map": "FAC-FAB:ENABLE:+100",
            "Invention_Reason": "SOC-NEED_COMPUTATION",
            "Social_Context": "MKT-SEMICON",
            "Drawbacks": "High Energy", "Side_Effects": "Toxic Waste", "External_Data_Link": "NULL",
            "Req_Infrastructure": "FAC-REFINERY", # <--- FIXED (Было HEAVY_REFINERY)
            "Req_Science": "SCI-LAW_QUANTUM_TUNNELING",
            "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.95
        }
        rows.append(row)
    return rows

def generate_ics():
    rows = []
    for arch in ARCHITECTURES:
        for node in NODES:
            syn = (node['trans_density'] / node['cost']) * 10.0
            cat = node['trans_density'] * 50.0
            row = {
                "ID": f"ASSY-CPU_{arch}_{node['nm']}NM",
                "Name": f"CPU {arch} {node['nm']}nm",
                "Description": f"Microprocessor. {node['trans_density']}B transistors.",
                "Era": node['era'],
                "Predecessor_ID": "PART-TRANSISTOR_MOSFET",
                "Status": "ACTIVE" if node['nm'] >= 5 else "PROTOTYPE",
                "Syntropy_Score": round(syn, 2),
                "Catalytic_Potential": cat,
                "Structural_Pattern": "LOGIC_GATE_ARRAY",
                "Properties": f"{{'Node': '{node['nm']}nm', 'Arch': '{arch}'}}",
                "Req_Material": "NULL",
                "Req_Process": "PROC-MIC_LITHOGRAPHY_STANDARD",
                "Impact_Map": "SOC-INFO:ACCELERATE:+1000",
                "Invention_Reason": "SOC-NEED_INTELLIGENCE",
                "Social_Context": "MKT-DIGITAL",
                "Drawbacks": "E-Waste", "Side_Effects": "Heat", "External_Data_Link": "NULL",
                "Req_Infrastructure": "FAC-FAB_CLEANROOM",
                "Req_Science": "SCI-LAW_E_MC2",
                "Bill_of_Materials": f"PART-WAFER_SI_300MM;PART-RES_0201_10kOHM",
                "Potential_Realization_Rate": 0.90
            }
            rows.append(row)
    return rows

def main():
    print("⚡ Генерация Массива Электроники (Combinatorial Explosion)...")
    tasks = {"PASSIVE": generate_passives(), "SEMICON": generate_semicon(), "IC": generate_ics()}
    total = 0
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        total += len(data)
    print(f"✅ Электроника: Сгенерировано {total} уникальных компонентов.")

if __name__ == "__main__":
    main()
