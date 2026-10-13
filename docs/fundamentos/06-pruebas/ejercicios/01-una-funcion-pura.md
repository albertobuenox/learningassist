---
tags:
  - ejercicio
  - medio
  - pruebas
---

# 01 — Una función pura

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos. La función es la del resumen de facturas, en Node o en PHP. Si todavía mezcla impresión y cálculo, sepáralas antes: la prueba llama a la que calcula.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Casos

Escribe una prueba por caso. Datos de entrada pequeños, escritos en la propia prueba, no leídos de un CSV externo.

1. Dos líneas válidas. El total es la suma. El número de válidas es 2.
2. Una línea con importe vacío. No entra en el total. El contador de ignoradas es 1.
3. Una línea con importe negativo. Igual que la vacía: ignorada, no restada.
4. Ninguna línea válida. El total es 0 y no hay “concepto ganador”, o hay el valor que tú definiste para ese caso. Escríbelo.

Arranca el runner. Las cuatro pasan.

!!! warning "Restricciones"

    - La prueba no imprime el total para que lo mires. Compara.
    - No llames a la base de datos ni al servidor.
    - Un caso que falle debe nombrar la situación (“importe vacío”), no llamarse `test1`.

!!! success "Cómo sabes que está bien"

    - Cambias la función para que el importe vacío sume cero como si fuera un número, o para que lo sume mal. La prueba 2 falla. La deshaces y vuelve a pasar.
    - Puedes ejecutar solo el runner, sin argumentos manuales, y el código de salida es 0 cuando todo pasa.
