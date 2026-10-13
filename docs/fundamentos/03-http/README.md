# HTTP, el contrato

Objetivo: un solo vocabulario para el navegador, Node, Nginx y PHP. Una petición tiene método, camino, cabeceras y cuerpo. Una respuesta tiene código, cabeceras y cuerpo. Una página HTML y una API JSON son dos representaciones del mismo recurso, no dos mundos.

Haz esta carpeta después del servidor JSON de frontend y antes de los ejercicios de PHP. El ejercicio 5 es el contrato que el backend tendrá que cumplir.

## Al terminar deberías poder

- Leer una transacción con `curl -v` y señalar método, camino, cabeceras, cuerpo y código.
- Elegir el código de estado antes de escribir el mensaje.
- Decir qué métodos son seguros y cuáles, repetidos, no deberían duplicar un efecto.
- Escribir el contrato de una API pequeña: rutas, códigos y forma del JSON, sin implementarlo todavía.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md) — MDN, por secciones, no entero.
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [Una transacción](ejercicios/01-una-transaccion.md) | Leer `curl -v` |
| 2 | [Dos representaciones](ejercicios/02-dos-representaciones.md) | HTML y JSON |
| 3 | [Repetir la petición](ejercicios/03-repetir-la-peticion.md) | Seguro e idempotente |
| 4 | [Otro origen](ejercicios/04-otro-origen.md) | Lo que el navegador añade |
| 5 | [Contrato de la clínica](ejercicios/05-contrato-de-la-clinica.md) | La API, en papel |

## Criterio de cierre

El contrato del ejercicio 5 cabe en una página y otra persona puede implementar el servidor o el cliente sin llamarte. Si hace falta una llamada para saber qué código devuelve un hueco ocupado, el contrato no está cerrado.
