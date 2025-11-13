#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de cuenta BNCR CRC 100-01-000-188618-3
Período: 27/10/2025 al 10/11/2025
Saldo disponible: ₡211.24
Total salidas: ₡500,230.00
Total entradas: ₡480,080.45
"""

# Movimientos del extracto bancario BNCR CRC
movimientos_banco = [
    # 10/11/2025
    {"fecha": "10/11/2025", "comprobante": "91351363", "salida": 12126.00, "entrada": 0, "descripcion": "08-11-25 MC DONALD/JOSE ALEJANDRO ALFARO ARIAS", "tipo": "Gasto - McDonald's"},
    {"fecha": "10/11/2025", "comprobante": "93662715", "salida": 3000.00, "entrada": 0, "descripcion": "PAGOS/ARIAS FALLAS ALEJANDRA", "tipo": "Pago - Alejandra Arias"},

    # 07/11/2025
    {"fecha": "07/11/2025", "comprobante": "54545292", "salida": 10000.00, "entrada": 0, "descripcion": "CASA 10E 70512250/BNCR", "tipo": "Pago - Casa"},
    {"fecha": "07/11/2025", "comprobante": "54261209", "salida": 25000.00, "entrada": 0, "descripcion": "CISCO BECA 83618705/ANDRES VELASCO ARANA", "tipo": "Beca - Andrés Velasco"},
    {"fecha": "07/11/2025", "comprobante": "58419485", "salida": 0, "entrada": 20000.00, "descripcion": "TOMAS/THOMAS DAVIDOVICH EG", "tipo": "Ingreso - Thomas"},
    {"fecha": "07/11/2025", "comprobante": "98652306", "salida": 0, "entrada": 30000.00, "descripcion": "TRANSFERENCIA DOLARES/BN-PAR", "tipo": "Conversión USD→CRC"},

    # 05/11/2025
    {"fecha": "05/11/2025", "comprobante": "96297548", "salida": 70000.00, "entrada": 0, "descripcion": "ADELANTO DE SALARIO/ALVARO VELASCO JIMEN", "tipo": "Adelanto salario"},

    # 03/11/2025
    {"fecha": "03/11/2025", "comprobante": "74750907", "salida": 5070.00, "entrada": 0, "descripcion": "02-11-2025 VISA-NUMERO DE TARJETA 5290-60XX-XXXX-8759/BN-PAR", "tipo": "Pago Tarjeta MC 8759"},
    {"fecha": "03/11/2025", "comprobante": "74750901", "salida": 31434.00, "entrada": 0, "descripcion": "02-11-2025 VISA-NUMERO DE TARJETA 4831-26XX-XXXX-9837/BN-PAR", "tipo": "Pago Tarjeta Visa 9837"},
    {"fecha": "03/11/2025", "comprobante": "74750898", "salida": 271600.00, "entrada": 0, "descripcion": "02-11-2025 VISA-NUMERO DE TARJETA 4831-26XX-XXXX-9837/BN-PAR", "tipo": "Pago Tarjeta Visa 9837"},
    {"fecha": "03/11/2025", "comprobante": "9048950", "salida": 5000.00, "entrada": 0, "descripcion": "MESADA SEMANAL DE ANDRES VELASCO/BN-PAR", "tipo": "Mesada - Andrés"},

    # 31/10/2025
    {"fecha": "31/10/2025", "comprobante": "97756190", "salida": 0, "entrada": 2000.00, "descripcion": "GAS/JOSE ALEJANDRO ALFAR", "tipo": "Ingreso - Gas"},
    {"fecha": "31/10/2025", "comprobante": "54748812", "salida": 36000.00, "entrada": 0, "descripcion": "ALE PAGO 72369832/ROSDEYLI SALOME LOPE", "tipo": "Pago - Rosdeyli"},
    {"fecha": "31/10/2025", "comprobante": "312742", "salida": 0, "entrada": 386080.45, "descripcion": "LIQ. AUT. BNAHORRO 01002061574/BNAHORRO", "tipo": "Liquidación Plan Ahorro"},
    {"fecha": "31/10/2025", "comprobante": "98652306", "salida": 0, "entrada": 30000.00, "descripcion": "TRANSFERENCIA DOLARES/BN-PAR", "tipo": "Conversión USD→CRC"},

    # 27/10/2025
    {"fecha": "27/10/2025", "comprobante": "98894010", "salida": 6000.00, "entrada": 0, "descripcion": "25-10-2025 PELUQUER A ALEJANDRO/ARIAS FALLAS ALEJAND", "tipo": "Gasto - Peluquería Alejandro"},
    {"fecha": "27/10/2025", "comprobante": "98285517", "salida": 5000.00, "entrada": 0, "descripcion": "25-10-2025 BARBA VELASCO 71957235/BNCR", "tipo": "Gasto - Barba Velasco"},
    {"fecha": "27/10/2025", "comprobante": "52749755", "salida": 0, "entrada": 6000.00, "descripcion": "26-10-2025 COMPRA LIBRO HAROLD/GONZALEZ TREJOS HARO", "tipo": "Ingreso - Venta libro Harold"},
    {"fecha": "27/10/2025", "comprobante": "52774760", "salida": 0, "entrada": 6000.00, "descripcion": "25-10-2025 LIBRO/ESTERLIN SALAZAR BAR", "tipo": "Ingreso - Venta libro Esterlin"},
    {"fecha": "27/10/2025", "comprobante": "17838009", "salida": 5000.00, "entrada": 0, "descripcion": "25-10-2025 ALVARO LIBRO 88673640/BNCR", "tipo": "Gasto - Libro Álvaro"},
    {"fecha": "27/10/2025", "comprobante": "18006745", "salida": 10000.00, "entrada": 0, "descripcion": "25-10-2025 PAGO VISA 4641-37XX-XXXX-3519/ALVARO VELASCO J.", "tipo": "Pago Tarjeta Visa 3519"},
    {"fecha": "27/10/2025", "comprobante": "9048950", "salida": 5000.00, "entrada": 0, "descripcion": "MESADA SEMANAL DE ANDRES VELASCO/BN-PAR", "tipo": "Mesada - Andrés"},
]

print("="*80)
print("CONCILIACIÓN: CUENTA BNCR CRC 100-01-000-188618-3")
print("Período: 27/10/2025 al 10/11/2025")
print("="*80)
print(f"\nSaldo disponible según banco: ₡211.24")
print(f"Total salidas del período: ₡{sum([m['salida'] for m in movimientos_banco]):,.2f}")
print(f"Total entradas del período: ₡{sum([m['entrada'] for m in movimientos_banco]):,.2f}")
print(f"Saldo neto: ₡{sum([m['entrada'] - m['salida'] for m in movimientos_banco]):,.2f}")
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
    print(f"\n📅 {fecha} - Salidas: ₡{total_salidas:,.2f} | Entradas: ₡{total_entradas:,.2f}")
    print("-" * 80)
    for mov in movs:
        if mov['salida'] > 0:
            print(f"  ❌ {mov['comprobante']:12} | ₡{mov['salida']:>10,.2f} | {mov['tipo']}")
        else:
            print(f"  ✅ {mov['comprobante']:12} | ₡{mov['entrada']:>10,.2f} | {mov['tipo']}")

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
        print(f"\n❌ {tipo}: {count} mov - Salidas: ₡{total_salidas:,.2f}")
    else:
        print(f"\n✅ {tipo}: {count} mov - Entradas: ₡{total_entradas:,.2f}")
    for mov in movs:
        if mov['salida'] > 0:
            print(f"  {mov['fecha']} | {mov['comprobante']:12} | ₡{mov['salida']:>10,.2f}")
        else:
            print(f"  {mov['fecha']} | {mov['comprobante']:12} | ₡{mov['entrada']:>10,.2f}")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. ⚠️ CONVERSIÓN USD→CRC DUPLICADA:
   - 31/10/2025: ₡30,000 (comprobante 98652306)
   - 07/11/2025: ₡30,000 (comprobante 98652306 - MISMO!)

   🔍 ¿Son dos conversiones diferentes con el mismo número?

2. 💰 LIQUIDACIÓN PLAN AHORRO (31/10):
   - Monto: ₡386,080.45
   - Plan: 01002061574
   - ¿Qué plan de ahorro liquidó?

3. 💳 PAGOS DE TARJETA VISA 9837 EL MISMO DÍA (03/11):
   - Pago 1: ₡271,600.00 (comprobante 74750898)
   - Pago 2: ₡31,434.00 (comprobante 74750901)
   - Total: ₡303,034.00
   - ¿Por qué dos pagos separados?

4. 👨‍👦 MESADA SEMANAL ANDRÉS:
   - 27/10: ₡5,000
   - 03/11: ₡5,000
   - ¿Es semanal? (6 días de diferencia)

5. 💸 ADELANTO DE SALARIO (05/11):
   - Monto: ₡70,000
   - ¿A quién se le dio este adelanto?

6. 📚 TRANSACCIONES DE LIBROS (27/10):
   - Gastos en libros: ₡5,000
   - Ingresos por ventas: ₡12,000 (Harold + Esterlin)
   - Utilidad neta: ₡7,000

7. 🏠 PAGO "CASA" (07/11):
   - Monto: ₡10,000
   - ¿Qué es este pago?

8. 🎓 BECA CISCO - ANDRÉS VELASCO (07/11):
   - Monto: ₡25,000
   - ¿Es pago de beca universitaria?
""")

