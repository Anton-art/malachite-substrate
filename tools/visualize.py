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
    print("🎨 Initializing Cyberpunk UI Engine...")
    
    # 1. Load Data
    loader = MalachiteLoader(os.path.join(root_dir, "data"))
    G = loader.build_graph()
    
    if len(G.nodes) == 0:
        print("⚠️ Graph is empty!")
        return

    # 2. Configure PyVis
    # Отключаем дефолтный UI PyVis, мы сделаем свой
    net = Network(height="100vh", width="100%", bgcolor="#0d1117", font_color="#c9d1d9", select_menu=False, filter_menu=False, cdn_resources='remote')
    
    # 3. Centrality & Styling
    try:
        centrality = nx.degree_centrality(G)
    except:
        centrality = {n: 1 for n in G.nodes()}

    print("✨ Styling nodes...")

    for node_id in G.nodes():
        nx_node = G.nodes[node_id]
        era = nx_node.get('era', 'UNKNOWN').upper()
        
        # Цветовая схема под "Dark UI"
        color_map = {
            'ETERNAL':    '#ffd700', 
            'INTUITIVE':  '#d2a8ff', 
            'SCIENTIFIC': '#58a6ff', 
            'ELECTRIC':   '#bc8cff', 
            'DIGITAL':    '#3fb950', 
            'UNKNOWN':    '#8b949e'
        }
        color = color_map.get(era, '#8b949e')
        size = 20 + (centrality.get(node_id, 0) * 50)

        # Подготавливаем данные для Sidebar (скрываем их в скрытом поле title, чтобы JS мог их прочитать)
        # Мы используем JSON внутри title, чтобы потом распарсить его в JS
        node_data = {
            "id": node_id,
            "name": nx_node.get('name', node_id),
            "type": nx_node.get('type', 'N/A'),
            "era": era,
            "trigger": nx_node.get('trigger', 'N/A'),
            "principle": nx_node.get('principle', 'N/A'),
            "parents": list(G.predecessors(node_id))
        }
        json_data = json.dumps(node_data).replace('"', '&quot;')

        net.add_node(
            node_id, 
            label=nx_node.get('name', node_id),
            title=json_data, # Храним данные здесь
            color=color,
            size=size,
            borderWidth=1,
            borderWidthSelected=2,
            font={'face': 'Segoe UI', 'color': '#c9d1d9', 'size': 14}
        )

    for source, target in G.edges():
        net.add_edge(source, target, color='#30363d', width=1)

    # Physics
    net.barnes_hut(gravity=-3000, central_gravity=0.1, spring_length=200, spring_strength=0.04, damping=0.09)
    
    # 4. Save raw file
    output_file = os.path.join(root_dir, "malachite_graph.html")
    net.save_graph(output_file)
    
    # --- 5. INJECT CUSTOM UI (THE MAGIC) ---
    print("🔧 Injecting Dashboard Interface...")
    
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # CSS STYLES (Dark Theme / Sidebar)
    custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        
        body, html { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: 'Inter', sans-serif; background: #0d1117; }
        
        /* Layout */
        .app-container { display: flex; height: 100vh; width: 100vw; }
        .graph-area { flex-grow: 1; position: relative; background: #0d1117; }
        #mynetwork { width: 100%; height: 100%; border: none; outline: none; }
        
        /* Sidebar */
        .sidebar {
            width: 400px;
            background: #161b22;
            border-left: 1px solid #30363d;
            display: flex;
            flex-direction: column;
            color: #c9d1d9;
            box-shadow: -5px 0 15px rgba(0,0,0,0.3);
            z-index: 10;
            transition: transform 0.3s ease;
        }
        
        .sidebar-header {
            padding: 20px;
            background: #21262d;
            border-bottom: 1px solid #30363d;
        }
        .node-id { font-size: 24px; font-weight: 600; color: #fff; margin: 0; word-break: break-all; }
        .node-type { font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
        
        /* Tabs */
        .tabs { display: flex; border-bottom: 1px solid #30363d; background: #161b22; }
        .tab { padding: 12px 20px; cursor: pointer; font-size: 14px; color: #8b949e; border-bottom: 2px solid transparent; }
        .tab.active { color: #58a6ff; border-bottom: 2px solid #58a6ff; }
        
        /* Content */
        .sidebar-content { padding: 20px; overflow-y: auto; flex-grow: 1; }
        .info-group { margin-bottom: 20px; }
        .label { font-size: 12px; color: #8b949e; margin-bottom: 4px; display: block; }
        .value { font-size: 14px; color: #e6edf3; background: #21262d; padding: 8px 12px; border-radius: 6px; border: 1px solid #30363d; word-wrap: break-word;}
        
        .tag { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-right: 5px; margin-bottom: 5px; }
        .tag-era { background: rgba(56, 139, 253, 0.15); color: #58a6ff; border: 1px solid rgba(56, 139, 253, 0.4); }
        .tag-parent { background: rgba(171, 174, 181, 0.15); color: #c9d1d9; border: 1px solid #30363d; cursor: pointer; }
        .tag-parent:hover { background: #30363d; }

        /* Search Bar */
        .search-container {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 5;
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 8px 12px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            width: 300px;
        }
        .search-icon { color: #8b949e; margin-right: 10px; }
        #search-input { background: transparent; border: none; color: #fff; width: 100%; outline: none; font-size: 14px; }
        
        /* Empty State */
        .empty-state { text-align: center; color: #8b949e; margin-top: 50px; }
        
        /* Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0d1117; }
        ::-webkit-scrollbar-thumb { background: #30363d; border-radius: 4px; }
    </style>
    """

    # HTML STRUCTURE
    custom_html = """
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
                <h1 class="node-id" id="detail-id">Select a Node</h1>
                <div class="node-type" id="detail-type">Waiting for input...</div>
            </div>
            
            <div class="tabs">
                <div class="tab active">Details</div>
                <div class="tab">Lineage</div>
            </div>
            
            <div class="sidebar-content" id="detail-content">
                <div class="empty-state">
                    <p>Click on any node in the graph to view its details, history, and technological dependencies.</p>
                </div>
            </div>
        </div>
    </div>
    """

    # JAVASCRIPT LOGIC
    custom_js = """
    <script>
        // Ждем загрузки сети PyVis
        setTimeout(function() {
            var network = network; // PyVis создает глобальную переменную network
            
            // 1. Обработка клика
            network.on("click", function (params) {
                if (params.nodes.length > 0) {
                    var nodeId = params.nodes[0];
                    var nodeData = nodes.get(nodeId); // nodes - глобальный DataSet PyVis
                    
                    if (nodeData && nodeData.title) {
                        try {
                            // Мы спрятали JSON в title, теперь достаем
                            var data = JSON.parse(nodeData.title);
                            updateSidebar(data);
                        } catch(e) {
                            console.error("Error parsing node data", e);
                        }
                    }
                } else {
                    // Клик в пустоту
                    resetSidebar();
                }
            });

            // 2. Функция обновления Sidebar
            function updateSidebar(data) {
                document.getElementById('detail-id').innerText = data.name;
                document.getElementById('detail-type').innerText = data.id + " • " + data.type;
                
                var parentsHtml = data.parents.map(p => `<span class="tag tag-parent" onclick="focusNode('${p}')">${p}</span>`).join('');
                if (!parentsHtml) parentsHtml = "<span class='label'>Root Technology</span>";

                var html = `
                    <div class="info-group">
                        <span class="label">Era</span>
                        <span class="tag tag-era">${data.era}</span>
                    </div>
                    <div class="info-group">
                        <span class="label">Trigger / Cause</span>
                        <div class="value">${data.trigger}</div>
                    </div>
                    <div class="info-group">
                        <span class="label">Operating Principle</span>
                        <div class="value">${data.principle}</div>
                    </div>
                    <div class="info-group">
                        <span class="label">Parents (Dependencies)</span>
                        <div style="margin-top: 5px;">${parentsHtml}</div>
                    </div>
                `;
                document.getElementById('detail-content').innerHTML = html;
            }

            // 3. Сброс
            function resetSidebar() {
                document.getElementById('detail-id').innerText = "Malachite Graph";
                document.getElementById('detail-type').innerText = "System Overview";
                document.getElementById('detail-content').innerHTML = `
                    <div class="empty-state">
                        <p>Select a node to inspect its properties.</p>
                    </div>`;
            }
            
            // 4. Поиск
            document.getElementById('search-input').addEventListener('input', function(e) {
                var term = e.target.value.toLowerCase();
                if(term.length < 2) return;
                
                var allNodes = nodes.get();
                var found = allNodes.find(n => 
                    n.id.toLowerCase().includes(term) || 
                    (n.label && n.label.toLowerCase().includes(term))
                );
                
                if(found) {
                    network.focus(found.id, { scale: 1.2, animation: true });
                    network.selectNodes([found.id]);
                    // Триггерим клик программно
                    var data = JSON.parse(found.title);
                    updateSidebar(data);
                }
            });

            // Глобальная функция для клика по тегам родителей
            window.focusNode = function(nodeId) {
                network.focus(nodeId, { scale: 1.2, animation: true });
                network.selectNodes([nodeId]);
                var nodeData = nodes.get(nodeId);
                if(nodeData) updateSidebar(JSON.parse(nodeData.title));
            };

        }, 1000); // Небольшая задержка для инициализации
    </script>
    """

    # INJECTION PROCESS
    # 1. Удаляем старый body
    content = content.replace('<body>', '<body>' + custom_html)
    # 2. Удаляем старый div mynetwork (он теперь внутри custom_html)
    # PyVis создает <div id="mynetwork" ...></div>. Нам нужно убрать его дубликат, 
    # но оставить скрипты. Самый простой способ - CSS хак или JS перемещение.
    # В нашем случае мы просто перезапишем стили PyVis.
    
    # Вставляем CSS в head
    content = content.replace('</head>', custom_css + '</head>')
    
    # Вставляем JS в конец body
    content = content.replace('</body>', custom_js + '</body>')

    # Очистка: PyVis добавляет свой CSS для #mynetwork, который может конфликтовать.
    # Мы просто перебиваем его нашим CSS (он ниже).

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n🚀 Cyberpunk Graph generated at: {output_file}")

if __name__ == "__main__":
    generate_interactive_graph()