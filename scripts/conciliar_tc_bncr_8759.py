#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de Tarjeta BNCR Mastercard 8759
Período: 18/10/2025 al 03/11/2025
Saldo actual: ₡2,841,545.17 + $126.48
Fecha corte: 17/10/2025
Fecha límite pago: 03/11/2025
"""

# Movimientos del extracto de tarjeta BNCR MC 8759
movimientos = [
    # OCTUBRE
    {"ref": "845031", "fecha": "18/10/2025", "tipo": "COMPRAS", "establecimiento": "NETFLIX.COM", "monto": 18.98, "moneda": "USD"},
    {"ref": "845031", "fecha": "18/10/2025", "tipo": "COMPRAS", "establecimiento": "IVA NETFLIX.COM", "monto": 2.47, "moneda": "USD"},
    {"ref": "556829", "fecha": "25/10/2025", "tipo": "COMPRAS", "establecimiento": "APPLE.COM/BILL", "monto": 39.99, "moneda": "USD"},

    # NOVIEMBRE
    {"ref": "356611", "fecha": "01/11/2025", "tipo": "COMPRAS", "establecimiento": "ANTHROPIC", "monto": 10.00, "moneda": "USD"},
    {"ref": "0", "fecha": "02/11/2025", "tipo": "PAGOS", "establecimiento": "PAGO DEBITO AUTOMATICO", "monto": -10.00, "moneda": "USD"},
    {"ref": "2961759", "fecha": "03/11/2025", "tipo": "PAGOS", "establecimiento": "DB CTA 100020876010664", "monto": -300000.00, "moneda": "CRC"},
]

print("="*80)
print("CONCILIACIÓN: TARJETA BNCR MASTERCARD 8759")
print("="*80)
print(f"\nTitular: ALVARO VELASCO JIMENEZ")
print(f"Tarjeta: 5290-60XX-XXXX-8759")
print(f"Límite de crédito: $6,000.00")
print(f"Fecha de corte: 17/10/2025")
print(f"Fecha límite de pago: 03/11/2025")
print(f"\nSaldo actual: ₡2,841,545.17 + $126.48")
print(f"Saldo disponible: ₡145,305.38 + $284.91")
print(f"Total movimientos: {len(movimientos)}")

# Calcular totales
compras_usd = sum([m['monto'] for m in movimientos if m['moneda'] == 'USD' and m['tipo'] == 'COMPRAS'])
pagos_crc = sum([abs(m['monto']) for m in movimientos if m['moneda'] == 'CRC' and m['tipo'] == 'PAGOS'])
pagos_usd = sum([abs(m['monto']) for m in movimientos if m['moneda'] == 'USD' and m['tipo'] == 'PAGOS'])

print(f"\nCompras USD: ${compras_usd:.2f}")
print(f"Pagos: ₡{pagos_crc:,.2f} + ${pagos_usd:.2f}")

print("\n" + "="*80)
print("RESUMEN DE MOVIMIENTOS POR FECHA")
print("="*80)

# Agrupar por fecha
from collections import defaultdict
por_fecha = defaultdict(lambda: {'CRC': [], 'USD': []})
for mov in movimientos:
    por_fecha[mov['fecha']][mov['moneda']].append(mov)

for fecha in sorted(por_fecha.keys()):
    movs_crc = por_fecha[fecha]['CRC']
    movs_usd = por_fecha[fecha]['USD']

    print(f"\n📅 {fecha}")
    print("-" * 80)

    if movs_usd:
        total_usd = sum([m['monto'] for m in movs_usd])
        print(f"  USD (Total: ${total_usd:.2f}):")
        for mov in movs_usd:
            signo = "❌" if mov['monto'] > 0 else "✅"
            print(f"    {signo} {mov['tipo']:10} | ${abs(mov['monto']):>8.2f} | {mov['establecimiento']}")

    if movs_crc:
        total_crc = sum([m['monto'] for m in movs_crc])
        print(f"  CRC (Total: ₡{total_crc:,.2f}):")
        for mov in movs_crc:
            signo = "❌" if mov['monto'] > 0 else "✅"
            print(f"    {signo} {mov['tipo']:10} | ₡{abs(mov['monto']):>10,.2f} | {mov['establecimiento']}")

print("\n" + "="*80)
print("ANÁLISIS POR CATEGORÍA")
print("="*80)

# Categorizar movimientos
categorias = {
    'Suscripciones (Netflix, Apple, Anthropic)': [],
    'Pagos realizados': [],
}

for mov in movimientos:
    establecimiento = mov['establecimiento'].upper()
    if mov['tipo'] == 'PAGOS':
        categorias['Pagos realizados'].append(mov)
    else:
        categorias['Suscripciones (Netflix, Apple, Anthropic)'].append(mov)

for cat, movs in categorias.items():
    if not movs:
        continue

    total_crc = sum([m['monto'] for m in movs if m['moneda'] == 'CRC'])
    total_usd = sum([m['monto'] for m in movs if m['moneda'] == 'USD'])

    print(f"\n{cat}: {len(movs)} movimiento(s)")
    if total_crc != 0:
        print(f"  Total CRC: ₡{total_crc:,.2f}")
    if total_usd != 0:
        print(f"  Total USD: ${total_usd:.2f}")

    for mov in movs:
        if mov['moneda'] == 'USD':
            print(f"    {mov['fecha']} | ${mov['monto']:>8.2f} | {mov['establecimiento']}")
        else:
            print(f"    {mov['fecha']} | ₡{mov['monto']:>10,.2f} | {mov['establecimiento']}")

print("\n" + "="*80)
print("MOVIMIENTOS ESPECÍFICOS A VERIFICAR EN EXCEL")
print("="*80)

print("""
Probablemente ya registrados:
- 07/11: Apple.com $16.95 ✅ (ref 531155064589 - visto en comprobantes)

