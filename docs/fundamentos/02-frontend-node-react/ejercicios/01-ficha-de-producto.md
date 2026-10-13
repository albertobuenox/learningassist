---
tags:
  - ejercicio
  - frontend
  - largo
---

# 01 — Ficha de producto

!!! info "Antes de empezar"

    HTML y CSS. Sin React, sin Bootstrap, sin Tailwind. Tiempo: 2–3 horas.

??? tip "Pista"

    Apoyo: MDN Learn (HTML y CSS) y Flexbox Froggy si el eje se te cruza.

## Pantalla

Una ficha de café para una tienda pequeña, en una sola página:

- Cabecera con el nombre de la tienda y un enlace a “Cesta”.
- Imagen (puede ser un rectángulo de color si no tienes foto), nombre del producto, precio y una frase.
- Lista de tres notas: origen, tueste, peso.
- Un botón “Añadir a la cesta” que todavía no hace nada.
- Un pie con una dirección.

A 800 píxeles o más, la imagen y el texto van en la misma fila. Por debajo, van en columna. El botón no se estira a todo el ancho en el escritorio; en el móvil, sí.

!!! warning "Restricciones"

    - Un `index.html` y un `styles.css`.
    - El botón es un `button`. El enlace es un `a`. El titular de la ficha es un encabezado, y no saltas de `h1` a `h3`.
    - Colores en variables CSS al principio del archivo, para poder cambiar el acento en un sitio.
    - Nada de `float` para la columna principal. Flexbox o Grid.

!!! success "Cómo sabes que está bien"

    - Desactivas el CSS. ¿Se distingue el título, la lista y el botón?
    - Navegas con el tabulador. ¿El enlace y el botón reciben foco visible?
    - Estrecha la ventana. ¿Aparece un scroll horizontal? Si aparece, alguna medida fija se ha pasado del ancho.
    - En las herramientas del navegador, la regla que pone la imagen al lado del texto es la que tú crees, no una que heredaste sin mirar.

    Cuando la ficha aguante eso, el ejercicio 2 le dará comportamiento.
