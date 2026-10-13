# Backend con PHP

Objetivo: recordar PHP 8 como lenguaje de la web, no como colección de etiquetas sueltas. Una petición entra, se valida, toca la base con consultas parametrizadas y sale por una respuesta con código y cuerpo claros.

Laravel y otros frameworks quedan **después** del proyecto. Si los usas antes, no verás qué te están ahorrando.

## Al terminar deberías poder

- Escribir un script de consola y una página que lean datos distintos (argumentos frente a `$_GET` / `$_POST`).
- Separar entrada, reglas y salida. La SQL no vive dentro del HTML.
- Guardar una contraseña con `password_hash` y comprobarla con `password_verify`.
- Hablar con PostgreSQL o MySQL mediante PDO y consultas preparadas.
- Devolver 200, 201, 400, 401, 403 o 404 a propósito, no por accidente.
- Exponer el mismo recurso en HTML y en JSON, y rechazar un `POST` con sesión pero sin token.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md) — el manual y PHP The Right Way; Laracasts si quieres vídeo.
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [CLI de facturas](ejercicios/01-cli-facturas.md) | Lenguaje, sin web |
| 2 | [Una petición](ejercicios/02-una-peticion.md) | GET, POST y códigos |
| 3 | [Formulario](ejercicios/03-formulario.md) | Validar y escapar la salida |
| 4 | [PDO](ejercicios/04-pdo.md) | Consultas parametrizadas |
| 5 | [Sesión](ejercicios/05-sesion.md) | Login mínimo |
| 6 | [Estructura](ejercicios/06-estructura.md) | Sacar SQL y HTML de un solo archivo |
| 7 | [CSRF](ejercicios/07-csrf.md) | El `POST` con solo la cookie no escribe |
| 8 | [API JSON](ejercicios/08-api-json.md) | El mismo recurso para React |
| 9 | [Proyecto](ejercicios/09-proyecto-notas.md) | CRUD, token y JSON |

## Herramienta

PHP 8.2 o superior (`php -v`). Para los primeros ejercicios basta el servidor de desarrollo (`php -S`). PDO con el driver de PostgreSQL (`pdo_pgsql`) o de MySQL, el mismo motor que hayas usado en bases de datos. Composer entra en el ejercicio 6, no antes: https://getcomposer.org/doc/00-intro.md

## Criterio de cierre

El proyecto de notas crea, lista, edita y borra. Una comilla en el título no rompe la consulta ni el HTML. Cerrar sesión impide ver las notas. Un `POST` con la cookie y sin token no escribe. `GET /api/notas` devuelve JSON.
