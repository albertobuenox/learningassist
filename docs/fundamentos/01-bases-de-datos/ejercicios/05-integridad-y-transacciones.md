---
tags:
  - bases-de-datos
  - ejercicio
  - medio
---

# 05 — Integridad y transacciones

!!! info "Antes de empezar"

    Tiempo: 90 minutos.

??? tip "Pista"

    Apoyo: tutorial oficial de PostgreSQL sobre transacciones (`BEGIN`, `COMMIT`, `ROLLBACK`) y la página de restricciones.

## Caso

Dos recepcionistas asignan la misma hora del mismo médico. El esquema mínimo:

- `medicos (id, nombre)`
- `huecos (id, medico_id, empieza_en)` — un médico no tiene dos huecos a la misma hora
- `citas (id, hueco_id, paciente, estado)` — un hueco tiene como mucho una cita que no esté cancelada

`estado` solo puede ser `reservada` o `cancelada`.

## Qué construir

1. El `CREATE TABLE` con claves, `UNIQUE`, `CHECK` y foráneas. La regla “como mucho una cita no cancelada por hueco” puede no salir con un `UNIQUE` de todo el hueco, porque las canceladas sí pueden acumularse. Prueba. Si el `UNIQUE` simple te estorba, investiga un índice único parcial y escribe en un comentario qué filas incluye.
2. Abre **dos** sesiones de `psql`. En ambas, intenta reservar el mismo hueco libre. Anota el orden de `BEGIN`, el `INSERT` y el `COMMIT`. ¿Una de las dos recibe un error? ¿Cuál? Si las dos confirman, la regla no está en la base.
3. Una transacción que inserte el hueco y la cita. A mitad, provoca un fallo (por ejemplo, un paciente vacío si lo prohibiste) y comprueba que no queda el hueco huérfano de una operación a medias. ¿Hizo falta `ROLLBACK` explícito o bastó con que la sesión terminara mal? Pruébalo y quédate con lo que hayas observado, no con lo que recuerdes.

!!! success "Cómo sabes que está bien"

    - Un compañero, con el mismo esquema, no puede dejar dos citas `reservada` en el mismo hueco ni desde otra aplicación.
    - Borrar un médico con huecos o bien falla o bien hace algo que tú declaraste (cascada). No hay filas apuntando a un médico que ya no existe.
    - Sabes decir, sin mirar el manual en ese momento, qué significa que la reserva “ocurrió” o “no ocurrió” como un solo hecho.
