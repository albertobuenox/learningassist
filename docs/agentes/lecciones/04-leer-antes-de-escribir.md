---
tags:
  - agentes
  - corto
  - leccion
---

# 04 — Leer antes de escribir

!!! info "Antes de empezar"

    Tiempo: 45 minutos.

    Fuente de los nombres en Cursor: https://cursor.com/help/ai-features/agent

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## Cómo forzar solo lectura

=== "Cursor"

    Usa el modo **Ask**. No pases a Agent hasta cerrar la lección.

=== "Claude Code"

    En el primer mensaje, prohíbe editar: solo lectura. Si edita, reviértelo y repite la orden.

=== "Chat"

    No hay otra opción: el chat ya es solo lectura. Esta lección es el modo normal.

## Encargo

Sobre un proyecto que no hayas escrito tú esta semana (un ejercicio antiguo, o un ejemplo del manual):

> Dime qué función decide el total y qué pasaría si el importe viene vacío. No modifiques archivos. No propongas un refactor.

## Qué comprobar

- El estado de git antes y después (`git status`). Tiene que ser el mismo. Si apareció un archivo, el modo no era de lectura: reviértelo.
- La respuesta cita un archivo y una función que existen. Ábrelos. Si la cita no está, márcala como inventada.
- Pregunta de seguimiento, en la misma conversación: “¿y el otro archivo?”. Si no hay otro archivo relevante, el agente debería decirlo. Anota si se inventa uno para complacerte.

!!! success "Cómo sabes que está bien"

    - Sabes en qué control de la herramienta se prohíbe editar, sin buscarlo.
    - Distingues “ha leído el código” de “ha escrito un ensayo plausible”. La prueba es una línea que tú encuentras en el archivo, no el tono seguro de la respuesta.
    - Decides una tarea de las tuyas que, a partir de ahora, empieza en lectura. Escríbela en una frase. Si todas te salen “de implementación”, estás saltándote esta lección.