print("\n" + "="*80)
print("ANÁLISIS: ¿QUÉ FALTA REGISTRAR EN EL EXCEL?")
print("="*80)

print("""
Movimientos que probablemente NO están en el Excel:

NOVIEMBRE (del 01/11 al 10/11):
- 10/11: McDonald's ₡12,126 (gasto personal?)
- 10/11: Pago Alejandra Arias ₡3,000
- 07/11: Pago Casa ₡10,000
- 07/11: Beca Cisco Andrés ₡25,000 (salida)
- 07/11: Ingreso Thomas ₡20,000 (entrada)
- 07/11: Conversión USD→CRC ₡30,000 ✅ (ya identificada)
- 05/11: Adelanto salario ₡70,000
- 03/11: Pago TC MC 8759 ₡5,070
- 03/11: Pago TC Visa 9837 ₡31,434
- 03/11: Pago TC Visa 9837 ₡271,600 (segundo pago)
- 03/11: Mesada Andrés ₡5,000

OCTUBRE (últimos días):
- 31/10: Ingreso Gas ₡2,000
- 31/10: Pago Rosdeyli ₡36,000
- 31/10: Liquidación Plan Ahorro ₡386,080.45 (GRANDE!)
- 31/10: Conversión USD→CRC ₡30,000
- 27/10: Varios gastos personales y transacciones libros

TOTAL MOVIMIENTOS A REVISAR: 21 transacciones
""")
