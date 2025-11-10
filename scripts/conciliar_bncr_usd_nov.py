#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de cuenta BNCR USD 100-02-601066-4
Período: 01/11/2025 al 10/11/2025
Saldo disponible: $1,030.87
Total salidas: $2,119.07
"""

# Movimientos del extracto bancario BNCR USD
movimientos_banco = [
    # 10/11/2025
    {"fecha": "10/11/2025", "comprobante": "76954232", "salida": 60.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 17000002201/BN-PAR", "tipo": "Plan Ahorro Nuevo"},
    {"fecha": "10/11/2025", "comprobante": "76952525", "salida": 25.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002388223/BN-PAR", "tipo": "Plan Ahorro Black Friday"},
    {"fecha": "10/11/2025", "comprobante": "76950132", "salida": 50.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002335826/BN-PAR", "tipo": "Plan Ahorro Matrimonio"},
    {"fecha": "10/11/2025", "comprobante": "76949655", "salida": 75.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002273441/BN-PAR", "tipo": "Plan Ahorro Impuestos Municipales"},

    # 07/11/2025
    {"fecha": "07/11/2025", "comprobante": "98652306", "salida": 60.48, "entrada": 0, "descripcion": "TRANSFERENCIA DOLARES/BN-PAR", "tipo": "Transferencia USD a CRC"},
    {"fecha": "07/11/2025", "comprobante": "34195590", "salida": 25.00, "entrada": 0, "descripcion": "SERVICIOS DE FACTURACION Y COBRO/BN-PAR", "tipo": "Servicio Bancario"},

    # 05/11/2025
    {"fecha": "05/11/2025", "comprobante": "16951587", "salida": 3.02, "entrada": 0, "descripcion": "COBRO DE COMISION TFT/ALVARO VELASCO J.", "tipo": "Comisión Bancaria"},
    {"fecha": "05/11/2025", "comprobante": "16951584", "salida": 681.42, "entrada": 0, "descripcion": "TC VELASCO SIMAN/ALVARO VELASCO J.", "tipo": "Pago Tarjeta Siman"},

    # 03/11/2025
    {"fecha": "03/11/2025", "comprobante": "12961759", "salida": 607.29, "entrada": 0, "descripcion": "PAGO VISA 5290-60XX-XXXX-8759/ALVARO VELASCO J.", "tipo": "Pago Tarjeta MC 8759"},
    {"fecha": "03/11/2025", "comprobante": "12956019", "salida": 321.86, "entrada": 0, "descripcion": "PAGO VISA 4831-26XX-XXXX-6386/ALVARO VELASCO J.", "tipo": "Pago Tarjeta Visa 6386"},
    {"fecha": "03/11/2025", "comprobante": "74978531", "salida": 60.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 17000002201/BN-PAR", "tipo": "Plan Ahorro Nuevo"},
    {"fecha": "03/11/2025", "comprobante": "74977457", "salida": 25.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002388223/BN-PAR", "tipo": "Plan Ahorro Black Friday"},
    {"fecha": "03/11/2025", "comprobante": "74976604", "salida": 50.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002335826/BN-PAR", "tipo": "Plan Ahorro Matrimonio"},
    {"fecha": "03/11/2025", "comprobante": "74976051", "salida": 75.00, "entrada": 0, "descripcion": "BNAHOR NO-NUMERO DE CONTRATO 01002273441/BN-PAR", "tipo": "Plan Ahorro Impuestos Municipales"},
]

print("="*80)
print("CONCILIACIÓN: CUENTA BNCR USD 100-02-601066-4")
print("Período: 01/11/2025 al 10/11/2025")
print("="*80)
print(f"\nSaldo disponible según banco: $1,030.87")
print(f"Total salidas del período: ${sum([m['salida'] for m in movimientos_banco]):.2f}")
print(f"Total movimientos: {len(movimientos_banco)}")

print("\n" + "="*80)
print("RESUMEN DE MOVIMIENTOS POR FECHA Y TIPO")
print("="*80)

# Agrupar por fecha
from collections import defaultdict
por_fecha = defaultdict(list)
for mov in movimientos_banco:
    por_fecha[mov['fecha']].append(mov)

for fecha in sorted(por_fecha.keys(), reverse=True):
    movs = por_fecha[fecha]
    total_dia = sum([m['salida'] for m in movs])
    print(f"\n📅 {fecha} - Total: ${total_dia:.2f}")
    print("-" * 80)
    for mov in movs:
        print(f"  {mov['comprobante']:12} | ${mov['salida']:8.2f} | {mov['tipo']}")

print("\n" + "="*80)
print("MOVIMIENTOS AGRUPADOS POR TIPO")
print("="*80)

por_tipo = defaultdict(list)
for mov in movimientos_banco:
    por_tipo[mov['tipo']].append(mov)

for tipo in sorted(por_tipo.keys()):
    movs = por_tipo[tipo]
    total_tipo = sum([m['salida'] for m in movs])
    count = len(movs)
    print(f"\n{tipo}: {count} movimiento(s) - Total: ${total_tipo:.2f}")
    for mov in movs:
        print(f"  {mov['fecha']} | {mov['comprobante']:12} | ${mov['salida']:8.2f}")

print("\n" + "="*80)
print("ANÁLISIS: ¿QUÉ FALTA REGISTRAR EN EL EXCEL?")
print("="*80)

print("""
Para completar el Excel necesitamos:

