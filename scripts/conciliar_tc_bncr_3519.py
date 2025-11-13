#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de Tarjeta BNCR Visa 3519
Período: 22/10/2025 al 10/11/2025
Saldo actual: ₡578,648.64 + $51.22
Fecha corte: 21/10/2025
Fecha límite pago: 06/11/2025
"""

# Movimientos del extracto de tarjeta BNCR Visa 3519
movimientos = [
    # OCTUBRE
    {"ref": "123612", "fecha": "22/10/2025", "tipo": "COMPRAS", "establecimiento": "AMAZON MKTPL*NM1IV3YQ2", "monto": 38.51, "moneda": "USD"},
    {"ref": "376751", "fecha": "22/10/2025", "tipo": "COMPRAS", "establecimiento": "PAYPAL *UBER BV", "monto": 6.49, "moneda": "USD"},
    {"ref": "376751", "fecha": "22/10/2025", "tipo": "COMPRAS", "establecimiento": "IVA PAYPAL *UBER BV", "monto": 0.84, "moneda": "USD"},

    {"ref": "8006745", "fecha": "25/10/2025", "tipo": "PAGOS", "establecimiento": "DB CTA 100010001886183", "monto": -10000.00, "moneda": "CRC"},
    {"ref": "635394", "fecha": "25/10/2025", "tipo": "COMPRAS", "establecimiento": "MULTIMERCADO AM PM S.FRAN", "monto": 3200.00, "moneda": "CRC"},
    {"ref": "670264", "fecha": "25/10/2025", "tipo": "COMPRAS", "establecimiento": "MINI SUPER SAN AGUSTIN", "monto": 600.00, "moneda": "CRC"},
    {"ref": "659870", "fecha": "25/10/2025", "tipo": "COMPRAS", "establecimiento": "ABASTECEDOR LA ESQUINA ID", "monto": 2400.00, "moneda": "CRC"},
    {"ref": "8007032", "fecha": "25/10/2025", "tipo": "PAGOS", "establecimiento": "DB CTA 100020876010664", "monto": -200.00, "moneda": "USD"},

    {"ref": "615169", "fecha": "27/10/2025", "tipo": "COMPRAS", "establecimiento": "AMAZON MKTPL*N45AT86V1", "monto": 89.71, "moneda": "USD"},

    {"ref": "5137123", "fecha": "30/10/2025", "tipo": "PAGOS", "establecimiento": "DB CTA 200020870111121", "monto": -100000.00, "moneda": "CRC"},
    {"ref": "119128", "fecha": "30/10/2025", "tipo": "DEVOLUCION", "establecimiento": "AUTO MERCADO ON LINE", "monto": -3350.00, "moneda": "CRC"},
    {"ref": "117336", "fecha": "30/10/2025", "tipo": "COMPRAS", "establecimiento": "AUTO MERCADO ON LINE", "monto": 50.00, "moneda": "CRC"},
    {"ref": "117529", "fecha": "30/10/2025", "tipo": "COMPRAS", "establecimiento": "AUTO MERCADO ON LINE", "monto": 122605.00, "moneda": "CRC"},
    {"ref": "115950", "fecha": "30/10/2025", "tipo": "COMPRAS", "establecimiento": "AUTO MERCADO ON LINE", "monto": 54010.00, "moneda": "CRC"},
    {"ref": "197982", "fecha": "30/10/2025", "tipo": "COMPRAS", "establecimiento": "TIENDA PRONTO BARREAL", "monto": 6550.00, "moneda": "CRC"},
    {"ref": "5135145", "fecha": "30/10/2025", "tipo": "PAGOS", "establecimiento": "DB CTA 200020870111121", "monto": -139.72, "moneda": "USD"},

    # NOVIEMBRE
    {"ref": "367716", "fecha": "01/11/2025", "tipo": "COMPRAS", "establecimiento": "COMUNIDAD PAS (RECAUDACIO", "monto": 5700.00, "moneda": "CRC"},
    {"ref": "388577", "fecha": "01/11/2025", "tipo": "COMPRAS", "establecimiento": "LA FRIKITONA", "monto": 22800.00, "moneda": "CRC"},
    {"ref": "392646", "fecha": "01/11/2025", "tipo": "COMPRAS", "establecimiento": "LA FRIKITONA", "monto": 3750.00, "moneda": "CRC"},

    {"ref": "454169", "fecha": "02/11/2025", "tipo": "COMPRAS", "establecimiento": "PAYPAL *UBERBV EATS", "monto": 26.60, "moneda": "USD"},
    {"ref": "454169", "fecha": "02/11/2025", "tipo": "COMPRAS", "establecimiento": "IVA PAYPAL *UBERBV EATS", "monto": 3.46, "moneda": "USD"},

    {"ref": "492231", "fecha": "03/11/2025", "tipo": "COMPRAS", "establecimiento": "AUTO MERCADO ON LINE", "monto": 6774.35, "moneda": "CRC"},

    {"ref": "742570", "fecha": "05/11/2025", "tipo": "COMPRAS", "establecimiento": "PAYPAL *UBERBV EATS", "monto": 18.73, "moneda": "USD"},
    {"ref": "742570", "fecha": "05/11/2025", "tipo": "COMPRAS", "establecimiento": "IVA PAYPAL *UBERBV EATS", "monto": 2.43, "moneda": "USD"},
]

print("="*80)
print("CONCILIACIÓN: TARJETA BNCR VISA 3519")
print("="*80)
print(f"\nTitular: ALVARO VELASCO JIMENEZ")
print(f"Tarjeta: 4641-37XX-XXXX-3519")
print(f"Límite de crédito: $1,200.00")
print(f"Fecha de corte: 21/10/2025")
print(f"Fecha límite de pago: 06/11/2025")
print(f"\nSaldo actual: ₡578,648.64 + $51.22")
print(f"Total movimientos: {len(movimientos)}")

# Calcular totales
compras_crc = sum([m['monto'] for m in movimientos if m['moneda'] == 'CRC' and m['tipo'] == 'COMPRAS'])
compras_usd = sum([m['monto'] for m in movimientos if m['moneda'] == 'USD' and m['tipo'] == 'COMPRAS'])
pagos_crc = sum([abs(m['monto']) for m in movimientos if m['moneda'] == 'CRC' and m['tipo'] == 'PAGOS'])
pagos_usd = sum([abs(m['monto']) for m in movimientos if m['moneda'] == 'USD' and m['tipo'] == 'PAGOS'])
devoluciones_crc = sum([abs(m['monto']) for m in movimientos if m['moneda'] == 'CRC' and m['tipo'] == 'DEVOLUCION'])

print(f"\nCompras: ₡{compras_crc:,.2f} + ${compras_usd:.2f}")
print(f"Pagos: ₡{pagos_crc:,.2f} + ${pagos_usd:.2f}")
print(f"Devoluciones: ₡{devoluciones_crc:,.2f}")

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
    'Uber/Uber Eats': [],
    'Amazon': [],
    'Auto Mercado': [],
    'Supermercados/Mini super': [],
    'Restaurantes': [],
    'Comunidad/PAS': [],
    'Pagos realizados': [],
    'Devoluciones': [],
    'Otros': []
}

for mov in movimientos:
    establecimiento = mov['establecimiento'].upper()
    if 'UBER' in establecimiento:
        categorias['Uber/Uber Eats'].append(mov)
    elif 'AMAZON' in establecimiento:
        categorias['Amazon'].append(mov)
    elif 'AUTO MERCADO' in establecimiento:
        categorias['Auto Mercado'].append(mov)
    elif 'AM PM' in establecimiento or 'MINI SUPER' in establecimiento or 'ABASTECEDOR' in establecimiento:
        categorias['Supermercados/Mini super'].append(mov)
    elif 'FRIKITONA' in establecimiento or 'PRONTO' in establecimiento:
        categorias['Restaurantes'].append(mov)
    elif 'COMUNIDAD' in establecimiento or 'PAS' in establecimiento:
        categorias['Comunidad/PAS'].append(mov)
    elif mov['tipo'] == 'PAGOS':
        categorias['Pagos realizados'].append(mov)
    elif mov['tipo'] == 'DEVOLUCION':
        categorias['Devoluciones'].append(mov)
    else:
        categorias['Otros'].append(mov)

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
Ya registrados anteriormente:
- 10/11: Uber/PayPal $2.21 (Ref 531413364318) ✅
- 10/11: Uber/PayPal $2.76 (Ref 531413060364) ✅
- 08/11: POPS ₡6,000 (Ref 531217089077) ✅
- 08/11: AM PM ₡5,510 (Ref 531213101326) ✅

Nuevos del extracto de tarjeta que probablemente NO están:
- 05/11: Uber Eats $18.73 + IVA $2.43 = $21.16 total
- 03/11: Auto Mercado ₡6,774.35
- 02/11: Uber Eats $26.60 + IVA $3.46 = $30.06 total
- 01/11: Comunidad PAS ₡5,700
- 01/11: La Frikitona ₡22,800
- 01/11: La Frikitona ₡3,750
- 30/10: Pago tarjeta $139.72 (desde cuenta 200020870111121)
- 30/10: Pago tarjeta ₡100,000 (desde cuenta 200020870111121)
- 30/10: Tienda Pronto ₡6,550
- 30/10: Auto Mercado ₡54,010
- 30/10: Auto Mercado ₡122,605
- 30/10: Auto Mercado ₡50
- 30/10: Devolución Auto Mercado -₡3,350
- 27/10: Amazon $89.71
- 25/10: Pago ₡10,000 (desde CRC 188618) ✅ Ya visto
- 25/10: Pago $200 (desde USD 601066)
- 25/10: AM PM ₡3,200
- 25/10: Mini Super ₡600
- 25/10: Abastecedor ₡2,400
- 22/10: Amazon $38.51
- 22/10: Uber $6.49 + IVA $0.84 = $7.33 total

TOTAL A REVISAR: ~25 transacciones
""")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. 💳 PAGOS REALIZADOS A LA TARJETA:
   - 25/10: $200.00 desde cuenta BNCR USD 601066
   - 25/10: ₡10,000 desde cuenta BNCR CRC 188618
   - 30/10: $139.72 desde cuenta 200020870111121 (¿cuál es esta?)
   - 30/10: ₡100,000 desde cuenta 200020870111121

2. 🛒 AUTO MERCADO - COMPRAS GRANDES 30/10:
   - ₡122,605 (compra grande)
   - ₡54,010
   - ₡50
   - Devolución: -₡3,350
   - Total neto: ₡173,315

3. 🍔 LA FRIKITONA - 01/11:
   - ₡22,800 (comida grande)
   - ₡3,750
   - Total: ₡26,550

4. 📦 AMAZON - DOS COMPRAS:
   - 22/10: $38.51
   - 27/10: $89.71
   - Total: $128.22

5. 🚗 UBER/UBER EATS - VARIOS DÍAS:
   - 22/10: $7.33 (transporte)
   - 02/11: $30.06 (comida)
   - 05/11: $21.16 (comida)
   - Total: $58.55

6. 🏘️ COMUNIDAD PAS - 01/11:
   - ₡5,700
   - ¿Cuota de mantenimiento comunidad?

7. ❓ CUENTA 200020870111121:
   - Hizo pagos a la tarjeta desde esta cuenta
   - ¿Qué cuenta es? ¿Promerica? ¿Otra?
""")
