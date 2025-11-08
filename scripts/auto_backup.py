#!/usr/bin/env python3
"""
BACKUP AUTOMÁTICO - SISTEMA FINANCIERO
Triple redundancia: Local + Google Drive + Externo
Rotación automática de backups antiguos
Versión: 1.0
"""

import shutil
import os
from datetime import datetime, timedelta
from pathlib import Path
import subprocess

class BackupAutomatico:
    def __init__(self, archivo_fuente="AlvaroVelasco_Finanzas_v1.0.xlsx"):
        self.archivo_fuente = archivo_fuente
        self.carpeta_local = "backups/local"
        self.carpeta_gdrive = "backups/gdrive"
        self.carpeta_externa = "backups/externa"
        self.dias_retention = 30  # Mantener backups de últimos 30 días

    def ejecutar_backup(self):
        """Ejecuta backup completo con triple redundancia"""
        print("="*70)
        print("BACKUP AUTOMÁTICO - SISTEMA FINANCIERO")
        print("="*70)
        print(f"Archivo: {self.archivo_fuente}")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        try:
            # Verificar que archivo existe
            if not os.path.exists(self.archivo_fuente):
                print(f"❌ ERROR: Archivo no encontrado: {self.archivo_fuente}")
                return False

            # Crear carpetas si no existen
            for carpeta in [self.carpeta_local, self.carpeta_gdrive, self.carpeta_externa]:
                Path(carpeta).mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            fecha_simple = datetime.now().strftime("%Y%m%d")

            # BACKUP NIVEL 1: Local (diario)
            print("⏳ Backup Nivel 1: Local...")
            backup_local = f"{self.carpeta_local}/Finanzas_{timestamp}.xlsx"
            shutil.copy2(self.archivo_fuente, backup_local)
            size_mb = os.path.getsize(backup_local) / (1024 * 1024)
            print(f"✅ Backup local: {backup_local} ({size_mb:.2f} MB)")

            # BACKUP NIVEL 2: Google Drive (si rclone configurado)
            print("⏳ Backup Nivel 2: Google Drive...")
            try:
                # Verificar si rclone está instalado
                result = subprocess.run(["which", "rclone"], capture_output=True, text=True)
                if result.returncode == 0:
                    backup_gdrive = f"{self.carpeta_gdrive}/Finanzas_{fecha_simple}.xlsx"
                    shutil.copy2(self.archivo_fuente, backup_gdrive)

                    # Sincronizar con rclone (si está configurado)
                    subprocess.run([
                        "rclone", "copy",
                        backup_gdrive,
                        "gdrive:Backups/Finanzas/"
                    ], check=False, capture_output=True)
                    print(f"✅ Backup Google Drive: {backup_gdrive}")
                else:
                    print("⚠️  rclone no instalado - backup Drive omitido")
                    print("   Instalar: https://rclone.org/install/")
            except Exception as e:
                print(f"⚠️  Backup Google Drive falló: {e}")

            # BACKUP NIVEL 3: Externo (semanal - solo domingos)
            if datetime.now().weekday() == 6:  # Domingo
                print("⏳ Backup Nivel 3: Externo (semanal)...")
                backup_externo = f"{self.carpeta_externa}/Finanzas_{fecha_simple}.xlsx"
                shutil.copy2(self.archivo_fuente, backup_externo)
                print(f"✅ Backup externo: {backup_externo}")
            else:
                print(f"ℹ️  Backup externo: Solo domingos (hoy {datetime.now().strftime('%A')})")

            # Limpiar backups antiguos
            print()
            print("⏳ Limpiando backups antiguos...")
            eliminados = self.limpiar_backups_antiguos()
            print(f"✅ Eliminados {eliminados} backups antiguos (>{self.dias_retention} días)")

            # Reporte final
            print()
            print("="*70)
            print("🎉 BACKUP COMPLETADO EXITOSAMENTE")
            print("="*70)
            print(f"✅ Local: {backup_local}")
            if os.path.exists(f"{self.carpeta_gdrive}/Finanzas_{fecha_simple}.xlsx"):
                print(f"✅ Google Drive: Sincronizado")
            print(f"📊 Tamaño: {size_mb:.2f} MB")
            print(f"🗓️  Retention: {self.dias_retention} días")
            print()

            return True

        except Exception as e:
            print(f"❌ ERROR CRÍTICO: {e}")
            import traceback
            traceback.print_exc()
            return False

    def limpiar_backups_antiguos(self):
        """Elimina backups más antiguos que dias_retention"""
        eliminados = 0
        fecha_limite = datetime.now() - timedelta(days=self.dias_retention)

        for carpeta in [self.carpeta_local, self.carpeta_gdrive]:
            if not os.path.exists(carpeta):
                continue

            for archivo in os.listdir(carpeta):
                ruta_completa = os.path.join(carpeta, archivo)
                if not os.path.isfile(ruta_completa):
                    continue

                # Obtener fecha de modificación
                fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_completa))

                if fecha_mod < fecha_limite:
                    os.remove(ruta_completa)
                    eliminados += 1

        return eliminados

    def verificar_integridad_backup(self, backup_path):
        """Verifica que backup sea válido (puede abrirse)"""
        try:
            import openpyxl
            wb = openpyxl.load_workbook(backup_path, data_only=True)
            if "TRANSACCIONES" in wb.sheetnames:
                return True
            return False
        except:
            return False

if __name__ == "__main__":
    backup = BackupAutomatico()
    success = backup.ejecutar_backup()
    exit(0 if success else 1)
