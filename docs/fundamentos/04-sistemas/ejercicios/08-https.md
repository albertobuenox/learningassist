---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 08 — HTTPS en el servidor

!!! info "Antes de empezar"

    Tiempo: 2–3 horas, en la VM del ejercicio 3. El sitio estático ya responde por el puerto 80.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Lecturas, en este orden:

- Qué es un certificado, en la página de Let's Encrypt: https://letsencrypt.org/getting-started/

- Si tienes un dominio apuntando a esa VM: las instrucciones de Certbot para tu sistema y Nginx, https://certbot.eff.org/instructions

- Si no tienes dominio: mkcert, para un certificado de confianza solo en tus máquinas, https://github.com/FiloSottile/mkcert

## Qué dejar hecho

1. Nginx escucha en el **443** y sirve el mismo sitio. El navegador muestra el candado, o el aviso desaparece después de instalar la autoridad local de mkcert. Anota cuál de los dos caminos tomaste.
2. El puerto 80 responde con una redirección al mismo camino en `https://`, no con una copia distinta del sitio.
3. UFW permite 443/tcp. El 22 sigue abierto. El 80 sigue abierto solo porque la redirección lo necesita. Escríbelo así en tus notas: no está abierto “por si acaso”.
4. La clave privada del certificado no está en el repositorio. Si usaste Let's Encrypt, anota qué temporizador renueva el certificado y cómo lo comprobarías sin esperar tres meses. Si usaste mkcert, anota qué cambiaría con Let's Encrypt: un nombre público, el reto por el puerto 80 y la renovación.

!!! warning "Restricciones"

    - No desactives la comprobación del certificado en el cliente “para que cargue”.
    - No copies la clave privada a `public/` ni a una imagen de Docker.
    - No hace falta un reverse proxy hacia PHP en este ejercicio. El sitio estático basta para ver el candado. El proxy es el ejercicio 9.

!!! success "Cómo sabes que está bien"

    - `curl -I http://tu-nombre` muestra una redirección, y `curl -I https://tu-nombre` muestra 200. En mkcert, `curl` solo confía si le indicas la autoridad local: cuando eso pase, lo habrás entendido.
    - Cierras el 443 en el firewall y HTTPS deja de entrar desde fuera. Lo vuelves a abrir en la misma sesión.
    - Sabes dónde está el archivo de la clave privada y quién puede leerlo. Si el modo es legible por todos, no has terminado.
