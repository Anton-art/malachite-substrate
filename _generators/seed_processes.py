import os
import csv
import math

# =================================================================================
# НАСТРОЙКИ И ПУТИ
# =================================================================================

BASE_DIR = os.path.join("data_v2", "06_PROCESSES")

# Пути к подпапкам
PATHS = {
    "MACHINING":    os.path.join(BASE_DIR, "Manufacturing", "Material_Removal", "index.csv"),
    "DEFORMATION":  os.path.join(BASE_DIR, "Manufacturing", "Deformation", "index.csv"),
    "CASTING":      os.path.join(BASE_DIR, "Manufacturing", "Primary_Shaping", "index.csv"),
    "JOINING":      os.path.join(BASE_DIR, "Manufacturing", "Joining", "index.csv"),
    "ADDITIVE":     os.path.join(BASE_DIR, "Manufacturing", "Additive", "index.csv"),
    "TREATMENT":    os.path.join(BASE_DIR, "Manufacturing", "Treatment", "index.csv"),
    "SYNTHESIS":    os.path.join(BASE_DIR, "Synthesis", "Chemical", "index.csv"),
    "METALLURGY":   os.path.join(BASE_DIR, "Synthesis", "Metallurgy", "index.csv"),
    "LOGISTICS":    os.path.join(BASE_DIR, "Logistics", "Transport", "index.csv"),
    "EXTRACTION":   os.path.join(BASE_DIR, "Extraction", "Mining", "index.csv"),
    "GENERATION":   os.path.join(BASE_DIR, "Energy", "Generation", "index.csv"),
    "RECYCLING":    os.path.join(BASE_DIR, "Recycling", "Waste_Mgmt", "index.csv"),
    "COMPUTATION":  os.path.join(BASE_DIR, "Information", "Computing", "index.csv")
}

HEADERS = [
    "ID", "Name", "Description", 
    "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", 
    "Drawbacks", "Side_Effects", "Impact_Map",
    "Scarcity_Score", "Properties", "External_Data_Link",
    "Input_State", "Output_State", "Physics_Law", "Energy_Type", "Energy_Cost_Estimate", "Req_Infrastructure"
]

# =================================================================================
# БАЗА ЗНАНИЙ ТЕХНОЛОГА
# =================================================================================

