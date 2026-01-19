import sys
import os
import json
import networkx as nx
from pyvis.network import Network

# --- SETUP PATHS ---
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from malachite.core.loader import MalachiteLoader

def generate_interactive_graph():
    print("🎨 Initializing Cyberpunk UI Engine (Direct Generation Mode)...")
    
    # 1. Load Data
    loader = MalachiteLoader(os.path.join(root_dir, "data"))
    G = loader.build_graph()
    
    if len(G.nodes) == 0:
        print("⚠️ Graph is empty!")
        return

    # 2. Calculate Centrality for sizing
    try:
        centrality = nx.degree_centrality(G)
    except:
        centrality = {n: 1 for n in G.nodes()}

    # 3. Prepare Data for Vis.js
    nodes_data = []
    edges_data = []

    print("✨ Processing nodes and edges...")

    for node_id in G.nodes():
        nx_node = G.nodes[node_id]
        era = nx_node.get('era', 'UNKNOWN').upper()
        
        # Color Logic
        color_map = {
            'ETERNAL':    '#ffd700', 
            'INTUITIVE':  '#d2a8ff', 
            'SCIENTIFIC': '#58a6ff', 
            'ELECTRIC':   '#bc8cff', 
            'DIGITAL':    '#3fb950', 
            'UNKNOWN':    '#8b949e'
        }
        color = color_map.get(era, '#8b949e')
        size = 20 + (centrality.get(node_id, 0) * 60)

        # Metadata for Sidebar
        metadata = {
            "id": node_id,
            "name": nx_node.get('name', node_id),
            "type": nx_node.get('type', 'N/A'),
            "era": era,
            "trigger": nx_node.get('trigger', 'N/A'),
            "principle": nx_node.get('principle', 'N/A'),
            "parents": list(G.predecessors(node_id))
        }

        nodes_data.append({
            "id": node_id,
            "label": nx_node.get('name', node_id),
            "color": color,
            "size": size,
            "title": "", # Оставляем пустым, чтобы не было стандартного тултипа!
            "metadata": metadata, # Наши данные для JS
            "font": {'face': 'Inter', 'color': '#c9d1d9', 'size': 14, 'strokeWidth': 0}
        })

    for source, target in G.edges():
        edges_data.append({
            "from": source,
            "to": target,
            "color": '#30363d',
            "width": 1,
            "arrows": "to"
        })

    # 4. Generate HTML Content Directly
    # Мы вставляем JSON данные прямо в переменную JS внутри HTML
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Malachite Graph</title>
    <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: 'Inter', sans-serif; background: #0d1117; color: #c9d1d9; }}
        
        /* Layout */
        .app-container {{ display: flex; height: 100vh; width: 100vw; }}
        .graph-area {{ flex-grow: 1; position: relative; background: #0d1117; }}
        #mynetwork {{ width: 100%; height: 100%; border: none; outline: none; }}
        
        /* Sidebar */
        .sidebar {{
            width: 400px;
            background: #161b22;
            border-left: 1px solid #30363d;
            display: flex;
            flex-direction: column;
            box-shadow: -5px 0 15px rgba(0,0,0,0.3);
            z-index: 10;
        }}
        
        .sidebar-header {{ padding: 20px; background: #21262d; border-bottom: 1px solid #30363d; }}
        .node-id {{ font-size: 20px; font-weight: 600; color: #fff; margin: 0; word-break: break-word; }}
        .node-type {{ font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }}
        
        .sidebar-content {{ padding: 20px; overflow-y: auto; flex-grow: 1; }}
        .info-group {{ margin-bottom: 20px; }}
        .label {{ font-size: 11px; color: #8b949e; margin-bottom: 6px; display: block; text-transform: uppercase; font-weight: 600; }}
        .value {{ font-size: 14px; color: #e6edf3; background: #0d1117; padding: 10px; border-radius: 6px; border: 1px solid #30363d; line-height: 1.5; }}
        
        .tag {{ display: inline-block; padding: 4px 10px; border-radius: 15px; font-size: 12px; font-weight: 600; margin-right: 5px; margin-bottom: 5px; }}
        .tag-era {{ background: rgba(56, 139, 253, 0.1); color: #58a6ff; border: 1px solid rgba(56, 139, 253, 0.3); }}
        .tag-parent {{ background: #21262d; color: #c9d1d9; border: 1px solid #30363d; cursor: pointer; transition: all 0.2s; }}
        .tag-parent:hover {{ background: #30363d; border-color: #8b949e; }}

        /* Search Bar */
        .search-container {{
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 5;
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 10px 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            width: 320px;
        }}
        .search-icon {{ color: #8b949e; margin-right: 10px; }}
        #search-input {{ background: transparent; border: none; color: #fff; width: 100%; outline: none; font-size: 14px; font-family: 'Inter', sans-serif; }}
        
        /* Hide default tooltip */
        div.vis-tooltip {{ display: none !important; }}
        
        /* Scrollbar */
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #0d1117; }}
        ::-webkit-scrollbar-thumb {{ background: #30363d; border-radius: 4px; }}
    </style>
</head>
<body>
    <div class="app-container">
        <div class="graph-area">
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="search-input" placeholder="Search nodes (ID or Name)...">
            </div>
            <div id="mynetwork"></div>
        </div>
        
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h1 class="node-id" id="detail-id">Malachite Graph</h1>
                <div class="node-type" id="detail-type">System Ready</div>
            </div>
            
            <div class="sidebar-content" id="detail-content">
                <div style="text-align: center; color: #8b949e; margin-top: 50px;">
                    <p>Select a node to inspect details.</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 1. INJECT DATA FROM PYTHON
        const nodesData = {json.dumps(nodes_data)};
        const edgesData = {json.dumps(edges_data)};

        // 2. SETUP VIS.JS
        const container = document.getElementById('mynetwork');
        const data = {{
            nodes: new vis.DataSet(nodesData),
            edges: new vis.DataSet(edgesData)
        }};
        const options = {{
            nodes: {{
                shape: 'dot',
                font: {{ size: 16, color: '#ffffff' }},
                borderWidth: 2
            }},
            edges: {{
                width: 1,
                smooth: {{ type: 'continuous' }}
            }},
            physics: {{
                stabilization: false,
                barnesHut: {{
                    gravitationalConstant: -3000,
                    springLength: 200,
                    springConstant: 0.04
                }}
            }},
            interaction: {{
                hover: true,
                tooltipDelay: 3600000 // Disable default tooltip effectively
            }}
        }};

        const network = new vis.Network(container, data, options);

        // 3. EVENT HANDLING
        network.on("click", function (params) {{
            if (params.nodes.length > 0) {{
                const nodeId = params.nodes[0];
                const node = data.nodes.get(nodeId);
                updateSidebar(node.metadata);
            }} else {{
                resetSidebar();
            }}
        }});

        function updateSidebar(meta) {{
            document.getElementById('detail-id').innerText = meta.name;
            document.getElementById('detail-type').innerText = meta.id + " • " + meta.type;
            
            let parentsHtml = meta.parents.map(p => 
                `<span class="tag tag-parent" onclick="focusNode('${{p}}')">${{p}}</span>`
            ).join('');
            
            if (!parentsHtml) parentsHtml = "<span style='color:#8b949e; font-size:12px;'>Root Technology</span>";

            const html = `
                <div class="info-group">
                    <span class="label">Era</span>
                    <span class="tag tag-era">${{meta.era}}</span>
                </div>
                <div class="info-group">
                    <span class="label">Trigger / Cause</span>
                    <div class="value">${{meta.trigger}}</div>
                </div>
                <div class="info-group">
                    <span class="label">Operating Principle</span>
                    <div class="value">${{meta.principle}}</div>
                </div>
                <div class="info-group">
                    <span class="label">Parents (Dependencies)</span>
                    <div style="margin-top: 8px;">${{parentsHtml}}</div>
                </div>
            `;
            document.getElementById('detail-content').innerHTML = html;
        }}

        function resetSidebar() {{
            document.getElementById('detail-id').innerText = "Malachite Graph";
            document.getElementById('detail-type').innerText = "System Ready";
            document.getElementById('detail-content').innerHTML = `
                <div style="text-align: center; color: #8b949e; margin-top: 50px;">
                    <p>Select a node to inspect details.</p>
                </div>`;
        }}

        // 4. SEARCH FUNCTIONALITY
        document.getElementById('search-input').addEventListener('input', function(e) {{
            const term = e.target.value.toLowerCase();
            if(term.length < 2) return;
            
            const allNodes = data.nodes.get();
            const found = allNodes.find(n => 
                n.id.toLowerCase().includes(term) || 
                n.label.toLowerCase().includes(term)
            );
            
            if(found) {{
                focusNode(found.id);
            }}
        }});

        // Global function for parent tags
        window.focusNode = function(nodeId) {{
            network.focus(nodeId, {{ scale: 1.2, animation: true }});
            network.selectNodes([nodeId]);
            const node = data.nodes.get(nodeId);
            if(node) updateSidebar(node.metadata);
        }};
    </script>
</body>
</html>
    """

    # 5. Write File
    output_file = os.path.join(root_dir, "malachite_graph.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n🚀 Cyberpunk Graph generated at: {output_file}")

if __name__ == "__main__":
    generate_interactive_graph()