---
name: ethazi-off
description: >-
  Desactiva las reglas ETHAZI del proyecto poniendo alwaysApply en false en
  .cursor/rules/ethazi-*.mdc. Usar solo cuando el usuario invoca /ethazi-off.
disable-model-invocation: true
---

# /ethazi-off

El usuario ya pidió este cambio. Ejecútalo. No lo conviertas en un reto. No toques el subagente @socrates ni otras reglas.

1. Desde la raíz del repositorio, ejecuta:

```bash
python3 .cursor/scripts/ethazi-toggle.py off
```

2. No edites el cuerpo de las reglas. El script solo cambia `alwaysApply` en el frontmatter de `.cursor/rules/ethazi-*.mdc`.
3. Responde con la salida del script y di que ETHAZI queda inactivo en los mensajes siguientes. Si este chat ya tenía las reglas cargadas, indica que hace falta un chat nuevo para que dejen de aplicarse aquí.
