---
tags:
  - corto
  - ejercicio
  - http
---

# 01 — Una transacción

!!! info "Antes de empezar"

    Tiempo: 45 minutos. MDN, visión general de HTTP, si un nombre no te suena.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Qué capturar

Con `curl -v`, haz estas llamadas y guarda la salida:

1. `GET` de https://example.com/
2. `GET /productos` de tu servidor Node del frontend, si ya existe. Si no existe, un `GET` a cualquier servidor tuyo que responda texto.
3. Un `POST` con cuerpo JSON pequeño al mismo servidor, aunque responda 404. La petición igual se puede leer.

En cada una, marca con un comentario encima de la salida:

- la línea de petición (método y camino);
- una cabecera de petición que haya puesto `curl`;
- el código de estado;
- el `Content-Type` de la respuesta, si viene;
- si hay cuerpo.

!!! warning "Restricciones"

    - No uses el navegador para este ejercicio. El navegador esconde la primera línea.
    - No hace falta que el `POST` tenga éxito. Un 404 también es una transacción completa.

!!! success "Cómo sabes que está bien"

    - Señalas el código sin confundirlo con un número que aparezca dentro del HTML.
    - Explicas por qué la tercera llamada puede ser un 404 y, aun así, haber llevado un cuerpo en la petición.
    - Si quitas `-v`, ¿qué parte de la transacción dejas de ver?
