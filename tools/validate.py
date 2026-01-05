import sys
import os
import pandas as pd
import networkx as nx

# Add the root directory to the system path so Python can find the 'malachite' package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from malachite.core.loader import MalachiteLoader

def validate():
    # Define the path to the data folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data")
    
    # Initialize the loader and build the graph
    loader = MalachiteLoader(data_path)
    G = loader.build_graph()
    
    errors = []
    
    # 1. Check for Cycles (Time Loops)
    # In a causal graph, a child cannot be the ancestor of its own parent.
    try:
        cycle = nx.find_cycle(G)
        errors.append(f"❌ CRITICAL: Time Loop detected: {cycle}")
    except nx.NetworkXNoCycle:
        print("✅ Time Flow: Linear (No Cycles)")

    # 2. Check for Orphans (Magic is not allowed)
    # Every node must have a parent, except for the fundamental foundation nodes.
    ROOTS = ["F-00", "F-01", "F-02", "F-03"] 
    
    for node in G.nodes():
        parents = list(G.predecessors(node))
        if not parents and node not in ROOTS:
            errors.append(f"⚠️ Orphan Node detected: {node} (No Causal Parent found)")

    # Final Verdict
    if errors:
        print("\n🚫 VALIDATION FAILED:")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("\n✨ THE CRYSTAL IS SOLID. Validation Passed.")

if __name__ == "__main__":
    validate()
