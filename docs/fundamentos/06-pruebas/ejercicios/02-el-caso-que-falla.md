---
tags:
  - corto
  - ejercicio
  - pruebas
---

# 02 — El caso que falla

!!! info "Antes de empezar"

    Tiempo: 45 minutos. Glosario: [rojo](../glosario.md#rojo), [verde](../glosario.md#verde).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [rojo](../glosario.md#rojo), [verde](../glosario.md#verde).

Añade una regla que **todavía no exista** en la función. Por ejemplo: un concepto vacío se ignora igual que un importe vacío. O un importe con más de dos decimales se rechaza. Elige una y escríbela en una frase antes de tocar código.

## Orden obligatorio

1. Escribe la prueba de esa regla.
2. Ejecuta el runner. Tiene que fallar. Guarda el mensaje de fallo (la salida basta).
3. Cambia la función lo mínimo para que esa prueba pase y las anteriores sigan pasando.
4. Si al escribir la prueba ya pasaba, la regla ya estaba cubierta o la prueba no ejerce el caso. No la cuentes. Busca otra regla que de verdad falle.

!!! success "Cómo sabes que está bien"

    - Tienes el mensaje rojo de antes del cambio. Si no lo guardaste, repite el orden en otra regla pequeña.
    - Las pruebas del ejercicio 1 siguen verdes.
    - El cambio en la función es pequeño. Si reescribiste el archivo entero, la prueba no te guió: te sirvió de permiso.
