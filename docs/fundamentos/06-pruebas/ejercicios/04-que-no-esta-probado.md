---
tags:
  - corto
  - ejercicio
  - pruebas
---

# 04 — Qué no está probado

!!! info "Antes de empezar"

    Tiempo: 30 minutos, más lo que tardes en añadir un solo caso que te importe.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Lista

Abre el proyecto que estés cerrando (notas, panel o clínica) y escribe diez situaciones que el código debería aguantar. Marca cuáles tienen prueba automática, cuáles compruebas a mano y cuáles no compruebas.

Ejemplos para no dejar la lista en abstracto: comilla en el título, sesión caducada, hueco duplicado, `POST` repetido, día sin citas, base apagada, token ausente.

Elige **una** de las que no tienen prueba y cuyo fallo te daría vergüenza en el integrador. Escríbela. Tiene que poder ponerse roja si quitas la protección.

!!! warning "Restricciones"

    - No intentes cubrir las diez. La lista es el entregable, junto con esa prueba nueva.
    - No cuentes como prueba un `console.log` que miraste una vez.
    - Si todas te salen “cubiertas” y llevas menos de cinco pruebas, estás contando deseos. Vuelve a la lista.

!!! success "Cómo sabes que está bien"

    - La lista cabe en una pantalla y cada línea es una situación, no un archivo.
    - Sabes decir, de la prueba nueva, qué línea del código la pone roja si la borras.
    - El integrador puede citar esta lista en el README como “esto no está automatizado”. Eso también es cerrar el ejercicio.
