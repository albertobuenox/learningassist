---
tags:
  - ejercicio
  - frontend
  - largo
---

# 06 — Formulario controlado

!!! info "Antes de empezar"

    Tiempo: 2–3 horas.

??? tip "Pista"

    Apoyo: la sección de React sobre estado y eventos. Glosario: [controlado.](../glosario.md#controlado)

## Pantalla

Alta de una tarea, encima de la lista del ejercicio 5.

- Campos: título (obligatorio, mínimo 3 caracteres) y notas (opcional, máximo 140).
- Los errores se ven junto al campo, no solo en un `alert`.
- Enviar con título inválido no añade nada.
- Enviar válido añade la tarea, limpia el formulario y deja el foco en el título.
- Mientras se envía no hay red: el “envío” es local. Aun así, desactiva el botón un instante o hasta limpiar, y observa si un doble clic crea dos tareas. Si las crea, el arreglo es de estado, no de CSS.

!!! warning "Restricciones"

    - El valor de cada campo sale de `useState` (o de un solo objeto de estado: elige y no mezcles).
    - No uses `document.getElementById` para leer el título.
    - La validación es una función pura: entra el texto, sale la lista de errores. El componente solo la llama.

!!! success "Cómo sabes que está bien"

    - Escribes dos letras, ves el error, llegas a tres, el error desaparece **sin** pulsar enviar. ¿Lo quieres así o solo al enviar? Las dos políticas valen; la pantalla tiene que coincidir con la que hayas escrito en un comentario.
    - Pegas 200 caracteres en notas. ¿El contador o el mensaje dicen que te pasaste, y el estado no guarda más de 140, o sí guarda y solo avisa? Elige una y pruébala.
    - Recorres el formulario con teclado. El botón de enviar se activa con Enter desde el título. Si no, el botón quedó fuera del `form`.
