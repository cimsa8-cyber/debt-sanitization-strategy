# Sistema de Alias para Normalización de Cuentas

## 📋 Problema que Resuelve

Cuando importas datos de diferentes fuentes (XML, PDF, extractos bancarios, facturas), los nombres de las cuentas bancarias aparecen con variaciones debido al enmascaramiento de seguridad:

- `Promerica USD (40000003881774)`
- `Promerica USD`
- `Promerica USD 1774`
- `Promerica USD (*1774)`

Esto causa que las fórmulas SUMIFS en la hoja **Efectivo** no capturen todas las transacciones, resultando en saldos incorrectos.

## ✅ Solución: Sistema de Alias Universal

### Componentes

1. **Hoja CUENTAS_ALIAS**: Tabla de mapeo que define el nombre estándar y sus alias
2. **Script de Normalización Universal**: Lee la tabla y unifica todos los nombres automáticamente

### Estructura de la Hoja CUENTAS_ALIAS

| Cuenta Estándar | Alias 1 | Alias 2 | Alias 3 | Alias 4 | Alias 5 | Notas |
|----------------|---------|---------|---------|---------|---------|-------|
| Promerica USD (40000003881774) | Promerica USD | Promerica USD 1774 | Promerica USD (*1774) | Promerica 1774 | | Cuenta corriente dólares |
| Tarjeta BNCR Visa 3519 | BNCR 3519 | Tarjeta BNCR | BNCR Visa *3519 | Visa 3519 | BNCR ****3519 | Tarjeta crédito BNCR |

## 🚀 Uso

### Paso 1: Crear la Hoja CUENTAS_ALIAS (Solo Primera Vez)

```powershell
python scripts/crear_hoja_alias_cuentas.py
```

Esto crea la hoja **CUENTAS_ALIAS** con 8 cuentas pre-configuradas:
- Promerica USD / CRC
- BNCR USD / CRC
- Tarjeta BNCR Visa 3519
- Efectivo
- Cuentas por Cobrar
- Pasivos

### Paso 2: Normalizar Todas las Cuentas

```powershell
python scripts/normalizar_cuentas_universal.py
```

El script:
1. ✅ Lee el mapeo de alias desde **CUENTAS_ALIAS**
2. ✅ Busca todas las variaciones en **TRANSACCIONES**
3. ✅ Reemplaza los alias por el nombre estándar
4. ✅ Reporta cuentas sin mapeo que necesitas agregar

### Paso 3: Agregar Nuevos Alias (Cuando Aparezcan)

Cuando importes datos y aparezca una nueva variación:

1. Abre el Excel
2. Ve a la hoja **CUENTAS_ALIAS**
3. Busca la cuenta estándar correspondiente
4. Agrega el nuevo alias en una columna **Alias** disponible
5. Guarda el Excel
6. Vuelve a ejecutar: `python scripts/normalizar_cuentas_universal.py`

**Ejemplo:**

Si aparece `"Promerica *774"`, agrégalo como **Alias 5** en la fila de `Promerica USD (40000003881774)`.

### Paso 4: Agregar Nueva Cuenta (Opcional)

Si obtienes una cuenta completamente nueva:

1. Abre **CUENTAS_ALIAS**
2. Agrega nueva fila:
   - **Cuenta Estándar**: Nombre oficial completo
   - **Alias 1-5**: Variaciones conocidas
   - **Notas**: Descripción de la cuenta
3. Guarda y ejecuta el script de normalización

## 📊 Ventajas

✅ **Escalable**: Funciona para todas las cuentas (bancarias, tarjetas, efectivo)
✅ **Mantenible**: Solo agregas alias nuevos cuando aparecen
✅ **Automático**: Un solo comando normaliza todo
✅ **Seguro**: Crea backup antes de cada ejecución
✅ **Auditable**: Reporta qué cambios realizó

## 🔄 Flujo de Trabajo Recomendado

### Importación Manual (Futuro)

Cuando tú mismo importes datos:

1. Agregar transacciones manualmente en Excel
2. Seleccionar cuenta desde lista desplegable (evita errores de tipeo)
3. No necesitarás normalización porque elegiste el nombre estándar

### Importación Automática (Ahora)

Cuando scripts importen datos automáticamente:

1. Script agrega transacciones con nombres como aparecen en la fuente
2. Ejecutas: `python scripts/normalizar_cuentas_universal.py`
3. El script unifica todos los nombres según **CUENTAS_ALIAS**
4. Verificas saldos en hoja **Efectivo**

## 🛠️ Mantenimiento

### Cada Vez que Importes Datos

```powershell
python scripts/normalizar_cuentas_universal.py
```

### Si el Script Reporta "Cuentas SIN MAPEO"

1. Identifica a qué cuenta estándar pertenece
2. Agrégala a **CUENTAS_ALIAS**
3. Vuelve a ejecutar el script

### Si Cambias el Nombre Estándar de una Cuenta

1. Actualiza la columna **Cuenta Estándar** en **CUENTAS_ALIAS**
2. Ejecuta el script de normalización
3. Todas las transacciones se actualizarán automáticamente

## 📝 Ejemplo Completo

### Situación Inicial

Tienes 80 transacciones de Promerica con 4 variaciones de nombre:
- 16 con `Promerica USD (40000003881774)`
- 25 con `Promerica USD`
- 38 con `Promerica USD 1774`
- 1 con `Promerica CRC (10000003881708)` (cuenta diferente)

**Problema**: SUMIFS en hoja Efectivo solo suma 16 transacciones.

### Solución

1. Ejecutar: `python scripts/crear_hoja_alias_cuentas.py` (solo primera vez)
2. Ejecutar: `python scripts/normalizar_cuentas_universal.py`
3. **Resultado**: 79 transacciones con nombre unificado `Promerica USD (40000003881774)`
4. SUMIFS ahora suma las 79 transacciones correctamente

## 🎯 Mejores Prácticas

1. **Nombre Estándar**: Usa el nombre más completo (incluye número de cuenta completo)
2. **Alias Descriptivos**: Incluye todas las variaciones que hayas visto
3. **Documentar**: Usa columna **Notas** para describir la cuenta
4. **Backup**: El script crea backup automático, pero ten tus propios backups
5. **Probar**: Después de normalizar, verifica saldos en hoja **Efectivo**

## 🔍 Troubleshooting

### "La hoja CUENTAS_ALIAS no existe"
**Solución**: Ejecuta primero `python scripts/crear_hoja_alias_cuentas.py`

### "Cuentas SIN MAPEO detectadas"
**Solución**: Agrega esas cuentas/alias a la hoja CUENTAS_ALIAS y vuelve a ejecutar

### "Saldo no coincide después de normalizar"
**Posibles causas**:
1. Faltan transacciones por registrar
2. Saldo inicial incorrecto
3. Transacciones duplicadas
4. Transacciones de otra cuenta mezcladas

**Solución**: Ejecuta script de diagnóstico para investigar

## 📚 Scripts Relacionados

- `crear_hoja_alias_cuentas.py`: Crea la hoja CUENTAS_ALIAS (solo primera vez)
- `normalizar_cuentas_universal.py`: Normaliza todas las cuentas según mapeo
- `diagnosticar_variaciones_promerica.py`: Diagnostica variaciones de una cuenta específica
- `normalizar_nombres_promerica.py`: Normalización específica de Promerica (legacy)

## 🆘 Soporte

Si encuentras una situación no cubierta:
1. Ejecuta el script de normalización con `-v` (verbose) si está disponible
2. Revisa el backup creado antes de la normalización
3. Documenta el caso para agregarlo como mejora futura
