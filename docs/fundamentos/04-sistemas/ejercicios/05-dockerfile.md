---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 05 — Un Dockerfile propio

!!! info "Antes de empezar"

    Tiempo: 2 horas.

??? tip "Pista"

    Apoyo: la sección de construir una imagen en la guía oficial de Docker.

Empaqueta un sitio estático (la ficha) **o** el servidor Node del ejercicio de productos, uno de los dos.

## La imagen

- Parte de una imagen oficial, con una etiqueta de versión concreta, no `latest`.
- Copia solo lo necesario. Hay un `.dockerignore`.
- El proceso principal es el servidor (Nginx o Node), en primer plano. Si el contenedor arranca y se apaga al momento, el proceso terminó: mira por qué un servidor tiene que quedarse en primer plano.
- `docker build` y `docker run` con el puerto publicado bastan para ver el sitio.
- La imagen no contiene `.env`, claves ni `node_modules` copiados del anfitrión si el proyecto es Node: las dependencias se instalan en la construcción. Escribe en un comentario por qué copiar `node_modules` de tu portátil es frágil.

!!! success "Cómo sabes que está bien"

    - Borras la carpeta de código y el contenedor **ya creado** sigue sirviendo. La imagen es autosuficiente. (Si usaste un bind mount, ese no cuenta: quítalo para esta prueba.)
    - Cambias una línea de código, reconstruyes y la capa de dependencias no se reinstala si no tocaste el manifiesto. Si se reinstala siempre, el orden del Dockerfile tira la caché.
    - `docker image ls` muestra un tamaño que puedes explicar en una frase (base + tus archivos). No hace falta microoptimizar.
