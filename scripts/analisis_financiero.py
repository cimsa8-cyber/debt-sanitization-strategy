#!/usr/bin/env python3
"""
Análisis financiero completo basado en Balance Sheet y transacciones
Autor: Alvaro Velasco
Fecha: Noviembre 2025
"""

import pandas as pd
import sys

def cargar_deudas(ruta='data/deudas_estructuradas_nov2025.csv'):
    """Carga el archivo de deudas estructuradas"""
    try:
        df = pd.read_csv(ruta)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        sys.exit(1)

def resumen_por_categoria(df):
    """Genera resumen de deudas por categoría"""
    resumen = df.groupby('categoria')['monto_usd'].sum().sort_values(ascending=False)
    return resumen

def resumen_por_tipo(df):
    """Genera resumen de deudas por tipo"""
    resumen = df.groupby('tipo')['monto_usd'].sum().sort_values(ascending=False)
    return resumen

def calcular_totales(df):
    """Calcula totales generales"""
    total = df['monto_usd'].sum()
    tarjetas = df[df['tipo'] == 'tarjeta_credito']['monto_usd'].sum()
    prestamos = df[df['tipo'] == 'prestamo']['monto_usd'].sum()
    impuestos = df[df['tipo'] == 'impuestos']['monto_usd'].sum()

    return {
        'total': total,
        'tarjetas': tarjetas,
        'prestamos': prestamos,
        'impuestos': impuestos
    }

def estrategia_avalancha(df, liquidez_disponible):
    """
    Estrategia de avalancha: pagar primero las deudas con mayor tasa de interés
    Nota: Necesitamos agregar columna de tasas de interés
    """
    # Por ahora ordenamos por monto (mayor a menor)
    df_sorted = df.sort_values('monto_usd', ascending=False)

    pagos = []
    liquidez = liquidez_disponible

    for idx, deuda in df_sorted.iterrows():
        if liquidez <= 0:
            break
        pago = min(deuda['monto_usd'], liquidez)
        pagos.append({
            'cuenta': deuda['cuenta'],
            'monto_original': deuda['monto_usd'],
            'pago_sugerido': pago,
            'tipo': deuda['tipo']
        })
        liquidez -= pago

    return pd.DataFrame(pagos)

def generar_reporte():
    """Genera reporte completo de análisis financiero"""
    print("=" * 70)
    print("ANÁLISIS FINANCIERO - DEBT SANITIZATION STRATEGY")
    print("=" * 70)
    print()

    # Cargar datos
    df_deudas = cargar_deudas()

    # Totales
    totales = calcular_totales(df_deudas)
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
    resumen_cat = resumen_por_categoria(df_deudas)
    for categoria, monto in resumen_cat.items():
        porcentaje = (monto / totales['total']) * 100
        print(f"  {categoria.capitalize():15} ${monto:>10,.2f}  ({porcentaje:5.1f}%)")
    print()

    # Detalle de tarjetas
    print("💳 DETALLE DE TARJETAS DE CRÉDITO")
    print("-" * 70)
    tarjetas = df_deudas[df_deudas['tipo'] == 'tarjeta_credito'].sort_values('monto_usd', ascending=False)
    for idx, tarjeta in tarjetas.iterrows():
        print(f"  {tarjeta['cuenta']:30} {tarjeta['moneda']:3} ${tarjeta['monto_usd']:>10,.2f}")
    print()

    # Estrategia sugerida
    print("🎯 ESTRATEGIA SUGERIDA (Avalancha)")
    print("-" * 70)
    print("Nota: Para optimizar, necesitamos tasas de interés de cada deuda")
    print("Prioridad actual: Mayor monto primero")
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

    print("=" * 70)
    print("Análisis generado exitosamente")
    print("=" * 70)

if __name__ == "__main__":
    generar_reporte()
