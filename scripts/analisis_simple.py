#!/usr/bin/env python3
"""
Análisis financiero simple sin dependencias externas
Autor: Alvaro Velasco
Fecha: Noviembre 2025
"""

import csv
from collections import defaultdict

def cargar_deudas(ruta='data/deudas_estructuradas_nov2025.csv'):
    """Carga el archivo de deudas estructuradas"""
    deudas = []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['monto_usd'] = float(row['monto_usd'])
                deudas.append(row)
        return deudas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return []

def resumen_por_categoria(deudas):
    """Genera resumen de deudas por categoría"""
    totales = defaultdict(float)
    for deuda in deudas:
        totales[deuda['categoria']] += deuda['monto_usd']
    return dict(sorted(totales.items(), key=lambda x: x[1], reverse=True))

def calcular_totales(deudas):
    """Calcula totales generales"""
    total = sum(d['monto_usd'] for d in deudas)
    tarjetas = sum(d['monto_usd'] for d in deudas if d['tipo'] == 'tarjeta_credito')
    prestamos = sum(d['monto_usd'] for d in deudas if d['tipo'] == 'prestamo')
    impuestos = sum(d['monto_usd'] for d in deudas if d['tipo'] == 'impuestos')

    return {
        'total': total,
        'tarjetas': tarjetas,
        'prestamos': prestamos,
        'impuestos': impuestos
    }

def generar_reporte():
    """Genera reporte completo de análisis financiero"""
    print("=" * 70)
    print("ANÁLISIS FINANCIERO - DEBT SANITIZATION STRATEGY")
    print("=" * 70)
    print()

    # Cargar datos
    deudas = cargar_deudas()
    if not deudas:
        return

    # Totales
    totales = calcular_totales(deudas)
    print("📊 RESUMEN GENERAL")
    print("-" * 70)
    print(f"Total Pasivos:           ${totales['total']:,.2f}")
    print(f"  • Tarjetas de Crédito: ${totales['tarjetas']:,.2f}")
    print(f"  • Préstamos:           ${totales['prestamos']:,.2f}")
    print(f"  • Impuestos:           ${totales['impuestos']:,.2f}")
    print()

    # Por categoría
    print("📈 DEUDAS POR CATEGORÍA")
    print("-" * 70)
    resumen_cat = resumen_por_categoria(deudas)
    for categoria, monto in resumen_cat.items():
        porcentaje = (monto / totales['total']) * 100
        print(f"  {categoria.capitalize():15} ${monto:>10,.2f}  ({porcentaje:5.1f}%)")
    print()

    # Detalle de tarjetas
    print("💳 DETALLE DE TARJETAS DE CRÉDITO")
    print("-" * 70)
    tarjetas = sorted([d for d in deudas if d['tipo'] == 'tarjeta_credito'],
                     key=lambda x: x['monto_usd'], reverse=True)
    for tarjeta in tarjetas:
        print(f"  {tarjeta['cuenta']:30} {tarjeta['moneda']:3} ${tarjeta['monto_usd']:>10,.2f}")
    print()

    # Balance de liquidez
    activos_disponibles = 14334.73  # Del balance sheet
    print("💰 BALANCE DE LIQUIDEZ")
    print("-" * 70)
    print(f"Activos disponibles:     ${activos_disponibles:,.2f}")
    print(f"Pasivos totales:         ${totales['total']:,.2f}")
    print(f"Déficit:                 ${totales['total'] - activos_disponibles:,.2f}")
    print()

    ratio = (activos_disponibles / totales['total']) * 100
    print(f"Ratio Activos/Pasivos:   {ratio:.1f}%")
    print()

    # Análisis por tipo de deuda
    print("🎯 PRIORIZACIÓN RECOMENDADA")
    print("-" * 70)
    print("1. URGENTE - Impuestos Hacienda:")
    impuestos_list = [d for d in deudas if d['tipo'] == 'impuestos']
    for imp in impuestos_list:
        print(f"   • {imp['cuenta']}: ${imp['monto_usd']:,.2f}")

    print("\n2. ALTO COSTO - Tarjetas de Crédito (mayor a menor):")
    for i, tarjeta in enumerate(tarjetas[:3], 1):
        print(f"   {i}. {tarjeta['cuenta']}: ${tarjeta['monto_usd']:,.2f}")

    print("\n3. ESTRUCTURADO - Préstamo Vehicular:")
    prestamos_list = [d for d in deudas if d['tipo'] == 'prestamo']
    for prest in prestamos_list:
        print(f"   • {prest['cuenta']}: ${prest['monto_usd']:,.2f}")
    print()

    print("=" * 70)
    print("⚠️  NOTA: Para estrategia óptima se requieren tasas de interés")
    print("=" * 70)

if __name__ == "__main__":
    generar_reporte()
