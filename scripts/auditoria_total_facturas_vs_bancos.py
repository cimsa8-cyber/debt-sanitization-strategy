#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDITORÍA TOTAL - Validar CADA factura en A_P contra extractos bancarios reales
"""
import openpyxl
import sys
import os
import re

if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

EXCEL_PATH = r"C:\Users\Alvaro Velasco\Desktop\debt-sanitization-strategy\AlvaroVelasco_Finanzas_v1.0_CORREGIDO.xlsx"
DATA_DIR = r"C:\Users\Alvaro Velasco\Desktop\debt-sanitization-strategy\data"

print("=" * 80)
print("AUDITORÍA TOTAL - FACTURAS VS EXTRACTOS BANCARIOS REALES")
print("=" * 80)

# 1. Leer todas las facturas marcadas como pendientes
wb = openpyxl.load_workbook(EXCEL_PATH)
ws = wb['TRANSACCIONES']

facturas_pendientes = []
for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), 2):
    if not row[0]:
        continue

    tipo = str(row[1]) if row[1] else ""
    estado = str(row[11]) if row[11] else ""

    if 'Factura Proveedor' in tipo and estado == 'Pendiente':
        facturas_pendientes.append({
            'fila': i,
            'fecha': row[0],
            'proveedor': str(row[5]) if row[5] else "",
            'concepto': str(row[6]) if row[6] else "",
            'referencia': str(row[7]) if row[7] else "",
            'monto': float(row[8]) if row[8] else 0
        })

print(f"\n[1] Facturas marcadas como PENDIENTES: {len(facturas_pendientes)}")
print("-" * 80)
for f in facturas_pendientes:
    fecha_str = f['fecha'].strftime('%d/%m/%Y') if f['fecha'] else 'N/A'
    print(f"  {fecha_str} | {f['proveedor'][:25]:25} | ${f['monto']:>10.2f} | {f['referencia'][:15]}")

# 2. Leer extractos bancarios
print("\n" + "=" * 80)
print("[2] Leyendo extractos bancarios REALES...")
print("-" * 80)

extractos = []

# Leer Promerica USD
promerica_usd = os.path.join(DATA_DIR, "estado_cuenta_promerica_usd_oct2025.txt")
if os.path.exists(promerica_usd):
    with open(promerica_usd, 'r', encoding='utf-8') as f:
        contenido = f.read()
        extractos.append(('Promerica USD', contenido))
        print(f"  ✓ Promerica USD (Octubre)")

# Leer Promerica corporativa noviembre
promerica_nov = os.path.join(DATA_DIR, "promerica_corporativa_usd_nov2025.csv")
if os.path.exists(promerica_nov):
    with open(promerica_nov, 'r', encoding='utf-8') as f:
        contenido = f.read()
        extractos.append(('Promerica USD Nov', contenido))
        print(f"  ✓ Promerica USD (Noviembre)")

# Leer BNCR
bncr_files = ['bncr_100_02_601066_oct_nov2025.txt']
for bncr_file in bncr_files:
    bncr_path = os.path.join(DATA_DIR, bncr_file)
    if os.path.exists(bncr_path):
        with open(bncr_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
            extractos.append(('BNCR USD', contenido))
            print(f"  ✓ {bncr_file}")

# 3. Buscar cada factura en los extractos
print("\n" + "=" * 80)
print("[3] VALIDACIÓN: ¿Cuáles facturas YA FUERON PAGADAS?")
print("=" * 80)

facturas_ya_pagadas = []
facturas_realmente_pendientes = []

for factura in facturas_pendientes:
    proveedor = factura['proveedor'].upper()
    monto = factura['monto']
    monto_str = f"{monto:.2f}"

    print(f"\n→ Verificando: {proveedor[:30]:30} ${monto:>10.2f}")

    # Buscar en extractos
    encontrado = False

    # Palabras clave del proveedor
    palabras_clave = []
    if 'INTCOMEX' in proveedor:
        palabras_clave = ['INTCOMEX', 'INTC']
    elif 'UNOPETROL' in proveedor:
        palabras_clave = ['UNOPETROL', 'BARREL']
    elif 'EUROCOMP' in proveedor:
        palabras_clave = ['EUROCOMP']
    elif 'INDUSTRIAS' in proveedor or 'BUENOS AIRES' in proveedor:
        palabras_clave = ['INDUSTRIAS', 'BUENOS AIRES', 'IBASA']
    elif 'SEA GLOBAL' in proveedor:
        palabras_clave = ['SEA GLOBAL', 'LOGISTICS']
    else:
        palabras_clave = [proveedor.split()[0]]  # Primera palabra

    for banco, extracto in extractos:
        # Buscar por proveedor
        for palabra in palabras_clave:
            if palabra in extracto.upper():
                # Verificar si el monto coincide
                # Buscar líneas con el proveedor
                lineas = extracto.split('\n')
                for linea in lineas:
                    if palabra in linea.upper():
                        # Buscar monto en la línea o líneas cercanas
                        # Buscar patrones de monto como: $63.03, 63.03, -63.03
                        patron_monto = re.findall(r'[\$\-]?\s*(\d+[\.,]\d{2})', linea)
                        for m in patron_monto:
                            m_clean = m.replace(',', '.')
                            if abs(float(m_clean) - monto) < 0.1:
                                print(f"  ✓ ENCONTRADO en {banco}: {linea.strip()[:70]}")
                                encontrado = True
                                break
                        if encontrado:
                            break
                if encontrado:
                    break
        if encontrado:
            break

    if encontrado:
        facturas_ya_pagadas.append(factura)
        print(f"  ⚠️  CONCLUSIÓN: FACTURA YA PAGADA (marcar como completada)")
    else:
        facturas_realmente_pendientes.append(factura)
        print(f"  ✓ CONCLUSIÓN: Realmente pendiente")

# 4. Resumen
print("\n" + "=" * 80)
print("RESUMEN DE AUDITORÍA")
print("=" * 80)

print(f"\n📊 ESTADÍSTICAS:")
print(f"  Total facturas marcadas PENDIENTES:     {len(facturas_pendientes)}")
print(f"  Facturas YA PAGADAS (error):            {len(facturas_ya_pagadas)}")
print(f"  Facturas REALMENTE PENDIENTES:          {len(facturas_realmente_pendientes)}")

if facturas_ya_pagadas:
    print(f"\n❌ FACTURAS CON ERROR - YA PAGADAS:")
    print("-" * 80)
    total_error = 0
    for f in facturas_ya_pagadas:
        print(f"  Fila {f['fila']:3}: {f['proveedor'][:30]:30} | ${f['monto']:>10.2f}")
        total_error += f['monto']
    print(f"\n  MONTO TOTAL INCORRECTAMENTE MARCADO COMO PENDIENTE: ${total_error:,.2f}")

if facturas_realmente_pendientes:
    print(f"\n✓ FACTURAS REALMENTE PENDIENTES:")
    print("-" * 80)
    total_pendiente = 0
    for f in facturas_realmente_pendientes:
        print(f"  Fila {f['fila']:3}: {f['proveedor'][:30]:30} | ${f['monto']:>10.2f}")
        total_pendiente += f['monto']
    print(f"\n  TOTAL REALMENTE POR PAGAR: ${total_pendiente:,.2f}")

wb.close()
print("\n" + "=" * 80)
