---
tags:
  - ejercicio
  - largo
  - ui-ux
---

# 06 — Tres componentes

!!! info "Antes de empezar"

    Tiempo: 2–3 horas. Curso de Figma, capítulo de componentes, si aún no lo hiciste.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Define un sistema mínimo y úsalo en dos pantallas (agenda y elegir hueco). No diseñes un sistema para una empresa imaginaria.

## Piezas

1. **Botón.** Variantes: principal, secundario, peligro. Estados: defecto, foco, desactivado, y el de “ocupado” si la acción tarda. El de peligro no es el principal de la pantalla de alta.
2. **Campo de texto.** Etiqueta, pista opcional, error, desactivado. El mensaje de error va asociado al campo, no en un toast genérico.
3. **Fila de cita.** Hora, nombre, estado. El estado es texto. La fila entera no es un botón si dentro hay otra acción; decide qué se pulsa y anótalo.

Color, tipo y espacios salen de lo que fijaste en el ejercicio 4. Si cambias un tamaño, cambia en la escala, no solo en esta pieza.

!!! warning "Restricciones"

    - Las dos pantallas usan estas piezas. Si “el botón de la agenda es un poco distinto”, no es el componente: es una copia.
    - Nada de iconos mudos. Si hay un icono de papelera, tiene nombre accesible pensado (“Cancelar cita”), aunque el nombre se muestre solo para el lector de pantalla. Escríbelo al lado, en una nota.

!!! success "Cómo sabes que está bien"

    - Cambias el radio de la esquina del botón en el componente principal y las dos pantallas cambian. Si no, estabas editando instancias sueltas.
    - El botón de peligro y el principal no dependen de que el lector distinga rojo de azul: el texto ya dice “Cancelar” o “Reservar”.
    - Hay una página o un frame “sistema” donde un extraño ve las variantes sin entrar en cada pantalla.
