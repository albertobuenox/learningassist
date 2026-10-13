# Glosario — sistemas, servidores y Docker

## Máquina

### Servidor

Un ordenador, virtual o no, que ofrece un servicio (web, base de datos, SSH). También se llama así al programa que escucha (Nginx es un servidor web). Cuando algo falle, aclara cuál de los dos quieres decir.

### SSH

Acceso cifrado a una shell remota. La clave pública se queda en el servidor (`authorized_keys`); la privada no sale de tu máquina. Entrar como root por contraseña es un hábito que este curso abandona.

### Usuario y privilegios

El día a día no usa root. `sudo` ejecuta un comando con privilegios y deja rastro. Un servicio (Nginx, Postgres) también corre con un usuario propio, a menudo sin login.

### Firewall

Filtro de qué puertos aceptan conexiones desde fuera. UFW es un frente cómodo sobre las reglas de Linux. Abrir “todo” para que funcione no es una configuración: es apagar el filtro.

### Puerto

Número que distingue servicios en una misma IP. 22 suele ser SSH, 80 HTTP, 443 HTTPS, 5432 PostgreSQL. Que el programa escuche en el puerto no implica que el firewall deje pasar ese puerto.

### Proceso y servicio

Un proceso es un programa en ejecución. Un servicio (systemd) es la forma de arrancarlo al iniciar la máquina, reiniciarlo si muere y ver su estado (`systemctl status`).

### DNS

Traduce un nombre (`tienda.test`) a una IP. Si el nombre no resuelve, ningún Nginx del mundo va a arreglarlo. En local se puede falsificar con el archivo `hosts`, y hay que recordar que lo hiciste.

### HTTP y HTTPS

HTTP es el protocolo de la petición y la respuesta. HTTPS es ese mismo HTTP dentro de TLS. El vocabulario de métodos y códigos está en la carpeta de HTTP. Aquí importa el tramo del servidor: quién termina TLS y qué puerto ve el visitante.

### Certificado

Un documento que ata una clave pública a un nombre. El navegador lo comprueba contra una autoridad en la que ya confía. Sin esa confianza, el candado no aparece aunque el cifrado exista. mkcert crea una autoridad solo para tus máquinas. Let's Encrypt crea certificados que cualquier navegador acepta, para un nombre público.

### Clave privada

La mitad que no sale del servidor. Quien la tiene puede hacerse pasar por tu sitio. No va al repositorio, ni a la imagen, ni a un directorio que Nginx sirva como archivos.

### Renovación

Un certificado caduca. Certbot deja un temporizador para pedir otro antes de esa fecha. Un certificado vencido se ve igual que uno mal instalado: el navegador se niega. La diferencia está en la fecha.

### Contenido mixto

Una página cargada por HTTPS que pide un trozo por HTTP. El navegador lo bloquea o avisa. Pasa cuando la aplicación no se entera de que, de puertas afuera, el esquema era `https`.

### Reverse proxy

Nginx recibe la petición pública y la pasa a otro proceso (PHP, Node) que escucha en un puerto interno. El visitante no tiene por qué ver el puerto 3000.

### Raíz del sitio

El directorio desde el que Nginx sirve archivos. No es tu carpeta de usuario. Confundirlas es la causa típica de un 404 con el servicio “en marcha”.

### Log

Archivo o diario donde el servicio escribe qué hizo. `journalctl` lee el diario de systemd. Mirar el log es el paso anterior a cambiar configuración al azar.

### Permisos

Quién puede leer o escribir un archivo. Si Nginx no puede leer la raíz del sitio, verás 403. El arreglo no es `chmod 777`.

## Docker

### Imagen

Plantilla de solo lectura: sistema de archivos y el comando de arranque. Se construye con un Dockerfile o se descarga de un registro. No “está en marcha”.

### Contenedor

Una instancia en ejecución (o parada) de una imagen. Puedes borrar el contenedor y la imagen sigue. Puedes tener dos contenedores de la misma imagen.

### Registro

Servicio que guarda imágenes. Docker Hub es el público. “Publicar” manda la imagen allí. Lo que esté copiado dentro de la imagen (contraseñas, `.env`) se publica con ella.

### Dockerfile

Receta de la imagen, instrucción a instrucción. Cada instrucción suele ser una capa. El orden importa para la caché: lo que cambia poco (dependencias) va antes que el código que cambia cada hora.

### Capa

Una pieza cacheada de la imagen. Cambiar una línea invalida esa capa y las siguientes.

### Volumen

Almacén gestionado por Docker, fuera del sistema de archivos efímero del contenedor. La base de datos va en un volumen si quieres conservar los datos al recrear el contenedor.

### Bind mount

Montar una carpeta tuya dentro del contenedor. Útil en desarrollo para ver el código sin reconstruir. No es lo mismo que un volumen: la carpeta es tuya y viaja con tus permisos del anfitrión.

### Red de Docker

Los contenedores de un mismo Compose se resuelven por el nombre del servicio (`db`, no `localhost`). `localhost` dentro de un contenedor es ese contenedor, no el de al lado ni tu portátil.

### Puerto publicado

`-p 8080:80` une el puerto 8080 de tu máquina con el 80 del contenedor. Sin publicarlo, el servicio existe y desde tu navegador no llega.

### Variable de entorno

Configuración que cambia entre máquinas (clave, nombre de base, modo). La imagen no debería hornear el secreto. Compose puede leer un `.env` que no se sube a git.

### Docker Compose

Un archivo que describe varios servicios, redes y volúmenes, y los levanta juntos. Es la unidad de “el entorno”, no el `docker run` de doce banderas que nadie anotó.

### Imagen oficial

La que publica el proyecto (postgres, nginx, php). Preferirla a un Dockerfile copiado de un foro de 2018. Mirar la página del Docker Hub de esa imagen: dice variables, puertos y cómo persisten los datos.

### .dockerignore

Lo que no debe entrar en el contexto de construcción. `node_modules`, `.git` y `.env` suelen estar ahí. Si el contexto es enorme, la construcción se arrastra.
