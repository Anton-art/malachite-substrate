import os
import csv
import shutil
from taxonomy_config import TAXONOMY


ROOT_DIR = "data_v2"


def create_system_layer(root_path):
    """Создает системные файлы конфигурации."""
    sys_path = os.path.join(root_path, "_system")
    os.makedirs(sys_path, exist_ok=True)
    
    matrix_path = os.path.join(sys_path, "evolution_matrix.csv")
    with open(matrix_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Era_ID", "Era_Name", "Allowed_Domains", "Dominant_Logic", "Simulation_Available"])
        writer.writerow(["ERA-01", "Primitive", "03,06,07,08", "INTUITION", "FALSE"])
        writer.writerow(["ERA-02", "Engineering", "03,04,05,06,07,08", "EMPIRICISM", "FALSE"])
        writer.writerow(["ERA-03", "Scientific", "ALL", "THEORY", "FALSE"])
        writer.writerow(["ERA-04", "Industrial", "ALL", "STANDARDIZATION", "FALSE"])
        writer.writerow(["ERA-05", "Electrical", "ALL", "SYSTEMS", "FALSE"])
        writer.writerow(["ERA-06", "Digital", "ALL", "COMPUTATION", "TRUE"]) # <--- ВАЖНО
        writer.writerow(["ERA-07", "Intellectual", "ALL", "SYNTROPY", "TRUE"])
    
    print(f"⚙️  Создана матрица эволюции: {matrix_path}")


def create_meta_file(path, node_data, parent_id):
    meta_path = os.path.join(path, "_meta.csv")
    with open(meta_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Type", "Parent_ID", "Description"])
        writer.writerow([node_data['id'], node_data['name'], node_data['type'], parent_id, node_data.get('description', "")])


def create_index_file(path):
    with open(os.path.join(path, "index.csv"), mode='w', newline='', encoding='utf-8') as file:
        pass


def build_structure(base_path, structure, parent_id="ROOT"):
    for folder_name, node_data in structure.items():
        current_path = os.path.join(base_path, folder_name)
        os.makedirs(current_path, exist_ok=True)
        create_meta_file(current_path, node_data, parent_id)
        create_index_file(current_path)
        if "children" in node_data:
            build_structure(current_path, node_data["children"], parent_id=node_data['id'])


def main():
    print("🚜 ЗАПУСК РЕЖИМА 'GENESIS' (БУЛЬДОЗЕР)...")
    if os.path.exists(ROOT_DIR):
        print(f"🔥 УДАЛЕНИЕ ВСЕГО в {ROOT_DIR}...")
        shutil.rmtree(ROOT_DIR)
    
    os.makedirs(ROOT_DIR)
    
    # 1. Строим таксономию
    build_structure(ROOT_DIR, TAXONOMY)
    
    # 2. Создаем системный слой (Исправление ошибки)
    create_system_layer(ROOT_DIR)
    
    print("✨ Чистая структура создана с нуля.")


if __name__ == "__main__":
    main()