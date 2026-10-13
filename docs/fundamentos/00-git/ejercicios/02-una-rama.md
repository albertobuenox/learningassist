---
tags:
  - ejercicio
  - git
  - medio
---

# 02 — Una rama

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos.

??? tip "Pista"

    Si te pierdes: https://learngitbranching.js.org/ , niveles de introducción, y vuelta al ejercicio.

Parte del repositorio del ejercicio 1.

## Qué hacer

1. Crea una rama `precio` desde el commit actual. En esa rama, cambia una cifra en `notas.txt` y commitea.
2. Vuelve a `main`. Sin mezclar todavía, cambia **la misma línea** de otra manera y commitea.
3. Mezcla `precio` en `main`. Tiene que haber conflicto. Abre el archivo, lee las dos versiones y deja una frase que tenga sentido. Quita las marcas. Commitea la mezcla.
4. En un párrafo, di qué commit tiene dos padres y cómo lo viste.

!!! warning "Restricciones"

    - No borres la rama para “quitar el conflicto”.
    - No copies el archivo desde otra carpeta para saltarte las marcas. Resuélvelo en el archivo que Git dejó a medias.
    - Una interfaz gráfica vale para ver el grafo. La resolución del conflicto se hace en el texto.

!!! success "Cómo sabes que está bien"

    - `git log --oneline --graph` muestra el desvío y la unión, y puedes señalar cuál de los dos cambios de la cifra sobrevivió.
    - Buscas `<<<<<<<` en el archivo y no está.
    - Sabes en qué rama estabas al commitear, porque `git status` te lo decía antes de cada commit.
