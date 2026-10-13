---
tags:
  - ejercicio
  - git
  - medio
---

# 03 — El remoto

!!! info "Antes de empezar"

    Tiempo: 60 minutos. Si no tienes cuenta en un forge, GitHub Skills te deja practicar el mecanismo: https://skills.github.com/

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Qué hacer

1. Crea un repositorio **privado** vacío. Añádelo como `origin` y haz `push` de `main`.
2. Añade un archivo `.env` con una contraseña falsa y obvia (`CLAVE=no-subir`). Añade `.env` al `.gitignore` **antes** de cualquier commit que lo incluya. Commitea el ignore. Comprueba que `.env` no aparece en `git status` como archivo a commitear.
3. Clona el remoto en otra carpeta. La contraseña falsa no está. El `notas.txt` sí, con la historia.
4. En el clon, haz un commit pequeño, haz `push`, y en la carpeta original haz `pull`. Las dos copias coinciden en `git log`.

!!! warning "Restricciones"

    - El remoto es privado. No hace falta un README público.
    - Si `.env` llegó a un commit, no sigas. Para este ejercicio, borra el repositorio remoto y empieza de nuevo: reescribir historia en un remoto ya compartido es el tema que el glosario deja para después, y aquí la lección es no subir el secreto.
    - `node_modules/` o `vendor/` no se versionan. Si todavía no tienes, escribe igual esas dos líneas en el ignore y anota por qué.

!!! success "Cómo sabes que está bien"

    - El clon arranca sin pedirte el `.env`.
    - `git log` en las dos carpetas muestra el mismo último commit después del pull.
    - Puedes explicar la diferencia entre “el archivo está en mi disco” y “el archivo está en el remoto”.
