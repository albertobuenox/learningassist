---
tags:
  - agentes
  - leccion
  - medio
---

# 06 — Una rebanada

!!! info "Antes de empezar"

    Tiempo: 60 minutos. Fuente: la sección de verificación en https://code.claude.com/docs/en/best-practices

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## Encargo

Una sola conducta, la que ya sabes probar. Ejemplo: un importe vacío no entra en el total. El mensaje incluye el caso (entrada y salida) y el comando del test, si existe. Si no existe, la primera rebanada es escribir ese test, no “arreglar las facturas”.

Prohibido en el mismo mensaje: renombrar, cambiar el estilo, añadir una librería, “ya que estás”.

Cuando termine, mira el diff antes de leer el resumen.

## Segunda rebanada, en otra conversación

Una conducta distinta (el importe negativo, o el 400 del `POST`). Conversación nueva, no un “ahora también”. Así ves qué contexto hace falta de verdad y qué era residuo de la charla anterior.

!!! success "Cómo sabes que está bien"

    - El diff de la primera rebanada se explica con una frase que coincide con el encargo. Si necesitas tres frases, entró trabajo de más.
    - El test, o el `curl`, lo ejecutas tú. El “all tests passed” del agente no cierra la lección.
    - La segunda conversación acertó el archivo sin que le pegaras el diff anterior. Si no acertó, ¿qué ruta mínima tendrías que haber dado?
