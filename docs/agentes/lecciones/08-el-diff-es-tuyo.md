---
tags:
  - agentes
  - corto
  - leccion
---

# 08 — El diff es tuyo

!!! info "Antes de empezar"

    Tiempo: 45 minutos, encima de un cambio que el agente ya haya hecho (la rebanada de la lección 6 vale).

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## Qué leer, en este orden

1. `git diff`, archivo por archivo. El resumen del agente se lee al final, no al principio.
2. Para cada archivo: ¿estaba en el encargo? Si no, es candidato a revertir esa parte, no a “dejarlo porque mejora”.
3. La comprobación, ejecutada por ti. Si falla, el agente no ha terminado, aunque el mensaje diga que sí.
4. Una línea que no entiendas. Pregúntale qué decisión es, en modo lectura. Si la explicación no coincide con la línea, manda la línea, no tu recuerdo.

## Qué anotar

Tres columnas: lo que el resumen afirma, lo que el diff hace, si coinciden. Al menos una fila debe ser incómoda (un renombre, un comentario, un cambio de comportamiento no pedido). Si no encuentras ninguna, mira otra vez el diff de un archivo que el resumen no mencionó.

!!! warning "Restricciones"

    - No pidas “revisa tu propio diff” como sustituto de leerlo. Puede ayudarte a cazar un descuido. No firma por ti.
    - No aceptes un cambio cuyo comportamiento nuevo no sabes nombrar.

!!! success "Cómo sabes que está bien"

    - Puedes explicar el diff en voz alta sin mirar el chat.
    - Has revertido o reescrito al menos un trozo que no pediste, o has escrito por qué lo conservas. “Quedaba más profesional” no es una razón.
    - El test que añadiste falla si quitas la condición a mano. Si no falla, la comprobación no ejerce el caso.
