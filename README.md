```markdown
# Malachite Substrate 🟢
### The Causal Ontology of Civilization

> *"Current AI models are gas: volatile, expansive, and amnesic. To build true AGI, we need a solid state. We need Malachite."*

**Malachite Substrate** is the **External Causal Memory** for AI Agents. It maps the evolution of humanity not as a list of dates, but as a chain of **Observations, Eurekas, and Tools**.

---

## 💎 The Philosophy: The Evolution of Reason

We structure the database into **3 Logic Eras**, reflecting how Intelligence interacts with the Universe:

1.  **Intuitive Era:** Observation + Surprise = **Idea** → Tool. (e.g., The Lever, Fire).
2.  **Scientific Era:** Idea + Proof = **Law** (Abstract Tool). (e.g., Thermodynamics).
3.  **Syntropy Era:** Invention + Social Simulation = **Harmonious Future**. (e.g., AI Alignment).

---

## 🏗️ Architecture

The repository consists of:
1.  **The Substrate (`data/`)**: Immutable CSV ledgers of history and physics.
2.  **The Engine (`malachite/`)**: Python SDK to traverse the graph, validate causality, and calculate **Syntropy Scores**.

### Data Layers
*   **FOUNDATIONS:** Earth, Water, Sky (The Environment).
*   **CRYSTALLIZED:** Verified History (Hard Constraints).
*   **HYPOTHESIS:** Latent space for AI exploration.
*   **SIMULATION:** "Package Deals" (Tech + Law) waiting for deployment.

---

## 🛠️ Quick Start

### Prerequisites
```bash
pip install pandas networkx
```

### Usage (Python)
```python
from malachite.core.loader import MalachiteLoader

# 1. Load the Civilization Graph
loader = MalachiteLoader("./data")
graph = loader.build_graph()

# 2. Trace the Lineage of the Wheel
# AI understands: Log -> Rolling Friction -> Wheel
ancestors = loader.get_lineage("S-04-WHEEL")
print(ancestors)
```

## 🤝 Contribution
See [CONTRIBUTING.md](CONTRIBUTING.md) for the **Genesis Protocol**.

**License:** CC-BY-4.0
```