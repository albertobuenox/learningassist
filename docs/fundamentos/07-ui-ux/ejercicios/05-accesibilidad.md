---
tags:
  - ejercicio
  - largo
  - ui-ux
---

# 05 — Accesibilidad en el diseño

!!! info "Antes de empezar"

    Tiempo: 2 horas. Curso: https://web.dev/learn/accessibility (las secciones de contraste, foco y nombres accesibles). No hace falta implementar; sí dejar la pantalla lista para quien implemente.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Trabaja sobre la agenda del ejercicio 4 y sobre el formulario de elegir hueco.

## Qué comprobar y anotar

- Contraste del texto pequeño y del texto sobre el botón, medido con una herramienta (el selector de Figma, o el de las herramientas del navegador si ya hay HTML). El objetivo habitual es el AA de las WCAG. Si un gris “elegante” no llega, cámbialo y apunta el antes y el después.
- El foco de teclado se ve. Dibuja el estado de foco del botón y del hueco seleccionable. Si tu acento desaparece al enfocar, el estado de foco está sin diseñar.
- Cada campo tiene etiqueta visible, no solo un placeholder. El placeholder no cuenta como etiqueta: desaparece al escribir.
- El estado “ocupado” no se comunica solo con rojo y verde. Hay texto.
- El orden de tabulación, escrito en una lista, sigue el orden visual. Si el botón de borrar queda antes que el de confirmar, cámbialo.

!!! success "Cómo sabes que está bien"

    - Puedes recorrer el alta de la cita sin ratón, sobre el papel: cada parada tiene nombre y se ve cuál está activa.
    - Un compañero que implemente en React no tiene que inventarse el texto del botón ni la etiqueta del campo.
    - Quitas el color de la leyenda y el día sigue entendiéndose.
