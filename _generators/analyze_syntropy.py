import os
import csv
import sys

# =================================================================================
# НАСТРОЙКИ ОКРУЖЕНИЯ
# =================================================================================

# Определяем папку, где лежит этот скрипт (_generators)
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Добавляем её в системный путь, чтобы Python увидел соседний файл syntropy_engine.py
if CURRENT_SCRIPT_DIR not in sys.path:
    sys.path.append(CURRENT_SCRIPT_DIR)

try:
    from syntropy_engine import SyntropicValueEngine, SyntropicEntity, Verdict
except ImportError:
    print("❌ КРИТИЧЕСКАЯ ОШИБКА: Не найден файл 'syntropy_engine.py'.")
    print(f"   Ожидаемое расположение: {os.path.join(CURRENT_SCRIPT_DIR, 'syntropy_engine.py')}")
    sys.exit(1)

# =================================================================================
# КОНФИГУРАЦИЯ
# =================================================================================

ROOT_DIR = "data_v2"

ERA_LEVELS = {
    "ERA-01": 1, # Primitive
    "ERA-02": 2, # Engineering
    "ERA-03": 3, # Scientific
    "ERA-04": 4, # Industrial (Default)
    "ERA-05": 5, # Electrical
    "ERA-06": 6, # Digital (Simulation Required)
    "ERA-07": 7  # Intellectual
}

def safe_float(val, default=0.0):
    """Безопасное преобразование строки или числа в float."""
    # 1. Если значение пустое (None)
    if val is None:
        return default
    
    # 2. Если это уже число (float или int) — просто возвращаем его
    if isinstance(val, (float, int)):
        return float(val)
    
    # 3. Если это строка — чистим и пробуем конвертировать
    s_val = str(val).strip()
    if not s_val or s_val == "NULL":
        return default
    try:
        return float(s_val)
    except ValueError:
        return default

def get_era_level(era_string):
    """
    Извлекает уровень развития из строки типа 'ERA-04_INDUSTRIAL'.
    По умолчанию возвращает 4 (Industrial).
    """
    if not era_string:
        return 4
    
    # Берем первую часть до подчеркивания (например, "ERA-05")
    key = era_string.split('_')[0]
    return ERA_LEVELS.get(key, 4)

# =================================================================================
# ЛОГИКА АНАЛИЗА
# =================================================================================

def scan_and_judge():
    print("⚖️  ЗАПУСК СУДЬИ (ANALYZER v2.2 - Robust Types)...")
    print(f"   - Сканирование папки: {ROOT_DIR}")
    
    engine = SyntropicValueEngine()
    
    # Словарь для сбора статистики по вердиктам
    report = {v: [] for v in Verdict}
    total_objects = 0
    
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if "index.csv" in filenames:
            filepath = os.path.join(dirpath, "index.csv")
            
            with open(filepath, mode='r', encoding='utf-8') as f:
                try:
                    reader = csv.DictReader(f)
                except Exception:
                    continue # Пропуск битых файлов
                
                # Пропускаем файлы без нужных колонок
                if not reader.fieldnames or "Syntropy_Score" not in reader.fieldnames:
                    continue
                
                for row in reader:
                    total_objects += 1
                    
                    # 1. Парсинг данных
                    era_str = row.get("Era", "ERA-04")
                    level = get_era_level(era_str)
                    
                    # 2. Создаем объект-сущность
                    # ВАЖНО: safe_float теперь не упадет, даже если получит число 1.0 вместо строки
                    entity = SyntropicEntity(
                        id=row.get("ID", "UNKNOWN"),
                        name=row.get("Name", "Unknown"),
                        syntropy_score=safe_float(row.get("Syntropy_Score")),
                        catalytic_potential=safe_float(row.get("Catalytic_Potential")),
                        scarcity=safe_float(row.get("Scarcity_Score")), 
                        knowledge=safe_float(row.get("Knowledge_Completeness", 1.0)),
                        realization=safe_float(row.get("Potential_Realization_Rate", 1.0)),
                        era_level=level
                    )
                    
                    # 3. Спрашиваем Ядро (Engine)
                    score, verdict, reason = engine.evaluate(entity)
                    
                    # 4. Записываем результат
                    report[verdict].append({
                        "id": entity.id,
                        "name": entity.name,
                        "reason": reason,
                        "score": score,
                        "era": era_str
                    })

    return report, total_objects

def print_report(report, total):
    print(f"\n{'='*80}")
    print(f"📊 ОТЧЕТ СИНТРОПИЧЕСКОГО АНАЛИЗА")
    print(f"   Всего проверено объектов: {total}")
    print(f"{'='*80}")

    # Порядок вывода (от Героев к Мусору)
    order = [
        Verdict.AMPLIFY,      # Герои
        Verdict.SIMULATE,     # Требуют симуляции (Будущее)
        Verdict.FORCED_RISK,  # Риск (Прошлое)
        Verdict.RECYCLE,      # Нейтральные / Убыточные
        Verdict.STOP,         # Вредные (Вандализм)
        Verdict.DELETE        # Мусор
    ]

    for verdict in order:
        items = report.get(verdict, [])
        if items:
            print(f"\n{verdict.value} (Total: {len(items)})")
            print(f"{'-'*80}")
            
            # Сортировка: Героев по Score, остальных по ID
            if verdict == Verdict.AMPLIFY:
                sorted_items = sorted(items, key=lambda x: x['score'], reverse=True)[:10]
            else:
                sorted_items = sorted(items, key=lambda x: x['id'])[:5]
            
            for item in sorted_items:
                # Форматированный вывод
                print(f"  • {item['id']:<35} | Era: {item['era']:<10} | {item['reason']}")
            
            if len(items) > 10:
                print(f"    ... и еще {len(items) - 10} объектов.")

    print(f"\n{'='*80}")
    
    # Глобальный вывод
    heroes = len(report[Verdict.AMPLIFY])
    sims = len(report[Verdict.SIMULATE])
    risks = len(report[Verdict.STOP]) + len(report[Verdict.FORCED_RISK])
    
    print("🏁 ИТОГОВЫЙ ВЕРДИКТ:")
    if heroes > risks:
        print(f"   🚀 ЦИВИЛИЗАЦИЯ РАЗВИВАЕТСЯ. (Syntropy Growth).")
        if sims > 0:
            print(f"   🧪 Обнаружены технологии Эры-06+. Активирован протокол симуляции ({sims} объектов).")
    else:
        print("   ⚠️ ВНИМАНИЕ: Высокий уровень энтропийных рисков.")

if __name__ == "__main__":
    if not os.path.exists(ROOT_DIR):
        print(f"❌ Ошибка: Папка {ROOT_DIR} не найдена. Сначала запустите генерацию.")
    else:
        rep, count = scan_and_judge()
        if count > 0:
            print_report(rep, count)
        else:
            print("⚠️ База пуста или не содержит данных с метриками.")
