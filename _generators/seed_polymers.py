import os
import csv
import random


TARGET_PATH = os.path.join("data_v2", "04_MATERIALS", "Polymers", "Commodity_TP", "index.csv")
HEADERS = ["ID", "Name", "Description", "Era", "Predecessor_ID", "Status", "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern", "Properties", "Chemical_Formula", "Req_Resource", "Req_Process", "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "Impact_Map", "External_Data_Link"]


# Расширенная база полимеров
POLYMERS = [
    # COMMODITY (Дешевые)
    {"code": "PE_HD", "name": "HDPE", "density": 0.95, "tm": 130, "recycle": 1.0, "desc": "Milk jugs, pipes."},
    {"code": "PE_LD", "name": "LDPE", "density": 0.92, "tm": 110, "recycle": 0.8, "desc": "Films, bags."},
    {"code": "PP_HOMO", "name": "Polypropylene", "density": 0.90, "tm": 160, "recycle": 0.9, "desc": "Containers, bumpers."},
    {"code": "PVC_RIGID", "name": "PVC (Rigid)", "density": 1.40, "tm": 160, "recycle": 0.5, "desc": "Pipes, windows."},
    {"code": "PET_BOT", "name": "PET (Bottle)", "density": 1.38, "tm": 250, "recycle": 1.0, "desc": "Water bottles."},
    {"code": "PS_GP", "name": "Polystyrene", "density": 1.05, "tm": 100, "recycle": 0.2, "desc": "Disposable cutlery."},
    
    # ENGINEERING (Дорогие)
    {"code": "ABS_HI", "name": "ABS", "density": 1.04, "tm": 105, "recycle": 0.6, "desc": "Lego bricks, housings."},
    {"code": "PA66", "name": "Nylon 66", "density": 1.14, "tm": 260, "recycle": 0.4, "desc": "Gears, bearings."},
    {"code": "PC_OPT", "name": "Polycarbonate", "density": 1.20, "tm": 150, "recycle": 0.7, "desc": "Lenses, CDs."},
]


def generate_grade(poly, index):
    # Симуляция: MFI (Текучесть)
    mfi = random.choice([0.5, 5.0, 20.0])
    app = "Extrusion (Pipe/Profile)" if mfi < 1 else ("Injection Molding" if mfi > 10 else "General Purpose")
    
    # Синтропия:
    # + Перерабатываемость (Recycle)
    # + Долговечность (Инженерные пластики служат дольше)
    # - Одноразовость (Высокий MFI часто для упаковки)
    base_syn = 1.0
    if poly['code'] in ["ABS_HI", "PA66", "PC_OPT"]: base_syn += 1.0 # Инженерные - герои
    if poly['code'] == "PS_GP": base_syn -= 0.5 # Полистирол - зло (хрупкий, мусор)
    
    syntropy = base_syn * poly['recycle']
    if mfi > 15: syntropy -= 0.3 # Скорее всего упаковка
    
    # Катализ: Инженерные пластики позволяют делать сложные машины
    catalytic = 50.0 if base_syn > 1.5 else 10.0


    return {
        "ID": f"MAT-POLY_{poly['code']}_MFI{int(mfi)}_{index:02d}",
        "Name": f"{poly['name']} (Grade {index})",
        "Description": f"{poly['desc']} MFI: {mfi}. Density: {poly['density']}.",
        "Era": "ERA-05_ELECTRICAL",
        "Predecessor_ID": "MAT-RUBBER_NATURAL",
        "Status": "ACTIVE",
        "Syntropy_Score": round(syntropy, 2),
        "Catalytic_Potential": catalytic,
        "Structural_Pattern": "CHAIN_AMORPHOUS" if "PC" in poly['code'] or "PS" in poly['code'] else "CHAIN_SEMI_CRYSTALLINE",
        "Properties": f"{{'MFI': '{mfi}', 'Density': '{poly['density']} g/cm3', 'Tm': '{poly['tm']} C', 'Recyclable': '{poly['recycle']*100}%'}}",
        "Chemical_Formula": "C-H-O-N Chain",
        "Req_Resource": "RES-FUEL_OIL_BRENT;RES-FUEL_GAS_NGL",
        "Req_Process": "PROC-SYNTH_POLYMERIZATION",
        "Invention_Reason": "SOC-NEED_LIGHTWEIGHT",
        "Social_Context": "MKT-CONSUMER_GOODS",
        "Drawbacks": "Microplastics; UV Degradation",
        "Side_Effects": "Ocean Accumulation",
        "Impact_Map": "ENV-OCEAN:POLLUTE:-10;FAC-MFG:ENABLE:+20",
        "External_Data_Link": "NULL"
    }


def main():
    rows = []
    for poly in POLYMERS:
        for i in range(1, 4): # 3 марки каждого
            rows.append(generate_grade(poly, i))
            
    if not os.path.exists(os.path.dirname(TARGET_PATH)): os.makedirs(os.path.dirname(TARGET_PATH))
    with open(TARGET_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Полимеры: Сгенерировано {len(rows)} марок (Commodity + Engineering).")


if __name__ == "__main__":
    main()