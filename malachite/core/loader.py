import pandas as pd
import networkx as nx
import os

class MalachiteLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        self.graph = nx.DiGraph()

    def build_graph(self):
        """Compiles all CSV layers into a single Knowledge Graph."""
        print("💎 Malachite: Crystallizing Graph...")
        
        # Walk through all data folders
        for root, dirs, files in os.walk(self.data_path):
            for file in files:
                if file.endswith(".csv"):
                    self._load_csv(os.path.join(root, file))
        
        print(f"✅ Graph Built: {self.graph.number_of_nodes()} nodes, {self.graph.number_of_edges()} edges.")
        return self.graph

    def _load_csv(self, filepath):
        try:
            df = pd.read_csv(filepath)
            # Clean column names (strip spaces)
            df.columns = [c.strip() for c in df.columns]
            
            for _, row in df.iterrows():
                node_id = row['ID'].strip()
                
                # Add Node with Metadata
                self.graph.add_node(
                    node_id,
                    name=row['Name'],
                    type=row['Type'],
                    era=row.get('Era', 'UNKNOWN'),
                    trigger=row.get('Trigger', 'Unknown'),
                    principle=row.get('Principle', 'Unknown')
                )

                # Create Edges (Causality)
                if pd.notna(row['Parents']) and row['Parents'] != "NULL":
                    parents = str(row['Parents']).split(';')
                    for p in parents:
                        p_id = p.strip().replace('[', '').replace(']', '')
                        self.graph.add_edge(p_id, node_id)
                        
        except Exception as e:
            print(f"⚠️ Error loading {filepath}: {e}")

    def get_lineage(self, node_id):
        """Returns the evolutionary path of a node."""
        if node_id not in self.graph:
            return "Node not found."
        return list(nx.ancestors(self.graph, node_id))
