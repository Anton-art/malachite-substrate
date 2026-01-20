import os
import csv
import random

TARGET_PATH = os.path.join("data_v2", "07_ARTIFACTS", "Parts_Mechanical", "Fasteners", "index.csv")
HEADERS = ["ID", "Name", "Description", "Era", "Predecessor_ID", "Status", "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern", "Properties", "Req_Material", "Req_Process", "Impact_Map", "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "External_Data_Link", "Req_Infrastructure", "Req_Science", "Bill_of_Materials", "Potential_Realization_Rate"]

SIZES = {"M6": {"d": 6, "area": 20.1}, "M8": {"d": 8, "area": 36.6}}
GRADES = {"8.8": {"tensile": 800, "mat": "MAT-STL_1045_HR_US__001"}} # Ссылка на конкретную сталь
COATINGS = [{"code": "ZN", "name": "Zinc Plated", "life": 5.0, "cost": 1.2}]

def generate_fastener(type_name, size_name, size_data, grade_name, grade_data, coating):
    id_str = f"PART-{type_name}_HEX_{size_name}_{grade_name.replace('.','')}_{coating['code']}"
    
    # ИСПРАВЛЕНО: Добавлены суффиксы _STANDARD к процессам
    if type_name == "BOLT":
        # Болт требует накатки резьбы (MACH)
        req_proc = "PROC-MACH_THREAD_ROLLING_STANDARD"
        req_infra = "FAC-MACH_THREADER"
    else:
        # Шайба требует штамповки (DEF)
        req_proc = "PROC-DEF_STAMPING_STANDARD"
        req_infra = "FAC-MACH_PRESS"

    return {
        "ID": id_str,
        "Name": f"Hex {type_name} {size_name}",
        "Description": "Fastener.",
        "Era": "ERA-04_INDUSTRIAL",
        "Predecessor_ID": "PART-RIVET",
        "Status": "ACTIVE",
        "Syntropy_Score": 5.0,
        "Catalytic_Potential": 5.0,
        "Structural_Pattern": "HELICAL",
        "Properties": "{}",
        "Req_Material": grade_data['mat'],
        "Req_Process": req_proc, # <--- Теперь здесь правильная ссылка
        "Impact_Map": "ASSY-MACHINE:ENABLE:+10",
        "Invention_Reason": "ASSEMBLY",
        "Social_Context": "NULL", "Drawbacks": "None", "Side_Effects": "None", "External_Data_Link": "NULL",
        "Req_Infrastructure": req_infra,
        "Req_Science": "SCI-LAW_FRICTION",
        "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
    }

def main():
    rows = []
    for size, s_data in SIZES.items():
        for grade, g_data in GRADES.items():
            for coat in COATINGS:
                rows.append(generate_fastener("BOLT", size, s_data, grade, g_data, coat))
                rows.append(generate_fastener("WASHER", size, s_data, grade, g_data, coat))

    if not os.path.exists(os.path.dirname(TARGET_PATH)): os.makedirs(os.path.dirname(TARGET_PATH))
    with open(TARGET_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Крепеж обновлен (Links Fixed: _STANDARD added).")

if __name__ == "__main__":
    main()