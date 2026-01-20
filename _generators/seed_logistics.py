import os
import csv


# =================================================================================
# НАСТРОЙКИ
# =================================================================================
BASE_DIR = os.path.join("data_v2", "06_PROCESSES", "Logistics")


PATHS = {
    "MODES": os.path.join(BASE_DIR, "Transport_Modes", "index.csv"),
    "ROUTES": os.path.join(BASE_DIR, "Infrastructure", "index.csv") # Порты, Хабы
}


HEADERS = [
    "ID", "Name", "Description", "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", "Drawbacks", "Side_Effects", "Impact_Map",
    "Scarcity_Score", "Properties", "External_Data_Link",
    "Input_State", "Output_State", "Physics_Law", "Energy_Type", "Energy_Cost_Estimate", "Req_Infrastructure"
]


# =================================================================================
# ДАННЫЕ
# =================================================================================


TRANSPORT_MODES = [
    # МОРЕ (Самая высокая синтропия - дешево везти много груза)
    {"code": "SEA_BULK", "name": "Bulk Shipping", "era": "ERA-04_INDUSTRIAL", "syn": 8.0, "nrg": "Low", "desc": "Transport of raw materials (ore, coal) by sea."},
    {"code": "SEA_CONTAINER", "name": "Container Shipping", "era": "ERA-05_ELECTRICAL", "syn": 10.0, "nrg": "Low", "desc": "Standardized intermodal freight."},
    
    # ЖЕЛЕЗНАЯ ДОРОГА (Эффективность на суше)
    {"code": "RAIL_FREIGHT", "name": "Rail Freight", "era": "ERA-04_INDUSTRIAL", "syn": 6.0, "nrg": "Medium", "desc": "Heavy overland transport."},
    
    # ДОРОГИ (Гибкость, но низкая эффективность)
    {"code": "ROAD_TRUCKING", "name": "Road Trucking", "era": "ERA-05_ELECTRICAL", "syn": 2.0, "nrg": "High", "desc": "Last mile delivery."},
    
    # ТРУБЫ (Идеально для жидкостей)
    {"code": "PIPELINE_FLOW", "name": "Pipeline Transport", "era": "ERA-05_ELECTRICAL", "syn": 15.0, "nrg": "Very Low", "desc": "Continuous flow of oil/gas/water."},
    
    # АВИА (Скорость, но ужасная эффективность)
    {"code": "AIR_CARGO", "name": "Air Freight", "era": "ERA-06_DIGITAL", "syn": 0.5, "nrg": "Extreme", "desc": "High value, time-critical goods."},
]


INFRASTRUCTURE = [
    {"code": "PORT_TERMINAL", "name": "Seaport Terminal", "era": "ERA-04_INDUSTRIAL", "desc": "Interface between sea and land."},
    {"code": "RAIL_YARD", "name": "Rail Marshalling Yard", "era": "ERA-04_INDUSTRIAL", "desc": "Train assembly area."},
    {"code": "WAREHOUSE_AUTO", "name": "Automated Warehouse", "era": "ERA-06_DIGITAL", "desc": "Robotic storage facility."},
]


def generate_modes():
    rows = []
    for t in TRANSPORT_MODES:
        row = {
            "ID": f"PROC-LOG_{t['code']}",
            "Name": t['name'],
            "Description": t['desc'],
            "Era": t['era'],
            "Predecessor_ID": "PROC-LOG_ANIMAL_CART", # Гужевой транспорт
            "Status": "ACTIVE",
            "Syntropy_Score": t['syn'],
            "Catalytic_Potential": 20.0, # Логистика связывает мир
            "Structural_Pattern": "NETWORK_EDGE",
            "Invention_Reason": "SOC-NEED_TRADE",
            "Social_Context": "MKT-GLOBALIZATION",
            "Drawbacks": "Emissions",
            "Side_Effects": "Invasive Species",
            "Impact_Map": "SOC-ECONOMY:ACCELERATE:+10",
            "Scarcity_Score": 0.0,
            "Properties": "{'Range': 'Global', 'Speed': 'Variable'}",
            "External_Data_Link": "NULL",
            "Input_State": "SOLID_CARGO",
            "Output_State": "SOLID_CARGO",
            "Physics_Law": "SCI-LAW_NEWTON_2",
            "Energy_Type": "KINETIC",
            "Energy_Cost_Estimate": t['nrg'],
            "Req_Infrastructure": "FAC-GENERIC" # Упрощение пока
        }
        rows.append(row)
    return rows


def generate_infra():
    # Это процессы управления инфраструктурой (не сами здания, а процессы их работы)
    rows = []
    for i in INFRASTRUCTURE:
        row = {
            "ID": f"PROC-LOG_OPS_{i['code']}",
            "Name": f"{i['name']} Operations",
            "Description": i['desc'],
            "Era": i['era'],
            "Predecessor_ID": "PROC-LOG_STORAGE_SIMPLE",
            "Status": "ACTIVE",
            "Syntropy_Score": 3.0,
            "Catalytic_Potential": 10.0,
            "Structural_Pattern": "NETWORK_NODE",
            "Invention_Reason": "SOC-NEED_STORAGE",
            "Social_Context": "MKT-LOGISTICS",
            "Drawbacks": "Land Use",
            "Side_Effects": "None",
            "Impact_Map": "PROC-LOG_SEA_CONTAINER:ENABLE:+100",
            "Scarcity_Score": 0.0,
            "Properties": "{}",
            "External_Data_Link": "NULL",
            "Input_State": "VARIES",
            "Output_State": "VARIES",
            "Physics_Law": "NULL",
            "Energy_Type": "ELECTRIC",
            "Energy_Cost_Estimate": "Medium",
            "Req_Infrastructure": "FAC-GENERIC"
        }
        rows.append(row)
    return rows


def main():
    print("🚚 Генерация Логистических Сетей...")
    
    tasks = {
        "MODES": generate_modes(),
        "ROUTES": generate_infra()
    }
    
    for key, data in tasks.items():
        path = PATHS[key]
        if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
        
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
            
    print(f"✅ Логистика добавлена ({len(tasks['MODES']) + len(tasks['ROUTES'])} объектов).")


if __name__ == "__main__":
    main()