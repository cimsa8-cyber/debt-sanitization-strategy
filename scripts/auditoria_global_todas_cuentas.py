#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDITORÍA GLOBAL - TODAS LAS CUENTAS
Verifica consistencia entre transacciones y hoja Efectivo
Identifica saldos iniciales faltantes y discrepancias
"""
import openpyxl
from datetime import datetime
from collections import defaultdict

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"

print("="*80)
print("AUDITORIA GLOBAL - TODAS LAS CUENTAS BANCARIAS Y TARJETAS")
print("="*80)

# Cargar Excel
wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
ws_trans = wb['TRANSACCIONES']

# Leer todas las transacciones agrupadas por cuenta
print("\nAnalizando todas las transacciones...")

movimientos_por_cuenta = defaultdict(list)
cuentas_detectadas = set()

for row in range(2, ws_trans.max_row + 1):
    cuenta = ws_trans[f'E{row}'].value

    if cuenta and cuenta != 'Cuenta Bancaria':  # Skip header
        fecha = ws_trans[f'A{row}'].value
        concepto = ws_trans[f'G{row}'].value
        monto_usd = ws_trans[f'I{row}'].value
        monto_crc = ws_trans[f'J{row}'].value
        tipo_mov = ws_trans[f'K{row}'].value

        cuenta_str = str(cuenta).strip()
        cuentas_detectadas.add(cuenta_str)

        # Determinar monto y moneda
        try:
            if monto_usd and float(monto_usd) != 0:
                monto = float(monto_usd)
                moneda = 'USD'
            elif monto_crc and float(monto_crc) != 0:
                monto = float(monto_crc)
                moneda = 'CRC'
            else:
                continue
        except:
            continue

        # Aplicar signo según tipo de movimiento
        if tipo_mov and 'Egreso' in str(tipo_mov):
            monto = -abs(monto)
        else:
            monto = abs(monto)

        movimientos_por_cuenta[cuenta_str].append({
            'fila': row,
            'fecha': fecha,
            'concepto': concepto,
            'monto': monto,
            'moneda': moneda,
            'tipo_mov': tipo_mov
        })

print(f"\n✓ Total cuentas detectadas: {len(cuentas_detectadas)}")
print(f"✓ Total transacciones analizadas: {sum([len(v) for v in movimientos_por_cuenta.values()])}")

# Calcular saldos por cuenta
print("\n" + "="*80)
print("SALDOS CALCULADOS POR CUENTA (DESDE TRANSACCIONES)")
print("="*80)

saldos_calculados = {}

for cuenta in sorted(cuentas_detectadas):
    movs = movimientos_por_cuenta[cuenta]

    if not movs:
        continue

    # Ordenar por fecha
    movs_ordenados = sorted([m for m in movs if m['fecha']], key=lambda x: x['fecha'])

    # Calcular saldo
    saldo = sum([m['monto'] for m in movs])
    moneda = movs[0]['moneda'] if movs else 'USD'

    # Fecha primer y último movimiento
    fecha_primer = movs_ordenados[0]['fecha'] if movs_ordenados else None
    fecha_ultimo = movs_ordenados[-1]['fecha'] if movs_ordenados else None

    saldos_calculados[cuenta] = {
        'saldo': saldo,
        'moneda': moneda,
        'num_movimientos': len(movs),
        'fecha_primer_mov': fecha_primer,
        'fecha_ultimo_mov': fecha_ultimo
    }

    # Mostrar
    fecha_primer_str = fecha_primer.strftime('%d/%m/%Y') if fecha_primer else 'N/A'
    fecha_ultimo_str = fecha_ultimo.strftime('%d/%m/%Y') if fecha_ultimo else 'N/A'

    print(f"\n{cuenta}")
    print(f"  Movimientos: {len(movs)}")
    print(f"  Rango: {fecha_primer_str} a {fecha_ultimo_str}")
    print(f"  Saldo calculado: {moneda} {saldo:,.2f}")

# Leer saldos de hoja Efectivo
print("\n" + "="*80)
print("COMPARACION CON HOJA EFECTIVO")
print("="*80)

try:
    ws_efectivo = wb['Efectivo']

    saldos_efectivo = {}

    # Buscar todas las líneas de balance inicial
    for row in range(1, 50):  # Buscar en primeras 50 filas
        concepto = ws_efectivo[f'B{row}'].value

        if concepto and 'Balance inicial' in str(concepto):
            cuenta = ws_efectivo[f'C{row}'].value
            balance = ws_efectivo[f'F{row}'].value
            fecha = ws_efectivo[f'A{row}'].value

            if cuenta and balance:
                saldos_efectivo[str(cuenta).strip()] = {
                    'balance': float(balance),
                    'fecha': fecha
                }

    print(f"\n✓ Encontrados {len(saldos_efectivo)} balances iniciales en hoja Efectivo")

    # Comparar
    print("\n" + "="*80)
    print("ANALISIS DE DISCREPANCIAS")
    print("="*80)

    discrepancias = []

    for cuenta in sorted(cuentas_detectadas):
        if cuenta not in saldos_calculados:
            continue

        calc = saldos_calculados[cuenta]

        # Buscar en efectivo (puede tener nombre ligeramente diferente)
        saldo_efectivo = None
        cuenta_efectivo_match = None

        for cuenta_ef, data_ef in saldos_efectivo.items():
            # Comparación flexible (contiene parte del nombre)
            if cuenta in cuenta_ef or cuenta_ef in cuenta:
                saldo_efectivo = data_ef['balance']
                cuenta_efectivo_match = cuenta_ef
                break

        if saldo_efectivo is None:
            print(f"\n⚠️ {cuenta}")
            print(f"  Saldo calculado: {calc['moneda']} {calc['saldo']:,.2f}")
            print(f"  Saldo en Efectivo: NO ENCONTRADO")
            print(f"  ⚠️ FALTA BALANCE INICIAL EN HOJA EFECTIVO")

            discrepancias.append({
                'cuenta': cuenta,
                'tipo': 'FALTA_EN_EFECTIVO',
                'saldo_calc': calc['saldo'],
                'moneda': calc['moneda']
            })
        else:
            diferencia = calc['saldo'] - saldo_efectivo

            if abs(diferencia) > 0.01:  # Tolerancia de 1 centavo
                print(f"\n⚠️ {cuenta}")
                print(f"  Saldo calculado: {calc['moneda']} {calc['saldo']:,.2f}")
                print(f"  Saldo en Efectivo: {calc['moneda']} {saldo_efectivo:,.2f}")
                print(f"  DIFERENCIA: {calc['moneda']} {diferencia:,.2f}")

                # Diagnóstico
                if calc['saldo'] < 0 and saldo_efectivo > 0:
                    print(f"  ⚠️ POSIBLE CAUSA: Falta saldo inicial en transacciones")
                    print(f"  💡 SOLUCION: Agregar saldo inicial ~{calc['moneda']} {saldo_efectivo - calc['saldo']:,.2f}")
                elif abs(diferencia) < calc['saldo'] * 0.1:  # Diferencia < 10%
                    print(f"  ⚠️ POSIBLE CAUSA: Movimientos faltantes o comisiones no registradas")
                else:
                    print(f"  ⚠️ POSIBLE CAUSA: Error significativo - revisar extractos")

                discrepancias.append({
                    'cuenta': cuenta,
                    'tipo': 'DIFERENCIA',
                    'saldo_calc': calc['saldo'],
                    'saldo_efectivo': saldo_efectivo,
                    'diferencia': diferencia,
                    'moneda': calc['moneda']
                })
            else:
                print(f"\n✅ {cuenta}")
                print(f"  Saldo calculado: {calc['moneda']} {calc['saldo']:,.2f}")
                print(f"  Saldo en Efectivo: {calc['moneda']} {saldo_efectivo:,.2f}")
                print(f"  ✓ COINCIDEN (diferencia < 1 centavo)")

except Exception as e:
    print(f"\n⚠️ Error al leer hoja Efectivo: {e}")

# Resumen final
print("\n" + "="*80)
print("RESUMEN DE AUDITORIA")
print("="*80)

print(f"\nTotal cuentas analizadas: {len(cuentas_detectadas)}")
print(f"Total discrepancias encontradas: {len(discrepancias)}")

if discrepancias:
    print(f"\n⚠️ CUENTAS CON PROBLEMAS:")
    for disc in discrepancias:
        if disc['tipo'] == 'DIFERENCIA':
            print(f"  - {disc['cuenta']}: Diferencia {disc['moneda']} {disc['diferencia']:,.2f}")
        else:
            print(f"  - {disc['cuenta']}: {disc['tipo']}")

# Análisis de saldos iniciales faltantes
print("\n" + "="*80)
print("ANALISIS: SALDOS INICIALES FALTANTES")
print("="*80)

print("""
TEORIA: Si una cuenta muestra saldo NEGATIVO en las transacciones
pero POSITIVO en la hoja Efectivo, probablemente FALTA el saldo inicial.

