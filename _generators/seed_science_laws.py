import os
import csv


# =================================================================================
# НАСТРОЙКИ
# =================================================================================


BASE_DIR = os.path.join("data_v2", "01_SCIENCE")


# Пути к конкретным папкам (согласно taxonomy_config.py v5.2)
PATHS = {
    "AXIOMS": os.path.join(BASE_DIR, "Axioms", "Universal_Laws", "index.csv"),
    "MECH":   os.path.join(BASE_DIR, "Physics", "Classical_Mech", "index.csv"),
    "THERMO": os.path.join(BASE_DIR, "Physics", "Thermodynamics", "index.csv"),
    "EM":     os.path.join(BASE_DIR, "Physics", "Electromagnetism", "index.csv"),
    "QUANT":  os.path.join(BASE_DIR, "Physics", "Quantum_Relativity", "index.csv"),
    "CHEM":   os.path.join(BASE_DIR, "Chemistry", "Inorganic", "index.csv"), # <--- НОВОЕ
    "BIO":    os.path.join(BASE_DIR, "Biology", "Genetics", "index.csv")      # <--- НОВОЕ
}


# Заголовки (v4.0)
HEADERS = [
    "ID", "Name", "Description", 
    "Era", "Predecessor_ID", "Status", 
    "Syntropy_Score", "Catalytic_Potential", "Structural_Pattern",
    "Invention_Reason", "Social_Context", 
    "Drawbacks", "Side_Effects", "Impact_Map",
    "Properties", "External_Data_Link",
    # Domain Specific
    "Prerequisite_Knowledge", "Key_Formula", "Discovered_By", "Experimental_Proof"
]


# =================================================================================
# ДАННЫЕ (ЗАКОНЫ МИРОЗДАНИЯ)
# =================================================================================


