---
tags:
  - ejercicio
  - largo
  - php
---

# 06 — Estructura

!!! info "Antes de empezar"

    Tiempo: medio día.

??? tip "Pista"

    Apoyo: PHP The Right Way (dependencias y bases de datos) y PSR-12 por encima. Composer solo para el autoload, sin paquetes de más.

El `index.php` de los ejercicios anteriores ha crecido. Pártalo hasta que cada archivo pueda explicarse con una frase.

## Forma objetivo

Una posible división, no un molde obligatorio:

- entrada: enruta método y camino, llama a una acción, no contiene SQL;
- una acción de listar y otra de crear;
- una clase o un grupo de funciones que ejecuta las consultas preparadas;
- una función de validación pura;
- plantillas PHP que solo imprimen, usando `e()`.

`index.php` queda en `public/`. El resto, fuera de `public/`, para que el servidor de desarrollo se arranque con la raíz en `public` y un visitante no descargue `src` ni el archivo de ejemplo de entorno.

!!! warning "Restricciones"

    - Ningún `require` circular. Si lo tienes, dos responsabilidades siguen pegadas.
    - Puedes introducir una clase de conexión. No introduzcas un framework.
    - El comportamiento visible no cambia respecto al ejercicio 5. Es una mudanza, no un producto nuevo.

!!! success "Cómo sabes que está bien"

    - Abres un archivo al azar y no aparecen a la vez SQL, HTML y `$_POST`.
    - Mueves la carpeta `public` como raíz del servidor y las facturas siguen listándose. Un archivo de `src` no se abre poniendo su ruta en el navegador.
    - El diff es aburrido a propósito: mismas reglas, otros archivos. Si aprovechaste para cambiar el diseño de la base, sepáralo en otro commit mental y termínalo antes o después, no durante la mudanza.
