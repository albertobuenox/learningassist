# Glosario — PHP

## Lenguaje

### PHP

Lenguaje pensado para la web, también útil en consola. En este curso se usa PHP 8: tipos, errores más estrictos y `match` existen. Los tutoriales de PHP 5 no son fuente.

### `<?php`

Apertura del código. Un archivo que solo contiene PHP no necesita la etiqueta de cierre. Un espacio en blanco antes de `<?php` ya es salida, y entonces las cabeceras HTTP fallan.

### Tipo

`int`, `float`, `string`, `bool`, `array`, y objetos. Puedes declarar tipos en parámetros y retornos. `declare(strict_types=1)` hace que `"3"` no se acepte donde pediste un `int`. Actívalo en los ejercicios y observa qué deja de colarse.

### Array

Mapa ordenado. Sirve como lista (`$xs[] = 1`) y como diccionario (`$xs['nombre']`). No es el array de JavaScript: aquí las claves pueden ser enteros o textos.

### Null y `??`

Ausencia de valor. `$a ?? $b` usa `$b` si `$a` no existe o es null. No sustituye a validar: solo elige un defecto.

### Función pura y efecto

Una función que calcula el total a partir de un array es fácil de probar. Una que además imprime y lee `$_POST` mezcla tres cosas. Los ejercicios empujan a separarlas.

### Excepción

Señal de que la operación no pudo cumplir su contrato. Capturarla en silencio (`catch` vacío) esconde el fallo. En la frontera HTTP la conviertes en un código 500 y un mensaje que no cuenta tus contraseñas.

### Composer

Gestor de dependencias de PHP. Genera `vendor/` y un autoload. `vendor/` no se versiona. El framework, cuando llegue, se instala así; la asignatura no empieza por ahí.

### PSR

Recomendaciones del PHP-FIG (estilo, autoload, interfaces de log y de HTTP). PSR-12 es el estilo que usarás al ordenar el proyecto. No hace falta memorizar el número: sí mirar cómo se nombran clases y archivos. https://www.php-fig.org/psr/

## Web

### Petición

Lo que el navegador envía: método, camino, cabeceras, cuerpo. PHP lo reparte en `$_GET`, `$_POST`, `$_SERVER` y el cuerpo crudo.

### Respuesta

Código de estado, cabeceras y cuerpo. `header()` va antes de cualquier salida. `http_response_code()` fija el estado.

### Servidor embebido

`php -S localhost:8000`. Vale para desarrollar. No es el servidor de producción. En producción, Nginx o Apache hablan con PHP-FPM.

### PHP-FPM

El proceso que ejecuta PHP, separado del servidor web. Nginx recibe HTTP y le pasa el trabajo. Lo verás en Sistemas cuando juntes las dos asignaturas.

### Front controller

Un único `index.php` que recibe las rutas y reparte. Evita un archivo PHP por cada pantalla con la configuración copiada. El ejercicio 2 puede ser un solo archivo; el 6 ya no.

### Superglobal

Variable que PHP rellena (`$_GET`, `$_POST`, `$_SESSION`, `$_COOKIE`). Es entrada de fuera. Trátala como no confiable hasta validarla.

### Sesión

Datos en el servidor asociados a una cookie de identificador. `session_start()` al principio. El carrito o el id de usuario viven aquí; la contraseña no.

### Cookie

Dato que el navegador reenvía. La de sesión debe ir marcada para que el JavaScript de la página no la lea (`HttpOnly`) y, con HTTPS, solo por TLS (`Secure`). En local sin HTTPS, anota qué bandera todavía no puedes activar.

### Escapar la salida

Convertir un texto para que el HTML lo muestre como texto, no como etiqueta. `htmlspecialchars` al pintar. Es la defensa de cada página, no un filtro de una sola vez al guardar.

### Hash de contraseña

`password_hash` produce una cadena que no permite recuperar la contraseña. `password_verify` la comprueba. No uses `md5` ni `sha1` para esto. No guardes la contraseña en claro “para depurar”.

### CSRF

Un sitio ajeno provoca un `POST` al tuyo y el navegador adjunta solo la cookie de sesión. La defensa de este curso es un token que tu HTML incluye y que un formulario de otro origen no conoce. Sin token, 403. No es lo mismo que estar sin sesión: eso es 401.

### API

Rutas que representan el recurso en JSON, pensadas para otro programa (React, `curl`), no para un humano que lee HTML. Mismas reglas de negocio que el formulario. Distinto código cuando falta la sesión: la API no redirige al login.

### Contrato

El documento de HTTP que fija método, camino, códigos y forma del JSON. La implementación que no coincide con él está mal, aunque “funcione” en tu máquina.

## Datos

### PDO

Extensión para hablar con bases desde PHP con una interfaz común. La conexión lleva host, nombre, usuario y contraseña. Esos cuatro datos salen de configuración, no van escritos en el repositorio.

### Consulta preparada

El SQL con marcadores (`:nombre` o `?`) y los valores aparte. El motor no concatena el texto del usuario dentro de la frase SQL. Construir la consulta con interpolación de cadenas es el hábito que este curso corrige.

### CRUD

Crear, leer, actualizar, borrar. El proyecto final es un CRUD pequeño a propósito: el valor está en las fronteras (validación, SQL, sesión), no en el número de pantallas.

## Organización

### Capa

Un trozo con una responsabilidad. Entrada HTTP, reglas (¿este título vale?), persistencia (PDO), vista (HTML). Si las cuatro están en `index.php`, el ejercicio 6 no está hecho.

### Autoload

Mecanismo por el que una clase se carga al usarla, sin una lista de `require`. Composer lo da con PSR-4. Hasta entonces, `require` explícito es honesto y suficiente.

### Entorno

Valores que cambian entre tu máquina y otra (`DSN`, usuario de la base). Un archivo que no se versiona, más un ejemplo sin secretos que sí se versiona.
