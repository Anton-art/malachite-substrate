"""
SYNTROPIC CORE (v7.3 - MALACHITE ADAPTER)
-----------------------------------------
Library for decision making.
Includes: Vandalism Check, Simulation Protocol, Investment Logic.
"""
import math
from enum import Enum
from dataclasses import dataclass
from typing import Tuple


# --- ENUMS ---
class Verdict(Enum):
    DELETE = "🗑️ BURN"
    ARCHIVE = "🔒 STORE"
    AMPLIFY = "🚀 EXECUTE"
    STOP = "🛑 VETO"
    RECOVERY = "🚑 HEAL"
    RECYCLE = "♻️ RECYCLE"
    SIMULATE = "🧪 SIMULATE"     # <--- НОВЫЙ ВЕРДИКТ (Для Эры 6+)
    FORCED_RISK = "⚠️ FORCED RISK" # <--- НОВЫЙ ВЕРДИКТ (Для Эры <6)


@dataclass
class SyntropicEntity:
    id: str
    name: str
    syntropy_score: float    # Energy Balance
    catalytic_potential: float # Information Potential (Alpha)
    scarcity: float = 0.0
    knowledge: float = 1.0
    realization: float = 1.0
    era_level: int = 6       # По умолчанию считаем, что мы в Цифровой Эре (6)


# --- LOGIC ENGINE ---
class SyntropicValueEngine:
    def evaluate(self, e: SyntropicEntity) -> Tuple[float, Verdict, str]:
        
        # 1. ПРОВЕРКА НА ВАНДАЛИЗМ (Vandalism Check)
        # Если ресурс редкий и мы о нем мало знаем.
        if e.scarcity > 0.8 and e.knowledge < 0.5:
            
            # --- ЛОГИКА СИМУЛЯЦИИ ---
            if e.era_level >= 6:
                # Мы в будущем -> Запрет на физику, требуем симуляцию
                return (0.0, Verdict.SIMULATE, "UNKNOWN RESOURCE: Physical interaction banned. Virtual Model required.")
            else:
                # Мы в прошлом -> Приходится рисковать
                return (0.0, Verdict.FORCED_RISK, "UNKNOWN RESOURCE: Simulation impossible. Physical trial required for survival.")


        # 2. ПРОВЕРКА НА ВАРВАРСТВО (Waste Check)
        # Если ресурс редкий, а КПД использования низкий (<10%)
        if e.scarcity > 0.8 and e.realization < 0.1:
            return (0.0, Verdict.STOP, f"WASTE: Low realization ({e.realization*100}%) of rare resource")


        # 3. ПРОВЕРКА НА ИНВЕСТИЦИЮ (The Bonfire Paradox)
        # Энергия в минусе, но Катализ огромный
        if e.syntropy_score < 0 and e.catalytic_potential > 50.0:
            return (e.catalytic_potential, Verdict.AMPLIFY, f"INVESTMENT: High Catalytic Potential ({e.catalytic_potential})")


        # 4. СТАНДАРТНАЯ ЭФФЕКТИВНОСТЬ
        if e.syntropy_score > 0:
            return (e.syntropy_score, Verdict.AMPLIFY, f"EFFICIENT: Positive Syntropy ({e.syntropy_score})")
        
        # 5. МУСОР
        return (e.syntropy_score, Verdict.RECYCLE, "ENTROPIC: Net Loss")


class AnalogyEngine:
    def find_resonance(self, pattern_a: str, pattern_b: str) -> float:
        if not pattern_a or not pattern_b: return 0.0
        if pattern_a == pattern_b: return 1.0
        common = set(pattern_a.split('_')) & set(pattern_b.split('_'))
        return len(common) / max(len(pattern_a.split('_')), 1)