1. ✅ 4 Planes de ahorro del 10/11/2025 ($210.00)
   - Ahora confirmado: salen de cuenta BNCR USD 100-02-601066

2. ❓ Transferencia USD a CRC del 07/11/2025 ($60.48)
   - Comprobante: 98652306
   - Descripción: "TRANSFERENCIA DOLARES/BN-PAR"
   - Usuario mencionó antes: transferencia de ₡30,000 CRC
   - PREGUNTA: ¿Es conversión $60.48 USD → ₡30,000 CRC?

3. ❓ Servicio de facturación 07/11/2025 ($25.00)
   - Comprobante: 34195590
   - ¿Qué servicio es este?

4. ❓ Comisión TFT 05/11/2025 ($3.02)
   - Comprobante: 16951587
   - Relacionado con pago Siman

5. ❓ Pago Siman 05/11/2025 ($681.42)
   - Comprobante: 16951584
   - Usuario mencionó SINPE ₡337,981.89 el mismo día
   - ¿Son el mismo pago o diferentes?

6. ❓ Pago Tarjeta MC 8759 - 03/11/2025 ($607.29)
   - ¿Cuál es el período de esta tarjeta?

7. ❓ Pago Tarjeta Visa 6386 - 03/11/2025 ($321.86)
   - ¿Qué tarjeta es la 6386?

8. ✅ 4 Planes de ahorro del 03/11/2025 ($210.00)
   - Mismos planes que el 10/11
   - ¿Son aportes semanales o quincenales?

""")

print("="*80)
print("PRÓXIMAS PREGUNTAS PARA EL USUARIO")
print("="*80)
print("""
Pregunta 2: Transferencia $60.48 del 07/11
¿Convirtió $60.48 USD a ₡30,000 CRC? (la que mencionó antes)

Pregunta 3: Servicio facturación $25.00 del 07/11
¿Qué servicio es este? (comprobante 34195590)

Pregunta 4: Comisión TFT $3.02 del 05/11
¿Es la comisión por el pago Siman?

Pregunta 5: Pago Siman
El extracto muestra $681.42 desde BNCR USD el 05/11
Usted mencionó antes un SINPE de ₡337,981.89 el 05/11
¿Son el mismo pago o 2 pagos diferentes?

Pregunta 6: Tarjeta Visa 6386
¿Qué tarjeta es la terminada en 6386? ($321.86 pagado el 03/11)
""")
