import os
import sys
import subprocess
import datetime

# ПОРЯДОК ЗАПУСКА (CRITICAL PATH)
SCRIPTS = [
    # 1. Основа
    "_generators/seed_foundations.py",      # Фундамент (ID предков)
    "_generators/seed_science_laws.py",     # Законы
    
    # 2. Ресурсы
    "_generators/seed_ferrous_extended.py", # Руда
    "_generators/seed_refining.py",         # Топливо (Заменил seed_energy)
    
    # 3. Материалы
    "_generators/seed_materials_massive.py", # Сталь
    "_generators/seed_advanced_materials.py",# Пластик/Керамика (Заменил seed_polymers)
    
    # 4. Процессы
    "_generators/seed_processes.py",        # Технологии (v9.1)
    "_generators/seed_logistics.py",        # Транспорт
    
    # 5. Компоненты (L2)
    "_generators/seed_mechanical_parts.py", # Болты/Подшипники (Заменил seed_components)
    "_generators/seed_structural_parts.py", # Профили/Корпуса
    "_generators/seed_electronics.py",      # Чипы/Резисторы
    
    # 6. Инфраструктура
    "_generators/seed_infrastructure.py",   # Заводы (ссылаются на процессы)
    
    # 7. Сборки (L3-L5)
    "_generators/seed_complex_assemblies.py" # Двигатели/Серверы
]

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open("generation_log.txt", "a", encoding="utf-8") as f:
        f.write(line + "\n")

def run_script(script_path):
    log(f"⏳ Запуск: {script_path}...")
    python_cmd = sys.executable
    try:
        subprocess.run([python_cmd, script_path], check=True)
        return True
    except subprocess.CalledProcessError:
        log(f"❌ ОШИБКА: {script_path} завершился с кодом ошибки.")
        return False
    except FileNotFoundError:
        log(f"❌ ОШИБКА: Файл {script_path} не найден.")
        return False

def main():
    with open("generation_log.txt", "w", encoding="utf-8") as f:
        f.write("=== MALACHITE v9.0 GENERATION LOG ===\n")

    log("🌍 ЗАПУСК ПОЛНОЙ ГЕНЕРАЦИИ МИРА (v9.0)")
    
    success_count = 0
    for script in SCRIPTS:
        if run_script(script):
            success_count += 1
            
    log("-" * 60)
    log(f"🏁 Генерация завершена. Успешно: {success_count}/{len(SCRIPTS)}")
    
    if success_count == len(SCRIPTS):
        log("⚖️  ВЫЗОВ СУДЬИ (ANALYZER)...")
        run_script("_generators/analyze_syntropy.py")
    else:
        log("⚠️  Судья не запущен из-за ошибок генерации.")

if __name__ == "__main__":
    main()