Nuevos del extracto de tarjeta que probablemente NO están:
- 18/10: Netflix $18.98 + IVA $2.47 = $21.45 total
- 25/10: Apple.com $39.99
- 01/11: Anthropic $10.00 (suscripción Claude Pro)
- 02/11: Pago débito automático $10.00 (¿pago mínimo?)
- 03/11: Pago tarjeta ₡300,000 (desde BNCR USD 601066)

TOTAL A REVISAR: 5 transacciones

NOTA: Esta tarjeta tiene pocas transacciones - principalmente suscripciones.
""")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. 💳 PAGO GRANDE EL 03/11:
   - Pago de ₡300,000 desde BNCR USD 601066
   - Ya vimos este movimiento en la conciliación de cuenta USD
   - Referencia: 2961759
   - Fecha: 03/11/2025

2. 🔄 PAGO DÉBITO AUTOMÁTICO:
   - Fecha: 02/11/2025
   - Monto: $10.00
   - ¿Es el pago mínimo automático?
   - ¿De qué cuenta se debita?

3. 📱 ANTHROPIC (Claude Pro):
   - Fecha: 01/11/2025
   - Monto: $10.00
   - Suscripción a Claude Pro (gasto operativo)

4. 🍎 APPLE.COM - DOS CARGOS:
   - 25/10: $39.99 (probablemente iCloud storage o app)
   - 07/11: $16.95 (ya registrado)
   - Total: $56.94

5. 📺 NETFLIX:
   - 18/10: $18.98 + IVA $2.47 = $21.45
   - Suscripción mensual

6. 💰 SALDO ALTO:
   - Saldo actual: ₡2,841,545.17 + $126.48
   - ⚠️ Este saldo es muy alto para una tarjeta de crédito
   - Límite: $6,000
   - Utilización: $126.48 / $6,000 = 2.1% (muy bajo)
   - ¿Hubo pagos grandes previos que redujeron el saldo?

7. 🔍 CUENTA BNCR USD 601066:
   - Ya vimos en conciliación previa:
     - 03/11: Pago TC MC 8759 ₡5,070.00 (pago en colones)
     - 03/11: Pago TC Visa 9837 ₡31,434.00
     - 03/11: Pago TC Visa 9837 ₡271,600.00
   - PERO el extracto de esta tarjeta muestra:
     - 03/11: Pago ₡300,000 (ref 2961759)

   ⚠️ DISCREPANCIA:
   - Extracto tarjeta dice: ₡300,000
   - Extracto cuenta dice: ₡5,070
   - Diferencia: ₡294,930

   ❓ ¿Por qué esta diferencia?
   - ¿El pago de ₡300,000 cubrió varias tarjetas?
   - ¿O hay un error de conciliación?
""")

print("\n" + "="*80)
print("PREGUNTAS PENDIENTES")
print("="*80)

print("""
1. Pago débito automático $10.00 (02/11)
   - ¿De qué cuenta se debita?
   - ¿Es configuración de pago mínimo automático?

2. Discrepancia en pago 03/11:
   - Tarjeta muestra: ₡300,000
   - Cuenta USD muestra: ₡5,070
   - ¿Cómo se explica esta diferencia?

3. Apple.com $39.99 (25/10)
   - ¿Qué compra/suscripción es?
   - ¿Gasto personal u operativo?
""")
