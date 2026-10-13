---
tags:
  - ejercicio
  - largo
  - php
---

# 01 — CLI de facturas

!!! info "Antes de empezar"

    PHP como lenguaje, en la terminal. Tiempo: 2 horas.

??? tip "Pista"

    Apoyo: manual, capítulo de tipos y de funciones. Exercism si la sintaxis se atasca.

## Programa

`php facturas.php datos.csv` lee un CSV (fecha, concepto, importe) y escribe:

- número de líneas válidas;
- total con dos decimales;
- el concepto de mayor importe;
- las líneas ignoradas (importe vacío o negativo).

Si falta el argumento o el archivo, el mensaje va a la salida de error y el código de salida no es cero.

Los números se suman en céntimos enteros o con un redondeo que tú declares. Un comentario de tres líneas explica por qué `0.1 + 0.2` no es asunto solo de JavaScript.

!!! warning "Restricciones"

    - `declare(strict_types=1);`
    - Una función calcula el resumen a partir de un array de filas ya parseadas. Otra imprime. No hay HTML.
    - Sin framework y sin base de datos.

!!! success "Cómo sabes que está bien"

    - Una fila con importe `-3` no resta del total: se ignora, y el contador de ignoradas sube.
    - Puedes llamar a la función de resumen desde otro script de prueba sin imprimir nada. Si no puedes, la función todavía hace dos trabajos.
    - El archivo de ejemplo del enunciado de Node (ejercicio 4 de frontend) te sirve de entrada. El resultado numérico debería coincidir. Si no coincide, uno de los dos programas está respondiendo otra pregunta.