CUENTAS A REVISAR:
""")

for cuenta, data in saldos_calculados.items():
    if data['saldo'] < 0:
        print(f"\n⚠️ {cuenta}")
        print(f"  Saldo calculado: {data['moneda']} {data['saldo']:,.2f} (NEGATIVO)")
        print(f"  Primer movimiento: {data['fecha_primer_mov'].strftime('%d/%m/%Y') if data['fecha_primer_mov'] else 'N/A'}")
        print(f"  💡 Probablemente necesita saldo inicial antes del {data['fecha_primer_mov'].strftime('%d/%m/%Y') if data['fecha_primer_mov'] else 'N/A'}")

# Índice de fiabilidad
print("\n" + "="*80)
print("INDICE DE FIABILIDAD DEL EXCEL")
print("="*80)

total_cuentas = len(cuentas_detectadas)
cuentas_ok = total_cuentas - len(discrepancias)
porcentaje_fiabilidad = (cuentas_ok / total_cuentas * 100) if total_cuentas > 0 else 0

print(f"\nCuentas correctas: {cuentas_ok} / {total_cuentas}")
print(f"Cuentas con problemas: {len(discrepancias)} / {total_cuentas}")
print(f"\n{'='*40}")
print(f"FIABILIDAD ACTUAL: {porcentaje_fiabilidad:.1f}%")
print(f"{'='*40}")

if porcentaje_fiabilidad >= 90:
    print("\n✅ EXCELENTE: Excel muy confiable")
elif porcentaje_fiabilidad >= 75:
    print("\n⚠️ BUENO: Excel generalmente confiable, con algunos ajustes menores")
elif porcentaje_fiabilidad >= 50:
    print("\n⚠️ REGULAR: Excel necesita correcciones importantes")
else:
    print("\n❌ BAJO: Excel necesita auditoría completa y corrección")

print("\n" + "="*80)
print("RECOMENDACIONES")
print("="*80)

if len(discrepancias) > 0:
    print("\n1. CORREGIR discrepancias encontradas")
    print("2. AGREGAR saldos iniciales faltantes")
    print("3. VALIDAR con extractos bancarios completos")
    print("4. EJECUTAR esta auditoría nuevamente después de correcciones")
else:
    print("\n✅ No se encontraron discrepancias significativas")
    print("✅ El Excel parece estar bien conciliado")

print("\n" + "="*80)
