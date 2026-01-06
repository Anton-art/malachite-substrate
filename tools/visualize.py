import sys
import os
import networkx as nx
from pyvis.network import Network

# --- SETUP PATHS ---
# Add root directory to path so we can import 'malachite'
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
    # height="100vh" uses full screen height
    # bgcolor="#111111" is a sleek dark mode
    net = Network(height="95vh", width="100%", bgcolor="#111111", font_color="white", select_menu=True, filter_menu=True)
    
    # 3. Calculate Centrality (Influence)
    # Nodes with more descendants will be larger
    try:
        # Degree centrality is faster and good enough for visualization
        centrality = nx.degree_centrality(G)
    except:
        centrality = {n: 1 for n in G.nodes()}

    # 4. Transform NetworkX to PyVis with Custom Styles
    print("✨ Styling nodes and edges...")
    
    for node_id in G.nodes():
        nx_node = G.nodes[node_id]
        
        # --- COLOR LOGIC (The Era Spectrum) ---
        era = nx_node.get('era', 'UNKNOWN').upper()
        color_map = {
            'ETERNAL':    '#FFD700', # Gold (Foundations)
            'INTUITIVE':  '#E67E22', # Orange (Primitive)
            'SCIENTIFIC': '#3498DB', # Blue (Science)
            'MODERN':     '#9B59B6', # Purple (Industrial/Electric)
            'DIGITAL':    '#2ECC71', # Green (Digital)
            'UNKNOWN':    '#95A5A6'  # Grey
        }
        color = color_map.get(era, '#95A5A6')

        # --- SIZE LOGIC ---
        # Base size 15 + Influence bonus
        size = 15 + (centrality.get(node_id, 0) * 100)

        # --- RICH TOOLTIP (HTML) ---
        # This is what appears when you hover
        parents = list(G.predecessors(node_id))
        parents_str = ", ".join(parents) if parents else "None (Root)"
        
        title_html = f"""
        <div style='font-family: sans-serif; padding: 5px; min-width: 200px;'>
            <h3 style='margin: 0; border-bottom: 2px solid {color};'>{nx_node.get('name', node_id)}</h3>
            <p><b>ID:</b> {node_id} <span style='color: #888;'>({nx_node.get('type', 'N/A')})</span></p>
            <p><b>Era:</b> {era}</p>
            <p><i>"{nx_node.get('trigger', 'No trigger data')}"</i></p>
            <hr style='border: 0; border-top: 1px solid #444;'>
            <p><b>Principle:</b> {nx_node.get('principle', 'N/A')}</p>
            <p><b>Tech Make:</b> {nx_node.get('tech_make', 'N/A')}</p>
            <p><b>Parents:</b> {parents_str}</p>
        </div>
        """

        # Add Node to PyVis
        net.add_node(
            node_id, 
            label=nx_node.get('name', node_id),
            title=title_html, # HTML Tooltip
            color=color,
            size=size,
            borderWidth=2,
            borderWidthSelected=4
        )

    # 5. Add Edges (Relationships)
    for source, target in G.edges():
        net.add_edge(
            source, 
            target, 
            color='#555555', 
            arrows='to',
            width=1
        )

    # 6. Physics Configuration (Stabilization)
    # BarnsHut is best for large datasets (200+ nodes)
    net.barnes_hut(
        gravity=-2000,        # Strong repulsion to spread nodes out
        central_gravity=0.3,  # Pull back to center
        spring_length=150,    # Long edges for readability
        spring_strength=0.05,
        damping=0.09,         # High damping stops jittering
        overlap=0
    )
    
    # Add control buttons to tweak physics in UI
    # net.show_buttons(filter_=['physics']) 

    # 7. Save and Open
    output_file = os.path.join(root_dir, "malachite_graph.html")
    net.save_graph(output_file)
    
    print(f"\n🚀 Success! Graph generated at: {output_file}")
    print("   Open this file in your browser to explore the Crystal.")

if __name__ == "__main__":
    generate_interactive_graph()
