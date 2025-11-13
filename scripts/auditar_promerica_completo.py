#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoría completa de Promerica USD 1774
Calcula saldo real desde transacciones y compara con hoja Efectivo
"""
import openpyxl
from datetime import datetime
from collections import defaultdict

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"

print("="*80)
print("AUDITORIA: PROMERICA USD 1774")
print("="*80)

# Cargar Excel
wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
ws_trans = wb['TRANSACCIONES']

# Leer todas las transacciones de Promerica
movimientos_promerica = []

print("\nLeyendo transacciones de Promerica...")

for row in range(2, ws_trans.max_row + 1):
    cuenta = ws_trans[f'E{row}'].value

    if cuenta and 'Promerica USD 1774' in str(cuenta):
        fecha = ws_trans[f'A{row}'].value
        tipo = ws_trans[f'B{row}'].value
        concepto = ws_trans[f'G{row}'].value
        referencia = ws_trans[f'H{row}'].value
        monto_usd = ws_trans[f'I{row}'].value
        tipo_mov = ws_trans[f'K{row}'].value

        # Convertir a número
        try:
            monto = float(monto_usd) if monto_usd else 0
        except:
            monto = 0

        if monto != 0:
            movimientos_promerica.append({
                'fila': row,
                'fecha': fecha,
                'tipo': tipo,
                'concepto': concepto,
                'referencia': referencia,
                'monto': monto,
                'tipo_mov': tipo_mov
            })

print(f"Total movimientos Promerica encontrados: {len(movimientos_promerica)}")

# Ordenar por fecha
movimientos_promerica.sort(key=lambda x: x['fecha'] if x['fecha'] else datetime(1900, 1, 1))

# Calcular saldo acumulado
print("\n" + "="*80)
print("MOVIMIENTOS DE PROMERICA USD 1774 (ORDENADOS POR FECHA)")
print("="*80)

saldo = 0
movimientos_por_mes = defaultdict(list)

for mov in movimientos_promerica:
    # Determinar si es ingreso o egreso
    if mov['tipo_mov'] and 'Ingreso' in str(mov['tipo_mov']):
        saldo += mov['monto']
        signo = "+"
    else:
        saldo -= mov['monto']
        signo = "-"

    # Agrupar por mes
    if mov['fecha']:
        mes = mov['fecha'].strftime('%Y-%m')
        movimientos_por_mes[mes].append({
            'fecha': mov['fecha'].strftime('%d/%m/%Y'),
            'concepto': mov['concepto'][:45] if mov['concepto'] else '',
            'referencia': mov['referencia'],
            'monto': mov['monto'],
            'signo': signo,
            'saldo': saldo
        })

# Mostrar por mes
for mes in sorted(movimientos_por_mes.keys()):
    movs = movimientos_por_mes[mes]
    print(f"\n{mes} - {len(movs)} movimientos")
    print("-" * 80)

    for m in movs:
        print(f"{m['fecha']} | {m['signo']}${m['monto']:>8.2f} | Saldo: ${m['saldo']:>10.2f} | {m['concepto']}")

# Calcular totales
total_ingresos = sum([m['monto'] for m in movimientos_promerica if m['tipo_mov'] and 'Ingreso' in str(m['tipo_mov'])])
total_egresos = sum([m['monto'] for m in movimientos_promerica if m['tipo_mov'] and 'Egreso' in str(m['tipo_mov'])])

print("\n" + "="*80)
print("RESUMEN FINANCIERO")
print("="*80)
print(f"\nTotal ingresos: ${total_ingresos:,.2f}")
print(f"Total egresos: ${total_egresos:,.2f}")
print(f"Saldo neto calculado: ${saldo:,.2f}")

# Leer lo que dice la hoja Efectivo
print("\n" + "="*80)
print("COMPARACION CON HOJA EFECTIVO")
print("="*80)

try:
    ws_efectivo = wb['Efectivo']

    # Buscar la línea de Promerica USD
    for row in range(1, 20):  # Buscar en las primeras 20 filas
        concepto = ws_efectivo[f'B{row}'].value
        if concepto and 'Promerica USD' in str(concepto):
            fecha_efectivo = ws_efectivo[f'A{row}'].value
            cuenta_efectivo = ws_efectivo[f'C{row}'].value
            ingreso_efectivo = ws_efectivo[f'D{row}'].value
            balance_efectivo = ws_efectivo[f'F{row}'].value

            print(f"\nHoja Efectivo dice:")
            print(f"  Fecha: {fecha_efectivo}")
            print(f"  Concepto: {concepto}")
            print(f"  Cuenta: {cuenta_efectivo}")
            print(f"  Balance: ${balance_efectivo:,.2f}" if balance_efectivo else "  Balance: (vacio)")

            print(f"\nSegún TRANSACCIONES:")
            print(f"  Saldo calculado: ${saldo:,.2f}")

            if balance_efectivo:
                diferencia = saldo - float(balance_efectivo)
                print(f"\nDIFERENCIA: ${diferencia:,.2f}")

                if abs(diferencia) > 0.01:
                    print(f"\n⚠️ INCONSISTENCIA DETECTADA: ${abs(diferencia):,.2f}")
                else:
                    print(f"\n✅ Saldos coinciden")

            break
except Exception as e:
    print(f"\n⚠️ No se pudo leer la hoja Efectivo: {e}")

# Movimientos recientes (últimos 20)
print("\n" + "="*80)
print("ULTIMOS 20 MOVIMIENTOS DE PROMERICA")
print("="*80)

for mov in movimientos_promerica[-20:]:
    fecha_str = mov['fecha'].strftime('%d/%m/%Y') if mov['fecha'] else 'SIN FECHA'
    tipo_mov = mov['tipo_mov'] if mov['tipo_mov'] else 'N/A'
    concepto = mov['concepto'][:50] if mov['concepto'] else ''
    print(f"Fila {mov['fila']} | {fecha_str} | {tipo_mov:8} | ${mov['monto']:>8.2f} | {concepto}")

# Análisis de movimientos de noviembre
print("\n" + "="*80)
print("MOVIMIENTOS DE NOVIEMBRE 2025")
print("="*80)

movs_nov = [m for m in movimientos_promerica if m['fecha'] and m['fecha'].month == 11 and m['fecha'].year == 2025]
print(f"\nTotal movimientos en noviembre: {len(movs_nov)}")

ingresos_nov = sum([m['monto'] for m in movs_nov if m['tipo_mov'] and 'Ingreso' in str(m['tipo_mov'])])
egresos_nov = sum([m['monto'] for m in movs_nov if m['tipo_mov'] and 'Egreso' in str(m['tipo_mov'])])

print(f"Ingresos noviembre: ${ingresos_nov:,.2f}")
print(f"Egresos noviembre: ${egresos_nov:,.2f}")
print(f"Neto noviembre: ${ingresos_nov - egresos_nov:,.2f}")

print("\nDetalle:")
for m in movs_nov:
    fecha_str = m['fecha'].strftime('%d/%m/%Y')
    signo = "+" if 'Ingreso' in str(m['tipo_mov']) else "-"
    concepto = m['concepto'][:45] if m['concepto'] else ''
    print(f"  {fecha_str} | {signo}${m['monto']:>8.2f} | {concepto}")

print("\n" + "="*80)
print("DIAGNOSTICO")
print("="*80)

print(f"""
Si la hoja Efectivo muestra un "Balance inicial" del 01/11/2025 de $2,999.24,
esto significa que es un SALDO DE CORTE al 01/11.

Los movimientos agregados incluyen:
- Movimientos de OCTUBRE (21/10 al 30/10): NO afectan el balance del 01/11
- Movimientos de NOVIEMBRE (03/11 al 10/11): SÍ deberían afectar

El saldo real al DÍA DE HOY debería ser:
  Balance 01/11: $2,999.24
  + Movimientos noviembre: ${ingresos_nov - egresos_nov:,.2f}
  = Saldo actual: ${2999.24 + (ingresos_nov - egresos_nov):,.2f}

Pero según TODAS las transacciones de Promerica en el Excel:
  Saldo calculado: ${saldo:,.2f}

POSIBLES CAUSAS DE DISCREPANCIA:
1. El "balance inicial" del 01/11 no refleja correctamente el saldo real a esa fecha
2. Hay movimientos de octubre que no están registrados
3. Hay movimientos anteriores a octubre que faltan
4. El balance inicial fue ingresado manualmente y no se actualizó
""")

print("\n" + "="*80)