PROCESS_TEMPLATES = {
    "MACHINING": [
        {"code": "TURN", "name": "Turning", "prec": 0.05, "waste": 0.4, "nrg": 2.0, "desc": "Lathe operation."},
        {"code": "MILL", "name": "Milling", "prec": 0.02, "waste": 0.5, "nrg": 3.0, "desc": "CNC milling."},
        {"code": "GRIND", "name": "Grinding", "prec": 0.005, "waste": 0.1, "nrg": 5.0, "desc": "Abrasive finishing."},
        {"code": "THREAD_ROLLING", "name": "Thread Rolling", "prec": 0.01, "waste": 0.0, "nrg": 1.0, "desc": "Cold forming of threads."},
    ],
    "DEFORMATION": [
        {"code": "STAMPING", "name": "Stamping", "prec": 0.1, "waste": 0.1, "nrg": 2.0, "desc": "Sheet metal punching."},
        {"code": "FORGING", "name": "Forging", "prec": 0.5, "waste": 0.0, "nrg": 4.0, "desc": "Hot metal shaping."},
        {"code": "ROLLING", "name": "Rolling", "prec": 1.0, "waste": 0.0, "nrg": 3.0, "desc": "Metal flattening."},
    ],
    "METALLURGY": [
        {"code": "SMELTING_BF", "name": "Blast Furnace Smelting", "prec": 10.0, "waste": 0.05, "nrg": 50.0, "desc": "Reduction of iron ore."},
        {"code": "REFINING_BOF", "name": "Basic Oxygen Refining", "prec": 1.0, "waste": 0.02, "nrg": 20.0, "desc": "Converting iron to steel."},
        {"code": "RECYCLING", "name": "EAF Recycling", "prec": 1.0, "waste": 0.02, "nrg": 30.0, "desc": "Melting scrap."},
    ],
    "CASTING": [
        {"code": "SAND", "name": "Sand Casting", "prec": 1.0, "waste": 0.2, "nrg": 4.0, "desc": "Molten metal into sand mold."},
        {"code": "DIE", "name": "Die Casting", "prec": 0.1, "waste": 0.1, "nrg": 3.5, "desc": "High pressure injection."},
    ],
    "JOINING": [
        {"code": "WELD_ARC", "name": "Arc Welding", "prec": 1.0, "waste": 0.05, "nrg": 2.5, "desc": "Fusion via electric arc."},
        {"code": "BOLT", "name": "Bolting", "prec": 0.1, "waste": 0.0, "nrg": 0.1, "desc": "Mechanical assembly."},
    ],
    "ADDITIVE": [
        {"code": "FDM", "name": "FDM Printing", "prec": 0.2, "waste": 0.01, "nrg": 1.5, "desc": "Plastic extrusion layering."},
        {"code": "SLS", "name": "SLS Sintering", "prec": 0.1, "waste": 0.05, "nrg": 4.0, "desc": "Laser powder fusion."},
    ],
    "TREATMENT": [
        {"code": "QUENCH", "name": "Quenching", "prec": 0.0, "waste": 0.0, "nrg": 3.0, "desc": "Rapid cooling for hardening."},
        {"code": "ANNEAL", "name": "Annealing", "prec": 0.0, "waste": 0.0, "nrg": 2.0, "desc": "Slow cooling for softening."},
    ],
    "SYNTHESIS": [
        {"code": "POLYMERIZATION", "name": "Polymerization", "prec": 0.0, "waste": 0.05, "nrg": 3.0, "desc": "Monomer linking."},
        {"code": "DISTILLATION", "name": "Distillation", "prec": 0.0, "waste": 0.1, "nrg": 4.0, "desc": "Fractional separation."},
        {"code": "REFINING", "name": "Oil Refining", "prec": 0.0, "waste": 0.1, "nrg": 5.0, "desc": "Crude oil separation."},
    ],
    "LOGISTICS": [
        {"code": "SHIPPING", "name": "Sea Freight", "prec": 0.0, "waste": 0.0, "nrg": 0.5, "desc": "Global container transport."},
        {"code": "TRUCKING", "name": "Road Freight", "prec": 0.0, "waste": 0.0, "nrg": 2.0, "desc": "Last mile delivery."},
    ],
    "EXTRACTION": [
        {"code": "MINING_OPEN", "name": "Open Pit Mining", "prec": 0.0, "waste": 0.9, "nrg": 2.0, "desc": "Surface excavation."},
        {"code": "DRILLING", "name": "Drilling", "prec": 0.0, "waste": 0.2, "nrg": 3.0, "desc": "Fluid extraction."},
    ],
    "GENERATION": [
        {"code": "COMBUSTION", "name": "Combustion", "prec": 0.0, "waste": 0.1, "nrg": -10.0, "desc": "Exothermic reaction."}, 
        {"code": "FISSION", "name": "Nuclear Fission", "prec": 0.0, "waste": 0.01, "nrg": -100.0, "desc": "Atom splitting."},
        {"code": "PV_EFFECT", "name": "Photovoltaic Effect", "prec": 0.0, "waste": 0.0, "nrg": -5.0, "desc": "Photon capture."},
    ],
    "RECYCLING": [
        {"code": "SORTING", "name": "Auto Sorting", "prec": 0.0, "waste": 0.1, "nrg": 1.0, "desc": "Material separation."},
        {"code": "MELTING", "name": "Remelting", "prec": 0.0, "waste": 0.05, "nrg": 3.0, "desc": "Scrap fusion."},
    ],
    "COMPUTATION": [
        {"code": "TRAINING", "name": "AI Training", "prec": 0.0, "waste": 0.0, "nrg": 10.0, "desc": "Gradient descent optimization."},
        {"code": "SIMULATION", "name": "Physics Simulation", "prec": 0.0, "waste": 0.0, "nrg": 5.0, "desc": "Virtual testing."},
    ]
}

# =================================================================================
# ЛОГИКА СИМУЛЯЦИИ
# =================================================================================

