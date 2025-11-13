#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis de discrepancia en Promerica USD 1774
Compara extracto bancario vs movimientos agregados al Excel
"""

# Movimientos del extracto bancario (46 movimientos del 16/10 al 08/11)
movimientos_extracto = [
    # 16/10/2025
    {"fecha": "16/10/2025", "comprobante": "585896", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Salario Quincena - Comisión", "incluido_excel": True},
    {"fecha": "16/10/2025", "comprobante": "585896", "salida": 500.00, "entrada": 0, "descripcion": "TFT: Salario Quincena", "incluido_excel": True},

    # 17/10/2025
    {"fecha": "17/10/2025", "comprobante": "8210835", "salida": 0, "entrada": 350.00, "descripcion": "CD: VWR INTERNATIONAL LT", "incluido_excel": True},

    # 21/10/2025
    {"fecha": "21/10/2025", "comprobante": "595744", "salida": 3.00, "entrada": 0, "descripcion": "TFT: fact 199488 - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "21/10/2025", "comprobante": "595744", "salida": 149.01, "entrada": 0, "descripcion": "TFT: fact 199488", "incluido_excel": True},
    {"fecha": "21/10/2025", "comprobante": "596247", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Casa 10E Alquiler - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "21/10/2025", "comprobante": "596247", "salida": 775.00, "entrada": 0, "descripcion": "TFT: Casa 10E Alquiler", "incluido_excel": True},

    # 22/10/2025
    {"fecha": "22/10/2025", "comprobante": "597597", "salida": 3.00, "entrada": 0, "descripcion": "TFT: fact 2502060 INTCOMEX - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "22/10/2025", "comprobante": "597597", "salida": 410.09, "entrada": 0, "descripcion": "TFT: fact 2502060 INTCOMEX", "incluido_excel": True},

    # 23/10/2025
    {"fecha": "23/10/2025", "comprobante": "8226004", "salida": 0, "entrada": 1186.50, "descripcion": "CD: CORPORACION TIERRARE", "incluido_excel": True},
    {"fecha": "23/10/2025", "comprobante": "547493", "salida": 73.61, "entrada": 0, "descripcion": "UNOPETROL BARREAL HEREDIA", "incluido_excel": True},

    # 24/10/2025
    {"fecha": "24/10/2025", "comprobante": "2785908", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "24/10/2025", "comprobante": "31821661", "salida": 29.38, "entrada": 0, "descripcion": "DD: SEA GLOBAL LOGISTICS", "incluido_excel": True},

    # 27/10/2025
    {"fecha": "27/10/2025", "comprobante": "5325194", "salida": 39.59, "entrada": 0, "descripcion": "TEF ELEC PAGO ESPH# 108511979", "incluido_excel": True},
    {"fecha": "27/10/2025", "comprobante": "5325195", "salida": 189.73, "entrada": 0, "descripcion": "TEF ELEC PAGO ESPH# 108506679", "incluido_excel": True},
    {"fecha": "27/10/2025", "comprobante": "5325197", "salida": 392.68, "entrada": 0, "descripcion": "TEF ELEC PAGO ICETEL# 2025", "incluido_excel": True},

    # 28/10/2025
    {"fecha": "28/10/2025", "comprobante": "8241248", "salida": 0, "entrada": 56.50, "descripcion": "CD: CPF SERVICIOS RADIOLOGICOS", "incluido_excel": True},
    {"fecha": "28/10/2025", "comprobante": "8241249", "salida": 0, "entrada": 56.50, "descripcion": "CD: ORTODEC SERVICIOS", "incluido_excel": True},
    {"fecha": "28/10/2025", "comprobante": "8241251", "salida": 0, "entrada": 356.50, "descripcion": "CD: ORTODONCIA DE LA CRUZ", "incluido_excel": True},
    {"fecha": "28/10/2025", "comprobante": "8241539", "salida": 0, "entrada": 1237.35, "descripcion": "CD: SMART WEB SERVICES", "incluido_excel": True},

    # 29/10/2025
    {"fecha": "29/10/2025", "comprobante": "611261", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Pago de tarjeta - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "29/10/2025", "comprobante": "611261", "salida": 305.50, "entrada": 0, "descripcion": "TFT: Pago de tarjeta", "incluido_excel": True},
    {"fecha": "29/10/2025", "comprobante": "611329", "salida": 3.00, "entrada": 0, "descripcion": "TFT: pago tarjeta - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "29/10/2025", "comprobante": "611329", "salida": 101.83, "entrada": 0, "descripcion": "TFT: pago tarjeta", "incluido_excel": True},
    {"fecha": "29/10/2025", "comprobante": "611345", "salida": 3.00, "entrada": 0, "descripcion": "TFT: Curso Pricing - Comisión", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "29/10/2025", "comprobante": "611345", "salida": 101.83, "entrada": 0, "descripcion": "TFT: Curso Pricing", "incluido_excel": True},
    {"fecha": "29/10/2025", "comprobante": "2788366", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "incluido_excel": False},  # COMISIÓN NO INCLUIDA
    {"fecha": "29/10/2025", "comprobante": "31889087", "salida": 800.00, "entrada": 0, "descripcion": "DD: CARROFACIL DE COSTA RICA", "incluido_excel": True},

    # 30/10/2025
    {"fecha": "30/10/2025", "comprobante": "93194651", "salida": 0, "entrada": 1171.18, "descripcion": "GRUPO PORCINAS: Cancela fact 2487", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "2.5103E+14", "salida": 0, "entrada": 282.50, "descripcion": "Transferencia a ALVARO VELASCONET", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "66679628", "salida": 0, "entrada": 284.76, "descripcion": "TEF. ELEC Volio Partners pago fact 2502", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "8254868", "salida": 0, "entrada": 149.16, "descripcion": "CD: SMART WEB SERVICES", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "8254872", "salida": 0, "entrada": 226.00, "descripcion": "CD: GENTRA DE COSTA RICA", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "730298", "salida": 226.83, "entrada": 0, "descripcion": "DON FERNANDO HEREDIA", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "737072", "salida": 40.46, "entrada": 0, "descripcion": "FARMAVALUE HEREDIA", "incluido_excel": True},
    {"fecha": "30/10/2025", "comprobante": "754410", "salida": 63.03, "entrada": 0, "descripcion": "UNOPETROL BARREAL HEREDIA", "incluido_excel": False},  # ⚠️ NO INCLUIDO EN SCRIPT

    # 03/11/2025
    {"fecha": "03/11/2025", "comprobante": "67169898", "salida": 733.20, "entrada": 0, "descripcion": "TEF. ELEC pago CCSS", "incluido_excel": True},

    # 04/11/2025
    {"fecha": "04/11/2025", "comprobante": "5490555", "salida": 0, "entrada": 761.06, "descripcion": "PEREZ BENAVIDES: facturas 2535 2530", "incluido_excel": True},

    # 06/11/2025 - ⚠️ MOVIMIENTOS NO INCLUIDOS EN SCRIPT
    {"fecha": "06/11/2025", "comprobante": "2795229", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "incluido_excel": False},
    {"fecha": "06/11/2025", "comprobante": "32048171", "salida": 58.76, "entrada": 0, "descripcion": "DD: SEA GLOBAL LOGISTICS", "incluido_excel": False},

    # 07/11/2025
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "incluido_excel": False},
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0, "entrada": 0.75, "descripcion": "Reversión de Comisión", "incluido_excel": False},
    {"fecha": "07/11/2025", "comprobante": "2796348", "salida": 0.75, "entrada": 0, "descripcion": "Comisión Debito por Transf. Sinpe", "incluido_excel": False},
    {"fecha": "07/11/2025", "comprobante": "32067344", "salida": 40.57, "entrada": 0, "descripcion": "DD: ALEJANDRA ARIAS FALLAS", "incluido_excel": False},
    {"fecha": "07/11/2025", "comprobante": "8313051", "salida": 0, "entrada": 333.35, "descripcion": "CD: ASOCIACION COSTARRICENSE", "incluido_excel": True},

    # 08/11/2025 - ⚠️ NO INCLUIDO EN SCRIPT
    {"fecha": "08/11/2025", "comprobante": "141111", "salida": 9.13, "entrada": 0, "descripcion": "ESTACION SERVICIOS NASA HEREDIA", "incluido_excel": False},
]

print("="*80)
print("ANÁLISIS DE DISCREPANCIA: PROMERICA USD 1774")
print("="*80)

# Calcular totales del extracto bancario
total_entradas_extracto = sum([m['entrada'] for m in movimientos_extracto])
total_salidas_extracto = sum([m['salida'] for m in movimientos_extracto])
saldo_neto_extracto = total_entradas_extracto - total_salidas_extracto

print(f"\n📋 EXTRACTO BANCARIO (16/10 al 08/11):")
print(f"   Total movimientos: {len(movimientos_extracto)}")
print(f"   Total entradas: ${total_entradas_extracto:,.2f}")
print(f"   Total salidas: ${total_salidas_extracto:,.2f}")
print(f"   Movimiento neto: ${saldo_neto_extracto:,.2f}")

# Calcular lo que se agregó al Excel
movimientos_excel = [m for m in movimientos_extracto if m['incluido_excel']]
movimientos_faltantes = [m for m in movimientos_extracto if not m['incluido_excel']]

total_entradas_excel = sum([m['entrada'] for m in movimientos_excel])
total_salidas_excel = sum([m['salida'] for m in movimientos_excel])
saldo_neto_excel = total_entradas_excel - total_salidas_excel

print(f"\n📝 MOVIMIENTOS AGREGADOS AL EXCEL:")
print(f"   Total movimientos: {len(movimientos_excel)}")
print(f"   Total entradas: ${total_entradas_excel:,.2f}")
print(f"   Total salidas: ${total_salidas_excel:,.2f}")
print(f"   Movimiento neto: ${saldo_neto_excel:,.2f}")

# Calcular faltantes
total_entradas_faltantes = sum([m['entrada'] for m in movimientos_faltantes])
total_salidas_faltantes = sum([m['salida'] for m in movimientos_faltantes])
saldo_neto_faltantes = total_entradas_faltantes - total_salidas_faltantes

print(f"\n❌ MOVIMIENTOS NO INCLUIDOS:")
print(f"   Total movimientos: {len(movimientos_faltantes)}")
print(f"   Total entradas: ${total_entradas_faltantes:,.2f}")
print(f"   Total salidas: ${total_salidas_faltantes:,.2f}")
print(f"   Movimiento neto: ${saldo_neto_faltantes:,.2f}")

print("\n" + "="*80)
print("DETALLE DE MOVIMIENTOS FALTANTES")
print("="*80)

# Agrupar por categoría
comisiones = [m for m in movimientos_faltantes if 'Comisión' in m['descripcion'] or 'comisión' in m['descripcion'].lower()]
otros = [m for m in movimientos_faltantes if m not in comisiones]

print(f"\n💰 COMISIONES BANCARIAS NO INCLUIDAS: {len(comisiones)} movimientos")
total_comisiones = sum([m['salida'] for m in comisiones]) - sum([m['entrada'] for m in comisiones])
print(f"   Total comisiones: ${total_comisiones:.2f}")
for m in comisiones:
    if m['salida'] > 0:
        print(f"   - {m['fecha']} | {m['comprobante']:12} | -${m['salida']:>6.2f} | {m['descripcion']}")
    else:
        print(f"   - {m['fecha']} | {m['comprobante']:12} | +${m['entrada']:>6.2f} | {m['descripcion']}")

print(f"\n📦 OTROS MOVIMIENTOS NO INCLUIDOS: {len(otros)} movimientos")
total_otros_entradas = sum([m['entrada'] for m in otros])
total_otros_salidas = sum([m['salida'] for m in otros])
print(f"   Total: -${total_otros_salidas:.2f}")
for m in otros:
    if m['salida'] > 0:
        print(f"   - {m['fecha']} | {m['comprobante']:12} | -${m['salida']:>7.2f} | {m['descripcion']}")
    else:
        print(f"   - {m['fecha']} | {m['comprobante']:12} | +${m['entrada']:>7.2f} | {m['descripcion']}")

print("\n" + "="*80)
print("ANÁLISIS DE SALDO")
print("="*80)

print(f"""
⚠️ DISCREPANCIA IDENTIFICADA:

