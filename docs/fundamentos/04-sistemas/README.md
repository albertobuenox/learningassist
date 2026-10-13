# Sistemas: servidores y Docker

Objetivo: dejar de tratar el entorno como magia. Un servidor Ubuntu mínimo, un sitio servido por Nginx, y Docker para describir ese entorno en archivos que otra máquina puede repetir.

Todo el trabajo es de **configuración y diagnóstico**. No hay ejercicios de romper servicios ajenos ni de esconder procesos.

## Al terminar deberías poder

- Entrar por SSH con clave, con un usuario que no es root, y con el firewall permitiendo solo lo que tú nombraste.
- Explicar por qué un puerto, un proceso y un directorio de archivos son tres cosas distintas cuando “la web no carga”.
- Escribir un Dockerfile y un Compose que levanten una app y su base, con datos que sobreviven a `docker compose down` si decidiste un volumen, y que no sobreviven si no lo decidiste.
- Saber qué va en una imagen, qué va en una variable de entorno y qué no debe publicarse en un registro.
- Servir el sitio por HTTPS, redirigir el puerto 80 y dejar el proceso de la aplicación en un puerto que el firewall no publica.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md)
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [La web no carga](ejercicios/01-la-web-no-carga.md) | Diagnosticar sin tocar aún el servidor |
| 2 | [Primer arranque](ejercicios/02-primer-arranque.md) | Usuario, SSH, firewall |
| 3 | [Sitio estático](ejercicios/03-nginx-estatico.md) | Nginx y un server block |
| 4 | [Imagen y contenedor](ejercicios/04-imagen-y-contenedor.md) | Docker a mano |
| 5 | [Dockerfile](ejercicios/05-dockerfile.md) | Construir una imagen propia |
| 6 | [Compose](ejercicios/06-compose.md) | App y base de datos juntas |
| 7 | [Proyecto](ejercicios/07-proyecto-entorno.md) | Entorno repetible y documentado |
| 8 | [HTTPS](ejercicios/08-https.md) | Certificado, 443 y redirección |
| 9 | [Proxy](ejercicios/09-proxy.md) | TLS en Nginx, la app por dentro |

## Dónde practicar

Una máquina virtual local (Multipass, UTM, VirtualBox) o un VPS barato que puedas borrar. No practiques el firewall en el portátil desde el que trabajas sin saber cómo recuperar el acceso. Docker Desktop o Docker Engine en Linux valen para los ejercicios 4 a 7. El 2, el 3, el 8 y el 9 piden un Linux de verdad, aunque sea virtual. El 8, además, pide un dominio si quieres Let's Encrypt; sin dominio, mkcert cierra el ejercicio en local.

## Criterio de cierre

Otra persona, con Docker instalado, levanta el proyecto del ejercicio 7. En la VM, el 443 responde el sitio, el 80 redirige, y el puerto de PHP o Node no se abre desde fuera.
