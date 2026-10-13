# Pruebas

Objetivo: dejar de usar el navegador como único instrumento. Una prueba automática ejecuta un trozo, compara con lo que esperabas y se puede repetir. El navegador sigue sirviendo para lo que se ve. No sirve para recordar, dentro de un mes, que un importe vacío no debía sumarse.

Haz el primer ejercicio en cuanto tengas la función pura de las facturas (PHP o Node). El resto, cuando exista el contrato HTTP.

## Al terminar deberías poder

- Distinguir una prueba de una función que imprime “ok”.
- Escribir primero el caso que falla, verlo fallar y luego hacer el cambio mínimo que lo pone verde.
- Cubrir un caso de la frontera HTTP (código y cuerpo) sin abrir el navegador.
- Nombrar qué no está probado. Una lista honesta vale más que diez pruebas que repiten el caso feliz.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md)
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [Una función pura](ejercicios/01-una-funcion-pura.md) | El total de las facturas |
| 2 | [El caso que falla](ejercicios/02-el-caso-que-falla.md) | Rojo, luego verde |
| 3 | [La frontera HTTP](ejercicios/03-la-frontera-http.md) | Código y cuerpo |
| 4 | [Qué no está probado](ejercicios/04-que-no-esta-probado.md) | La lista honesta |

## Herramienta

En Node, el runner que ya viene: `node --test`. Documentación: https://nodejs.org/api/test.html

En PHP, PHPUnit: https://phpunit.de/getting-started.html

Elige uno para el ejercicio 1 y quédate con él en el 2. El 3 puede ser un script que lance `curl` y compruebe el código, si montar el framework de HTTP te come el día. Anota esa elección.

## Criterio de cierre

Borras a propósito una condición (el importe vacío vuelve a sumar, o el 401 desaparece) y una orden, una sola, se pone roja. Si tienes que recorrer la aplicación a mano para enterarte, la prueba no estaba.
