import sys
import os
import re
import networkx as nx
from pyvis.network import Network

# --- SETUP PATHS ---
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from malachite.core.loader import MalachiteLoader

def generate_interactive_graph():
    print("🎨 Initializing Visualization Engine...")
    
    # 1. Load Data
    loader = MalachiteLoader(os.path.join(root_dir, "data"))
    G = loader.build_graph()
    
    if len(G.nodes) == 0:
        print("⚠️ Graph is empty! Check your data folder.")
        return

    # 2. Configure PyVis Network
    net = Network(height="95vh", width="100%", bgcolor="#111111", font_color="white", select_menu=True, filter_menu=True, cdn_resources='remote')
    
    # 3. Calculate Centrality
    try:
        centrality = nx.degree_centrality(G)
    except:
        centrality = {n: 1 for n in G.nodes()}

    print("✨ Styling nodes and edges...")

    # 4. Add Nodes
    for node_id in G.nodes():
        nx_node = G.nodes[node_id]
        
        # --- COLOR LOGIC ---
        era = nx_node.get('era', 'UNKNOWN').upper()
        color_map = {
            'ETERNAL':    '#FFD700',
            'INTUITIVE':  '#E67E22',
            'SCIENTIFIC': '#3498DB',
            'ELECTRIC':   '#9B59B6',
            'DIGITAL':    '#2ECC71',
            'UNKNOWN':    '#95A5A6'
        }
        color = color_map.get(era, '#95A5A6')
        size = 15 + (centrality.get(node_id, 0) * 60)

        # --- RICH TOOLTIP (HTML) ---
        parents = list(G.predecessors(node_id))
        parents_str = ", ".join(parents) if parents else "None (Root)"
        
        # HTML Content (используем одинарные кавычки внутри)
        raw_html = (
            f"<div style='font-family: sans-serif; padding: 10px; background-color: white; color: black; border-radius: 5px; min-width: 250px; box-shadow: 0px 0px 10px rgba(0,0,0,0.2);'>"
            f"<h3 style='margin: 0 0 5px 0; border-bottom: 2px solid {color};'>{nx_node.get('name', node_id)}</h3>"
            f"<p style='margin: 3px 0;'><b>ID:</b> {node_id} <span style='color: #666;'>({nx_node.get('type', 'N/A')})</span></p>"
            f"<p style='margin: 3px 0;'><b>Era:</b> {era}</p>"
            f"<p style='margin: 5px 0; font-style: italic; background: #f0f0f0; padding: 5px; border-radius: 3px;'>\"{nx_node.get('trigger', 'No trigger')}\"</p>"
            f"<hr style='border: 0; border-top: 1px solid #ccc; margin: 5px 0;'>"
            f"<p style='margin: 3px 0;'><b>Principle:</b> {nx_node.get('principle', 'N/A')}</p>"
            f"<p style='margin: 3px 0;'><b>Parents:</b> {parents_str}</p>"
            f"</div>"
        )
        
        # Оборачиваем в маркеры @@@ для Regex-замены
        title_with_markers = f"@@@{raw_html}@@@"

        net.add_node(
            node_id, 
            label=nx_node.get('name', node_id),
            title=title_with_markers, 
            color=color,
            size=size,
            borderWidth=1,
            borderWidthSelected=3
        )

    # 5. Add Edges
    for source, target in G.edges():
        net.add_edge(source, target, color='#555555', arrows='to', width=1)

    # 6. Physics
    net.barnes_hut(gravity=-2000, central_gravity=0.3, spring_length=150, spring_strength=0.05, damping=0.09, overlap=0)
    
    # 7. Save
    output_file = os.path.join(root_dir, "malachite_graph.html")
    net.save_graph(output_file)
    
    # --- 8. POST-PROCESSING (CSS & HTML FIX) ---
    print("🔧 Injecting Dark UI & Fixing Tooltips...")
    
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. FIX TOOLTIPS (REGEX METHOD)
    # Находим всё между @@@ и @@@ и чиним экранирование
    def fix_tooltip_content(match):
        inner = match.group(1)
        # Возвращаем угловые скобки
        inner = inner.replace('&lt;', '<').replace('&gt;', '>')
        inner = inner.replace('\\u003c', '<').replace('\\u003e', '>')
        # Экранируем кавычки для JS строки
        inner = inner.replace("'", "\\'")
        return f"'{inner}'"

    # Регулярка ищет: title: (любая кавычка) @@@ (контент) @@@ (любая кавычка)
    content = re.sub(r"title:\s*['\"]?@@@(.*?)(?:@@@)['\"]?", fix_tooltip_content, content, flags=re.DOTALL)

    # B. INJECT DARK CSS (UI FIX)
    # Добавляем стили для панели управления
    dark_ui_css = """
    <style>
        /* Сжимаем и затемняем панель управления */
        .vis-configuration-wrapper {
            background-color: #222 !important;
            color: #eee !important;
            padding: 5px !important;
            border-bottom: 1px solid #444;
            max-height: 150px; /* Ограничиваем высоту */
            overflow-y: auto;
        }
        .vis-filter {
            margin: 2px !important;
            padding: 2px !important;
        }
        /* Стили для выпадающих списков и кнопок */
        select, input, button {
            background-color: #333 !important;
            color: white !important;
            border: 1px solid #555 !important;
            border-radius: 3px;
            padding: 2px 5px;
        }
        /* Убираем лишние отступы */
        .vis-network {
            outline: none;
        }
    </style>
    """
    # Вставляем CSS перед закрывающим тегом head
    content = content.replace('</head>', f'{dark_ui_css}</head>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n🚀 Success! Graph generated at: {output_file}")

if __name__ == "__main__":
    generate_interactive_graph()