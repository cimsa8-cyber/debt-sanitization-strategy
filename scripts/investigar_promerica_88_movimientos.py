#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INVESTIGACIÓN: 88 movimientos de Promerica USD 1774
Identifica duplicados, movimientos fuera de período, y problemas
"""
import openpyxl
from datetime import datetime
from collections import defaultdict
import sys
import os

try:
    from alias_cuentas import obtener_nombre_canonico
except ImportError:
    print("ERROR: No se pudo importar alias_cuentas.py")
    sys.exit(1)

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"

print("="*80)
print("INVESTIGACIÓN: 88 MOVIMIENTOS PROMERICA USD 1774")
print("="*80)

if not os.path.exists(EXCEL_FILE):
    print(f"\nERROR: No se encontró {EXCEL_FILE}")
    sys.exit(1)

# Cargar Excel
wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
ws_trans = wb['TRANSACCIONES']

# Leer TODOS los movimientos de Promerica (cualquier nombre)
print("\nLeyendo movimientos de Promerica...")

movimientos_promerica = []

for row in range(2, ws_trans.max_row + 1):
    cuenta_original = ws_trans[f'E{row}'].value

    if not cuenta_original:
        continue

    cuenta_canonica = obtener_nombre_canonico(str(cuenta_original).strip())

    if cuenta_canonica != "Promerica USD 1774":
        continue

    # Leer todos los campos
    fecha = ws_trans[f'A{row}'].value
    tipo = ws_trans[f'B{row}'].value
    concepto = ws_trans[f'G{row}'].value
    referencia = ws_trans[f'H{row}'].value
    monto_usd = ws_trans[f'I{row}'].value
    tipo_mov = ws_trans[f'K{row}'].value
    id_trans = ws_trans[f'P{row}'].value

    try:
        monto = float(monto_usd) if monto_usd else 0
    except:
        monto = 0

    if monto == 0:
        continue

    # Aplicar signo
    if tipo_mov and 'Egreso' in str(tipo_mov):
        monto_signed = -abs(monto)
    else:
        monto_signed = abs(monto)

    movimientos_promerica.append({
        'fila': row,
        'fecha': fecha,
        'tipo': tipo,
        'concepto': concepto,
        'referencia': referencia,
        'monto_usd': monto,
        'monto_signed': monto_signed,
        'tipo_mov': tipo_mov,
        'id_trans': id_trans,
        'nombre_cuenta_usado': str(cuenta_original).strip()
    })

print(f"✓ Total movimientos encontrados: {len(movimientos_promerica)}")

# Agrupar por nombre de cuenta usado
por_nombre = defaultdict(list)
for mov in movimientos_promerica:
    por_nombre[mov['nombre_cuenta_usado']].append(mov)

print(f"\nDesglose por nombre usado:")
for nombre, movs in sorted(por_nombre.items()):
    print(f"  - '{nombre}': {len(movs)} movimientos")

# Ordenar por fecha
movimientos_promerica.sort(key=lambda x: x['fecha'] if x['fecha'] else datetime(1900, 1, 1))

# Agrupar por mes
print("\n" + "="*80)
print("MOVIMIENTOS POR MES")
print("="*80)

por_mes = defaultdict(list)
for mov in movimientos_promerica:
    if mov['fecha']:
        mes = mov['fecha'].strftime('%Y-%m')
        por_mes[mes].append(mov)
    else:
        por_mes['SIN_FECHA'].append(mov)

for mes in sorted(por_mes.keys()):
    movs = por_mes[mes]
    saldo_mes = sum([m['monto_signed'] for m in movs])
    print(f"\n{mes}: {len(movs)} movimientos, Saldo neto: ${saldo_mes:,.2f}")

    # Mostrar primeros 10
    for i, mov in enumerate(movs[:10]):
        fecha_str = mov['fecha'].strftime('%d/%m/%Y') if mov['fecha'] else 'SIN FECHA'
        signo = "+" if mov['monto_signed'] > 0 else ""
        print(f"   Fila {mov['fila']} | {fecha_str} | {signo}${mov['monto_signed']:>8.2f} | {mov['concepto'][:40] if mov['concepto'] else 'SIN CONCEPTO'}")

    if len(movs) > 10:
        print(f"   ... y {len(movs) - 10} movimientos más")

# Identificar duplicados potenciales
print("\n" + "="*80)
print("ANÁLISIS DE DUPLICADOS")
print("="*80)

# Por fecha + referencia
duplicados_ref = defaultdict(list)
for mov in movimientos_promerica:
    if mov['fecha'] and mov['referencia']:
        fecha_str = mov['fecha'].strftime('%Y-%m-%d')
        clave = f"{fecha_str}_{mov['referencia']}"
        duplicados_ref[clave].append(mov)

duplicados_encontrados = {k: v for k, v in duplicados_ref.items() if len(v) > 1}

if duplicados_encontrados:
    print(f"\n⚠️ Encontrados {len(duplicados_encontrados)} posibles duplicados (misma fecha + referencia):")

    for clave, movs in sorted(duplicados_encontrados.items()):
        print(f"\n   {clave}: {len(movs)} movimientos")
        for mov in movs:
            print(f"      Fila {mov['fila']} | ${mov['monto_usd']:>8.2f} | '{mov['nombre_cuenta_usado']}' | {mov['concepto'][:35]}")
else:
    print("\n✅ No se encontraron duplicados por fecha+referencia")

# Por concepto + monto
duplicados_concepto = defaultdict(list)
for mov in movimientos_promerica:
    if mov['concepto'] and mov['monto_usd']:
        clave = f"{mov['concepto'][:50]}_{mov['monto_usd']:.2f}"
        duplicados_concepto[clave].append(mov)

duplicados_concepto_encontrados = {k: v for k, v in duplicados_concepto.items() if len(v) > 1}

if len(duplicados_concepto_encontrados) > 0:
    print(f"\n⚠️ Encontrados {len(duplicados_concepto_encontrados)} posibles duplicados (mismo concepto + monto):")
    for i, (clave, movs) in enumerate(sorted(duplicados_concepto_encontrados.items())[:5]):
        print(f"\n   {clave}: {len(movs)} movimientos")
        for mov in movs:
            fecha_str = mov['fecha'].strftime('%d/%m/%Y') if mov['fecha'] else 'SIN FECHA'
            print(f"      Fila {mov['fila']} | {fecha_str} | Ref: {mov['referencia']}")

    if len(duplicados_concepto_encontrados) > 5:
        print(f"\n   ... y {len(duplicados_concepto_encontrados) - 5} grupos más")

# Movimientos de septiembre (sospechosos)
print("\n" + "="*80)
print("MOVIMIENTOS DE SEPTIEMBRE (SOSPECHOSOS)")
print("="*80)

movs_septiembre = por_mes.get('2025-09', [])
if movs_septiembre:
    print(f"\n⚠️ Hay {len(movs_septiembre)} movimientos de SEPTIEMBRE:")
    saldo_sept = sum([m['monto_signed'] for m in movs_septiembre])
    print(f"   Saldo neto septiembre: ${saldo_sept:,.2f}")

    for mov in movs_septiembre:
        fecha_str = mov['fecha'].strftime('%d/%m/%Y')
        signo = "+" if mov['monto_signed'] > 0 else ""
        print(f"   Fila {mov['fila']} | {fecha_str} | {signo}${mov['monto_signed']:>8.2f} | {mov['concepto'][:40]}")

    print(f"\n   💡 Si estos NO deberían estar, eliminarlos reduciría el saldo en ${abs(saldo_sept):,.2f}")
else:
    print("\n✅ No hay movimientos de septiembre")

# Calcular saldos por período
print("\n" + "="*80)
print("CÁLCULO DE SALDOS POR PERÍODO")
print("="*80)

# Septiembre
saldo_sept = sum([m['monto_signed'] for m in por_mes.get('2025-09', [])])

# Octubre
saldo_oct = sum([m['monto_signed'] for m in por_mes.get('2025-10', [])])

# Noviembre
saldo_nov = sum([m['monto_signed'] for m in por_mes.get('2025-11', [])])

# Total
saldo_total = sum([m['monto_signed'] for m in movimientos_promerica])

print(f"\nSeptiembre 2025: ${saldo_sept:,.2f} ({len(por_mes.get('2025-09', []))} movimientos)")
print(f"Octubre 2025: ${saldo_oct:,.2f} ({len(por_mes.get('2025-10', []))} movimientos)")
print(f"Noviembre 2025: ${saldo_nov:,.2f} ({len(por_mes.get('2025-11', []))} movimientos)")
print(f"\n{'='*40}")
print(f"SALDO TOTAL: ${saldo_total:,.2f}")
print(f"{'='*40}")

print(f"\nBalance en hoja Efectivo (01/11): $2,999.24")
print(f"Diferencia: ${saldo_total - 2999.24:,.2f}")

# Análisis del saldo inicial
movs_saldo_inicial = [m for m in movimientos_promerica if m['tipo'] and 'Saldo Inicial' in str(m['tipo'])]

if movs_saldo_inicial:
    print(f"\n✓ Saldos iniciales encontrados: {len(movs_saldo_inicial)}")
    for mov in movs_saldo_inicial:
        fecha_str = mov['fecha'].strftime('%d/%m/%Y') if mov['fecha'] else 'SIN FECHA'
        print(f"   Fila {mov['fila']} | {fecha_str} | ${mov['monto_usd']:,.2f} | {mov['concepto'][:50]}")
else:
    print(f"\n⚠️ No se encontraron movimientos de tipo 'Saldo Inicial'")

print("\n" + "="*80)
print("DIAGNÓSTICO")
print("="*80)

print(f"""
PROBLEMA IDENTIFICADO:
  - Total movimientos: {len(movimientos_promerica)}
  - Saldo calculado: ${saldo_total:,.2f}
  - Balance Efectivo: $2,999.24
  - Diferencia: ${saldo_total - 2999.24:,.2f}

POSIBLES CAUSAS:
  1. Movimientos de SEPTIEMBRE que no deberían estar
  2. Duplicados entre los 3 nombres diferentes
  3. Movimientos de otra cuenta Promerica mezclados
  4. Balance inicial incorrecto

RECOMENDACIONES:
  1. Si hay movimientos de septiembre, verificar si son correctos
  2. Revisar duplicados potenciales
  3. Comparar con extracto bancario completo
  4. Verificar que todos los movimientos sean de cuenta 1774
""")

print("\n" + "="*80)
