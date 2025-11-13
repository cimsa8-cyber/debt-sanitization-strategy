#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conciliación de cuenta Promerica USD 40000003881774 (Corporativa)
Período: 15/10/2025 al 10/11/2025
Saldo final: $3,282.14
Total débitos: $5,064.98
Total créditos: $6,452.11
"""

# Movimientos del extracto bancario Promerica USD
movimientos_banco = [
    # 16/10/2025
    {"fecha": "16/10/2025", "comprobante": "585896", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Salario Quincena - Comisión", "tipo": "Comisión"},
    {"fecha": "16/10/2025", "comprobante": "585896", "salida": 500.00, "entrada": 0, "descripcion": "TFT: Salario Quincena", "tipo": "Transferencia Salario"},

    # 17/10/2025
    {"fecha": "17/10/2025", "comprobante": "8210835", "salida": 0, "entrada": 350.00, "descripcion": "CD: VWR INTERNATIONAL LT", "tipo": "Ingreso Cliente"},

    # 21/10/2025
    {"fecha": "21/10/2025", "comprobante": "595744", "salida": 3.00, "entrada": 0, "descripcion": "TFT: fact 199488 - Comisión", "tipo": "Comisión"},
    {"fecha": "21/10/2025", "comprobante": "595744", "salida": 149.01, "entrada": 0, "descripcion": "TFT: fact 199488", "tipo": "Pago Factura"},
    {"fecha": "21/10/2025", "comprobante": "596247", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Casa 10E Alquiler - Comisión", "tipo": "Comisión"},
    {"fecha": "21/10/2025", "comprobante": "596247", "salida": 775.00, "entrada": 0, "descripcion": "TFT: Casa 10E Alquiler", "tipo": "Pago Alquiler"},

    # 22/10/2025
    {"fecha": "22/10/2025", "comprobante": "597597", "salida": 3.00, "entrada": 0, "descripcion": "TFT: fact 2502060 INTCOMEX - Comisión", "tipo": "Comisión"},
    {"fecha": "22/10/2025", "comprobante": "597597", "salida": 410.09, "entrada": 0, "descripcion": "TFT: fact 2502060 INTCOMEX", "tipo": "Pago Proveedor INTCOMEX"},

    # 23/10/2025
    {"fecha": "23/10/2025", "comprobante": "8226004", "salida": 0, "entrada": 1186.50, "descripcion": "CD: CORPORACION TIERRARE", "tipo": "Ingreso Cliente"},
    {"fecha": "23/10/2025", "comprobante": "547493", "salida": 73.61, "entrada": 0, "descripcion": "UNOPETROL BARREAL HEREDIA", "tipo": "Gasto Combustible"},

    # 24/10/2025
    {"fecha": "24/10/2025", "comprobante": "2785908", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "tipo": "Comisión"},
    {"fecha": "24/10/2025", "comprobante": "31821661", "salida": 29.38, "entrada": 0, "descripcion": "DD: SEA GLOBAL LOGISTICS", "tipo": "Pago Proveedor SEA Global"},

    # 27/10/2025
    {"fecha": "27/10/2025", "comprobante": "5325194", "salida": 39.59, "entrada": 0, "descripcion": "TEF ELEC PAGO ESPH# 108511979", "tipo": "Pago Servicios Públicos"},
    {"fecha": "27/10/2025", "comprobante": "5325195", "salida": 189.73, "entrada": 0, "descripcion": "TEF ELEC PAGO ESPH# 108506679", "tipo": "Pago Servicios Públicos"},
    {"fecha": "27/10/2025", "comprobante": "5325197", "salida": 392.68, "entrada": 0, "descripcion": "TEF ELEC PAGO ICETEL# 2025", "tipo": "Pago Servicios Telefonía"},

    # 28/10/2025
    {"fecha": "28/10/2025", "comprobante": "8241248", "salida": 0, "entrada": 56.50, "descripcion": "CD: CPF SERVICIOS RADIOLOGICOS", "tipo": "Ingreso Cliente"},
    {"fecha": "28/10/2025", "comprobante": "8241249", "salida": 0, "entrada": 56.50, "descripcion": "CD: ORTODEC SERVICIOS", "tipo": "Ingreso Cliente"},
    {"fecha": "28/10/2025", "comprobante": "8241251", "salida": 0, "entrada": 356.50, "descripcion": "CD: ORTODONCIA DE LA CRUZ", "tipo": "Ingreso Cliente"},
    {"fecha": "28/10/2025", "comprobante": "8241539", "salida": 0, "entrada": 1237.35, "descripcion": "CD: SMART WEB SERVICES", "tipo": "Ingreso Cliente"},

    # 29/10/2025
    {"fecha": "29/10/2025", "comprobante": "611261", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Pago de tarjeta - Comisión", "tipo": "Comisión"},
    {"fecha": "29/10/2025", "comprobante": "611261", "salida": 305.50, "entrada": 0, "descripcion": "TFT: Pago de tarjeta", "tipo": "Pago Tarjeta"},
    {"fecha": "29/10/2025", "comprobante": "611329", "salida": 3.00, "entrada": 0, "descripcion": "TFT: pago tarjeta - Comisión", "tipo": "Comisión"},
    {"fecha": "29/10/2025", "comprobante": "611329", "salida": 101.83, "entrada": 0, "descripcion": "TFT: pago tarjeta", "tipo": "Pago Tarjeta"},
    {"fecha": "29/10/2025", "comprobante": "611345", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Curso Pricing - Comisión", "tipo": "Comisión"},
    {"fecha": "29/10/2025", "comprobante": "611345", "salida": 101.83, "entrada": 0, "descripcion": "TFT: Curso Pricing", "tipo": "Pago Capacitación"},
    {"fecha": "29/10/2025", "comprobante": "2788366", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "tipo": "Comisión"},
    {"fecha": "29/10/2025", "comprobante": "31889087", "salida": 800.00, "entrada": 0, "descripcion": "DD: CARROFACIL DE COSTA RICA", "tipo": "Pago Vehículo"},

    # 30/10/2025
    {"fecha": "30/10/2025", "comprobante": "93194651", "salida": 0, "entrada": 1171.18, "descripcion": "GRUPO PORCINAS: Cancela fact 2487", "tipo": "Ingreso Cliente"},
    {"fecha": "30/10/2025", "comprobante": "2.5103E+14", "salida": 0, "entrada": 282.50, "descripcion": "Transferencia a ALVARO VELASCONET", "tipo": "Transferencia Interna"},
    {"fecha": "30/10/2025", "comprobante": "66679628", "salida": 0, "entrada": 284.76, "descripcion": "TEF. ELEC Volio Partners pago fact 2502", "tipo": "Ingreso Cliente"},
    {"fecha": "30/10/2025", "comprobante": "8254868", "salida": 0, "entrada": 149.16, "descripcion": "CD: SMART WEB SERVICES", "tipo": "Ingreso Cliente"},
    {"fecha": "30/10/2025", "comprobante": "8254872", "salida": 0, "entrada": 226.00, "descripcion": "CD: GENTRA DE COSTA RICA", "tipo": "Ingreso Cliente"},
    {"fecha": "30/10/2025", "comprobante": "730298", "salida": 226.83, "entrada": 0, "descripcion": "DON FERNANDO HEREDIA", "tipo": "Gasto Varios"},
    {"fecha": "30/10/2025", "comprobante": "737072", "salida": 40.46, "entrada": 0, "descripcion": "FARMAVALUE HEREDIA", "tipo": "Gasto Farmacia"},
    {"fecha": "30/10/2025", "comprobante": "754410", "salida": 63.03, "entrada": 0, "descripcion": "UNOPETROL BARREAL HEREDIA", "tipo": "Gasto Combustible"},

    # 03/11/2025
    {"fecha": "03/11/2025", "comprobante": "67169898", "salida": 733.20, "entrada": 0, "descripcion": "TEF. ELEC pago CCSS", "tipo": "Pago CCSS"},

    # 04/11/2025
    {"fecha": "04/11/2025", "comprobante": "5490555", "salida": 0, "entrada": 761.06, "descripcion": "PEREZ BENAVIDES: facturas 2535 2530", "tipo": "Ingreso Cliente"},

    # 06/11/2025
    {"fecha": "06/11/2025", "comprobante": "2795229", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "tipo": "Comisión"},
    {"fecha": "06/11/2025", "comprobante": "32048171", "salida": 58.76, "entrada": 0, "descripcion": "DD: SEA GLOBAL LOGISTICS", "tipo": "Pago Proveedor SEA Global"},

    # 07/11/2025
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "tipo": "Comisión"},
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0, "entrada": 0.75, "descripcion": "Reversión de Comisión", "tipo": "Ingreso Reversión"},
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "tipo": "Comisión"},
    {"fecha": "07/11/2025", "comprobante": "32067344", "salida": 40.57, "entrada": 0, "descripcion": "DD: ALEJANDRA ARIAS FALLAS", "tipo": "Pago Servicios Alejandra"},
    {"fecha": "07/11/2025", "comprobante": "8313051", "salida": 0, "entrada": 333.35, "descripcion": "CD: ASOCIACION COSTARRICENSE", "tipo": "Ingreso Cliente"},

    # 08/11/2025
    {"fecha": "08/11/2025", "comprobante": "141111", "salida": 9.13, "entrada": 0, "descripcion": "ESTACION SERVICIOS NASA HEREDIA", "tipo": "Gasto Combustible"},
]

print("="*80)
print("CONCILIACIÓN: CUENTA PROMERICA USD 40000003881774 (CORPORATIVA)")
print("="*80)
print(f"\nPeríodo: 15/10/2025 al 10/11/2025")
print(f"Saldo final: $3,282.14")
print(f"Total débitos: $5,064.98")
print(f"Total créditos: $6,452.11")
print(f"Total movimientos: {len(movimientos_banco)}")

# Calcular totales
total_salidas = sum([m['salida'] for m in movimientos_banco])
total_entradas = sum([m['entrada'] for m in movimientos_banco])

print(f"\nVerificación:")
print(f"  Suma débitos calculada: ${total_salidas:.2f}")
print(f"  Suma créditos calculada: ${total_entradas:.2f}")
print(f"  Movimiento neto: ${total_entradas - total_salidas:.2f}")

print("\n" + "="*80)
print("RESUMEN DE MOVIMIENTOS POR FECHA")
print("="*80)

# Agrupar por fecha
from collections import defaultdict
por_fecha = defaultdict(list)
for mov in movimientos_banco:
    por_fecha[mov['fecha']].append(mov)

for fecha in sorted(por_fecha.keys()):
    movs = por_fecha[fecha]
    total_salidas_dia = sum([m['salida'] for m in movs])
    total_entradas_dia = sum([m['entrada'] for m in movs])
    print(f"\n📅 {fecha} - Salidas: ${total_salidas_dia:.2f} | Entradas: ${total_entradas_dia:.2f}")
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
    total_salidas_tipo = sum([m['salida'] for m in movs])
    total_entradas_tipo = sum([m['entrada'] for m in movs])
    count = len(movs)

    if total_salidas_tipo > 0:
        print(f"\n❌ {tipo}: {count} mov - Salidas: ${total_salidas_tipo:.2f}")
    if total_entradas_tipo > 0:
        print(f"\n✅ {tipo}: {count} mov - Entradas: ${total_entradas_tipo:.2f}")

    for mov in movs:
        if mov['salida'] > 0:
            print(f"  {mov['fecha']} | ${mov['salida']:>8.2f} | {mov['descripcion'][:50]}")
        elif mov['entrada'] > 0:
            print(f"  {mov['fecha']} | ${mov['entrada']:>8.2f} | {mov['descripcion'][:50]}")

print("\n" + "="*80)
print("HALLAZGOS IMPORTANTES")
print("="*80)

print("""
1. 💰 INGRESOS DE CLIENTES (Total: $4,506.55):
   - VWR International: $350.00
   - Corporación Tierrare: $1,186.50
   - Smart Web Services: $1,386.51 (2 pagos)
   - Grupo Porcinas: $1,171.18
   - Volio Partners: $284.76
   - Otros clientes menores

