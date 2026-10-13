---
tags:
  - ejercicio
  - frontend
  - largo
---

# 05 — Lista filtrable en React

!!! info "Antes de empezar"

    Primer ejercicio de React. Tiempo: 3 horas. Crea el proyecto con la herramienta que indica la documentación actual de React. Componentes en funciones.

??? tip "Pista"

    Apoyo: https://react.dev/learn hasta “Sharing data between components”, y el tutorial del tres en raya si no has escrito JSX nunca.

## Pantalla

Una lista de tareas en memoria (no hay servidor):

- Cada tarea tiene `id`, `titulo` y `hecha` (booleano).
- Un campo de texto filtra por título, sin distinguir mayúsculas, mientras escribes.
- Pulsar la fila cambia `hecha`. Lo hecho se ve tachado.
- Un contador dice cuántas quedan sin hacer **dentro del filtro actual**, y cuántas hay en total sin hacer. Esas dos cifras no son la misma pregunta: comprueba con un filtro que esconde una tarea pendiente.

!!! warning "Restricciones"

    - El array de tareas no se muta con `push` o cambiando `tarea.hecha = true` sobre el objeto viejo. Construye el estado siguiente y pásalo al setter.
    - La lista usa `key` con el `id`.
    - Un componente `Tarea` recibe la tarea y una función para alternarla. No importa el array entero si no lo necesita.
    - Sin router, sin Redux, sin librería de estilos. CSS de un archivo basta.

!!! success "Cómo sabes que está bien"

    - Filtras `a`, marcas hecha una tarea visible, borras el filtro. ¿Sigue hecha?
    - ¿El campo de filtro se vacía solo al marcar una tarea? Si se vacía, el estado del filtro vive en un sitio que se destruye. ¿Cuál?
    - En React DevTools, el estado está en el componente que posee la lista, no copiado en cada fila.
