# Frontend con Node y React

Objetivo: reconstruir el camino corto que se olvida cuando se vive dentro de un framework. Primero la plataforma (HTML, CSS, JavaScript, el navegador), después un proceso Node que escucha HTTP, y solo entonces React como forma de dibujar estado en pantalla.

## Al terminar deberías poder

- Marcar una página con HTML que se entienda sin CSS, y maquetarla con Flexbox o Grid.
- Guardar un estado en memoria (un carrito, un filtro) y reflejarlo en el DOM, en vanilla.
- Levantar un servidor Node que responda JSON y sepa qué es una ruta, un método y un código de estado.
- Partir una interfaz React en componentes, con estado local, un formulario controlado y una petición que contempla carga, vacío y error.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md) — MDN y javascript.info como base; React solo después del ejercicio 2.
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [Ficha de producto](ejercicios/01-ficha-de-producto.md) | HTML y CSS, sin librerías |
| 2 | [Carrito en vanilla](ejercicios/02-carrito-vanilla.md) | Estado y DOM |
| 3 | [Servidor JSON](ejercicios/03-servidor-json.md) | Node sin Express |
| 4 | [CLI](ejercicios/04-cli-resumen.md) | Node fuera del navegador |
| 5 | [Lista en React](ejercicios/05-lista-react.md) | Componentes y estado |
| 6 | [Formulario](ejercicios/06-formulario-react.md) | Validación visible |
| 7 | [Datos remotos](ejercicios/07-datos-remotos.md) | Fetch y tres estados |
| 8 | [Proyecto](ejercicios/08-proyecto-panel.md) | Piezas juntas |

## Herramienta

Node en una versión actual con soporte (mira https://nodejs.org/). Para React, el asistente oficial de https://react.dev/learn/creating-a-react-app (Vite es la opción habitual). No hace falta TypeScript para cerrar esta asignatura; si ya lo usas, no lo conviertas en el tema del ejercicio.

## Criterio de cierre

El proyecto del panel se abre en el navegador, habla con tu servidor Node y no se queda en blanco cuando la API falla o no hay filas.
