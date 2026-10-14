---
name: ethazi-on
description: >-
  Activa las reglas ETHAZI del proyecto poniendo alwaysApply en true en
  .cursor/rules/ethazi-*.mdc. Usar solo cuando el usuario invoca /ethazi-on.
disable-model-invocation: true
---

# /ethazi-on

El usuario ya pidió este cambio. Ejecútalo. No lo conviertas en un reto.

1. Desde la raíz del repositorio, ejecuta:

```bash
python3 .cursor/scripts/ethazi-toggle.py on
```

2. No edites el cuerpo de las reglas. El script solo cambia `alwaysApply` en el frontmatter de `.cursor/rules/ethazi-*.mdc`.
3. Responde con la salida del script y di que ETHAZI queda activo. Si este chat se abrió con las reglas apagadas, indica que hace falta un chat nuevo para que entren.
