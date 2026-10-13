---
tags:
  - ejercicio
  - largo
  - php
---

# 09 — Proyecto: notas

!!! info "Antes de empezar"

    Cierre de la asignatura. Tiempo: un día. Arrastra el token del ejercicio 7 y el JSON del ejercicio 8: sin eso, React no puede consumir este backend y un `POST` con solo la cookie seguiría escribiendo. Una nota tiene título, cuerpo y fecha de actualización. Pertenece al usuario de la sesión. En esta versión sigue habiendo un solo usuario; aun así, la tabla guarda `usuario_id`. Así el día que haya dos, la consulta ya exige ese filtro.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Comportamiento

- Listar notas de ese usuario, la más recientemente actualizada primero.
- Crear, editar y borrar. Borrar pide confirmación en el formulario (un `POST` dedicado, no un enlace `GET`).
- Título obligatorio, máximo 80 caracteres. Cuerpo obligatorio, máximo 2000.
- Editar una nota que no existe responde 404.
- Validación en PHP y restricciones en la tabla.
- Los `POST` del HTML sin token responden 403 y no escriben.
- `GET /api/notas` y `POST /api/notas` cumplen el contrato: 200 con lista (vacía si no hay notas), 201 al crear, 400 si el cuerpo no vale, 401 sin sesión, JSON también en el error.

## Entrega

Repositorio con README: versión de PHP, cómo crear la base, cómo sembrar el usuario, cómo arrancar. `.env.example` sin secretos. `esquema.sql` versionado.

!!! success "Cómo sabes que está bien"

    - El título `</title><script>` se ve como texto en la lista y en el formulario de edición.
    - Una comilla en el cuerpo no rompe el `UPDATE`.
    - Borrar y luego recargar no vuelve a borrar: hubo una redirección.
    - Puedes señalar la línea donde la consulta de listado filtra por el usuario de la sesión. Si esa línea no existe porque “total, solo hay uno”, el proyecto no está cerrado: el hábito que se practica es el filtro, no el atajo.
    - `curl` con la cookie y sin token no aumenta el número de notas. `GET /api/notas` devuelve un array, también cuando está vacío.
