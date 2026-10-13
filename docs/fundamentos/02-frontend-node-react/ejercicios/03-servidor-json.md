---
tags:
  - ejercicio
  - frontend
  - largo
---

# 03 — Servidor JSON

!!! info "Antes de empezar"

    Node y el módulo `node:http`. Sin Express. Tiempo: 2–3 horas.

??? tip "Pista"

    Apoyo: https://nodejs.org/en/learn y la documentación de `node:http`.

## Comportamiento

Un proceso escucha en el puerto 3000.

- `GET /productos` responde 200 y un JSON: un array de tres productos (`id`, `nombre`, `precio`).
- `GET /productos/1` responde ese producto, o 404 con un JSON `{ "error": "no encontrado" }` si el id no existe.
- `POST /productos` lee un JSON `{ "nombre", "precio" }`. Si falta el nombre o el precio no es un número positivo, responde 400. Si vale, lo añade en memoria y responde 201 con el producto y un `id` nuevo.
- Cualquier otra ruta responde 404.
- Al cerrar el proceso, los productos creados desaparecen. Es aceptable. Escribir a disco es ampliación.

Pruébalo con `curl` o con la pestaña de red, no solo con el navegador (el navegador solo hace `GET` fácil).

!!! warning "Restricciones"

    - El cuerpo de la respuesta lleva `Content-Type: application/json`.
    - El id de la URL no se concatena dentro de una cadena HTML. Aquí no hay HTML.
    - No instales un framework. El objetivo es ver la petición cruda: método, URL y cuerpo que llega a trozos.

!!! success "Cómo sabes que está bien"

    - ¿Un `POST` sin `Content-Type` JSON lo rechazas o lo interpretas por accidente?
    - ¿El 404 de un producto y el 404 de una ruta desconocida se distinguen en el cuerpo, y ambos usan 404?
    - Arrancas dos veces seguidas. ¿El puerto ocupado te dice algo comprensible, o el proceso se cae con un número que no miraste?

    Cuando esto responda, el ejercicio 7 de React puede usarlo como API. Hasta entonces, no hace falta CORS si pruebas con `curl`. Anótalo en el README del ejercicio: desde qué origen hablará el navegador.