DATA_SETS = {
    "AXIOMS": [
        {
            "ID": "SCI-LAW_SYNTROPY",
            "Name": "Principle of Syntropy (The Malachite Law)",
            "Description": "Intelligence is a physical operator that reverses entropy by organizing energy flows.",
            "Era": "ERA-07_INTELLECTUAL",
            "Syntropy_Score": 10000.0,
            "Catalytic_Potential": 10000.0,
            "Key_Formula": "S = (E_acc - E_cost) / E_create",
            "Discovered_By": "System Architects",
            "Status": "AXIOM",
            "Impact_Map": "ALL_SYSTEMS:OPTIMIZE:+100",
            "External_Data_Link": "local://01_SCIENCE/Axioms/Universal_Laws/THEORY_OF_SYNTROPY.md"
        },
        {
            "ID": "SCI-LAW_ENTROPY",
            "Name": "Second Law of Thermodynamics",
            "Description": "Entropy of an isolated system always increases. The arrow of time.",
            "Era": "ERA-04_INDUSTRIAL",
            "Syntropy_Score": -10000.0,
            "Catalytic_Potential": 5000.0,
            "Key_Formula": "dS >= dQ/T",
            "Discovered_By": "Clausius, Boltzmann",
            "Status": "AXIOM",
            "Impact_Map": "FAC-STEAM_ENGINE:LIMIT_EFFICIENCY:-100"
        }
    ],
    "MECH": [
        {
            "ID": "SCI-LAW_NEWTON_2",
            "Name": "Newton's Second Law",
            "Description": "Force equals mass times acceleration.",
            "Era": "ERA-03_SCIENTIFIC",
            "Syntropy_Score": 500.0,
            "Catalytic_Potential": 2000.0,
            "Key_Formula": "F = ma",
            "Discovered_By": "Isaac Newton",
            "Status": "ACTIVE",
            "Impact_Map": "FAC-MACHINERY:ENABLE:+100;VEH-ALL:ENABLE:+100"
        }
    ],
    "THERMO": [
        {
            "ID": "SCI-LAW_THERMO_1",
            "Name": "First Law of Thermodynamics",
            "Description": "Conservation of energy.",
            "Era": "ERA-04_INDUSTRIAL",
            "Syntropy_Score": 1000.0,
            "Key_Formula": "dU = Q - W",
            "Discovered_By": "Joule",
            "Status": "AXIOM",
            "Impact_Map": "FAC-POWER_PLANT:ENABLE:+100"
        }
    ],
    "EM": [
        {
            "ID": "SCI-LAW_OHM",
            "Name": "Ohm's Law",
            "Description": "Voltage equals current times resistance.",
            "Era": "ERA-05_ELECTRICAL",
            "Syntropy_Score": 500.0,
            "Key_Formula": "V = IR",
            "Discovered_By": "Georg Ohm",
            "Status": "ACTIVE",
            "Impact_Map": "GRID-ALL:ENABLE:+100"
        }
    ],
    "QUANT": [
        {
            "ID": "SCI-LAW_E_MC2",
            "Name": "Mass-Energy Equivalence",
            "Description": "Matter is condensed energy.",
            "Era": "ERA-05_ELECTRICAL",
            "Syntropy_Score": 5000.0,
            "Catalytic_Potential": 10000.0,
            "Key_Formula": "E = mc^2",
            "Discovered_By": "Albert Einstein",
            "Status": "ACTIVE",
            "Impact_Map": "FAC-NPP:ENABLE:+1000"
        }
    ],
    "CHEM": [ # <--- НОВЫЙ РАЗДЕЛ
        {
            "ID": "SCI-LAW_PERIODIC",
            "Name": "Periodic Law",
            "Description": "Properties of elements depend on atomic weight.",
            "Era": "ERA-04_INDUSTRIAL",
            "Syntropy_Score": 2000.0,
            "Catalytic_Potential": 5000.0,
            "Key_Formula": "Table Structure",
            "Discovered_By": "Dmitri Mendeleev",
            "Status": "AXIOM",
            "Impact_Map": "MAT-ALL:ENABLE:+1000"
        }
    ],
    "BIO": [ # <--- НОВЫЙ РАЗДЕЛ
        {
            "ID": "SCI-LAW_EVOLUTION",
            "Name": "Natural Selection",
            "Description": "Survival of the fittest.",
            "Era": "ERA-04_INDUSTRIAL",
            "Syntropy_Score": 1000.0,
            "Catalytic_Potential": 5000.0,
            "Key_Formula": "Variation + Selection",
            "Discovered_By": "Charles Darwin",
            "Status": "AXIOM",
            "Impact_Map": "RES-BIO_ALL:EXPLAIN:+100"
        },
        {
            "ID": "SCI-LAW_DNA",
            "Name": "Central Dogma of Molecular Biology",
            "Description": "DNA -> RNA -> Protein.",
            "Era": "ERA-06_DIGITAL",
            "Syntropy_Score": 3000.0,
            "Catalytic_Potential": 8000.0,
            "Key_Formula": "Code Translation",
            "Discovered_By": "Crick & Watson",
            "Status": "AXIOM",
            "Impact_Map": "MED-GENETICS:ENABLE:+1000"
        }
    ]
}


# =================================================================================
# ЛОГИКА ЗАПИСИ
# =================================================================================


def write_category(key, rows):
    path = PATHS.get(key)
    if not path: return


    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


    for row in rows:
        if "Predecessor_ID" not in row: row["Predecessor_ID"] = "NULL"
        if "Structural_Pattern" not in row: row["Structural_Pattern"] = "ABSTRACT_FORMULA"
        if "Properties" not in row: row["Properties"] = "{}"
        if "External_Data_Link" not in row: row["External_Data_Link"] = "NULL"
        if "Invention_Reason" not in row: row["Invention_Reason"] = "CURIOSITY"
        if "Social_Context" not in row: row["Social_Context"] = "ACADEMIA"
        
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✅ Наука ({key}): Записано {len(rows)} законов.")


def main():
    print("🔬 Генерация Научной Базы (v5.0 - Full)...")
    for key, data in DATA_SETS.items():
        write_category(key, data)


if __name__ == "__main__":
    main()