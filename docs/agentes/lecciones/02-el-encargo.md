---
tags:
  - agentes
  - corto
  - leccion
---

# 02 — El encargo

!!! info "Antes de empezar"

    Tiempo: 45 minutos. Fuente, después de escribir el tuyo: https://code.claude.com/docs/en/best-practices (la parte de dar una tarea verificable).

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## El encargo flojo

Este texto es el punto de partida. No lo mejores todavía:

> Arregla el código y hazlo más profesional. Que quede bien.

## Qué escribir

Traduce ese encargo a uno que se pueda comprobar, sobre un archivo real tuyo. Tiene que caber en diez líneas y contener:

- el resultado observable (qué hace el programa después, con un ejemplo de entrada y salida);
- dos restricciones (qué no puede cambiar: una firma, un archivo, una dependencia);
- el criterio de hecho (el comando o el gesto con el que tú, no el agente, decides que terminó).

Pídeselo al agente. Guarda la respuesta. No tiene que implementar todavía si el encargo era solo de diagnóstico: en ese caso el criterio de hecho es una respuesta tuya, no un diff.

!!! warning "Restricciones"

    - Prohibido “etc.”, “lo que veas” y “best practices” sin decir cuáles.
    - Si el criterio de hecho es “cuando el agente diga que está listo”, no cuenta. Cámbialo por algo que puedas ejecutar o leer.

!!! success "Cómo sabes que está bien"

    - Otra persona, con solo esas diez líneas, sabe qué no debe tocar.
    - Quitas el ejemplo de entrada y salida. ¿El encargo sigue decidiendo un comportamiento, o ya admite dos?
    - El agente hizo algo que no pediste. ¿Estaba fuera de las restricciones? Si no lo estaba, la restricción faltaba. Añádela en una línea, no en un párrafo.
