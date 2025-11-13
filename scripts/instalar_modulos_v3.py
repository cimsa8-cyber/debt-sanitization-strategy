#!/usr/bin/env python3
"""
Script de instalación de módulos necesarios para Excel v3.0
Ejecutar: python scripts/instalar_modulos_v3.py
"""

import subprocess
import sys

MODULOS_NECESARIOS = [
    ('pandas', 'Análisis de datos y detección de duplicados'),
    ('numpy', 'Cálculos numéricos y proyecciones'),
    ('matplotlib', 'Gráficos y visualizaciones'),
    ('xlsxwriter', 'Creación avanzada de archivos Excel'),
    ('lxml', 'Procesamiento de XML de Hacienda'),
    ('reportlab', 'Generación de reportes PDF'),
    ('pillow', 'Procesamiento de imágenes para PDFs'),
]

def instalar_modulo(nombre, descripcion):
    """Instala un módulo usando pip"""
    print(f"\n{'='*60}")
    print(f"📦 Instalando: {nombre}")
    print(f"   Uso: {descripcion}")
    print(f"{'='*60}")

    try:
        subprocess.check_call([
            sys.executable,
            '-m',
            'pip',
            'install',
            '--upgrade',
            nombre
        ])
        print(f"✅ {nombre} instalado exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error instalando {nombre}: {e}")
        return False

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║     INSTALACIÓN DE MÓDULOS PARA EXCEL V3.0                ║
║     Sistema de Saneamiento de Deuda - CIMSA              ║
╚═══════════════════════════════════════════════════════════╝
    """)

    total = len(MODULOS_NECESARIOS)
    exitosos = 0
    fallidos = []

    for nombre, descripcion in MODULOS_NECESARIOS:
        if instalar_modulo(nombre, descripcion):
            exitosos += 1
        else:
            fallidos.append(nombre)

    print(f"\n{'='*60}")
    print(f"📊 RESUMEN DE INSTALACIÓN")
    print(f"{'='*60}")
    print(f"✅ Exitosos: {exitosos}/{total}")
    if fallidos:
        print(f"❌ Fallidos: {len(fallidos)}")
        print(f"   Módulos: {', '.join(fallidos)}")
    else:
        print(f"🎉 TODOS LOS MÓDULOS INSTALADOS CORRECTAMENTE")

    print(f"\n{'='*60}")
    print("📋 VERIFICACIÓN DE MÓDULOS INSTALADOS:")
    print(f"{'='*60}")

    # Verificar cada módulo
    for nombre, _ in MODULOS_NECESARIOS:
        try:
            __import__(nombre)
            version = __import__(nombre).__version__ if hasattr(__import__(nombre), '__version__') else 'OK'
            print(f"✅ {nombre:20s} - {version}")
        except ImportError:
            print(f"❌ {nombre:20s} - NO DISPONIBLE")

    print(f"\n{'='*60}")
    print("🚀 Sistema listo para desarrollo de Excel v3.0")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
