#!/usr/bin/env python3
"""
Corrige formatos de celdas en v3.0
- Fechas: DD/MM/YY
- Montos: #,##0.00 (miles + decimales)
"""

import openpyxl

V3_FILE = "AlvaroVelasco_Finanzas_v3.0.xlsx"

print("Corrigiendo formatos...")

wb = openpyxl.load_workbook(V3_FILE)
ws = wb["TRANSACCIONES"]

# Columna A: Fechas DD/MM/YY
for row in range(2, ws.max_row + 1):
    ws.cell(row, 1).number_format = 'DD/MM/YY'

# Columnas H e I: Montos con separador miles
for row in range(2, ws.max_row + 1):
    ws.cell(row, 8).number_format = '#,##0.00'  # CRC
    ws.cell(row, 9).number_format = '#,##0.00'  # USD

print(f"Aplicando formatos a {ws.max_row - 1} filas...")

wb.save(V3_FILE)
wb.close()

print("✅ Formatos corregidos")
