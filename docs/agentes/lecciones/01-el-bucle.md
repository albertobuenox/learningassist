---
tags:
  - agentes
  - corto
  - leccion
---

# 01 — El bucle

!!! info "Antes de empezar"

    Tiempo: 45 minutos.

    Glosario: [chat](../glosario.md#chat), [agente](../glosario.md#agente), [herramienta](../glosario.md#herramienta), [bucle](../glosario.md#bucle).

??? tip "Pista"

    Todavía no leas el artículo largo de Anthropic. Esta lección es ver el bucle, no adoptar una arquitectura.

## Qué hacer

Elige una función pequeña que ya entiendas (el total de unas facturas, un filtro de una lista). En dos sitios distintos, pide lo mismo: “explica qué hace y señala el caso del importe vacío”, o el caso que tú conozcas.

=== "Chat"

    Pega solo la función. No pegues el repo. El chat no tiene herramientas: solo ve lo que tú pegas.

=== "Agente (Cursor / Claude Code)"

    Indica el archivo y pide que no lo modifique: que lo lea y responda. Observa si la interfaz muestra la herramienta (lectura, búsqueda).

Anota, en una tabla de cuatro filas:

- qué viste tú del código antes de preguntar;
- qué dijo el chat;
- qué dijo el agente;
- qué herramienta usó el agente, si puedes verla. Si la interfaz no la muestra, dilo: esa opacidad también es un dato.

!!! warning "Restricciones"

    - No aceptes un cambio de código en esta lección. Si el agente edita, reviértelo y repite la orden dejando claro que solo lee.
    - No corrijas al agente todavía. La lección es ver el bucle, no ganar la discusión.

!!! success "Cómo sabes que está bien"

    - Señalas una frase del agente que solo podía salir de haber leído el archivo, y una frase del chat que solo podía salir de lo que pegaste.
    - Si uno de los dos se inventa una rama que no está en la función, lo has marcado. ¿Cuál de los dos tenía más facilidad para inventarla, y por qué?
    - Escribes una frase: qué seguiría siendo responsabilidad tuya aunque el agente acierte.
