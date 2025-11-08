#!/usr/bin/env python3
"""
CONFIGURACIÓN AUTOMÁTICA DE CRON JOBS
Configura backups y health checks automáticos
Versión: 1.0
"""

import subprocess
import os
from pathlib import Path

class SetupCron:
    def __init__(self):
        self.project_dir = str(Path(__file__).parent.parent.absolute())
        self.cron_entries = []

    def setup(self):
        """Configura cron jobs automáticamente"""
        print("="*70)
        print("CONFIGURACIÓN AUTOMÁTICA CRON JOBS")
        print("="*70)
        print(f"Directorio proyecto: {self.project_dir}")
        print()

        # Verificar que estamos en Linux
        if os.name != 'posix':
            print("❌ ERROR: Cron solo disponible en Linux/Mac")
            print("   En Windows, use Programador de Tareas manualmente")
            return False

        try:
            # Crear entradas cron
            print("⏳ Creando entradas cron...")

            # Backup diario a las 11pm
            self.cron_entries.append(
                f"0 23 * * * cd {self.project_dir} && /usr/bin/python3 scripts/auto_backup.py >> logs/backup.log 2>&1"
            )

            # Health check diario a las 8am
            self.cron_entries.append(
                f"0 8 * * * cd {self.project_dir} && /usr/bin/python3 scripts/health_check.py >> logs/healthcheck.log 2>&1"
            )

            # Interfaz Claude mensual (día 1 de cada mes)
            self.cron_entries.append(
                f"0 9 1 * * cd {self.project_dir} && /usr/bin/python3 scripts/interfaz_claude.py >> logs/claude_audit.log 2>&1"
            )

            print(f"✅ {len(self.cron_entries)} entradas creadas")
            print()

            # Mostrar entradas
            print("📋 ENTRADAS CRON A AGREGAR:")
            print("-" * 70)
            for entry in self.cron_entries:
                print(f"   {entry}")
            print("-" * 70)
            print()

            # Leer crontab actual
            print("⏳ Leyendo crontab actual...")
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)

            if result.returncode == 0:
                current_crontab = result.stdout
            else:
                current_crontab = ""

            # Verificar si ya existen
            entries_to_add = []
            for entry in self.cron_entries:
                if "auto_backup.py" in entry and "auto_backup.py" in current_crontab:
                    print("   ⚠️  Backup job ya existe, omitiendo")
                elif "health_check.py" in entry and "health_check.py" in current_crontab:
                    print("   ⚠️  Health check job ya existe, omitiendo")
                elif "interfaz_claude.py" in entry and "interfaz_claude.py" in current_crontab:
                    print("   ⚠️  Claude audit job ya existe, omitiendo")
                else:
                    entries_to_add.append(entry)

            if not entries_to_add:
                print()
                print("✅ Todos los cron jobs ya están configurados")
                print()
                self.mostrar_status()
                return True

            # Agregar nuevas entradas
            print()
            print(f"⏳ Agregando {len(entries_to_add)} nuevas entradas...")

            new_crontab = current_crontab.strip() + "\n"
            new_crontab += "\n# AlvaroVelasco.Net - Sistema Financiero Automático\n"
            for entry in entries_to_add:
                new_crontab += entry + "\n"

            # Crear carpeta logs
            logs_dir = f"{self.project_dir}/logs"
            Path(logs_dir).mkdir(exist_ok=True)
            print(f"   ✅ Carpeta logs creada: {logs_dir}")

            # Aplicar nuevo crontab
            process = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
            process.communicate(input=new_crontab)

            if process.returncode == 0:
                print("✅ Crontab actualizado exitosamente")
                print()
                self.mostrar_status()
                return True
            else:
                print("❌ ERROR: Falló actualización de crontab")
                return False

        except Exception as e:
            print(f"❌ ERROR: {e}")
            import traceback
            traceback.print_exc()
            return False

    def mostrar_status(self):
        """Muestra status de cron jobs configurados"""
        print("="*70)
        print("STATUS CRON JOBS")
        print("="*70)
        print()

        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)

        if result.returncode == 0:
            crontab_lines = result.stdout.split('\n')

            backup_configured = any("auto_backup.py" in line for line in crontab_lines)
            health_configured = any("health_check.py" in line for line in crontab_lines)
            claude_configured = any("interfaz_claude.py" in line for line in crontab_lines)

            print(f"✅ Backup automático (diario 11pm): {'ACTIVO' if backup_configured else '❌ NO CONFIGURADO'}")
            print(f"✅ Health check (diario 8am): {'ACTIVO' if health_configured else '❌ NO CONFIGURADO'}")
            print(f"✅ Auditoría Claude (mensual día 1): {'ACTIVO' if claude_configured else '❌ NO CONFIGURADO'}")
            print()

            if backup_configured and health_configured and claude_configured:
                print("🎉 TODOS LOS CRON JOBS CONFIGURADOS CORRECTAMENTE")
                print()
                print("PRÓXIMAS EJECUCIONES:")
                print(f"   - Health Check: Mañana 8:00 AM")
                print(f"   - Backup: Hoy 11:00 PM")
                print(f"   - Auditoría Claude: Día 1 del próximo mes 9:00 AM")
            else:
                print("⚠️  Algunos cron jobs no están configurados")

        print()
        print("VERIFICAR LOGS:")
        print(f"   tail -f {self.project_dir}/logs/backup.log")
        print(f"   tail -f {self.project_dir}/logs/healthcheck.log")
        print(f"   tail -f {self.project_dir}/logs/claude_audit.log")
        print()
        print("="*70)

    def remover_cron_jobs(self):
        """Remueve cron jobs del sistema (para desinstalación)"""
        print("⏳ Removiendo cron jobs del sistema...")

        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)

        if result.returncode != 0:
            print("ℹ️  No hay crontab configurado")
            return True

        current_crontab = result.stdout
        lines = current_crontab.split('\n')

        # Filtrar líneas que no sean del sistema financiero
        new_lines = [line for line in lines
                     if not any(script in line for script in
                               ["auto_backup.py", "health_check.py", "interfaz_claude.py"])]

        new_crontab = '\n'.join(new_lines)

        # Aplicar
        process = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
        process.communicate(input=new_crontab)

        if process.returncode == 0:
            print("✅ Cron jobs removidos")
            return True
        else:
            print("❌ ERROR removiendo cron jobs")
            return False

if __name__ == "__main__":
    import sys

    setup = SetupCron()

    if len(sys.argv) > 1 and sys.argv[1] == "--remove":
        success = setup.remover_cron_jobs()
    else:
        success = setup.setup()

    exit(0 if success else 1)
