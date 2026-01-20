import os
import sys
import subprocess
import datetime


SCRIPTS = [
    "_generators/seed_foundations.py",
    "_generators/seed_science_laws.py",
    "_generators/seed_ferrous_extended.py",
    "_generators/seed_energy.py",
    "_generators/seed_infrastructure.py",
    "_generators/seed_materials_massive.py",
    "_generators/seed_polymers.py",
    "_generators/seed_processes.py",
    "_generators/seed_logistics.py",
    "_generators/seed_components.py",
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
    # Очистка лога
    with open("generation_log.txt", "w", encoding="utf-8") as f:
        f.write("=== MALACHITE GENERATION LOG ===\n")


    log("🌍 ЗАПУСК ПОЛНОЙ ГЕНЕРАЦИИ МИРА")
    
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