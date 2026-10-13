# Cursos — sistemas, servidores y Docker

Empieza por la VM y el arranque de Ubuntu. Docker sin haber visto un proceso y un puerto se convierte en pegar archivos.

## Gratuitos

### Linux Upskill Challenge

- https://linuxupskillchallenge.org/
- Veinte lecciones breves, una por día de laborable, pensadas para un servidor Ubuntu expuesto con cuidado. Cubre shell, usuarios, SSH, logs y servicios. El mejor gratuito para el ejercicio 2.

### The Linux Command Line (William Shotts)

- https://linuxcommand.org/tlcl.php
- Libro gratuito. Úsalo como consulta cuando una palabra del glosario (permisos, procesos, redirecciones) se quede corta, no como lectura lineal obligatoria. Los capítulos de permisos y de procesos cubren el ejercicio 3.

### Initial Server Setup with Ubuntu (DigitalOcean)

- https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu
- La checklist canónica: usuario, `sudo`, SSH, UFW. Está validada en Ubuntu 22.04 y 24.04. Síguela en una VM. Lee el aviso de no cerrarte la puerta SSH.

### Nginx, Beginner’s Guide

- https://nginx.org/en/docs/beginners_guide.html
- Corta y oficial. Suficiente para el server block del ejercicio 3. La referencia completa está en el mismo sitio cuando una directiva no haga lo que crees.

### Docker, Getting Started

- https://docs.docker.com/get-started/
- Serie oficial: instalar, primer contenedor, primera imagen, publicar. Hazla antes de escribir Compose.

### Docker Curriculum

- https://docker-curriculum.com/
- Tutorial gratuito, más narrativo que la documentación. Buen segundo pase si la guía oficial se te hace telegráfica.

### Guía de PHP en Docker (oficial)

- https://docs.docker.com/guides/php/
- Cuando llegues al backend PHP y quieras el contenedor alineado con lo que Docker documenta hoy (desarrollo, pruebas, varias etapas). No la uses para saltarte el ejercicio 5.

### Let's Encrypt y Certbot

- https://letsencrypt.org/getting-started/
- https://certbot.eff.org/instructions
- El camino con dominio real. Let's Encrypt explica qué es el certificado. Certbot pregunta el sistema y el servidor web, y da los comandos para ese par. Úsalos en el ejercicio 8 solo si tienes un nombre apuntando a la VM.

### mkcert

- https://github.com/FiloSottile/mkcert
- Certificados de confianza en local, sin dominio. Sirve para cerrar el ejercicio 8 en la VM de prácticas. No sustituye a Let's Encrypt el día que el sitio tenga un nombre público.

### Mozilla SSL Configuration Generator

- https://ssl-config.mozilla.org/
- Cuando Nginx ya termina TLS y quieres un perfil de cifrados mantenido por alguien que se dedica a eso. Genera la configuración para tu versión de Nginx. Úsalo como referencia del ejercicio 8, no como un archivo que se pega sin leer.

### Play with Docker

- https://labs.play-with-docker.com/
- Laboratorio en el navegador, temporal. Vale para probar un comando. No dejes ahí el proyecto: la sesión se borra.

## De pago

### Docker Mastery (Bret Fisher, Udemy)

- https://www.udemy.com/course/docker-mastery/
- El curso de pago de referencia, de un Docker Captain. Imágenes, volúmenes, Compose y, más adelante, orquestación. Cómpralo si vas a usar Docker en el trabajo y no solo en el ejercicio 7. Pide nociones de terminal y de un servidor; por eso va después del ejercicio 2.

### KodeKloud, Docker for the Absolute Beginner

- https://kodekloud.com/courses/docker-for-the-absolute-beginner/
- Laboratorios guiados. La plataforma es de pago, con cursos sueltos a menudo accesibles en tramo introductorio. Útil si aprendes mejor rompiendo un lab que leyendo.

## Qué dejar para más adelante

Kubernetes, service mesh y “un clúster de tres nodos”. El ejercicio 7 con Compose es el fundamento. Orquestar antes de saber qué es un volumen produce YAML que nadie puede explicar.
