---
tags:
  - agentes
  - leccion
  - medio
---

# 03 — El contexto

!!! info "Antes de empezar"

    Tiempo: 60 minutos. Glosario: [contexto](../glosario.md#contexto), [ventana de contexto](../glosario.md#ventana-de-contexto).

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## Dos intentos

Misma pregunta: “¿por qué este caso falla?”. Tú ya sabes la respuesta, o la acabas de provocar.

1. Primer mensaje: pega el error de verdad (el traceback o la frase del test) y el nombre del archivo. Nada más.
2. Conversación nueva: pega el error, tres archivos que no vienen a cuento y un README entero.

No mires el segundo hasta haber anotado qué tendría que leer alguien para responder.

## Qué anotar

- En cuál supo antes de qué archivo se hablaba.
- Qué pieza de contexto fue la que permitió acertar, si acertó.
- Qué pieza podía haber borrado sin cambiar la respuesta. Esa pieza, en un agente, también gasta ventana y empuja fuera el criterio de hecho.

=== "Chat"

    Solo puedes pegar. Elige bien qué entra: el error y el mínimo de código.

=== "Agente (Cursor / Claude Code)"

    Repite el primer intento sin pegar el archivo: dale la ruta y el error, y deja que lo lea. Compara con el pegado a mano. ¿El resultado cambia, o solo cambia quién seleccionó el texto?

!!! warning "Restricciones"

    - No subas secretos, `.env` ni volcados de producción para “dar contexto”.
    - No abras una tercera conversación “con todo el repo” para desempatar. Si los dos fallan, el fallo es la pregunta, y vuelves a la lección 2.

!!! success "Cómo sabes que está bien"

    - Tienes una lista de tres cosas que a partir de ahora no pegas por defecto.
    - Puedes decir qué se pierde cuando la conversación es tan larga que el principio se resume. ¿Tu criterio de hecho sobreviviría a ese resumen?
