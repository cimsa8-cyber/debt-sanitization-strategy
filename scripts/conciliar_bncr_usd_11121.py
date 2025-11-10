#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de cuenta BNCR USD 200-02-087-011112-1 (Personal Álvaro)
Período: 27/10/2025 al 10/11/2025
Saldo disponible: $21.84
Total salidas: $593.98
Total entradas: $609.66
"""

# Movimientos del extracto bancario BNCR USD Personal
movimientos_banco = [
    # 30/10/2025
    {"fecha": "30/10/2025", "comprobante": "15133894", "salida": 0, "entrada": 500.00, "descripcion": "SALARIO 2DA QUINCENA OCTUBRE/ALVARO VELASCO J.", "tipo": "Ingreso - Salario"},
    {"fecha": "30/10/2025", "comprobante": "15135145", "salida": 139.72, "entrada": 0, "descripcion": "PAGO VISA 4641-37XX-XXXX-3519/ALVARO VELASCO J.", "tipo": "Pago Tarjeta Visa 3519"},
    {"fecha": "30/10/2025", "comprobante": "15137123", "salida": 202.84, "entrada": 0, "descripcion": "PAGO VISA 4641-37XX-XXXX-3519/ALVARO VELASCO J.", "tipo": "Pago Tarjeta Visa 3519"},
    {"fecha": "30/10/2025", "comprobante": "15151419", "salida": 0, "entrada": 109.66, "descripcion": "REINTEGRO COMPRAS OFICINA AUTOMERCADO/ALVARO VELASCO J.", "tipo": "Reintegro - Auto Mercado"},
    {"fecha": "30/10/2025", "comprobante": "96755715", "salida": 100.00, "entrada": 0, "descripcion": "CAMBIO DE MONEDA/ALVARO VELASCO JIMEN", "tipo": "Cambio de moneda"},

    # 31/10/2025
    {"fecha": "31/10/2025", "comprobante": "17250058", "salida": 101.42, "entrada": 0, "descripcion": "FERIA 31 DE OCTUBRE 2025/JOSE ALEJANDRO ALFAR", "tipo": "Gasto - Feria"},

    # 03/11/2025
    {"fecha": "03/11/2025", "comprobante": "90535048", "salida": 50.00, "entrada": 0, "descripcion": "CENA PAS/ALVARO VELASCO JIMEN", "tipo": "Gasto - Cena"},
]

print("="*80)
print("CONCILIACIÓN: CUENTA BNCR USD 200-02-087-011112-1 (Personal)")
print("="*80)
print(f"\nTitular: ALVARO VELASCO JIMENEZ")
print(f"Cuenta: 200-02-087-011112-1 (CR16015108720020111121)")
print(f"Moneda: USD")
print(f"Período: 27/10/2025 al 10/11/2025")
print(f"\nSaldo disponible: $21.84")
print(f"Total salidas: ${sum([m['salida'] for m in movimientos_banco]):.2f}")
print(f"Total entradas: ${sum([m['entrada'] for m in movimientos_banco]):.2f}")
print(f"Movimiento neto: ${sum([m['entrada'] - m['salida'] for m in movimientos_banco]):.2f}")
print(f"Total movimientos: {len(movimientos_banco)}")

print("\n" + "="*80)
print("RESUMEN DE MOVIMIENTOS POR FECHA")
print("="*80)

# Agrupar por fecha
from collections import defaultdict
por_fecha = defaultdict(list)
for mov in movimientos_banco:
    por_fecha[mov['fecha']].append(mov)

for fecha in sorted(por_fecha.keys(), reverse=True):
    movs = por_fecha[fecha]
    total_salidas = sum([m['salida'] for m in movs])
    total_entradas = sum([m['entrada'] for m in movs])
    print(f"\n📅 {fecha} - Salidas: ${total_salidas:.2f} | Entradas: ${total_entradas:.2f}")
    print("-" * 80)
    for mov in movs:
        if mov['salida'] > 0:
            print(f"  ❌ {mov['comprobante']:12} | ${mov['salida']:>8.2f} | {mov['tipo']}")
        else:
            print(f"  ✅ {mov['comprobante']:12} | ${mov['entrada']:>8.2f} | {mov['tipo']}")

print("\n" + "="*80)
print("MOVIMIENTOS AGRUPADOS POR TIPO")
print("="*80)

por_tipo = defaultdict(list)
for mov in movimientos_banco:
    por_tipo[mov['tipo']].append(mov)

for tipo in sorted(por_tipo.keys()):
    movs = por_tipo[tipo]
    total_salidas = sum([m['salida'] for m in movs])
    total_entradas = sum([m['entrada'] for m in movs])
    count = len(movs)
    if total_salidas > 0:
        print(f"\n❌ {tipo}: {count} mov - Salidas: ${total_salidas:.2f}")
    else:
        print(f"\n✅ {tipo}: {count} mov - Entradas: ${total_entradas:.2f}")
    for mov in movs:
        if mov['salida'] > 0:
            print(f"  {mov['fecha']} | {mov['comprobante']:12} | ${mov['salida']:>8.2f}")
        else:
            print(f"  {mov['fecha']} | {mov['comprobante']:12} | ${mov['entrada']:>8.2f}")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. 💰 INGRESO DE SALARIO (30/10):
   - Monto: $500.00
   - Concepto: Salario 2da quincena octubre
   - Fecha: 30/10/2025

2. 💳 PAGOS A TARJETA VISA 3519 (30/10):
   ✅ RESUELVE EL MISTERIO:
   - Pago 1: $139.72 (comprobante 15135145)
   - Pago 2: $202.84 (comprobante 15137123)
   - Total: $342.56

   Pero extracto tarjeta 3519 muestra:
   - Pago USD: $139.72 ✓ (coincide)
   - Pago CRC: ₡100,000

   ⚠️ DISCREPANCIA:
   - Pago 2 ($202.84) no aparece en extracto tarjeta 3519
   - ¿O el pago de $202.84 USD equivale a ₡100,000 CRC?
   - Tasa cambio: ₡100,000 / $202.84 = ₡493.00 x USD (razonable)

3. 🏢 REINTEGRO AUTO MERCADO (30/10):
   - Monto: $109.66
   - Concepto: Compras oficina
   - ¿Es reembolso de gastos de empresa?

4. 💱 CAMBIO DE MONEDA (30/10):
   - Monto: $100.00
   - ¿Convirtió USD a CRC?
   - ¿A dónde fueron esos dólares?

5. 🎉 GASTO FERIA (31/10):
   - Monto: $101.42
   - Fecha: Halloween (31 octubre)
   - Beneficiario: José Alejandro Alfaro

6. 🍽️ CENA PAS (03/11):
   - Monto: $50.00
   - ¿Cena comunidad/PAS?

7. 📊 FLUJO DE CAJA:
   - Ingreso: $500.00 (salario)
   - Salidas: $593.98
   - Entradas adicionales: $109.66 (reintegro)
   - Neto: +$15.68
   - Saldo final: $21.84
   - Saldo inicial estimado: $6.16
""")

