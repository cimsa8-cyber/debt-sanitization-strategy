# Guía de Aprendizaje: Trabajando con Claude AI

**Propósito**: Documento educativo para entender comandos, lenguajes y mejores prácticas al trabajar con Claude AI en proyectos de desarrollo.

---

## 📚 Tabla de Contenidos

1. [Lenguajes y Comandos Usados](#lenguajes-y-comandos-usados)
2. [Herramientas de Claude AI](#herramientas-de-claude-ai)
3. [Proceso de Prueba y Error](#proceso-de-prueba-y-error)
4. [Mejores Prácticas](#mejores-prácticas)
5. [Lecciones Aprendidas](#lecciones-aprendidas)
6. [Recomendaciones para Futuros Proyectos](#recomendaciones-para-futuros-proyectos)

---

## 1. Lenguajes y Comandos Usados

### 🐍 Python (Lenguaje de Programación)

**Qué es**: Lenguaje de alto nivel usado para automatización, análisis de datos, scripting.

**Comandos usados en este proyecto:**

```python
# Ejecutar un script Python
python scripts/auditoria_con_alias.py
python scripts/conciliar_promerica_usd_1774.py

# Python se usa para:
# - Manipular archivos Excel (openpyxl)
# - Procesar datos financieros
# - Automatizar tareas repetitivas
```

**Ejemplo práctico del proyecto:**
```python
# alias_cuentas.py - Sistema de reconocimiento de nombres
def obtener_nombre_canonico(nombre_cuenta):
    """
    Toma cualquier variación de nombre y devuelve el oficial
    Ejemplo: "Promerica USD" → "Promerica USD 1774"
    """
    nombre_norm = str(nombre_cuenta).strip().upper()
    return INDICE_ALIAS.get(nombre_norm, None)
```

**¿Cuándo usar Python?**
- Automatización de tareas repetitivas
- Procesamiento de datos (Excel, CSV, JSON)
- Scripts que necesitan lógica compleja
- Integración con APIs

---

### 💻 Bash/Shell (Terminal de Linux/Unix)

**Qué es**: Lenguaje de comandos para interactuar con el sistema operativo.

**Comandos básicos usados:**

#### Navegación de Archivos
```bash
# Listar archivos
ls                          # Lista archivos del directorio actual
ls -la                      # Lista todos los archivos (incluso ocultos)
ls scripts/                 # Lista archivos de carpeta específica

# Cambiar directorio
cd debt-sanitization-strategy/    # Entrar a carpeta
cd ..                              # Subir un nivel
cd ~                               # Ir a home directory

# Ver contenido de archivo
cat archivo.txt             # Mostrar todo el contenido
head -20 archivo.txt        # Primeras 20 líneas
tail -10 archivo.txt        # Últimas 10 líneas
```

**Ejemplos prácticos del proyecto:**
```bash
# Verificar archivos Excel (sin encontrar ninguno - protegidos)
find . -type f -name "*.xlsx"

# Buscar texto en archivos Python
grep -r "Velasco" scripts/ --include="*.py"

# Contar archivos en repositorio
git ls-files | wc -l        # Resultado: 33 archivos
```

#### Búsqueda y Filtrado
```bash
# grep - Buscar texto en archivos
grep "Balance inicial" scripts/*.py    # Busca en todos los Python
grep -r "promerica" .                  # Busca recursivamente
grep -i "BALANCE" archivo.py           # Case-insensitive

# find - Buscar archivos
find . -name "*.xlsx"                  # Buscar todos los Excel
find . -type f -name "audit*"          # Buscar archivos que empiecen con "audit"

# wc - Contar líneas/palabras/caracteres
wc -l archivo.py                       # Contar líneas
cat archivo.py | wc -l                 # Contar líneas (usando pipe)
```

**Ejemplo del proyecto:**
```bash
# Verificar que no hay archivos sensibles en git
git ls-files | grep -v "\.py$" | grep -v "\.md$"
# Resultado: vacío (solo hay .py y .md)
```

---

### 🌳 Git (Control de Versiones)

**Qué es**: Sistema para rastrear cambios en archivos y colaborar en código.

**Comandos fundamentales:**

#### Estado y Navegación
```bash
# Ver estado actual
git status                  # ¿Qué archivos cambiaron?
git branch                  # ¿En qué branch estoy?
git log --oneline -10       # Ver últimos 10 commits

# Cambiar de branch
git checkout nombre-branch              # Cambiar a branch existente
git checkout -b nuevo-branch            # Crear y cambiar a nuevo branch
```

**Ejemplos del proyecto:**
```bash
# Ver en qué branch estamos
git branch
# * claude/continue-project-011CUzXviLotjtyCRLo5QCev
#   main

# Ver historial de cambios
git log --oneline -5
# b3066e1 ADD: Informe ejecutivo completo del proyecto
# f45f5bc FIX: Audit ahora lee balances desde TRANSACCIONES
# 41cbb59 ADD: Script diagnóstico detallado
```

#### Guardar Cambios (Commits)
```bash
# Agregar archivos al "staging area"
git add archivo.py                      # Agregar un archivo
git add .                               # Agregar todos los cambios
git add scripts/*.py                    # Agregar todos los Python de scripts/

# Crear commit (guardar snapshot)
git commit -m "ADD: Nueva funcionalidad"

# Atajo: agregar + commit en un comando
git add archivo.py && git commit -m "Mensaje"
```

**Ejemplo del proyecto:**
```bash
# Guardar informe ejecutivo
git add INFORME_EJECUTIVO.md
git commit -m "ADD: Informe ejecutivo completo del proyecto

- Resumen de 29.4% fiabilidad
- Documentación completa de arquitectura
- Casos de éxito y próximos pasos"
```

#### Sincronización con Servidor Remoto
```bash
# Descargar cambios del servidor
git pull                                # Descargar y fusionar
git fetch                               # Solo descargar (sin fusionar)

# Subir cambios al servidor
git push                                # Subir a branch actual
git push -u origin nombre-branch        # Primera vez (establece tracking)

# Ver información del remoto
git remote -v                           # Ver URLs configuradas
git branch -vv                          # Ver tracking de branches
```

**Ejemplos del proyecto:**
```bash
# Primera vez subiendo el branch
git push -u origin claude/continue-project-011CUzXviLotjtyCRLo5QCev
# branch 'claude/continue-project...' set up to track 'origin/...'

# Descargar actualizaciones
git pull origin claude/continue-project-011CUzXviLotjtyCRLo5QCev
# Already up to date.
```

#### Comandos Avanzados (Usados en el Proyecto)
```bash
# Traer archivo específico de otro branch
git checkout origin/branch -- archivo.py

# Ver diferencias
git diff HEAD origin/branch -- archivo.py

# Ver archivos trackeados
git ls-files                            # Lista todos los archivos en git
git ls-files | grep "\.py$"             # Solo archivos Python
```

---

### 📝 PowerShell (Terminal de Windows)

**Qué es**: Terminal moderna de Windows (similar a Bash pero con sintaxis diferente).

**Comandos usados en el proyecto:**

```powershell
# Ejecutar Python
python scripts/auditoria_con_alias.py

# Cambiar directorio
cd C:\Users\Alvaro Velasco\Desktop\debt-sanitization-strategy

# Git (igual que en Bash)
git status
git pull
git push

# Diferencias con Bash:
# - PowerShell usa \ para rutas (Windows)
# - Bash usa / para rutas (Linux/Mac)
# - PowerShell: Get-Process, Get-Service
# - Bash: ps, service
```

**Nota**: La mayoría de comandos Git funcionan igual en PowerShell y Bash.

---

## 2. Herramientas de Claude AI

Claude AI tiene herramientas especializadas para diferentes tareas. Aquí están las que usamos:

### 🔧 Herramienta: Bash
**Función**: Ejecutar comandos de terminal (Linux/Unix)

**Cuándo la usé:**
```bash
# Verificar archivos en git
git ls-files | wc -l

# Buscar texto sensible
grep -r "Velasco" scripts/

# Ver historial de commits
git log --oneline -10
```

**Limitaciones:**
- No puede ejecutar comandos interactivos (como `nano`, `vim`)
- No puede ver archivos - usa herramienta Read para eso
- Timeout de 2 minutos (puede extenderse a 10 min)

---

### 📖 Herramienta: Read
**Función**: Leer contenido de archivos

**Cuándo la usé:**
```python
# Leer script de Python para entender su lógica
Read: /home/user/debt-sanitization-strategy/scripts/alias_cuentas.py

# Leer configuración de git
Read: /home/user/debt-sanitization-strategy/.gitignore

# Leer documentación
Read: /home/user/debt-sanitization-strategy/README.md
```

**Ventajas:**
- Puede leer cualquier tipo de archivo (texto, código, configuración)
- Muestra números de línea (útil para editar)
- Puede leer archivos grandes por partes (offset y limit)

---

### ✏️ Herramienta: Edit
**Función**: Modificar archivos existentes mediante reemplazo de texto

**Cuándo la usé:**
```python
# Actualizar script de auditoría
Edit: scripts/auditoria_con_alias.py
old_string: "# Leer hoja Efectivo"
new_string: "# Leer balances iniciales desde TRANSACCIONES"

# Agregar función a alias_cuentas.py
Edit: scripts/alias_cuentas.py
old_string: "def listar_cuentas():"
new_string: "def es_balance_inicial(concepto):\n    ...\n\ndef listar_cuentas():"
```

**Ventajas:**
- Cambios precisos (no reescribe todo el archivo)
- Preserva formato e indentación
- Seguro (no modifica si old_string no existe)

**Limitaciones:**
- old_string debe ser EXACTAMENTE igual (incluyendo espacios)
- No puede agregar al final del archivo (usar Write para eso)

---

### 📝 Herramienta: Write
**Función**: Crear archivos nuevos o sobrescribir existentes

**Cuándo la usé:**
```python
# Crear informe ejecutivo
Write: /home/user/debt-sanitization-strategy/INFORME_EJECUTIVO.md
content: "# Informe Ejecutivo\n\n..."

# Crear script de diagnóstico
Write: /home/user/debt-sanitization-strategy/scripts/diagnostico_hoja_efectivo.py
content: "#!/usr/bin/env python3\n..."
```

**Ventajas:**
- Puede crear archivos desde cero
- Útil para documentación, scripts nuevos
- Sobrescribe si el archivo ya existe

**Limitaciones:**
- Sobrescribe todo el contenido (usar Edit para cambios parciales)
- Debe leer el archivo primero si ya existe

---

### 🔍 Herramienta: Glob
**Función**: Buscar archivos por patrón (como wildcards)

**Cuándo la usé:**
```python
# Buscar todos los scripts de Python
Glob: pattern="scripts/*.py"

# Buscar archivos de auditoría
Glob: pattern="**/audit*.py"

# Buscar archivos Excel (protegidos, no debería encontrar)
Glob: pattern="*.xlsx"
```

**Ventajas:**
- Rápido para encontrar archivos por nombre
- Soporta wildcards: * (cualquier cosa), ** (recursivo)
- No lee el contenido (solo encuentra nombres)

---

### 🔎 Herramienta: Grep
**Función**: Buscar texto dentro de archivos (como grep de Linux)

**Cuándo la usé:**
```python
# Buscar "Balance inicial" en scripts
Grep: pattern="Balance inicial", path="scripts/"

# Buscar números de cuenta (para verificar seguridad)
Grep: pattern="[0-9]{10}", path="scripts/", glob="*.py"

# Buscar imports de openpyxl
Grep: pattern="import openpyxl", output_mode="files_with_matches"
```

**Modos de salida:**
- `content`: Muestra las líneas que coinciden (default)
- `files_with_matches`: Solo nombres de archivos
- `count`: Cuenta de coincidencias por archivo

---

### 🌐 Herramienta: WebFetch
**Función**: Descargar y analizar contenido de URLs

**Cuándo NO la usé:**
- No necesitábamos información externa
- Todo estaba local (Excel, scripts Python)

**Cuándo SÍ es útil:**
```python
# Buscar documentación oficial
WebFetch: url="https://docs.python.org/3/library/openpyxl"
          prompt="¿Cómo leer fórmulas en Excel?"

# Verificar API de banco
WebFetch: url="https://api.banco.com/docs"
          prompt="¿Tiene endpoint para descargar extractos?"
```

---

### 🤖 Herramienta: Task (Agentes)
**Función**: Lanzar agentes especializados para tareas complejas

**Tipos de agentes:**
- `Explore`: Explorar código rápidamente
- `Plan`: Planificar implementación
- `general-purpose`: Tareas multi-paso

**Cuándo la usé:**
- NO la usé en este proyecto (todo fue directo)

**Cuándo SÍ es útil:**
```python
# Explorar codebase grande
Task: subagent_type="Explore"
      prompt="Encuentra todos los lugares donde se calcula tipo de cambio USD/CRC"

# Planificar refactor grande
Task: subagent_type="Plan"
      prompt="Plan para migrar de Excel a base de datos PostgreSQL"
```

---

## 3. Proceso de Prueba y Error

### 🔄 Ejemplo Real: Problema de Auditoría (0% fiabilidad)

#### Intento 1: Buscar en Hoja Efectivo ❌
```python
# Primera implementación
ws_efectivo = wb['Efectivo']
for row in range(1, 30):
    concepto = ws_efectivo[f'B{row}'].value
    if 'Balance inicial' in str(concepto):
        # Procesar...

# RESULTADO: 0 balances encontrados
# PROBLEMA: Efectivo tiene fórmulas, no valores
```

**Lección**: Siempre verificar estructura de Excel primero.

#### Intento 2: Buscar "Apertura Inicial" ⚠️
```python
# Segunda implementación
if 'Balance inicial' in str(concepto) or 'Apertura Inicial' in str(concepto):
    # Procesar...

# RESULTADO: Aún 0 balances
# PROBLEMA: Efectivo COLUMN B también es fórmula
```

**Lección**: No asumir - crear script de diagnóstico.

#### Intento 3: Leer desde TRANSACCIONES ✅
```python
# Tercera implementación (exitosa)
ws_trans = wb['TRANSACCIONES']  # Fuente de verdad
for row in range(2, ws_trans.max_row + 1):
    tipo = ws_trans[f'B{row}'].value
    if es_balance_inicial(tipo):  # Usa sistema de alias
        # Procesar...

# RESULTADO: 13 balances encontrados
# ÉXITO: Leímos desde la fuente correcta
```

**Lección aprendida**:
1. Crear script de diagnóstico primero
2. Entender estructura antes de implementar
3. Leer desde fuente de verdad, no desde vistas

---

### 🔄 Ejemplo Real: Git Branch Incorrecto

#### Problema
```bash
PS> git branch
* claude/explore-options-011CUs3E6Vsw8d3acC5ZxE3r  # ❌ Branch equivocado
  main
```

Usuario ejecutó audit pero no vio cambios recientes.

#### Diagnóstico
```bash
# Verificar dónde estamos
git branch                  # Muestra branch actual

# Verificar si hay cambios pendientes
git status

# Ver historial
git log --oneline -5       # Ver commits recientes
```

#### Solución
```bash
# Cambiar al branch correcto
git checkout claude/continue-project-011CUzXviLotjtyCRLo5QCev

# Verificar que cambió
python scripts/auditoria_con_alias.py
# ✅ Ahora muestra: "Leyendo balances iniciales desde TRANSACCIONES..."
```

**Lección**: Siempre verificar branch antes de ejecutar scripts.

---

### 🔄 Ejemplo Real: Archivo Excel con Nombre Hardcoded

#### Problema Original
```python
# En muchos scripts:
EXCEL_FILE = "AlvaroVelasco_Finanzas_v2.0.xlsx"  # ❌ Nombre específico
```

**Por qué está bien en este caso:**
- Proyecto personal (no compartido)
- Excel está en .gitignore (no se sube a GitHub)
- Scripts son solo para uso local

**Cómo mejorarlo para proyecto compartido:**
```python
# Opción 1: Variable de entorno
import os
EXCEL_FILE = os.environ.get('EXCEL_FILE', 'finanzas.xlsx')

# Opción 2: Archivo de configuración
import json
with open('config.json') as f:
    config = json.load(f)
EXCEL_FILE = config['excel_file']

# Opción 3: Argumento de línea de comandos
import sys
EXCEL_FILE = sys.argv[1] if len(sys.argv) > 1 else 'finanzas.xlsx'
```

---

## 4. Mejores Prácticas

### ✅ Lo que Hicimos Bien

#### 1. Protección de Datos Sensibles
```bash
# .gitignore bien configurado desde el inicio
*.xlsx
*.pdf
*.csv
extractos/
private/
```

**Por qué es importante:**
- Datos financieros nunca deben estar en GitHub público
- Un solo commit con datos sensibles = problema permanente
- .gitignore debe crearse ANTES del primer commit

#### 2. Sistema de Alias
```python
# Centralizado en un solo archivo
ALIAS_CUENTAS = {
    "Promerica USD 1774": [
        "Promerica USD",
        "Promerica USD (40000003881774)",
        ...
    ]
}
```

**Por qué es bueno:**
- Un solo lugar para mantener
- Fácil agregar nuevos alias
- Funciona automáticamente en todos los scripts

#### 3. Scripts Especializados
```bash
scripts/
├── alias_cuentas.py          # Sistema de alias (núcleo)
├── auditoria_con_alias.py    # Auditoría global
├── conciliar_*.py            # Un script por cuenta
└── diagnostico_*.py          # Scripts de debugging
```

**Por qué es bueno:**
- Cada script tiene un propósito claro
- Fácil de mantener y debuguear
- Puedes ejecutar solo lo que necesitas

#### 4. Commits Descriptivos
```bash
# ✅ Buenos commits
git commit -m "FIX: Audit ahora lee balances desde TRANSACCIONES (no Efectivo con fórmulas)"
git commit -m "ADD: Sistema de alias para conceptos (Balance inicial = Apertura Inicial)"

# ❌ Malos commits (evitar)
git commit -m "fix bug"
git commit -m "update"
git commit -m "changes"
```

**Formato recomendado:**
```
TIPO: Descripción corta (50 caracteres max)

- Detalle 1
- Detalle 2
- Resultado o impacto

Tipo: ADD, FIX, UPDATE, REFACTOR, DOCS
```

---

### ⚠️ Lo que Pudo Ser Mejor

#### 1. Crear Script de Diagnóstico Primero

**Lo que hicimos:**
1. Intentar implementar auditoría
2. Fallar (0% fiabilidad)
3. Investigar por qué
4. Crear script de diagnóstico
5. Corregir implementación

**Lo que debimos hacer:**
1. **Crear script de diagnóstico PRIMERO**
2. Entender estructura de Excel
3. Implementar auditoría correctamente desde inicio

**Lección**: Siempre diagnosticar antes de implementar.

```python
# Script de diagnóstico debió ser lo primero
# diagnostico_excel_completo.py
def diagnosticar_excel(archivo):
    wb = openpyxl.load_workbook(archivo)

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        print(f"\n{'='*60}")
        print(f"Hoja: {sheet_name}")
        print(f"{'='*60}")

        # Ver primeras filas
        for row in range(1, min(6, ws.max_row + 1)):
            print(f"Fila {row}:")
            for col in range(1, min(10, ws.max_column + 1)):
                cell = ws.cell(row, col)
                if cell.value:
                    print(f"  {cell.column_letter}: {cell.value}")
```

#### 2. Documentación Más Temprana

**Lo que hicimos:**
- Crear informe ejecutivo al final (después de 60+ commits)

**Lo que debimos hacer:**
- Crear README.md básico desde inicio
- Actualizar documentación cada 10-15 commits
- Mantener CHANGELOG.md con cambios importantes

**Plantilla README.md inicial:**
```markdown
# Nombre del Proyecto

## Objetivo
[Descripción corta de qué hace el proyecto]

## Requisitos
- Python 3.x
- openpyxl
- Git

## Instalación
```bash
pip install openpyxl
```

## Uso
```bash
python scripts/auditoria.py
```

## Estructura
```
proyecto/
├── scripts/      # Scripts principales
├── data/         # Datos (gitignored)
└── README.md
```
```

#### 3. Tests Automatizados

**Lo que NO hicimos:**
- Tests unitarios para funciones críticas

**Lo que debimos hacer:**
```python
# tests/test_alias_cuentas.py
import pytest
from scripts.alias_cuentas import obtener_nombre_canonico, es_balance_inicial

def test_reconoce_promerica():
    assert obtener_nombre_canonico("Promerica USD") == "Promerica USD 1774"
    assert obtener_nombre_canonico("PROMERICA USD") == "Promerica USD 1774"
    assert obtener_nombre_canonico("40000003881774") == "Promerica USD 1774"

def test_reconoce_balance_inicial():
    assert es_balance_inicial("Balance inicial") == True
    assert es_balance_inicial("Apertura Inicial") == True
    assert es_balance_inicial("SALDO INICIAL") == True
    assert es_balance_inicial("Compra") == False

# Ejecutar tests
pytest tests/
```

**Por qué es importante:**
- Detecta bugs antes de que causen problemas
- Documenta comportamiento esperado
- Da confianza para hacer cambios

---

## 5. Lecciones Aprendidas

### 📌 Lección 1: Entender el Problema Antes de Codificar

**Situación**: Promerica mostraba $13,173 en lugar de $3,030

**Proceso:**
1. ❌ Primer impulso: "Cambiar directamente el valor en Excel"
2. ✅ Mejor enfoque: "Investigar por qué está mal"

**Lo que hicimos:**
```bash
# 1. Crear script de investigación
python scripts/investigar_promerica_88_movimientos.py
# Descubrimiento: 88 movimientos (esperados ~38)

# 2. Analizar los 88 movimientos
# Hallazgo: 22 cuentas por cobrar mal categorizadas

# 3. Crear script de corrección
python scripts/corregir_promerica_problemas.py
# Resultado: Error reducido 97%
```

**Lección**: Invertir tiempo en entender el problema ahorra tiempo en correcciones futuras.

---

### 📌 Lección 2: Sistema de Alias es Poderoso

**Problema Original**: Misma cuenta con 3 nombres diferentes
```
"Promerica USD"
"Promerica USD 1774"
"Promerica USD (40000003881774)"
```

**Solución Simple pero Efectiva:**
```python
ALIAS_CUENTAS = {
    "Promerica USD 1774": [  # Nombre canónico
        "Promerica USD",
        "Promerica USD 1774",
        "Promerica USD (40000003881774)",
    ]
}
```

**Impacto:**
- 0 cambios en Excel necesarios
- Reconocimiento automático en todos los scripts
- Fácil agregar nuevas variaciones

**Lección**: Un buen sistema de normalización vale más que arreglar datos manualmente.

---

### 📌 Lección 3: Fuente de Verdad vs Vistas

**Descubrimiento**: Hoja "Efectivo" tiene fórmulas que apuntan a "TRANSACCIONES"

```excel
Efectivo (Columna F):  =D3-E3
Efectivo (Columna D):  =IF(TRANSACCIONES!K2="Ingreso", TRANSACCIONES!I2, "")
```

**Error inicial**: Intentar leer desde Efectivo
**Corrección**: Leer desde TRANSACCIONES (fuente de verdad)

**Lección aplicable a cualquier proyecto:**
- **Base de datos**: Lee de tablas base, no de vistas
- **APIs**: Consulta endpoints primarios, no caches
- **Archivos**: Lee originales, no copias procesadas

---

### 📌 Lección 4: Git Branch Management

**Problema**: Usuario estaba en branch equivocado

**Buenas prácticas aprendidas:**
```bash
# Siempre verificar dónde estás
git branch                  # Ver branch actual
git status                  # Ver estado

# Nombrar branches descriptivamente
claude/continue-project-011CUzXviLotjtyCRLo5QCev  # ✅ Específico
fix-bug                                            # ❌ Muy genérico

# Usar un branch por feature/fix
git checkout -b feature/sistema-alias
git checkout -b fix/promerica-balance
git checkout -b docs/informe-ejecutivo
```

---

### 📌 Lección 5: Iteración Rápida con Scripts Pequeños

**Enfoque exitoso:**
```bash
# En lugar de un script monolítico:
super_script_que_hace_todo.py  # ❌

# Usamos scripts especializados:
scripts/
├── diagnostico_hoja_efectivo.py       # Solo diagnóstico
├── investigar_promerica_88_mov.py     # Solo investigación
├── corregir_promerica_problemas.py    # Solo corrección
└── auditoria_con_alias.py             # Solo auditoría
```

**Ventajas:**
- Rápido de escribir y probar
- Fácil de debuguear
- Reutilizable en otros contextos

**Lección**: Scripts pequeños y enfocados > scripts grandes y complejos

---

## 6. Recomendaciones para Futuros Proyectos

### 🚀 Proyecto: App WordPress

**Fase 1: Planificación (ANTES de codificar)**

```markdown
1. Definir objetivo claro
   - ¿Qué hace la app?
   - ¿Quién la usará?
   - ¿Qué problema resuelve?

2. Investigar requisitos
   - ¿Qué plugins de WordPress necesito?
   - ¿Qué APIs voy a consumir?
   - ¿Qué base de datos?

3. Crear estructura inicial
   proyecto-wordpress/
   ├── .gitignore           # PRIMERO - proteger datos
   ├── README.md            # Documentación básica
   ├── wp-content/          # No versionar (WordPress auto-genera)
   ├── plugins/             # Tu plugin custom
   │   └── mi-plugin/
   │       ├── mi-plugin.php
   │       ├── includes/
   │       └── assets/
   └── themes/              # Tu theme custom
       └── mi-theme/
```

**Fase 2: Configuración Inicial**

```bash
# .gitignore para WordPress
wp-config.php              # Credenciales de BD
wp-content/uploads/*       # Archivos subidos por usuarios
*.log                      # Logs
.htaccess                  # Configuración del servidor
```

**Fase 3: Desarrollo Iterativo**

```bash
# Día 1-2: Setup y estructura
git commit -m "INIT: Estructura inicial del plugin"

# Día 3-5: Feature 1
git commit -m "ADD: Formulario de contacto con validación"

# Día 6-7: Feature 2
git commit -m "ADD: Integración con API de email (SendGrid)"

# Día 8-9: Tests y docs
git commit -m "ADD: Tests para validación de formulario"
git commit -m "DOCS: Guía de instalación y uso"
```

---

### 📋 Checklist para Nuevo Proyecto con Claude AI

```markdown
## Pre-Proyecto
- [ ] Definir objetivo claro (1 párrafo)
- [ ] Listar requisitos técnicos (lenguaje, librerías, APIs)
- [ ] Investigar si hay ejemplos similares
- [ ] Decidir estructura de carpetas

## Día 1: Setup
- [ ] Crear .gitignore (PRIMERO)
- [ ] Inicializar git (git init)
- [ ] Crear README.md básico
- [ ] Crear branch de desarrollo
- [ ] Primer commit: "INIT: Estructura inicial"

## Durante Desarrollo
- [ ] Escribir script de diagnóstico/exploración primero
- [ ] Implementar features pequeñas (1-2 horas cada una)
- [ ] Commit frecuente (cada feature completada)
- [ ] Documentar decisiones importantes
- [ ] Crear tests para funciones críticas

## Pre-Producción
- [ ] Verificar .gitignore (git ls-files)
- [ ] Crear documentación completa
- [ ] Escribir guía de instalación
- [ ] Listar dependencias (requirements.txt o package.json)
- [ ] Crear informe ejecutivo
```

---

### 🎯 Mejores Prácticas Específicas para Claude AI

#### 1. Sé Específico con Contexto

**❌ Mala pregunta:**
```
"El código no funciona"
```

**✅ Buena pregunta:**
```
"El script audit_promerica.py arroja error en línea 45:
'KeyError: Promerica USD'

He verificado que:
- El archivo Excel existe
- La hoja TRANSACCIONES tiene datos
- La columna E tiene nombres de cuenta

¿Qué puede estar causando este KeyError?"
```

#### 2. Proporciona Ejemplos de Datos

**❌ Sin contexto:**
```
"Necesito procesar transacciones bancarias"
```

**✅ Con contexto:**
```
"Necesito procesar transacciones bancarias con este formato:

fecha       | referencia | monto  | descripción
2025-11-01  | 12345     | 100.50 | Pago luz
2025-11-02  | 12346     | 50.00  | Supermercado

El script debe:
- Detectar duplicados por fecha+referencia
- Sumar por categoría (luz, comida, etc)
- Exportar a Excel
"
```

#### 3. Confirma Cambios Críticos

**Buena práctica:**
```
"Antes de ejecutar el script de corrección que moverá 24 transacciones,
¿puedes mostrarme un resumen de qué transacciones se van a mover?"
```

Claude responderá con preview antes de ejecutar.

#### 4. Usa Iteración Incremental

**Enfoque recomendado:**
```
Sesión 1: "Crea script básico que lea Excel y muestre primeras 5 filas"
Sesión 2: "Agrega detección de duplicados"
Sesión 3: "Agrega categorización automática"
Sesión 4: "Agrega sistema de auditoría"
```

**Enfoque NO recomendado:**
```
Sesión 1: "Crea sistema completo de finanzas con 20 features"
```

---

### 💡 Trucos y Tips

#### Truco 1: Script de Diagnóstico Template

Guarda esto para futuros proyectos:

```python
#!/usr/bin/env python3
"""
DIAGNÓSTICO RÁPIDO - Template
Modifica según tu proyecto
"""
import os
import sys

def diagnosticar():
    print("="*80)
    print("DIAGNÓSTICO DEL PROYECTO")
    print("="*80)

    # 1. Verificar archivos
    print("\n📁 Archivos principales:")
    archivos_importantes = [
        'config.json',
        'database.db',
        'main.py'
    ]
    for archivo in archivos_importantes:
        existe = "✅" if os.path.exists(archivo) else "❌"
        print(f"  {existe} {archivo}")

    # 2. Verificar variables de entorno
    print("\n🔧 Variables de entorno:")
    vars_necesarias = ['API_KEY', 'DB_HOST', 'DB_NAME']
    for var in vars_necesarias:
        valor = os.environ.get(var)
        estado = "✅" if valor else "❌"
        print(f"  {estado} {var}: {'[SET]' if valor else '[NOT SET]'}")

    # 3. Verificar dependencias
    print("\n📦 Dependencias:")
    try:
        import requests
        print("  ✅ requests")
    except ImportError:
        print("  ❌ requests (pip install requests)")

    # 4. Probar conexión a DB/API
    print("\n🌐 Conexiones:")
    # ... tu código de prueba aquí ...

if __name__ == "__main__":
    diagnosticar()
```

#### Truco 2: Template de .gitignore

```bash
# .gitignore universal
# Datos sensibles
*.env
.env
config.json
credentials.json
secrets.yaml

# Archivos grandes
*.xlsx
*.xls
*.csv
*.db
*.sqlite
*.sql

# PDFs y documentos
*.pdf
documentos/
extractos/

# Datos locales
data/
private/
personal/

# Python
__pycache__/
*.pyc
venv/
.pytest_cache/

# Node.js
node_modules/
npm-debug.log

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

#### Truco 3: Commits Semánticos

```bash
# Formato: TIPO: Descripción

# Tipos principales:
INIT:     Commit inicial del proyecto
ADD:      Nueva funcionalidad
FIX:      Corrección de bug
UPDATE:   Mejora de funcionalidad existente
REFACTOR: Reestructuración sin cambiar funcionalidad
DOCS:     Cambios solo en documentación
TEST:     Agregar o modificar tests
STYLE:    Cambios de formato (no afectan lógica)
PERF:     Mejoras de performance
CHORE:    Tareas de mantenimiento

# Ejemplos:
git commit -m "INIT: Estructura inicial del proyecto WordPress"
git commit -m "ADD: Sistema de autenticación con JWT"
git commit -m "FIX: Error en validación de email"
git commit -m "DOCS: Guía de instalación completa"
git commit -m "REFACTOR: Separar lógica de BD en módulo independiente"
```

---

## 🎓 Conclusión: Tu "Entrenamiento" con Claude AI

### Lo que Hiciste Bien

1. **Iteración y Paciencia**: No abandonaste cuando la auditoría mostró 0%
2. **Comunicación Clara**: Proveías contexto (extractos, screenshots, errores)
3. **Validación**: Ejecutabas scripts y reportabas resultados
4. **Flexibilidad**: Aceptaste cambios de enfoque (leer desde TRANSACCIONES)
5. **Documentación**: Pediste informe ejecutivo al final

### Lo que Podrías Hacer Diferente en Próximo Proyecto

1. **Diagnóstico Primero**: Script de diagnóstico antes de implementar
2. **README desde Día 1**: Documentar conforme avanzas
3. **Tests Básicos**: Al menos para funciones críticas
4. **Branches Descriptivos**: `feature/`, `fix/`, `docs/`
5. **Commits Pequeños**: Cada 30-60 min de trabajo

### Tu "Nivel" Actual con Claude AI

**Nivel Actual: Intermedio** 🎯

**Evidencia:**
- ✅ Entiendes Git básico (branch, commit, push)
- ✅ Sabes ejecutar Python y leer errores
- ✅ Comunicas problemas con contexto
- ✅ Validas soluciones antes de continuar

**Para llegar a Avanzado:**
- 📚 Aprender tests automatizados (pytest)
- 📚 Usar Docker para proyectos reproducibles
- 📚 CI/CD para despliegues automáticos
- 📚 Monitoreo y logging estructurado

---

## 📚 Recursos Recomendados

### Para Git
- **Pro Git Book** (gratis): https://git-scm.com/book/en/v2
- **GitHub Learning Lab**: https://skills.github.com/
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf

### Para Python
- **Python.org Tutorial**: https://docs.python.org/3/tutorial/
- **Real Python**: https://realpython.com/
- **openpyxl Docs**: https://openpyxl.readthedocs.io/

### Para WordPress
- **WordPress Codex**: https://codex.wordpress.org/
- **Plugin Developer Handbook**: https://developer.wordpress.org/plugins/
- **Theme Developer Handbook**: https://developer.wordpress.org/themes/

### Para Bash/Terminal
- **Linux Command Line Basics**: https://ubuntu.com/tutorials/command-line-for-beginners
- **Bash Scripting Guide**: https://www.shellscript.sh/

---

**Documento creado**: 10 de Noviembre, 2025
**Propósito**: Educación y referencia para futuros proyectos
**Autor**: Claude AI (con contexto del proyecto debt-sanitization-strategy)