def calculate_syntropy(category, precision_mm, waste_ratio, energy_cost):
    if category == "GENERATION":
        output = abs(energy_cost)
        return round(output / (1 + waste_ratio * 10), 2)
    if category == "COMPUTATION":
        return round(100.0 / max(energy_cost, 0.1), 2)
    
    if precision_mm <= 0.0: precision_score = 5.0
    else: precision_score = 1.0 / max(precision_mm, 0.001)
    
    material_efficiency = 1.0 - waste_ratio
    score = (math.log(max(precision_score, 1.1)) * 10 * material_efficiency) / max(energy_cost, 0.1)
    if category == "EXTRACTION": score -= 5.0
    return round(score, 2)

def generate_rows(category):
    rows = []
    templates = PROCESS_TEMPLATES.get(category, [])
    
    for tmpl in templates:
        # Вариации качества
        if category in ["MACHINING", "ADDITIVE", "DEFORMATION", "METALLURGY"]:
            variants = [
                {"type": "Rough", "prec_mod": 5.0, "nrg_mod": 0.5, "waste_mod": 1.2},
                {"type": "Standard", "prec_mod": 1.0, "nrg_mod": 1.0, "waste_mod": 1.0},
                {"type": "Precision", "prec_mod": 0.2, "nrg_mod": 3.0, "waste_mod": 0.8}
            ]
        else:
            variants = [{"type": "Standard", "prec_mod": 1, "nrg_mod": 1, "waste_mod": 1}]

        for var in variants:
            real_prec = tmpl['prec'] * var['prec_mod']
            real_nrg = tmpl['nrg'] * var['nrg_mod']
            real_waste = min(tmpl['waste'] * var['waste_mod'], 0.99)
            syn = calculate_syntropy(category, real_prec, real_waste, real_nrg)
            
            cat = 10.0
            if category == "COMPUTATION": cat = 1000.0
            if category == "GENERATION": cat = 100.0
            if category == "METALLURGY": cat = 50.0

            era = "ERA-04_INDUSTRIAL"
            if category == "COMPUTATION": era = "ERA-06_DIGITAL"
            if category == "ADDITIVE": era = "ERA-05_ELECTRICAL"

            # --- ИСПРАВЛЕНИЕ ПРЕФИКСА ---
            # По умолчанию берем 3 буквы (MET, DEF)
            prefix = category[:3]
            # Но для MACHINING принудительно ставим MACH (4 буквы)
            if category == "MACHINING": prefix = "MACH"
            
            row = {
                "ID": f"PROC-{prefix}_{tmpl['code']}_{var['type'].upper()}",
                "Name": f"{tmpl['name']} ({var['type']})",
                "Description": f"{tmpl['desc']} Waste: {int(real_waste*100)}%.",
                "Era": era,
                "Predecessor_ID": "PROC-HAND_CRAFT",
                "Status": "ACTIVE",
                "Syntropy_Score": syn,
                "Catalytic_Potential": cat,
                "Structural_Pattern": category,
                "Scarcity_Score": 0.0,
                "Properties": f"{{'Precision': '{real_prec} mm', 'Waste': '{int(real_waste*100)}%', 'Energy': '{real_nrg} units'}}",
                "Impact_Map": "SOC-PROGRESS:ENABLE:+10",
                "Invention_Reason": "SOC-NEED_EFFICIENCY",
                "Social_Context": "MKT-GLOBAL",
                "Drawbacks": "Pollution" if real_waste > 0.5 else "None",
                "Side_Effects": "None",
                "External_Data_Link": "NULL",
                "Input_State": "VARIES",
                "Output_State": "VARIES",
                "Physics_Law": "SCI-LAW_THERMO_2",
                "Energy_Type": "ELECTRIC" if category in ["COMPUTATION", "ADDITIVE"] else "KINETIC",
                "Energy_Cost_Estimate": "High" if real_nrg > 5 else "Medium",
                "Req_Infrastructure": "FAC-GENERIC"
            }
            rows.append(row)
    return rows

def main():
    print("⚙️ Генерация Полного Цикла Процессов (v9.0 - MACH Prefix Fix)...")
    for category, path in PATHS.items():
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        data = generate_rows(category)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
        print(f"   - {category}: {len(data)} процессов.")
    print("✅ Процессы сгенерированы.")

if __name__ == "__main__":
    main()