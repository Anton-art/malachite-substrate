import sys
import os
import networkx as nx

# Добавляем корневую директорию в путь, чтобы Python мог найти пакет 'malachite'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from malachite.core.loader import MalachiteLoader

def validate():
    print("🔍 Malachite Guardian: Starting Causal Integrity Check...")
    
    # Определяем путь к данным
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data")
    
    # 1. Загрузка данных
    try:
        loader = MalachiteLoader(data_path)
        G = loader.build_graph()
    except Exception as e:
        print(f"❌ CRITICAL ERROR: Failed to load data. {e}")
        sys.exit(1)

    errors = []

    # 2. Проверка на циклы (Петли времени)
    # В причинном графе ребенок не может быть предком своего родителя.
    try:
        cycle = nx.find_cycle(G, orientation='original')
        errors.append(f"❌ CAUSAL LOOP: Time paradox detected! Cycle: {cycle}")
    except nx.NetworkXNoCycle:
        print("✅ Topology: No cycles detected (Time flows forward).")

    # 3. Проверка на "Сирот" (Магия запрещена)
    # Каждый узел должен иметь родителя, кроме базовых основ (F-00, F-01 и т.д.)
    FOUNDATIONS = ["F-00", "F-01", "F-02", "F-03"]
    
    for node in G.nodes():
        parents = list(G.predecessors(node))
        if not parents and node not in FOUNDATIONS:
            errors.append(f"⚠️ ORPHAN NODE: '{node}' has no parents. Every invention must have a cause.")

    # 4. Итоговый вердикт
    if errors:
        print("\n🚫 VALIDATION FAILED:")
        for e in errors:
            print(e)
        sys.exit(1) # Сообщаем GitHub, что проверка провалена
    else:
        print("\n✨ THE CRYSTAL IS SOLID. All causal chains are valid.")
        sys.exit(0) # Сообщаем GitHub, что всё отлично

if __name__ == "__main__":
    validate()