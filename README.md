# Automatización OPS

Sistema de automatización para procesos transaccionales bancarios: valida, consolida y
depura archivos operativos a gran escala, reemplazando un proceso que antes se hacía a mano.

## Qué resuelve

En un banco, los archivos operativos que respaldan transacciones (cargos, abonos, ajustes
contables) llegan en formatos de ancho fijo con reglas estrictas de estructura. Validarlos y
consolidarlos a mano es lento y propenso a error humano — un campo mal alineado o un duplicado
no detectado puede significar una conciliación contable incorrecta.

Este proyecto automatiza tres etapas de ese flujo:

- **Prevalidador** — valida la estructura de los archivos de entrada antes de procesarlos:
  longitud de campos, tipos de dato, columnas ancla, columnas obligatorias no vacías.
- **Validador** — reglas de negocio sobre los datos ya estructurados: justificación contable,
  cuentas de contrapartida, formato de documento y dígito de verificación.
- **Consolidación e histórico** — unifica archivos de cargos y abonos, depura duplicados y
  mantiene un histórico por ventana móvil en vez de acumular todo indefinidamente.

## Stack

Python (pandas, openpyxl, python-docx) + VBA para la integración con Excel. Interfaz de
escritorio simple con PySimpleGUI para quien no vaya a correrlo por consola.

## Estructura

```
Prevalidador/   validación de estructura de archivos de entrada
Validador/      reglas de negocio y validaciones contables
  Consolidacion/       unificación de cargos y abonos
  Historico_resumen/   depuración de históricos por ventana móvil
  estructuras_base/    plantillas de referencia
```

## Estado

Proyecto activo en el trabajo diario, sin movimiento reciente en este repo mientras se prepara
para ser público. En proceso de sanitización: se removieron archivos con datos reales de
operaciones antes de este README.

---

Parte de mi portfolio — más contexto en [mi perfil](https://github.com/DavidCanon07).
