---
tags:
  - ejercicio
  - largo
  - pruebas
---

# 03 — La frontera HTTP

!!! info "Antes de empezar"

    Tiempo: 2 horas. Hace falta una ruta tuya que ya responda códigos de verdad: la API de notas, el contrato de la clínica o el `POST /productos` de Node.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Casos

Automatiza cuatro peticiones. Cada una comprueba código y, si hay cuerpo, un campo.

1. `GET` de la colección. 200. Si está vacía, el cuerpo es una lista vacía, no un 404.
2. `POST` válido. 201, y un `GET` posterior ve el recurso. Elige datos que no dependan de la hora ni de un id que solo tú recuerdas.
3. `POST` inválido (importe negativo, título vacío, JSON roto: el que ya rechaces). 400. La colección no crece.
4. La misma operación de escritura sin sesión, si la ruta exige sesión. 401. La colección no crece.

Entre pruebas, la base tiene que estar en un estado conocido. O cada prueba crea y borra lo suyo, o usas una base desechable. Anota cuál. Una prueba que solo pasa si ayer dejaste tres filas no es una prueba.

!!! warning "Restricciones"

    - No mires la pantalla para decidir si pasó. El runner (o el script) termina con código distinto de cero cuando el status no es el esperado.
    - No hace falta un navegador ni Playwright.
    - No ataques una URL que no sea tuya. El servidor es el de tu máquina.

!!! success "Cómo sabes que está bien"

    - Quitas la comprobación de sesión un momento. La prueba 4 se pone roja. La vuelves a poner.
    - La prueba 3 no da por buena un 200 con un JSON que dice `"error"`.
    - Puedes ejecutarlas dos veces seguidas. La segunda también pasa. Si la segunda falla, el estado se escapó entre ejecuciones.
