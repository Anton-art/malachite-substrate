README.md


---


# 💎 Project Malachite (v4.0)


> **The Engineering Core of the Syntropic Civilization.**
> *A generative knowledge graph optimized for AGI training and evolutionary simulation.*


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)]()
[![Alignment: Syntropy Protocol](https://img.shields.io/badge/Alignment-Syntropy_Protocol-blue.svg)](https://github.com/YOUR_ORG/SYNTROPY_PROTOCOL)


---


## 🌍 Mission


**Malachite** is not just a database of facts. It is a digital model of the **Technosphere**, designed to teach Artificial Intelligence the causal links between:
*   **Resources** (What we have)
*   **Science** (What is possible)
*   **Technology** (How to build)
*   **Society** (Why we need it)


This repository provides the **"Hard Skills"** (Memory & Logic) for the Global Intelligence.
For the **"Soft Skills"** (Ethics, Goals, & Alignment), please refer to the **[SYNTROPY PROTOCOL](https://github.com/YOUR_ORG/SYNTROPY_PROTOCOL)** repository.


---


## 🏗️ Architecture


The system is built on the **"Start Flat, Grow Deep"** principle.


### 1. The 8 Fundamental Domains
The world is mapped into a strict directory structure (`data_v2/`):
*   **`01_SCIENCE`**: Laws, Axioms, and Effects.
*   **`02_DESIGN`**: Standards, Code, and Methodologies.
*   **`03_RESOURCES`**: Raw Matter (Ores, Energy, Biosphere).
*   **`04_MATERIALS`**: Processed Matter (Alloys, Polymers).
*   **`05_INFRASTRUCTURE`**: Tools, Factories, Power Plants.
*   **`06_PROCESSES`**: Technologies (Verbs: Casting, Coding).
*   **`07_ARTIFACTS`**: Products (The Goal).
*   **`08_SOCIETY`**: Context, History, and Needs.


### 2. Storage Format
*   **Dense CSV:** We use optimized CSV tables (1k-5k rows) to maximize **Token Efficiency** for LLM training. No JSONL bloat.
*   **Generative Core:** Data is not static. It is grown by Python simulators located in `_generators/`.


---


## 🧠 The Syntropy Engine


The repository includes a logic core (`_generators/syntropy_engine.py`) that evaluates every object based on the **Law of Syntropy**:


$$ S = \frac{E_{acc} - E_{cost}}{E_{create}} $$


*   **Syntropy Score ($S$):** Energy Efficiency. (>1.0 = Good).
*   **Catalytic Potential ($C$):** Information Leverage.
*   **Verdict:** The system automatically tags objects as `HERO`, `INVEST`, `BAN`, or `SIMULATE`.


---


## 🚀 Quick Start


### 1. Initialize Structure
Create the folder skeleton (The "Shelves").
```bash
python init_genesis.py
```
*(Warning: This will wipe existing data in `data_v2`)*


### 2. Apply Schema
Add columns and headers to all CSV files.
```bash
python update_headers.py
```


### 3. Seed the World (Simulation)
Launch the factory to generate 5,000+ objects with calculated physics.
```bash
python run_all_seeds.py
```


### 4. Analyze Syntropy
Run the "Judge" to evaluate the energy efficiency of the civilization.
```bash
python _generators/analyze_syntropy.py
```


---


## 🔗 Integration with Syntropy Protocol


This database implements the axioms defined in the **Syntropy Protocol**:
1.  **The Syntropic Square:** The DB structure mirrors the interaction between Human, AI, Biosphere, and Technosphere.
2.  **The Simulation Barrier:** In the Digital Era (Era-06+), unknown resources are flagged as `SIMULATE` instead of `RISK`.
3.  **The Bonfire Paradox:** Projects with negative energy balance are allowed if `Catalytic_Potential` is high.


---


## 🤝 Contributing


1.  **Do not edit `index.csv` manually** if a generator exists. Update the generator logic instead.
2.  **Respect the Era:** Do not introduce Digital tech in the Primitive Era.
3.  **Check Syntropy:** If your addition increases Entropy without Catalytic Potential, it will be rejected by the Judge.


---


*Project Malachite © 2025. Built for the future of Intelligence.*