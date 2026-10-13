---
tags:
  - bases-de-datos
  - ejercicio
  - largo
---

# 07 — Proyecto: agenda de clínica

!!! info "Antes de empezar"

    Cierre de la asignatura. Tiempo: medio día. Aquí ya no hay curso nuevo: usa el glosario y lo que hayas escrito en los ejercicios 1 a 6.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Alcance

Un profesional, varios pacientes, citas de 30 minutos entre las 09:00 y las 14:00, de lunes a viernes. Un paciente tiene nombre y teléfono. Una cita tiene paciente, inicio y estado (`programada`, `hecha`, `cancelada`).

Reglas:

- No hay dos citas `programada` con el mismo inicio.
- No se programa en fin de semana ni fuera de ese horario. Decide si eso lo obliga la base, la aplicación, o las dos, y defiende la decisión en cuatro líneas.
- No se borra un paciente con citas: se rechaza el borrado.

## Entrega

1. `esquema.sql` con tablas, restricciones e índices que justifiques en comentarios de una línea.
2. `consultas.sql` con:
   - la agenda de un día concreto, ordenada;
   - cuántas citas `hecha` tuvo el profesional esta semana;
   - los pacientes sin ninguna cita `programada` futura.
3. `pruebas.sql`: sentencias que **deben fallar** (duplicada, paciente inexistente, borrado prohibido) y una transacción que mueve una cita de hora (cancela o reescribe el inicio) sin dejar dos programadas.
4. Un párrafo: qué dejarías fuera a propósito (varios profesionales, salas, recordatorios).

!!! success "Cómo sabes que está bien"

    - Ejecutas `pruebas.sql` y los fallos son los que esperabas, con un error del motor, no con un “no pasa nada”.
    - La consulta del día no depende de ordenar en la aplicación.
    - Alguien que no ha visto tus ejercicios anteriores entiende el esquema leyendo solo los comentarios.
