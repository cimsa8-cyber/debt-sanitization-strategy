#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de Tarjeta BNCR Visa 9837
Período: 22/10/2025 al 02/11/2025
Saldo actual: ₡2,030,004.01 + $1,775.45
Fecha corte: 17/10/2025
Fecha límite pago: 03/11/2025
"""

# Movimientos del extracto de tarjeta BNCR Visa 9837
movimientos = [
    # OCTUBRE
    {"ref": "174348", "fecha": "22/10/2025", "tipo": "COMPRAS", "establecimiento": "PAYPAL *CLEVERBRIDG", "monto": 275.00, "moneda": "USD"},

    # NOVIEMBRE
    {"ref": "0", "fecha": "02/11/2025", "tipo": "PAGOS", "establecimiento": "PAGO DEBITO AUTOMATICO", "monto": -62.00, "moneda": "USD"},
    {"ref": "0", "fecha": "02/11/2025", "tipo": "PAGOS", "establecimiento": "PAGO DEBITO AUTOMATICO", "monto": -271600.00, "moneda": "CRC"},
]

print("="*80)
print("CONCILIACIÓN: TARJETA BNCR VISA 9837")
print("="*80)
print(f"\nTitular: ALVARO VELASCO JIMENEZ")
print(f"Tarjeta: 4831-26XX-XXXX-9837")
print(f"Límite de crédito: $9,000.00")
print(f"Fecha de corte: 17/10/2025")
print(f"Fecha límite de pago: 03/11/2025")
print(f"\nSaldo actual: ₡2,030,004.01 + $1,775.45")
print(f"Saldo disponible: ₡406,470.71 + $797.00")
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
print("ANÁLISIS")
print("="*80)

print("""
Movimientos:
1. 22/10: Compra PayPal Cleverbridg $275.00 (software)
2. 02/11: Pago débito automático $62.00
3. 02/11: Pago débito automático ₡271,600.00
""")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. 💳 PAGOS DÉBITO AUTOMÁTICO (02/11):
   - Pago USD: $62.00
   - Pago CRC: ₡271,600.00
   - Total: ~$536 USD

2. 💻 COMPRA SOFTWARE (22/10):
   - PayPal Cleverbridg: $275.00
   - Probablemente software o suscripción empresarial

3. 💰 SALDO MUY ALTO:
   - Saldo actual: ₡2,030,004.01 + $1,775.45
   - Límite: $9,000
   - ⚠️ Este saldo parece un CRÉDITO A FAVOR (no deuda)
   - ¿Hubo pagos en exceso o reembolsos grandes?

4. 🔍 CONEXIÓN CON CUENTA BNCR USD 601066:

   Extracto cuenta 601066 (03/11):
   - Pago TC Visa 9837: ₡31,434
   - Pago TC Visa 9837: ₡271,600 ✓

   Extracto tarjeta 9837 (02/11):
   - Pago automático: ₡271,600 ✓
   - Pago automático: $62.00

   ⚠️ DISCREPANCIAS:
   a) Fecha diferente:
      - Tarjeta: 02/11/2025
      - Cuenta: 03/11/2025
      - Probable: procesamiento nocturno

   b) Pago de ₡31,434 NO aparece en extracto tarjeta 9837
      - ¿Fue a otra tarjeta?
      - ¿O es un pago parcial previo?

5. 📊 RESUMEN DE PAGOS:
   - Pago automático CRC: ₡271,600
   - Pago automático USD: $62.00
   - Total: ~$536 USD

   Compra del período: $275.00
   Diferencia: $261.00 (pagó más de lo que gastó)

6. ❓ CUENTA CRC 188618 MUESTRA:
   - 03/11: Pago TC Visa 9837 ₡31,434
   - 03/11: Pago TC Visa 9837 ₡271,600

   Suma: ₡303,034

   ⚠️ PERO tarjeta 9837 solo muestra:
   - 02/11: Pago ₡271,600

   Falta: ₡31,434

   ¿De dónde vino este pago adicional?
""")

print("\n" + "="*80)
print("MOVIMIENTOS A REGISTRAR EN EXCEL")
print("="*80)

print("""
Nuevos movimientos:
- 22/10: PayPal Cleverbridg $275.00 (software empresarial)
- 02/11: Pago débito automático $62.00
- 02/11: Pago débito automático ₡271,600.00

TOTAL: 3 transacciones

NOTA: Esta tarjeta tiene MUY pocos movimientos - principalmente
se usa para compras de software/subscripciones online.
""")

print("\n" + "="*80)
print("PREGUNTAS PENDIENTES")
print("="*80)

print("""
1. Pago de ₡31,434 (03/11)
   - Aparece en extracto cuenta CRC 188618
   - NO aparece en extracto tarjeta 9837
   - ¿A qué tarjeta fue realmente este pago?

2. Saldo alto a favor
   - ¿Por qué esta tarjeta tiene saldo POSITIVO tan alto?
   - ¿Hubo reembolsos o devoluciones grandes?

3. PayPal Cleverbridg $275
   - ¿Qué software/servicio es?
   - ¿Gasto operativo empresarial?
""")
