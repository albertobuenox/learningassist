---
tags:
  - ejercicio
  - http
  - medio
---

# 05 — Contrato de la clínica

!!! info "Antes de empezar"

    Tiempo: 60 minutos. Sin implementar. Este documento lo implementa después el backend PHP y lo consume React.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Recursos

- Hueco: un inicio de cita posible para el único profesional.
- Cita: un hueco ya asignado a un paciente (nombre y teléfono).
- Sesión del mostrador: quién está logueado. Quien pide cita desde casa no usa esa sesión.

## Qué escribir

Una página, en el repositorio de práctica, con una fila por operación:

- método y camino;
- quién puede llamarla (mostrador con sesión, o cualquiera);
- cuerpo de la petición, si lo hay, con los campos y sus tipos;
- códigos posibles y qué significa cada uno;
- forma del cuerpo de la respuesta.

Operaciones mínimas:

- listar huecos de un día;
- crear una cita;
- cancelar una cita;
- listar las citas del día (solo mostrador).

Incluye, como mínimo, estos casos: día sin huecos (200 y lista vacía, no 404), hueco ya ocupado, cita que no existe, mostrador sin sesión, cuerpo que no es JSON.

El código del hueco ocupado lo eliges tú (409 es un candidato). Lo importante es que quede escrito antes de programar.

!!! warning "Restricciones"

    - No hay historia clínica en el JSON.
    - Cancelar no es un `GET`.
    - El contrato cabe en una página. Si necesitas dos, sobran campos.

!!! success "Cómo sabes que está bien"

    - Otra persona puede escribir el `curl` de “crear cita” sin preguntarte el nombre de un campo.
    - El caso vacío y el caso de error no comparten el mismo código.
    - Guardas este archivo. Cuando PHP y React discrepen, se corrige el código o se corrige el contrato, y el commit dice cuál de las dos cosas cambió.
