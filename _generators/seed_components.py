import os
import csv
import random


TARGET_PATH = os.path.join("data_v2", "07_ARTIFACTS", "Parts_Mechanical", "Fasteners", "index.csv")
HEADERS = ["ID", "Name", "Description", "Era", "Predecessor_ID", "Status", "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern", "Properties", "Req_Material", "Req_Process", "Impact_Map", "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "External_Data_Link", "Req_Infrastructure", "Req_Science", "Bill_of_Materials", "Potential_Realization_Rate"]


# Геометрия
SIZES = {
    "M6": {"d": 6, "pitch": 1.0, "area": 20.1},
    "M8": {"d": 8, "pitch": 1.25, "area": 36.6},
    "M10": {"d": 10, "pitch": 1.5, "area": 58.0},
    "M12": {"d": 12, "pitch": 1.75, "area": 84.3},
}


# Классы прочности
GRADES = {
    "4.8": {"tensile": 400, "mat": "MAT-STL_1010_HR", "cost_factor": 1.0},
    "8.8": {"tensile": 800, "mat": "MAT-STL_1045_Q_T", "cost_factor": 1.5},
    "10.9": {"tensile": 1000, "mat": "MAT-STL_4140_Q_T", "cost_factor": 2.0},
}


# Покрытия (Влияют на долговечность)
COATINGS = [
    {"code": "BLK", "name": "Black Oxide", "life": 1.0, "cost": 1.0, "friction": 0.14},
    {"code": "ZN", "name": "Zinc Plated", "life": 5.0, "cost": 1.2, "friction": 0.12}, # Оптимум
    {"code": "HDG", "name": "Hot Dip Galv", "life": 20.0, "cost": 1.8, "friction": 0.15},
]


def generate_fastener(type_name, size_name, size_data, grade_name, grade_data, coating):
    # 1. Расчет нагрузки (только для болтов)
    load_kn = 0
    if type_name == "BOLT":
        load_kn = round((size_data['area'] * grade_data['tensile']) / 1000, 1)
    
    # 2. Расчет веса (упрощенно)
    # Болт 50мм, Гайка ~0.8d, Шайба ~0.15d
    length_factor = 50 if type_name == "BOLT" else (size_data['d'] * 0.8 if type_name == "NUT" else 2)
    weight_g = round((size_data['area'] * length_factor * 7.85) / 1000, 1)
    
    # 3. Синтропия
    # (Нагрузка * Долговечность) / (Вес * Цена)
    # Оцинкованный болт 8.8 - это золотой стандарт.
    utility = (load_kn if load_kn > 0 else 10) * coating['life']
    cost = weight_g * grade_data['cost_factor'] * coating['cost']
    syntropy = round(utility / cost, 2)


    # ID: PART-BOLT_HEX_M8_88_ZN
    id_str = f"PART-{type_name}_HEX_{size_name}_{grade_name.replace('.','')}_{coating['code']}"
    
    name_str = f"Hex {type_name.title()} {size_name}"
    if type_name == "BOLT": name_str += " x 50mm"
    name_str += f" (Gr {grade_name}, {coating['name']})"


    return {
        "ID": id_str,
        "Name": name_str,
        "Description": f"{coating['name']} fastener. Load: {load_kn} kN. Life: {coating['life']}x.",
        "Era": "ERA-04_INDUSTRIAL",
        "Predecessor_ID": "PART-RIVET",
        "Status": "ACTIVE",
        "Syntropy_Score": syntropy,
        "Catalytic_Potential": 5.0,
        "Structural_Pattern": "HELICAL_THREAD" if type_name != "WASHER" else "FLAT_RING",
        "Properties": f"{{'Thread': '{size_name}', 'Friction': '{coating['friction']}', 'Coating': '{coating['name']}'}}",
        "Req_Material": grade_data['mat'],
        "Req_Process": "PROC-MACH_THREAD_ROLLING" if type_name == "BOLT" else "PROC-FORM_STAMPING",
        "Impact_Map": "ASSY-MACHINE:ENABLE:+10",
        "Invention_Reason": "SOC-NEED_ASSEMBLY",
        "Social_Context": "NULL", "Drawbacks": "Corrosion risk" if coating['code']=="BLK" else "None",
        "Side_Effects": "None", "External_Data_Link": "NULL",
        "Req_Infrastructure": "FAC-MACH_THREADER", "Req_Science": "SCI-LAW_FRICTION",
        "Bill_of_Materials": "NULL", "Potential_Realization_Rate": 0.99
    }


def main():
    rows = []
    # Генерируем Болты, Гайки и Шайбы
    for size, s_data in SIZES.items():
        for grade, g_data in GRADES.items():
            for coat in COATINGS:
                # Болты (все варианты)
                rows.append(generate_fastener("BOLT", size, s_data, grade, g_data, coat))
                
                # Гайки (только если покрытие совпадает, чтобы не было гальванопары)
                rows.append(generate_fastener("NUT", size, s_data, grade, g_data, coat))
                
                # Шайбы (обычно из мягкой стали, но для упрощения берем те же)
                if grade == "4.8": # Шайбы обычно простые
                    rows.append(generate_fastener("WASHER", size, s_data, grade, g_data, coat))


    if not os.path.exists(os.path.dirname(TARGET_PATH)): os.makedirs(os.path.dirname(TARGET_PATH))
    with open(TARGET_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Крепеж: Сгенерировано {len(rows)} деталей (Болты, Гайки, Шайбы + Покрытия).")


if __name__ == "__main__":
    main()