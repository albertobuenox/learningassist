---
tags:
  - ejercicio
  - frontend
  - medio
---

# 04 — CLI que resume un CSV

!!! info "Antes de empezar"

    Node fuera de la web. Tiempo: 90 minutos.

??? tip "Pista"

    Apoyo: documentación de `node:fs` y de `process.argv`.

## Entrada

Un archivo `ventas.csv` que tú creas:

```text
fecha,producto,importe
2026-04-01,cafe,2.50
2026-04-01,te,2.00
2026-04-02,cafe,2.50
2026-04-02,cafe,
```

La última fila tiene el importe vacío.

## Salida

`node resumen.js ventas.csv` imprime:

- cuántas filas válidas hay;
- el importe total de las válidas;
- el producto con mayor importe acumulado;
- cuántas filas se ignoraron, y por qué (importe vacío o no numérico).

Si el archivo no existe, el proceso termina con un mensaje en la salida de error y un código distinto de cero. Compruébalo con `echo $?` en la shell, justo después.

!!! warning "Restricciones"

    - Sin librerías de CSV. Parte líneas y comas. Tus datos no llevan comas dentro del nombre; escribe esa limitación en un comentario.
    - No uses el servidor del ejercicio 3. Este programa acaba al terminar.

!!! success "Cómo sabes que está bien"

    - ¿La fila rota entra en el total? No debería.
    - ¿“Mayor importe” y “más unidades” podrían dar productos distintos? Tu enunciado pide importe. Si tu código cuenta filas, está respondiendo otra pregunta.
    - Ejecutas sin argumentos. ¿El mensaje dice que falta la ruta, o explota al leer `undefined`?
