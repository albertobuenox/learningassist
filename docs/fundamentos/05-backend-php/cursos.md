# Cursos — backend PHP

Un vídeo de “PHP en 30 minutos” de 2014 enseña hábitos que luego hay que desaprender (`mysql_query`, contraseñas en claro, mezclar SQL y HTML). Las fuentes de abajo están en PHP 8.

## Gratuitos

### Manual de PHP

- https://www.php.net/manual/es/getting-started.php
- Empieza por “Getting Started” y el tutorial de idioma. La referencia de `password_hash`, PDO y sesiones es la que manda cuando un blog discrepe.
- Versión en inglés, a menudo más al día en los comentarios: https://www.php.net/manual/en/

### PHP: The Right Way

- https://phptherightway.com/
- No es un curso con ejercicios: es el mapa de prácticas actuales (versiones, Composer, seguridad, bases de datos). Léelo en diagonal al empezar y vuelve a la sección que toque cada ejercicio. Hay traducción enlazada desde la propia página.

### Laracasts, episodios sueltos en abierto

- https://laracasts.com/series/php-for-beginners-2023-edition
- La serie “PHP For Beginners” (edición 2023, PHP 8) es el mejor vídeo de fundamentos. Parte del catálogo de Laracasts se ve sin suscripción y el resto pide cuenta de pago. Si una lección está cerrada, no busques un sucedáneo viejo: usa el manual para ese tema y sigue.

### Exercism, pista de PHP

- https://exercism.org/tracks/php
- Más de cien ejercicios del lenguaje, gratis, con análisis del código. Úsalo en paralelo al ejercicio 1 para soltar sintaxis. La guía de aprendizaje del track apunta al manual y a The Right Way: https://exercism.org/docs/tracks/php/learning

### Composer, introducción

- https://getcomposer.org/doc/00-intro.md
- Cuando llegues al ejercicio 6. Media hora. No hace falta un curso aparte.

### OWASP, chuleta de configuración PHP

- https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html
- Lectura corta de producción: errores que no se muestran al visitante, sesión, exposición de archivos. Léela al cerrar el proyecto, no el primer día.

### OWASP, prevención de CSRF

- https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- Léela justo antes del ejercicio 7. Quédate con el token sincronizado con la sesión. No hace falta implementar todas las variantes de la chuleta.

## De pago

### Laracasts (suscripción)

- https://laracasts.com/
- La opción de pago que vale la pena en PHP. Además de “PHP For Beginners”, el catálogo tiene principios de orientación a objetos y Laravel. Haz el de objetos cuando el ejercicio 6 te pida clases y aún no te salgan.
- Laravel From Scratch, en el mismo sitio, es el paso **siguiente** al proyecto de notas, no el reemplazo.

### PHP for Beginners, solo si Laracasts no te encaja

Hay varios cursos en Udemy con ese título y calidades distintas. Si compras uno, comprueba que el temario dice PHP 8, PDO y `password_hash`. Si el temario muestra la extensión `mysql_` (sin la i), es material viejo: no lo uses.

## Qué dejar para más adelante

Laravel, Symfony, colas, eventos y un ORM. El proyecto integrador permite rehacer el backend en Laravel **después** de haberlo escrito en PHP pelado, para comparar. Hacerlo al revés salta la asignatura.