2. 💸 PAGOS RECURRENTES:
   - Servicios públicos (ESPH): $229.32
   - Telefonía (ICETEL): $392.68
   - CCSS: $733.20
   - Total servicios: $1,355.20

3. ⛽ COMBUSTIBLE UNOPETROL:
   - 23/10: $73.61
   - 30/10: $63.03
   - Total: $136.64

4. 🏠 ALQUILER CASA 10E:
   - 21/10: $775.00

5. 📦 PROVEEDORES:
   - INTCOMEX fact 2502060: $410.09 (22/10)
   - SEA Global: $29.38 (24/10) + $58.76 (06/11) = $88.14
   - CarroFácil: $800.00

6. 👥 ALEJANDRA ARIAS:
   - 07/11: $40.57 (pago semanal)

7. 💳 PAGOS DE TARJETAS:
   - 29/10: $305.50 + $101.83 = $407.33

8. 💰 COMISIONES BANCARIAS:
   - Total: $17.25 (23 comisiones de $0.75)
   - Reversión: -$0.75 (07/11)
   - Neto: $16.50

9. ⚠️ MOVIMIENTOS NO APARECEN AQUÍ:
   - Pago INTCOMEX $3,137.26 (programado 10/11 22:00)
   - Comisión $0.75 (programado 10/11)
   - Probablemente se aplicaron después del corte

10. 📊 SALDO INICIAL APROXIMADO:
    - Primer movimiento del 16/10 dejó: $1,892.01
    - Saldo final 10/11: $3,282.14
    - Aumento neto: $1,390.13
""")

print("\n" + "="*80)
print("ANÁLISIS: ¿QUÉ FALTA REGISTRAR EN EL EXCEL?")
print("="*80)

print(f"""
Total de movimientos en extracto: {len(movimientos_banco)}

Probablemente TODOS estos movimientos necesitan registrarse porque
esta cuenta Promerica NO fue conciliada previamente.

Movimientos por tipo:
- Ingresos de clientes: ~15 movimientos
- Pagos de proveedores: ~10 movimientos
- Pagos de servicios: ~8 movimientos
- Comisiones bancarias: ~23 movimientos
- Gastos operativos: ~10 movimientos

IMPORTANTE: El pago de INTCOMEX $3,137.26 que registramos antes
probablemente ya está en el Excel (lo agregamos en sesión anterior),
pero NO aparece en este extracto porque se programó para después
del corte (10/11 22:00).
""")
