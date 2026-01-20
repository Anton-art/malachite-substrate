import os
import csv
from pyvis.network import Network

# =================================================================================
# КОНФИГУРАЦИЯ
# =================================================================================

ROOT_DIR = "data_v2"
OUTPUT_FILE = "malachite_holoscope.html"

# Цвета Узлов (Neon Palette)
NODE_COLORS = {
    "SCI":  "#00FFFF", # Cyan (Наука)
    "RES":  "#FF8C00", # DarkOrange (Ресурсы)
    "MAT":  "#E0E0E0", # Platinum (Материалы)
    "PROC": "#FFD700", # Gold (Процессы)
    "FAC":  "#FF4500", # OrangeRed (Заводы)
    "GRID": "#FF4500", # Энергия
    "PART": "#BA55D3", # MediumOrchid (Детали)
    "ASSY": "#9932CC", # DarkOrchid (Сборки)
    "SOC":  "#00FF7F", # SpringGreen (Общество)
    "MKT":  "#00FF7F", # Рынок
    "DEFAULT": "#808080"
}

# Цвета Связей (Semantic Edges)
EDGE_STYLES = {
    "PHYSICAL":  {"color": "#FF8C00", "dashes": False, "opacity": 0.4}, # Поток материи (Оранжевый)
    "LOGICAL":   {"color": "#00FFFF", "dashes": False, "opacity": 0.3}, # Поток знаний (Голубой)
    "INFRA":     {"color": "#FF4500", "dashes": False, "opacity": 0.3}, # Энергия/Станки (Красный)
    "IMPACT":    {"color": "#00FF7F", "dashes": True,  "opacity": 0.6}, # Влияние (Зеленый пунктир)
    "EVOLUTION": {"color": "#808080", "dashes": True,  "opacity": 0.2}  # Наследие (Серый)
}

# Карта колонок к типам связей
COLUMN_MAP = {
    "Req_Resource": "PHYSICAL",
    "Req_Material": "PHYSICAL",
    "Bill_of_Materials": "PHYSICAL",
    "Req_Process": "LOGICAL",
    "Req_Science": "LOGICAL",
    "Req_Infrastructure": "INFRA",
    "Power_Source": "INFRA",
    "Predecessor_ID": "EVOLUTION",
    "Impact_Map": "IMPACT"
}

# =================================================================================
# ЛОГИКА
# =================================================================================

def get_node_size(row):
    size = 15
    try:
        syn = float(row.get("Syntropy_Score", 1.0))
        if syn > 50: size = 35
        elif syn > 10: size = 25
        elif syn < 0: size = 10
    except: pass
    
    # Катализаторы важнее
    try:
        cat = float(row.get("Catalytic_Potential", 0.0))
        if cat > 20: size += 5
    except: pass
    return size

def build_graph():
    print("🔭 Инициализация Голоскопа v2.0 (Semantic Edges)...")
    
    # Настройки UI: темная тема, кнопки управления физикой
    net = Network(height="95vh", width="100%", bgcolor="#0E1117", font_color="#cccccc", select_menu=True, filter_menu=True)
    
    # Тонкая настройка физики для "Технологического Древа"
    # Увеличили spring_length, чтобы граф "дышал"
    net.barnes_hut(gravity=-10000, central_gravity=0.1, spring_length=250, spring_strength=0.04, damping=0.09)

    nodes = {}
    edges = []

    print("   - Сканирование data_v2...")
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if "index.csv" in filenames:
            path = os.path.join(dirpath, "index.csv")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if not row.get("ID"): continue
                        obj_id = row["ID"]
                        
                        # Богатый Tooltip
                        tooltip = (
                            f"<div style='font-family: monospace; padding: 5px;'>"
                            f"<b style='font-size: 14px; color: white;'>{row.get('Name')}</b><br>"
                            f"<hr style='border-color: #444;'>"
                            f"🆔 {obj_id}<br>"
                            f"📅 {row.get('Era')}<br>"
                            f"⚡ Syntropy: <span style='color: {'#0f0' if float(row.get('Syntropy_Score',0))>0 else '#f00'}'>{row.get('Syntropy_Score')}</span><br>"
                            f"🧩 Pattern: {row.get('Structural_Pattern', 'N/A')}<br>"
                            f"<br><i>{row.get('Description')}</i>"
                            f"</div>"
                        )

                        prefix = obj_id.split('-')[0]
                        nodes[obj_id] = {
                            "id": obj_id,
                            "label": row.get("Name"),
                            "title": tooltip,
                            "color": NODE_COLORS.get(prefix, NODE_COLORS["DEFAULT"]),
                            "size": get_node_size(row),
                            "shape": "star" if prefix == "RES" and "ORE" in obj_id else "dot" # Руды как звезды
                        }

                        # Обработка связей
                        for col, style_key in COLUMN_MAP.items():
                            val = row.get(col)
                            if val and val != "NULL":
                                targets = val.split(';')
                                for t in targets:
                                    clean_t = t.split(':')[0].strip()
                                    if not clean_t: continue
                                    
                                    style = EDGE_STYLES[style_key]
                                    
                                    # ЛОГИКА НАПРАВЛЕНИЯ
                                    if col == "Impact_Map":
                                        # Влияние: Я -> Цель (Source -> Target)
                                        edges.append({
                                            "src": obj_id, "dst": clean_t, 
                                            "color": style["color"], 
                                            "dashes": style["dashes"],
                                            "width": 1
                                        })
                                    else:
                                        # Зависимость: Цель -> Я (Target -> Source)
                                        # "Мне нужен Ресурс", значит Ресурс течет ко мне
                                        edges.append({
                                            "src": clean_t, "dst": obj_id, 
                                            "color": style["color"], 
                                            "dashes": style["dashes"],
                                            "width": 1 if style_key == "EVOLUTION" else 2
                                        })

            except Exception as e:
                print(f"⚠️ Ошибка в {path}: {e}")

    print(f"   - Рендеринг {len(nodes)} узлов и {len(edges)} связей...")

    for n in nodes.values():
        net.add_node(n["id"], label=n["label"], title=n["title"], color=n["color"], size=n["size"], shape=n["shape"])

    for e in edges:
        if e["src"] in nodes and e["dst"] in nodes:
            net.add_edge(e["src"], e["dst"], color=e["color"], dashes=e["dashes"], width=e["width"])

    print(f"💾 Сохранение в {OUTPUT_FILE}...")
    net.save_graph(OUTPUT_FILE)
    print("✅ Готово! Откройте HTML файл.")

if __name__ == "__main__":
    build_graph()