print("\n" + "="*80)
print("ANÁLISIS: ¿QUÉ FALTA REGISTRAR EN EL EXCEL?")
print("="*80)

print("""
Movimientos que probablemente NO están en el Excel:

30/10/2025:
- Ingreso salario $500.00 (2da quincena octubre)
- Pago TC Visa 3519 $139.72
- Pago TC Visa 3519 $202.84 (o ₡100,000 convertidos)
- Reintegro Auto Mercado $109.66
- Cambio de moneda $100.00

31/10/2025:
- Feria Halloween $101.42 (José Alejandro)

03/11/2025:
- Cena PAS $50.00

TOTAL A REVISAR: 7 transacciones

NOTA: Esta cuenta es la PERSONAL de Álvaro (salario, gastos personales)
La otra cuenta USD (601066) parece ser EMPRESARIAL (proveedores, facturas)
""")

print("\n" + "="*80)
print("CONEXIÓN CON OTRAS CUENTAS")
print("="*80)

print("""
✅ PAGOS A TARJETA 3519 AHORA CUADRAN:

   Extracto Tarjeta 3519 (30/10):
   - Pago USD: $139.72 desde "DB CTA 200020870111121"
   - Pago CRC: ₡100,000 desde "DB CTA 200020870111121"

   Extracto Cuenta 11121 (30/10):
   - Pago: $139.72 (comprobante 15135145) ✓
   - Pago: $202.84 (comprobante 15137123) → ₡100,000 ✓

   Total pagado: $342.56 USD

   ✅ TODO CUADRA - Era la misma cuenta (11121)
""")
