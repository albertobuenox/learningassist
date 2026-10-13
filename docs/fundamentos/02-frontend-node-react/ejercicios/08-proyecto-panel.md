---
tags:
  - ejercicio
  - frontend
  - largo
---

# 08 — Proyecto: panel de pedidos

!!! info "Antes de empezar"

    Cierre de la asignatura. Tiempo: un día. Sin curso nuevo.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Producto

Un panel local para la tienda de café.

- El servidor Node guarda pedidos en memoria: `POST /pedidos` con líneas `{ productoId, cantidad }`, `GET /pedidos`, `GET /productos`.
- Validación en el servidor: cantidad entera positiva, producto existente. Si no, 400 con un mensaje concreto.
- React muestra los productos, deja elegir cantidades y envía el pedido.
- Tras un 201, el nuevo pedido aparece en una lista “Hoy” sin recargar la página entera.
- Estados de carga y de error en el envío, distintos del error de la carga inicial.

!!! warning "Restricciones"

    - El precio que se cobra es el que devuelve el servidor al crear el pedido, no un total calculado solo en el cliente. El cliente puede mostrar una estimación; el número que queda guardado lo confirma la respuesta.
    - Sin Express, salvo que primero lo hagas con `node:http` y, en un segundo commit, migres. El README explica qué te ahorró Express.
    - Un README con: cómo instalar, cómo arrancar API y cliente, y en qué puertos.

!!! success "Cómo sabes que está bien"

    - Creas un pedido con `curl` y el panel, al refrescar, lo enseña. Si no lo enseña, la memoria del servidor y la del cliente se han separado y no lo habías notado.
    - Un `POST` con cantidad `-1` no crea nada y la interfaz muestra el mensaje del 400, no un éxito.
    - Otra persona, con Node instalado, levanta el panel siguiendo solo el README.
