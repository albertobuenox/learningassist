# Fundamentos de desarrollo

Recorrido para **recordar** el oficio, no para coleccionar certificados. Cada carpeta tiene glosario, cursos (gratuitos y de pago) y enunciados. Las soluciones no están escritas: el criterio de cierre sí.

Los enlaces se contrastaron en octubre de 2026. Los precios de Udemy, Coursera, Laracasts, Frontend Masters e Interaction Design Foundation cambian; comprueba el importe en la página antes de pagar.

## Asignaturas

| Orden | Carpeta | Para qué |
| --- | --- | --- |
| 0 | [00-git](00-git/README.md) | Historia del proyecto, el primer día |
| 1 | [01-bases-de-datos](01-bases-de-datos/README.md) | Modelar datos y pedirles cosas con SQL sin sorpresas |
| 2 | [02-frontend-node-react](02-frontend-node-react/README.md) | HTML, CSS, JavaScript, un servidor Node y React |
| 3 | [03-http](03-http/README.md) | El contrato que comparten el navegador, Nginx y PHP |
| 4 | [04-sistemas](04-sistemas/README.md) | Ubuntu, Docker y HTTPS en un servidor tuyo |
| 5 | [05-backend-php](05-backend-php/README.md) | PHP 8: HTML, JSON, sesión y token |
| 6 | [06-pruebas](06-pruebas/README.md) | Un caso que se pone rojo solo cuando el código se rompe |
| 7 | [07-ui-ux](07-ui-ux/README.md) | Decisiones de interfaz que se pueden justificar |

Git se empieza el primer día, aunque sigas por otra carpeta: el ejercicio 1 cabe en una hora. UI/UX puede ir en paralelo desde el principio. HTTP va después del servidor Node y antes de la API de PHP. Las pruebas esperan a que exista una función pura o una ruta.

## Cómo estudiar cada asignatura

1. Lee el `README.md` de la carpeta y el `glosario.md` una vez, sin memorizar.
2. Haz el primer ejercicio **antes** de abrir un curso largo. Así descubres qué ya recuerdas.
3. Cuando te atasques, abre solo el curso marcado en ese enunciado. Vuelve al ejercicio.
4. Cierra el ejercicio cuando puedas responder las preguntas de “cómo sabes que está bien” sin mirar apuntes.
5. Anota en una frase: qué decidiste y qué duda te queda. Esa duda es el siguiente tema, no un curso nuevo entero.

Si un curso de pago repite lo que ya resuelves en los enunciados, no lo compres. Paga cuando quieras profundidad (índices, Compose en serio, PHP orientado a objetos, sistema visual) o un certificado con nombre.

## Qué es un enunciado aquí

Cada archivo en `ejercicios/` plantea un problema, restricciones y una forma de autoevaluarte. No trae el código, el SQL, el Dockerfile ni el wireframe resueltos. Si te bloqueas, el siguiente paso es una pista o un concepto del glosario, no la solución completa.

## Cierre del recorrido

Cuando hayas cerrado el proyecto de cada carpeta, el [proyecto integrador](proyecto-integrador.md) junta diseño, datos, el contrato HTTP, PHP, React, una prueba y un entorno con Docker. Es el examen: una pieza pequeña que un compañero podría arrancar clonando el repositorio.
