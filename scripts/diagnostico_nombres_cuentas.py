#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DIAGNÓSTICO: Nombres de cuentas inconsistentes
Identifica variaciones del mismo nombre y consolida saldos
"""
import openpyxl
from datetime import datetime
from collections import defaultdict
import re

EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"

print("="*80)
print("DIAGNOSTICO: NOMBRES DE CUENTAS INCONSISTENTES")
print("="*80)

# Cargar Excel
wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
ws_trans = wb['TRANSACCIONES']

# Leer todos los nombres de cuenta únicos en TRANSACCIONES
print("\nLeyendo nombres de cuenta en TRANSACCIONES (columna E)...")

nombres_cuenta_unicos = set()
movimientos_por_nombre = defaultdict(list)

for row in range(2, ws_trans.max_row + 1):
    cuenta = ws_trans[f'E{row}'].value

    if cuenta and str(cuenta).strip() and cuenta != 'Cuenta Bancaria':
        nombre_limpio = str(cuenta).strip()
        nombres_cuenta_unicos.add(nombre_limpio)

        # Guardar movimiento
        fecha = ws_trans[f'A{row}'].value
        monto_usd = ws_trans[f'I{row}'].value
        monto_crc = ws_trans[f'J{row}'].value
        tipo_mov = ws_trans[f'K{row}'].value

        movimientos_por_nombre[nombre_limpio].append({
            'fila': row,
            'fecha': fecha,
            'monto_usd': monto_usd,
            'monto_crc': monto_crc,
            'tipo_mov': tipo_mov
        })

print(f"✓ Encontrados {len(nombres_cuenta_unicos)} nombres únicos de cuenta")

# Leer hoja Efectivo
print("\nLeyendo hoja Efectivo...")

try:
    ws_efectivo = wb['Efectivo']

    balances_efectivo = {}

    # Buscar balances (probablemente en las primeras 20 filas)
    for row in range(1, 30):
        concepto = ws_efectivo[f'B{row}'].value
        cuenta = ws_efectivo[f'C{row}'].value
        balance = ws_efectivo[f'F{row}'].value
        fecha = ws_efectivo[f'A{row}'].value

        if concepto and 'Balance inicial' in str(concepto) and cuenta and balance:
            try:
                balances_efectivo[str(cuenta).strip()] = {
                    'balance': float(balance),
                    'fecha': fecha,
                    'concepto': concepto
                }
            except:
                pass

    print(f"✓ Encontrados {len(balances_efectivo)} balances en hoja Efectivo")

    print("\nBalances en hoja Efectivo:")
    for cuenta, data in balances_efectivo.items():
        print(f"  - {cuenta}: ${data['balance']:,.2f}")

except Exception as e:
    print(f"⚠️ Error al leer hoja Efectivo: {e}")
    balances_efectivo = {}

# Función para normalizar nombre de cuenta (quitar paréntesis, guiones, etc)
def normalizar_cuenta(nombre):
    """Extrae el identificador principal de la cuenta"""
    nombre = str(nombre).upper().strip()

    # Patrones comunes
    if 'PROMERICA USD' in nombre:
        if '1774' in nombre or '3881774' in nombre:
            return 'PROMERICA_USD_1774'
        else:
            return 'PROMERICA_USD_OTRO'

    if 'PROMERICA CRC' in nombre:
        return 'PROMERICA_CRC_1708'

    if 'BNCR USD' in nombre or 'USD BNCR' in nombre:
        if '601066' in nombre:
            return 'BNCR_USD_601066'
        elif '11121' in nombre or '1112-1' in nombre:
            return 'BNCR_USD_11121'
        else:
            return 'BNCR_USD_OTRO'

    if 'BNCR CRC' in nombre or 'CRC BNCR' in nombre:
        if '188618' in nombre:
            return 'BNCR_CRC_188618'
        else:
            return 'BNCR_CRC_OTRO'

    if 'AHORRO' in nombre:
        if '1002273441' in nombre:
            return 'AHORRO_IMPUESTOS'
        elif '1002335826' in nombre:
            return 'AHORRO_MATRIMONIO'
        elif '1002388223' in nombre:
            return 'AHORRO_BLACK_FRIDAY'
        elif '17000002201' in nombre:
            return 'AHORRO_VEHICULO'

    if 'TC BNCR' in nombre or 'TARJETA BNCR' in nombre:
        if '3519' in nombre:
            return 'TC_BNCR_VISA_3519'
        elif '8759' in nombre:
            return 'TC_BNCR_MC_8759'
        elif '9837' in nombre:
            return 'TC_BNCR_VISA_9837'
        elif '6386' in nombre:
            return 'TC_BNCR_6386'

    if 'TC BAC' in nombre or 'BAC TC' in nombre:
        return 'TC_BAC'

    if 'PASIVOS' in nombre:
        return 'PASIVOS'

    if 'POR COBRAR' in nombre or 'COBRAR' in nombre:
        return 'POR_COBRAR'

    if 'POR PAGAR' in nombre or 'PAGAR' in nombre:
        return 'POR_PAGAR'

    # Si no coincide con ningún patrón, devolver limpio
    return nombre.replace(' ', '_').replace('(', '').replace(')', '')

# Agrupar por cuenta normalizada
print("\n" + "="*80)
print("AGRUPACION POR CUENTA REAL (NORMALIZADA)")
print("="*80)

cuentas_consolidadas = defaultdict(lambda: {
    'nombres_variantes': set(),
    'movimientos': [],
    'saldo_usd': 0,
    'saldo_crc': 0
})

for nombre_original, movs in movimientos_por_nombre.items():
    cuenta_norm = normalizar_cuenta(nombre_original)

    cuentas_consolidadas[cuenta_norm]['nombres_variantes'].add(nombre_original)
    cuentas_consolidadas[cuenta_norm]['movimientos'].extend(movs)

    # Calcular saldo
    for mov in movs:
        try:
            if mov['monto_usd']:
                monto = float(mov['monto_usd'])
                if mov['tipo_mov'] and 'Egreso' in str(mov['tipo_mov']):
                    monto = -abs(monto)
                cuentas_consolidadas[cuenta_norm]['saldo_usd'] += monto

            if mov['monto_crc']:
                monto = float(mov['monto_crc'])
                if mov['tipo_mov'] and 'Egreso' in str(mov['tipo_mov']):
                    monto = -abs(monto)
                cuentas_consolidadas[cuenta_norm]['saldo_crc'] += monto
        except:
            pass

# Mostrar consolidado
print("\nCUENTAS CONSOLIDADAS:")

for cuenta_norm in sorted(cuentas_consolidadas.keys()):
    data = cuentas_consolidadas[cuenta_norm]

    print(f"\n{'='*80}")
    print(f"📊 {cuenta_norm}")
    print(f"{'='*80}")

    # Mostrar variantes de nombre
    if len(data['nombres_variantes']) > 1:
        print(f"⚠️ TIENE {len(data['nombres_variantes'])} NOMBRES DIFERENTES:")
        for nombre in sorted(data['nombres_variantes']):
            num_movs = len(movimientos_por_nombre[nombre])
            print(f"   - '{nombre}' ({num_movs} movimientos)")
        print(f"   ⚠️ ESTOS NOMBRES DEBERÍAN SER UNO SOLO")
    else:
        nombre_unico = list(data['nombres_variantes'])[0]
        print(f"✓ Nombre único: '{nombre_unico}'")

    # Mostrar saldo
    print(f"\nSaldo calculado (TRANSACCIONES):")
    if data['saldo_usd'] != 0:
        print(f"   USD: ${data['saldo_usd']:,.2f}")
    if data['saldo_crc'] != 0:
        print(f"   CRC: ₡{data['saldo_crc']:,.2f}")

    print(f"Total movimientos: {len(data['movimientos'])}")

    # Buscar balance en Efectivo
    balance_encontrado = None
    nombre_balance = None

    for nombre_ef, data_ef in balances_efectivo.items():
        cuenta_ef_norm = normalizar_cuenta(nombre_ef)
        if cuenta_ef_norm == cuenta_norm:
            balance_encontrado = data_ef['balance']
            nombre_balance = nombre_ef
            break

    if balance_encontrado is not None:
        print(f"\nBalance en hoja Efectivo: ${balance_encontrado:,.2f}")
        print(f"   (bajo nombre: '{nombre_balance}')")

        diferencia = data['saldo_usd'] - balance_encontrado

        if abs(diferencia) > 0.01:
            print(f"\n⚠️ DIFERENCIA: ${diferencia:,.2f}")

            if data['saldo_usd'] < 0 and balance_encontrado > 0:
                print(f"   💡 CAUSA: Probablemente falta saldo inicial en TRANSACCIONES")
                saldo_inicial_necesario = balance_encontrado - data['saldo_usd']
                print(f"   💡 SOLUCION: Agregar saldo inicial de ~${saldo_inicial_necesario:,.2f}")
            elif abs(diferencia) < abs(balance_encontrado) * 0.1:
                print(f"   💡 CAUSA: Movimientos faltantes o comisiones (~{abs(diferencia/balance_encontrado)*100:.1f}%)")
            else:
                print(f"   💡 CAUSA: Discrepancia significativa - revisar extractos")
        else:
            print(f"\n✅ COINCIDE con hoja Efectivo")
    else:
        print(f"\n⚠️ NO encontrado en hoja Efectivo")

# Resumen de problemas
print("\n" + "="*80)
print("RESUMEN DE PROBLEMAS DETECTADOS")
print("="*80)

problemas_nombres = []
problemas_saldo = []

for cuenta_norm, data in cuentas_consolidadas.items():
    if len(data['nombres_variantes']) > 1:
        problemas_nombres.append({
            'cuenta': cuenta_norm,
            'variantes': data['nombres_variantes']
        })

    # Buscar diferencias de saldo
    for nombre_ef, data_ef in balances_efectivo.items():
        if normalizar_cuenta(nombre_ef) == cuenta_norm:
            diferencia = data['saldo_usd'] - data_ef['balance']
            if abs(diferencia) > 0.01:
                problemas_saldo.append({
                    'cuenta': cuenta_norm,
                    'saldo_trans': data['saldo_usd'],
                    'saldo_efectivo': data_ef['balance'],
                    'diferencia': diferencia
                })

print(f"\n1. NOMBRES INCONSISTENTES: {len(problemas_nombres)} cuentas")
for prob in problemas_nombres:
    print(f"\n   {prob['cuenta']}:")
    for var in sorted(prob['variantes']):
        print(f"      - {var}")

print(f"\n2. DIFERENCIAS DE SALDO: {len(problemas_saldo)} cuentas")
for prob in problemas_saldo:
    print(f"\n   {prob['cuenta']}:")
    print(f"      Trans: ${prob['saldo_trans']:,.2f}")
    print(f"      Efectivo: ${prob['saldo_efectivo']:,.2f}")
    print(f"      Diferencia: ${prob['diferencia']:,.2f}")

# Fiabilidad recalculada
print("\n" + "="*80)
print("FIABILIDAD RECALCULADA")
print("="*80)

total_cuentas_reales = len(cuentas_consolidadas)
cuentas_con_problemas = len(set([p['cuenta'] for p in problemas_nombres] + [p['cuenta'] for p in problemas_saldo]))
cuentas_ok = total_cuentas_reales - cuentas_con_problemas

if total_cuentas_reales > 0:
    fiabilidad = (cuentas_ok / total_cuentas_reales) * 100
else:
    fiabilidad = 0

print(f"\nCuentas reales (consolidadas): {total_cuentas_reales}")
print(f"Cuentas OK: {cuentas_ok}")
print(f"Cuentas con problemas: {cuentas_con_problemas}")
print(f"\n{'='*40}")
print(f"FIABILIDAD: {fiabilidad:.1f}%")
print(f"{'='*40}")

print("\n" + "="*80)
print("RECOMENDACIONES")
print("="*80)

print("""
1. NORMALIZAR NOMBRES DE CUENTA:
   - Elegir UN nombre estándar para cada cuenta
   - Reemplazar todas las variantes por ese nombre
   - Ejemplo: "Promerica USD 1774" como estándar

2. PRIORIDAD ALTA:
   - Promerica USD tiene 3 nombres diferentes
   - BNCR USD tiene múltiples variantes
   - Tarjetas BNCR duplicadas (TC vs Tarjeta)

3. DESPUÉS de normalizar:
   - Ejecutar auditoría nuevamente
   - Los saldos se consolidarán correctamente
   - Fiabilidad subirá significativamente
""")

print("\n" + "="*80)
