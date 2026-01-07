import sys
import os
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
    # cdn_resources='remote' обеспечивает загрузку скриптов из интернета
    net = Network(height="95vh", width="100%", bgcolor="#111111", font_color="white", select_menu=True, filter_menu=True, cdn_resources='remote')
    
    # 3. Calculate Centrality (Influence)
    try:
        centrality = nx.degree_centrality(G)
    except:
        centrality = {n: 1 for n in G.nodes()}

    print("✨ Styling nodes and edges...")
    
    # 4. Add Nodes manually (Custom Styling)
    for node_id in G.nodes():
        nx_node = G.nodes[node_id]
        
        # --- COLOR LOGIC ---
        era = nx_node.get('era', 'UNKNOWN').upper()
        color_map = {
            'ETERNAL':    '#FFD700', # Gold
            'INTUITIVE':  '#E67E22', # Orange
            'SCIENTIFIC': '#3498DB', # Blue
            'ELECTRIC':   '#9B59B6', # Purple
            'DIGITAL':    '#2ECC71', # Green
            'UNKNOWN':    '#95A5A6'  # Grey
        }
        color = color_map.get(era, '#95A5A6')

        # --- SIZE LOGIC ---
        size = 15 + (centrality.get(node_id, 0) * 60)

        # --- RICH TOOLTIP (HTML) ---
        # Важно: убираем переносы строк, чтобы JS не ломался
        parents = list(G.predecessors(node_id))
        parents_str = ", ".join(parents) if parents else "None (Root)"
        
        title_html = f"""
        <div style='font-family: sans-serif; padding: 10px; background-color: white; color: black; border-radius: 5px; min-width: 250px;'>
            <h3 style='margin: 0 0 5px 0; border-bottom: 2px solid {color};'>{nx_node.get('name', node_id)}</h3>
            <p style='margin: 3px 0;'><b>ID:</b> {node_id} <span style='color: #666;'>({nx_node.get('type', 'N/A')})</span></p>
            <p style='margin: 3px 0;'><b>Era:</b> {era}</p>
            <p style='margin: 5px 0; font-style: italic; background: #f0f0f0; padding: 3px;'>"{nx_node.get('trigger', 'No trigger')}"</p>
            <hr style='border: 0; border-top: 1px solid #ccc; margin: 5px 0;'>
            <p style='margin: 3px 0;'><b>Principle:</b> {nx_node.get('principle', 'N/A')}</p>
            <p style='margin: 3px 0;'><b>Parents:</b> {parents_str}</p>
        </div>
        """.replace("\n", "") # <--- ВОТ ЭТО ИСПРАВЛЯЕТ ОШИБКУ

        # Add Node
        net.add_node(
            node_id, 
            label=nx_node.get('name', node_id),
            title=title_html, # Теперь это чистая строка HTML
            color=color,
            size=size,
            borderWidth=1,
            borderWidthSelected=3
        )

    # 5. Add Edges
    for source, target in G.edges():
        net.add_edge(
            source, 
            target, 
            color='#555555', 
            arrows='to',
            width=1
        )

    # 6. Physics Configuration
    net.barnes_hut(
        gravity=-2000,
        central_gravity=0.3,
        spring_length=150,
        spring_strength=0.05,
        damping=0.09,
        overlap=0
    )
    
    # 7. Save
    output_file = os.path.join(root_dir, "malachite_graph.html")
    net.save_graph(output_file)
    print(f"\n🚀 Success! Graph generated at: {output_file}")

if __name__ == "__main__":
    generate_interactive_graph()