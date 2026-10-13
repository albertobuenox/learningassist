---
tags:
  - ejercicio
  - http
  - medio
---

# 04 — Otro origen

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos. Glosario: [origen](../glosario.md#origen), [CORS](../glosario.md#cors), [cookie](../glosario.md#cookie-de-sesión).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [origen](../glosario.md#origen), [CORS](../glosario.md#cors), [cookie](../glosario.md#cookie-de-sesión).

Hace falta una página servida en un puerto y una API en otro. El servidor Node en el 3000 y un HTML abierto desde `php -S` en el 8000 valen. También vale el HTML como archivo `file://`: anota qué origen cree el navegador que tiene.

## Qué observar

1. Desde la página, `fetch` a `GET /productos` del otro puerto. Abre la pestaña de red y la consola. Anota el error tal como lo escribe el navegador.
2. La misma URL con `curl`. Funciona. Escribe por qué las dos pruebas no miden lo mismo.
3. Mira la petición que el navegador hizo sola antes del `GET`, si aparece (método `OPTIONS`). Anota qué cabeceras pide permiso para usar. No hace falta aún autorizarla.
4. Cuando autorices el origen en la API, el `GET` se lee. Documenta la cabecera que añadiste y el origen exacto, no `*` “porque así va”, salvo que decidas `*` y escribas qué dejas de poder hacer con cookies.

No construyas una página en otro sitio para disparar acciones contra la sesión de nadie. Aquí solo se observa una lectura tuya, entre dos puertos tuyos.

!!! success "Cómo sabes que está bien"

    - Distingues “el servidor no llegó a responder” de “el navegador no me deja leer la respuesta”.
    - `curl` deja de ser tu única prueba en cuanto hay un navegador de por medio.
    - Sabes decir el origen de la página y el de la API como esquema + host + puerto.