1. Saldo según extracto bancario (08/11): $3,282.14
2. Si falta registrar movimientos netos de: ${saldo_neto_faltantes:.2f}
3. Saldo que debería mostrar el Excel ahora: $3,282.14 - (${abs(saldo_neto_faltantes):.2f}) = ${3282.14 + saldo_neto_faltantes:.2f}

Usuario reporta saldo en Excel: $2,999.24

POSIBLES EXPLICACIONES:

A) Los movimientos faltantes explican parte de la diferencia:
   - Faltan registrar ${abs(saldo_neto_faltantes):.2f} en egresos netos

B) Diferencia total a explicar:
   - Saldo extracto: $3,282.14
   - Saldo Excel: $2,999.24
   - Diferencia: ${3282.14 - 2999.24:.2f}

C) Si restamos los movimientos faltantes:
   - $2,999.24 (Excel actual) + ${abs(saldo_neto_faltantes):.2f} (faltantes) = ${2999.24 + abs(saldo_neto_faltantes):.2f}
   - VS saldo extracto: $3,282.14
   - Nueva diferencia: ${3282.14 - (2999.24 + abs(saldo_neto_faltantes)):.2f}

⚠️ ATENCIÓN: Esta diferencia de ${3282.14 - (2999.24 + abs(saldo_neto_faltantes)):.2f} sugiere que:
   1. Hay OTROS movimientos no considerados
   2. El saldo inicial de Promerica estaba incorrecto en el Excel
   3. Se registró DUPLICADO el pago INTCOMEX $3,137.26
""")

print("\n" + "="*80)
print("PRÓXIMOS PASOS")
print("="*80)

print("""
1. VERIFICAR en el Excel:
   - ¿Aparece el pago INTCOMEX de $3,137.26 del 10/11?
   - Este pago NO está en el extracto (programado después del corte)
   - Si ya está registrado, explicaría gran parte de la diferencia

2. AGREGAR movimientos faltantes:
   - 11 movimientos identificados (principalmente comisiones)
   - Total impacto: ${:.2f} en egresos netos

3. REVISAR saldo inicial de Promerica:
   - ¿Cuál era el saldo al 15/10/2025?
   - Verificar que sea consistente con el primer movimiento
""".format(abs(saldo_neto_faltantes)))

print("\n" + "="*80)
