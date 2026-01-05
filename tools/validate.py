import sys
import os
# Add root to path to import malachite
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from malachite.core.loader import MalachiteLoader
import networkx as nx

def validate():
    loader = MalachiteLoader("./data")
    G = loader.build_graph()
    
    errors = []
    
    # 1. Check for Cycles (Time Paradoxes)
    try:
        cycle = nx.find_cycle(G)
        errors.append(f"❌ CRITICAL: Time Loop detected: {cycle}")
    except nx.NetworkXNoCycle:
        print("✅ Time Flow: Linear (No Cycles)")

    # 2. Check for Orphans (Magic)
    # Roots are allowed to have no parents
    ROOTS = ["F-00", "F-01", "F-02", "F-03"] 
    
    for node in G.nodes():
        parents = list(G.predecessors(node))
        if not parents and node not in ROOTS:
            # Check if it's a Seed defined in seeds.csv (they have parents in CSV but maybe not loaded if file missing)
            # For strict validation:
            errors.append(f"⚠️ Orphan Node: {node} (No Causal Parent)")

    if errors:
        print("\n🚫 VALIDATION FAILED:")
        for e in errors: print(e)
        sys.exit(1)
    else:
        print("\n✨ THE CRYSTAL IS SOLID. Validation Passed.")

if __name__ == "__main__":
    validate()
