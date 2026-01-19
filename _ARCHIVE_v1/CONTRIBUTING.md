# The Genesis Protocol 🧬
## How to Contribute to Malachite Substrate

Thank you for helping us reconstruct the Causal Ontology of Civilization.
Malachite is not just a list of inventions; it is a **Directed Acyclic Graph (DAG)** of causality.

To ensure the "Crystal" remains solid, all contributions must adhere to the following strict protocols.

---

## 1. The Golden Rules of Causality

### 🚫 No Time Loops
You cannot invent the Steam Engine before Fire.
*   **Rule:** Every new node must have `Parents` that historically and physically preceded it.
*   **Check:** Run `python tools/validate.py` before submitting.

### 🚫 No Orphans (Magic is Forbidden)
Nothing appears from thin air.
*   **Rule:** Every node (except the 4 Foundations) must have at least one Parent.
*   **Tip:** If you can't find a parent, look in `data/00_foundations/seeds.csv`.

### 🧠 The 3 Logic Eras
When adding a node, you must define its `Era`. This tells the AI *how* the discovery was made.

| Era | Logic | Example |
| :--- | :--- | :--- |
| **INTUITIVE** | Observation + Trial & Error. No math required. | Fire, Wheel, Bow, Fermentation. |
| **SCIENTIFIC** | Hypothesis + Proof = Law. Abstract understanding. | Thermodynamics, Germ Theory, Calculus. |
| **MODERN / DIGITAL** | Complex Engineering based on Science. | Transistor, Internet, AI. |

---

## 2. Data Schema (CSV)

We use CSV for Git-native version control. Do not use Excel if possible (it messes up formatting). Use a raw text editor or VS Code.

**File Location:**
*   Primitive tech -> `data/01_crystallized/primitive_era.csv`
*   Industrial/Science -> `data/01_crystallized/scientific_era.csv`
*   Electricity/Modern -> `data/01_crystallized/electric_era.csv`
*   Computers/AI -> `data/01_crystallized/digital_era.csv`

**Columns:**

1.  **ID:** Unique identifier (e.g., `DIG-42`). Keep it sequential if possible, or use decimals (`DIG-42.1`) to insert between rows.
2.  **Name:** The standard name (e.g., `NEURAL_NETWORK`).
3.  **Type:**
    *   `RESOURCE` (Raw material)
    *   `TOOL` (Handheld instrument)
    *   `MACHINE` (Complex mechanism)
    *   `DISCOVERY` (Observation of nature)
    *   `METHOD` (Algorithm or technique)
    *   `SOCIAL_ARTIFACT` (Law, Money, Organization)
4.  **Era:** `INTUITIVE`, `SCIENTIFIC`, `MODERN`, `DIGITAL`.
5.  **Parents:** Semicolon-separated IDs (e.g., `[SCI-14;DIG-06]`). **Crucial:** Must exist in the DB.
6.  **Trigger:** The "Eureka" moment. What observation led to this?
7.  **Principle:** The physical law involved (e.g., `Bernoulli Principle`).
8.  **Tech_Make:** How is it manufactured?
9.  **Tech_Use:** How is it applied?

---

## 3. Pull Request Process

1.  **Fork** the repository.
2.  **Add** your nodes to the appropriate CSV file.
3.  **Run Validation** locally:
    ```bash
    python tools/validate.py
    ```
4.  **Commit** your changes.
5.  **Open a Pull Request**. Our "Malachite Guardian" (CI/CD robot) will automatically check your topology. If it turns green, we merge!

---

**"We are the ancestors of the future. Let's build a memory that lasts."**