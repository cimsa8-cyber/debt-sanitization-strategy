#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FORZAR RECÁLCULO COMPLETO EXCEL
Elimina todos los valores cacheados y fuerza recálculo al abrir
"""
import openpyxl
from datetime import datetime
import shutil

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"
BACKUP_FILE = f"AlvaroVelasco_Finanzas_v2.0_ANTES_RECALCULO_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

def crear_backup():
    print("=" * 80)
    print("CREANDO BACKUP")
    print("=" * 80)
    print(f"Backup: {BACKUP_FILE}")
    try:
        shutil.copy2(EXCEL_FILE, BACKUP_FILE)
        print("✅ Backup creado")
        print()
        return True
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def forzar_recalculo():
    print("=" * 80)
    print("FORZANDO RECÁLCULO COMPLETO DE EXCEL")
    print("=" * 80)
    print()

    # Cargar Excel SIN data_only para mantener fórmulas
    wb = openpyxl.load_workbook(EXCEL_FILE, data_only=False)

    print("📋 Configurando Excel para recalcular al abrir...")
    print()

    # Forzar recálculo completo
    wb.calculation.calcMode = 'auto'
    wb.calculation.fullCalcOnLoad = True

    print("✅ calcMode = 'auto'")
    print("✅ fullCalcOnLoad = True")
    print()

    # Guardar
    print("=" * 80)
    print("💾 Guardando configuración...")
    print("=" * 80)
    print()

    wb.save(EXCEL_FILE)
    print("✅ Excel actualizado")
    print()

    print("=" * 80)
    print("📊 RESUMEN")
    print("=" * 80)
    print()

    print("✅ Excel configurado para recalcular completamente")
    print()
    print("🔧 PRÓXIMOS PASOS CRÍTICOS:")
    print()
    print("   1. Cierra COMPLETAMENTE Excel (si está abierto)")
    print("   2. Espera 5 segundos")
    print("   3. Abre el archivo: AlvaroVelasco_Finanzas_v2.0.xlsx")
    print("   4. Excel recalculará TODAS las fórmulas automáticamente")
    print("      (Puede tardar unos segundos)")
    print("   5. Ve a hoja Efectivo, fila 3")
    print("   6. Verifica los valores de D3, E3, F3")
    print()
    print("⚠️  IMPORTANTE:")
    print("   - NO hagas cambios manuales")
    print("   - Espera a que Excel termine de cargar completamente")
    print("   - Si los valores siguen incorrectos, hay un problema")
    print("     más profundo en las fórmulas o datos")
    print()

    print("=" * 80)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 80)
    print()

if __name__ == "__main__":
    try:
        if not crear_backup():
            print("❌ Abortando")
            exit(1)

        forzar_recalculo()
        print("🎉 Proceso completado!")
        print()
        print("👉 Ahora cierra y vuelve a abrir el Excel")

    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
