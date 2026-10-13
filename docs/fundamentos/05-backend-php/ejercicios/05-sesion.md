---
tags:
  - ejercicio
  - largo
  - php
---

# 05 — Sesión y login mínimo

!!! info "Antes de empezar"

    Tiempo: 3 horas. Manual: sesiones y `password_hash` / `password_verify`.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Un único usuario, creado por ti en la base o en un script de semilla: correo y hash. No hay registro público. No hace falta recuperar contraseña.

## Comportamiento

- `GET /login` muestra el formulario.
- `POST /login` verifica. Si falla, 401 y un mensaje único: “correo o contraseña incorrectos”. No digas cuál de los dos falló.
- Si acierta, guardas en la sesión el id del usuario, no la contraseña ni el hash, y rediriges a `/`.
- `GET /` sin sesión redirige a `/login`.
- `POST /salir` destruye la sesión y vuelve al login.
- Las facturas del ejercicio 4 solo se ven y se crean con sesión iniciada.

!!! warning "Restricciones"

    - `password_hash` en el momento de crear el usuario. Si en la base puedes leer la contraseña, el ejercicio no vale.
    - La cookie de sesión: anota en un comentario qué banderas pondrías detrás de HTTPS. En local, no finjas que `Secure` está activo si sirves por HTTP.
    - La sesión demuestra quién llama. No demuestra que el formulario lo pintó tu página. Ese segundo hueco es el ejercicio 7. No lo tapes aquí con un comentario de “luego se verá” sin enlace: cuando este login escriba, el 7 tiene que poder rechazar el `POST`.
    - Sin librería de autenticación.

!!! success "Cómo sabes que está bien"

    - Copias la URL de `/` en una ventana de incógnito y caes en el login.
    - Un `POST /facturas` sin cookie de sesión no inserta. Lo pruebas con `curl`, no solo con el navegador.
    - Dos contraseñas distintas no producen el mismo hash, y la misma contraseña, hasheada dos veces, tampoco tiene por qué producir la misma cadena. `password_verify` aun así acepta la buena. Si esto te sorprende, lee en el manual qué se guarda junto al hash.
