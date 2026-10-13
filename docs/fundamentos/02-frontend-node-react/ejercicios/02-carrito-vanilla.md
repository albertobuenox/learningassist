---
tags:
  - ejercicio
  - frontend
  - largo
---

# 02 — Carrito en vanilla

!!! info "Antes de empezar"

    JavaScript en el navegador, sin framework. Tiempo: 3–4 horas. Parte de la ficha del ejercicio 1, o de una lista de tres productos escrita en el HTML. Cada producto tiene nombre, precio e id.

??? tip "Pista"

    Apoyo: javascript.info, secciones de DOM, eventos y arrays.

## Comportamiento

- Pulsar “Añadir” incrementa la cantidad de ese id en el carrito. El carrito es un array o un mapa en memoria, no el texto del botón.
- Una zona “Cesta” lista nombre, cantidad, subtotal y total. Si la cantidad pasa de cero, se puede restar. A cero, la línea desaparece.
- El número de unidades junto a “Cesta” coincide con la suma de cantidades.
- Recargar la página vacía el carrito. Persistirlo es una ampliación, no el requisito: si lo haces, usa `localStorage` y anota qué ocurre con una pestaña duplicada.

!!! warning "Restricciones"

    - Un solo sitio actualiza el DOM a partir del estado. Si encuentras que cambias un `textContent` en el listener y también en otro sitio, para y deja un único “pintar”.
    - No uses `innerHTML` con cadenas que incluyan el nombre del producto si ese nombre pudiera venir de fuera. Con datos fijos tuyos, aun así, practica crear elementos (`createElement`) o `textContent`.
    - Sin jQuery y sin React.

!!! success "Cómo sabes que está bien"

    - Añades dos veces el mismo café. ¿Hay una línea con cantidad 2, o dos líneas?
    - El total lo calculas desde el array. Cámbialo a mano en la consola y vuelve a pintar: ¿la vista obedece al array?
    - ¿Qué pasa si el precio es `2.5` y sumas con decimales de binario? Decide si redondeas al mostrar o guardas céntimos enteros, y escribe esa decisión en un comentario de tres líneas.
