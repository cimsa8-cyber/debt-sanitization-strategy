#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDITORÍA GLOBAL CON SISTEMA DE ALIAS
Reconoce automáticamente todas las variaciones de nombres
y consolida saldos correctamente
"""
import openpyxl
from datetime import datetime
from collections import defaultdict
import sys
import os

# Importar sistema de alias
try:
    from alias_cuentas import (
        obtener_nombre_canonico,
        listar_cuentas,
        es_misma_cuenta,
        es_balance_inicial
    )
except ImportError:
    print("ERROR: No se pudo importar alias_cuentas.py")
    print("Asegúrese de que alias_cuentas.py esté en el mismo directorio")
    sys.exit(1)

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"

print("="*80)
print("AUDITORIA GLOBAL CON SISTEMA DE ALIAS")
print("="*80)

if not os.path.exists(EXCEL_FILE):
    print(f"\nERROR: No se encontró {EXCEL_FILE}")
    sys.exit(1)

# Cargar Excel
wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
ws_trans = wb['TRANSACCIONES']

# Leer transacciones y agrupar por cuenta canónica
print("\nLeyendo transacciones y aplicando alias...")

movimientos_por_cuenta = defaultdict(list)
nombres_originales_por_cuenta = defaultdict(set)
total_transacciones = 0
transacciones_no_reconocidas = []

for row in range(2, ws_trans.max_row + 1):
    cuenta_original = ws_trans[f'E{row}'].value

    if not cuenta_original or str(cuenta_original).strip() == 'Cuenta Bancaria':
        continue

    cuenta_original = str(cuenta_original).strip()

    # Obtener nombre canónico usando sistema de alias
    cuenta_canonica = obtener_nombre_canonico(cuenta_original)

    if not cuenta_canonica:
        # No se reconoció - agregar a lista de no reconocidos
        transacciones_no_reconocidas.append({
            'fila': row,
            'cuenta_original': cuenta_original
        })
        continue

    # Guardar nombre original usado
    nombres_originales_por_cuenta[cuenta_canonica].add(cuenta_original)

    # Leer datos del movimiento
    fecha = ws_trans[f'A{row}'].value
    concepto = ws_trans[f'G{row}'].value
    monto_usd = ws_trans[f'I{row}'].value
    monto_crc = ws_trans[f'J{row}'].value
    tipo_mov = ws_trans[f'K{row}'].value

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

    # Aplicar signo
    if tipo_mov and 'Egreso' in str(tipo_mov):
        monto = -abs(monto)
    else:
        monto = abs(monto)

    movimientos_por_cuenta[cuenta_canonica].append({
        'fila': row,
        'fecha': fecha,
        'concepto': concepto,
        'monto': monto,
        'moneda': moneda,
        'tipo_mov': tipo_mov,
        'nombre_usado': cuenta_original
    })

    total_transacciones += 1

print(f"✓ Total transacciones analizadas: {total_transacciones}")
print(f"✓ Cuentas canónicas detectadas: {len(movimientos_por_cuenta)}")

if transacciones_no_reconocidas:
    print(f"⚠️ Transacciones NO reconocidas: {len(transacciones_no_reconocidas)}")
    print("\nPrimeras 10 no reconocidas:")
    for t in transacciones_no_reconocidas[:10]:
        print(f"   Fila {t['fila']}: '{t['cuenta_original']}'")

# Leer hoja Efectivo
print("\nLeyendo hoja Efectivo...")

balances_efectivo = {}

try:
    ws_efectivo = wb['Efectivo']

    for row in range(1, 30):
        concepto = ws_efectivo[f'B{row}'].value
        cuenta_ef = ws_efectivo[f'C{row}'].value
        balance = ws_efectivo[f'F{row}'].value
        fecha = ws_efectivo[f'A{row}'].value

        # Verificar si es un balance inicial usando sistema de alias
        if not concepto or not cuenta_ef or not balance:
            continue

        # Usar función del sistema de alias para reconocer todos los formatos
        if not es_balance_inicial(concepto):
            continue

        # Convertir nombre de Efectivo a canónico
        cuenta_ef_str = str(cuenta_ef).strip()
        cuenta_canonica = obtener_nombre_canonico(cuenta_ef_str)

        if cuenta_canonica:
            try:
                balances_efectivo[cuenta_canonica] = {
                    'balance': float(balance),
                    'fecha': fecha,
                    'nombre_en_efectivo': cuenta_ef_str
                }
            except:
                pass

    print(f"✓ Balances en Efectivo: {len(balances_efectivo)}")

except Exception as e:
    print(f"⚠️ Error al leer hoja Efectivo: {e}")

# Calcular saldos consolidados
print("\n" + "="*80)
print("SALDOS CONSOLIDADOS POR CUENTA")
print("="*80)

saldos_calculados = {}
problemas_detectados = []

for cuenta_canonica in sorted(movimientos_por_cuenta.keys()):
    movs = movimientos_por_cuenta[cuenta_canonica]

    # Calcular saldo
    saldo_total = sum([m['monto'] for m in movs])
    moneda = movs[0]['moneda'] if movs else 'USD'

    # Fechas
    movs_con_fecha = [m for m in movs if m['fecha']]
    if movs_con_fecha:
        movs_ordenados = sorted(movs_con_fecha, key=lambda x: x['fecha'])
        fecha_primer_mov = movs_ordenados[0]['fecha']
        fecha_ultimo_mov = movs_ordenados[-1]['fecha']
    else:
        fecha_primer_mov = None
        fecha_ultimo_mov = None

    saldos_calculados[cuenta_canonica] = {
        'saldo': saldo_total,
        'moneda': moneda,
        'num_movimientos': len(movs),
        'fecha_primer_mov': fecha_primer_mov,
        'fecha_ultimo_mov': fecha_ultimo_mov,
        'nombres_usados': nombres_originales_por_cuenta[cuenta_canonica]
    }

    # Mostrar
    print(f"\n📊 {cuenta_canonica}")
    print(f"   Movimientos: {len(movs)}")

    # Mostrar nombres usados (si hay variaciones)
    if len(nombres_originales_por_cuenta[cuenta_canonica]) > 1:
        print(f"   ⚠️ Nombres usados ({len(nombres_originales_por_cuenta[cuenta_canonica])}):")
        for nombre in sorted(nombres_originales_por_cuenta[cuenta_canonica]):
            count = sum(1 for m in movs if m['nombre_usado'] == nombre)
            print(f"      - '{nombre}' ({count} transacciones)")
    else:
        nombre_unico = list(nombres_originales_por_cuenta[cuenta_canonica])[0]
        print(f"   ✓ Nombre único: '{nombre_unico}'")

    # Saldo calculado
    simbolo_moneda = '$' if moneda == 'USD' else '₡'
    print(f"   Saldo calculado: {simbolo_moneda}{saldo_total:,.2f}")

    # Comparar con Efectivo
    if cuenta_canonica in balances_efectivo:
        balance_ef = balances_efectivo[cuenta_canonica]['balance']
        nombre_ef = balances_efectivo[cuenta_canonica]['nombre_en_efectivo']

        diferencia = saldo_total - balance_ef

        print(f"   Balance Efectivo: ${balance_ef:,.2f}")
        if nombres_originales_por_cuenta[cuenta_canonica] != {nombre_ef}:
            print(f"      (bajo nombre: '{nombre_ef}')")

        if abs(diferencia) > 0.01:
            print(f"   ⚠️ DIFERENCIA: ${diferencia:,.2f}")

            # Diagnóstico
            if saldo_total < 0 and balance_ef > 0:
                saldo_inicial_necesario = balance_ef - saldo_total
                print(f"      💡 Falta saldo inicial de ~${saldo_inicial_necesario:,.2f}")
                problemas_detectados.append({
                    'cuenta': cuenta_canonica,
                    'tipo': 'FALTA_SALDO_INICIAL',
                    'saldo_necesario': saldo_inicial_necesario
                })
            elif abs(diferencia) < abs(balance_ef) * 0.1:
                porcentaje = abs(diferencia / balance_ef) * 100
                print(f"      💡 Movimientos faltantes (~{porcentaje:.1f}%)")
                problemas_detectados.append({
                    'cuenta': cuenta_canonica,
                    'tipo': 'MOVIMIENTOS_FALTANTES',
                    'diferencia': diferencia
                })
            else:
                print(f"      💡 Discrepancia significativa - revisar extractos")
                problemas_detectados.append({
                    'cuenta': cuenta_canonica,
                    'tipo': 'DISCREPANCIA_GRANDE',
                    'diferencia': diferencia
                })
        else:
            print(f"   ✅ COINCIDE con Efectivo")
    else:
        print(f"   ⚠️ NO está en hoja Efectivo")
        problemas_detectados.append({
            'cuenta': cuenta_canonica,
            'tipo': 'NO_EN_EFECTIVO'
        })

# Resumen
print("\n" + "="*80)
print("RESUMEN DE AUDITORIA")
print("="*80)

total_cuentas = len(saldos_calculados)
cuentas_con_problemas = len(set([p['cuenta'] for p in problemas_detectados]))
cuentas_ok = total_cuentas - cuentas_con_problemas

print(f"\nTotal cuentas (canónicas): {total_cuentas}")
print(f"Cuentas correctas: {cuentas_ok}")
print(f"Cuentas con problemas: {cuentas_con_problemas}")

if cuentas_con_problemas > 0:
    print(f"\n⚠️ PROBLEMAS DETECTADOS:")

    for tipo_problema in ['FALTA_SALDO_INICIAL', 'MOVIMIENTOS_FALTANTES', 'DISCREPANCIA_GRANDE', 'NO_EN_EFECTIVO']:
        problemas_tipo = [p for p in problemas_detectados if p['tipo'] == tipo_problema]
        if problemas_tipo:
            print(f"\n{tipo_problema} ({len(problemas_tipo)} cuentas):")
            for prob in problemas_tipo:
                if tipo_problema == 'FALTA_SALDO_INICIAL':
                    print(f"   - {prob['cuenta']}: Necesita saldo inicial ~${prob['saldo_necesario']:,.2f}")
                elif tipo_problema == 'MOVIMIENTOS_FALTANTES':
                    print(f"   - {prob['cuenta']}: Diferencia ${prob['diferencia']:,.2f}")
                elif tipo_problema == 'DISCREPANCIA_GRANDE':
                    print(f"   - {prob['cuenta']}: Diferencia ${prob['diferencia']:,.2f}")
                else:
                    print(f"   - {prob['cuenta']}")

# Análisis de nombres inconsistentes
print("\n" + "="*80)
print("ANALISIS: NOMBRES INCONSISTENTES")
print("="*80)

cuentas_con_multiples_nombres = []

for cuenta in sorted(saldos_calculados.keys()):
    if len(nombres_originales_por_cuenta[cuenta]) > 1:
        cuentas_con_multiples_nombres.append(cuenta)

if cuentas_con_multiples_nombres:
    print(f"\n⚠️ {len(cuentas_con_multiples_nombres)} cuentas usan múltiples nombres:")
    for cuenta in cuentas_con_multiples_nombres:
        print(f"\n   {cuenta}:")
        for nombre in sorted(nombres_originales_por_cuenta[cuenta]):
            print(f"      - '{nombre}'")
    print(f"\n💡 RECOMENDACIÓN: Normalizar a un solo nombre por cuenta")
    print(f"   (Aunque el sistema de alias ya los reconoce correctamente)")
else:
    print("\n✅ Todas las cuentas usan un nombre único")

# Fiabilidad
print("\n" + "="*80)
print("ÍNDICE DE FIABILIDAD")
print("="*80)

if total_cuentas > 0:
    fiabilidad = (cuentas_ok / total_cuentas) * 100
else:
    fiabilidad = 0

print(f"\n{'='*40}")
print(f"FIABILIDAD: {fiabilidad:.1f}%")
print(f"{'='*40}")

if fiabilidad >= 90:
    print("\n✅ EXCELENTE: Excel muy confiable")
elif fiabilidad >= 75:
    print("\n✅ BUENO: Excel generalmente confiable")
elif fiabilidad >= 50:
    print("\n⚠️ REGULAR: Necesita correcciones")
else:
    print("\n❌ BAJO: Necesita auditoría completa")

print("\n" + "="*80)
print("SIGUIENTE PASOS")
print("="*80)

if cuentas_con_problemas > 0:
    print("\n1. CORREGIR problemas detectados (ver arriba)")
    print("2. AGREGAR saldos iniciales faltantes")
    print("3. VALIDAR con extractos bancarios")
else:
    print("\n✅ No se detectaron problemas significativos")

if cuentas_con_multiples_nombres:
    print(f"\n4. OPCIONAL: Normalizar {len(cuentas_con_multiples_nombres)} cuentas a un solo nombre")
    print("   (Mejora legibilidad, pero el sistema de alias ya funciona)")

print("\n" + "="*80)
