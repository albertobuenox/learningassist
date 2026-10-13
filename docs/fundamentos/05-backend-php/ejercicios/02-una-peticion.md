---
tags:
  - ejercicio
  - largo
  - php
---

# 02 — Una petición

!!! info "Antes de empezar"

    El salto a HTTP. Tiempo: 2 horas. Un solo `index.php` basta.

??? tip "Pista"

    Apoyo: manual de `$_SERVER`, `$_GET`, `header` y `http_response_code`. Servidor: `php -S localhost:8000`.

## Rutas

Míralas con `$_SERVER['REQUEST_URI']` y el método. No hace falta un router de Composer.

- `GET /` muestra un HTML mínimo con un formulario: concepto (texto) e importe (número). El formulario envía con `POST` a `/facturas`.
- `POST /facturas` no guarda nada todavía. Si el concepto está vacío o el importe no es un número mayor que cero, responde **400** y un HTML corto que dice qué falló. Si vale, responde **201** y repite el concepto y el importe.
- Cualquier otra ruta responde **404**.

Prueba con el navegador y con `curl`. El navegador esconde el código de estado; `curl -i` no.

!!! warning "Restricciones"

    - Nada de SQL.
    - El 201 y el 400 se ven en el código de estado, no solo en un párrafo que dice “error” con un 200.
    - No uses `echo` antes de fijar el estado. Si te sale “headers already sent”, ese eco sobraba.

!!! success "Cómo sabes que está bien"

    - Un `GET` a `/facturas` no crea una factura imaginaria. ¿Qué código le das, y por qué no es 201?
    - El importe `0` y el importe `abc` fallan. El importe `1.5` pasa. Anota dónde convertiste el texto del formulario en número y qué pasa con la coma decimal.
    - Recargar tras el `POST` vuelve a enviar. Es el comportamiento del navegador. ¿Dónde lo notarás cuando de verdad guardes? Escríbelo; el arreglo (redirigir tras guardar) llega en el ejercicio 4.
