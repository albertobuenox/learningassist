---
tags:
  - corto
  - ejercicio
  - git
---

# 01 — Tres commits

!!! info "Antes de empezar"

    Tiempo: 45–60 minutos.

??? tip "Pista"

    Consulta: Pro Git, capítulos 1 y 2, solo si un comando te sorprende.

## Qué hacer

En una carpeta nueva, fuera de `fundamentos/`:

1. Inicia un repositorio. Crea `notas.txt` con una línea. Míralo en `git status` antes y después de `git add`. Anota, con tus palabras, en qué sitio está el cambio en cada momento.
2. Haz un commit. El mensaje dice por qué existe el archivo, no “primer commit”.
3. Cambia la línea y añade una segunda. Prepara solo una de las dos modificaciones y commitea. El otro cambio sigue en el directorio de trabajo. Compruébalo con `status` y con `diff`.
4. Tercer commit, con el cambio que quedaba. `git log` muestra tres entradas que se pueden leer en voz alta.

!!! warning "Restricciones"

    - No subas nada a internet en este ejercicio.
    - No uses una interfaz gráfica. El objetivo es reconocer el estado, no recordar un botón.
    - Si un commit salió mal de mensaje, no reescribas la historia todavía. Haz otro commit que lo aclare, o anota qué comando del libro lo reescribiría y por qué no lo necesitas hoy.

!!! success "Cómo sabes que está bien"

    - Señalas un cambio y dices si está sin seguimiento, preparado o ya en un commit, sin mirar el manual.
    - `git show` del segundo commit no contiene la modificación que dejaste fuera a propósito.
    - Los tres mensajes, leídos solos, cuentan una historia. Si uno dice “update”, ese no cuenta.
