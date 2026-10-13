---
tags:
  - ejercicio
  - largo
  - php
---

# 08 — API JSON

!!! info "Antes de empezar"

    Tiempo: medio día. El contrato es el del ejercicio 5 de HTTP, o uno más pequeño si la clínica todavía no existe: las notas del proyecto, en JSON, para que React pueda consumirlas.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Hazlo cuando el HTML de las notas (o de las facturas) ya esté separado del SQL. La misma regla de negocio sirve las dos representaciones. No copies la validación en dos funciones que puedan divergir.

## Rutas

Prefijo `/api`, para no chocarlo con el HTML.

- `GET /api/notas` — 200 y un array JSON de las notas del usuario de la sesión. Vacío si no hay, no 404.
- `POST /api/notas` — cuerpo JSON `{"titulo", "cuerpo"}`. 201 y la nota creada, con su id. 400 si no cumple las mismas reglas que el formulario. 401 sin sesión.
- `POST /api/notas/{id}/cancelar` no hace falta. Para borrar o actualizar, elige una ruta y el método que ya escribiste en el contrato (`DELETE` o `POST`). 404 si el id no es de este usuario: no confirmes que la nota existe y es de otro.

`Content-Type` de la respuesta: `application/json`. Un `POST` que no traiga JSON se rechaza con 400.

El HTML anterior sigue funcionando, token incluido.

!!! warning "Restricciones"

    - Consultas parametrizadas. El id del camino no se concatena dentro del SQL.
    - El 401 de la API es JSON, no una redirección al login. Una redirección la entendería el navegador al pedir HTML. `fetch` se merece el código.
    - CORS: si React vive en otro puerto, autoriza ese origen y anótalo. No abras `*` si la petición lleva cookie.

!!! success "Cómo sabes que está bien"

    - Los cuatro casos del ejercicio de pruebas sobre la frontera HTTP pueden apuntar aquí. Si todavía no los has escrito, pruébalos con `curl` y guarda los comandos en el README.
    - Un título con una comilla se guarda. Al pedirlo en JSON vuelve como texto dentro del JSON, no como SQL roto. Al pintarlo en HTML, el ejercicio 3 sigue aplicando.
    - React, o un `fetch` de veinte líneas, lista las notas. Si la API está caída, se ve el error. Eso ya lo practicaste en frontend: aquí se trata de que el contrato coincida con lo que el cliente lee.
