import os
import csv
from pyvis.network import Network

# =================================================================================
# КОНФИГУРАЦИЯ
# =================================================================================

ROOT_DIR = "data_v2"
OUTPUT_FILE = "malachite_holoscope.html"

# Цвета (Строгий Neon)
NODE_COLORS = {
    "SCI":  "#00FFFF", # Cyan (Наука)
    "RES":  "#FF8C00", # DarkOrange (Ресурсы)
    "MAT":  "#E0E0E0", # Platinum (Материалы)
    "PROC": "#FFD700", # Gold (Процессы)
    "FAC":  "#FF4500", # OrangeRed (Заводы)
    "GRID": "#FF4500", # Энергия
    "PART": "#BA55D3", # MediumOrchid (Детали)
    "ASSY": "#9932CC", # DarkOrchid (Сборки)
    "PROD": "#9400D3", # DarkViolet (Изделия)
    "SOC":  "#00FF7F", # SpringGreen (Общество)
    "MKT":  "#00FF7F", # Рынок
    "DEFAULT": "#696969"
}

# Типы связей
COLUMN_MAP = {
    "Req_Resource":      {"color": "#FF8C00", "width": 1.5, "dashes": False}, # Поток материи
    "Req_Material":      {"color": "#FF8C00", "width": 1.5, "dashes": False},
    "Bill_of_Materials": {"color": "#BA55D3", "width": 2.0, "dashes": False}, # Сборка
    "Req_Process":       {"color": "#FFD700", "width": 1.0, "dashes": True},  # Технология
    "Req_Science":       {"color": "#00FFFF", "width": 1.0, "dashes": True},  # Знание
    "Req_Infrastructure":{"color": "#FF4500", "width": 1.0, "dashes": True},  # Энергия/Место
    "Power_Source":      {"color": "#FF0000", "width": 1.5, "dashes": False}, # Питание
    "Predecessor_ID":    {"color": "#444444", "width": 0.5, "dashes": [5, 5]},# Эволюция
    "Impact_Map":        {"color": "#00FF7F", "width": 1.5, "dashes": [2, 2]} # Влияние
}

def get_node_size(row):
    try:
        syn = float(row.get("Syntropy_Score", 0))
        if syn > 50: return 30
        if syn > 10: return 20
        if syn < 0: return 10
    except: pass
    return 15

def build_graph():
    print("🔭 Рендеринг Голоскопа v3.0 (Stable Physics)...")
    
    # 1. Инициализация
    net = Network(height="95vh", width="100%", bgcolor="#0b0c10", font_color="#c5c6c7", select_menu=True, filter_menu=True)
    
    # 2. НАСТРОЙКА ФИЗИКИ (УСМИРЕНИЕ ОДУВАНЧИКА)
    # forceAtlas2Based - лучший алгоритм для больших графов.
    # damping=0.9 - очень быстрое затухание колебаний.
    net.force_atlas_2based(
        gravity=-100, 
        central_gravity=0.005, 
        spring_length=100, 
        spring_strength=0.08, 
        damping=0.95, 
        overlap=0
    )
    
    # Включаем кнопки управления, чтобы пользователь мог нажать "Stop"
    net.show_buttons(filter_=['physics'])

    nodes = {}
    edges = []

    # 3. Сканирование
    print("   - Чтение данных...")
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if "index.csv" in filenames:
            path = os.path.join(dirpath, "index.csv")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if not row.get("ID"): continue
                        obj_id = row["ID"]
                        
                        # Tooltip
                        tooltip = (
                            f"ID: {obj_id}\n"
                            f"Name: {row.get('Name')}\n"
                            f"Era: {row.get('Era')}\n"
                            f"Syntropy: {row.get('Syntropy_Score')}"
                        )

                        prefix = obj_id.split('-')[0]
                        nodes[obj_id] = {
                            "id": obj_id,
                            "label": "  " + row.get("Name"), # Отступ для красоты
                            "title": tooltip,
                            "color": NODE_COLORS.get(prefix, NODE_COLORS["DEFAULT"]),
                            "size": get_node_size(row),
                            "shape": "dot"
                        }

                        # Связи
                        for col, style in COLUMN_MAP.items():
                            val = row.get(col)
                            if val and val != "NULL":
                                targets = val.split(';')
                                for t in targets:
                                    clean_t = t.split(':')[0].strip()
                                    if not clean_t: continue
                                    
                                    # Направление стрелок
                                    if col in ["Impact_Map"]:
                                        src, dst = obj_id, clean_t
                                    else:
                                        src, dst = clean_t, obj_id # Ресурс -> Продукт
                                        
                                    edges.append({
                                        "src": src, "dst": dst,
                                        "color": style["color"],
                                        "width": style["width"],
                                        "dashes": style["dashes"]
                                    })

            except Exception as e:
                print(f"⚠️ Ошибка в {path}: {e}")

    # 4. Сборка
    print(f"   - Узлов: {len(nodes)}, Связей: {len(edges)}")
    
    for n in nodes.values():
        net.add_node(n["id"], label=n["label"], title=n["title"], color=n["color"], size=n["size"], shape=n["shape"])

    for e in edges:
        if e["src"] in nodes and e["dst"] in nodes:
            net.add_edge(e["src"], e["dst"], color=e["color"], width=e["width"], dashes=e["dashes"])

    # 5. Сохранение
    net.save_graph(OUTPUT_FILE)
    print(f"✅ Готово: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_graph()
