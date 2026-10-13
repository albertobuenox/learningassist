---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 03 — Nginx y un sitio estático

!!! info "Antes de empezar"

    Tiempo: 2 horas. Guía: https://nginx.org/en/docs/beginners_guide.html

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

En la misma VM del ejercicio 2, sirve la ficha de producto del frontend (o un `index.html` de una línea si aún no existe).

## Qué lograr

- Nginx instalado desde los paquetes de la distribución, arrancado con systemd, habilitado al reiniciar. Reinicia la VM y comprueba que sigue.
- Los archivos viven en un directorio pensado para ello (por ejemplo bajo `/var/www`), con permisos de lectura para el usuario del servicio, no en un home con permisos cerrados a cal y canto.
- Un server block con `server_name` y `root` explícitos. Sabes qué archivo gana si también existe el sitio por defecto.
- UFW permite 80/tcp. SSH sigue permitido.
- La página se ve desde el anfitrión usando la IP de la VM.

!!! warning "Restricciones"

    - No uses Docker en este ejercicio. El contraste con el ejercicio 4 es precisamente que aquí ves el servicio en el sistema.
    - Si algo responde 403 o 404, el siguiente paso es el log de Nginx y los permisos, y solo después un cambio de configuración. Pega en tus notas la línea del log que te dio la pista.

!!! success "Cómo sabes que está bien"

    - `systemctl status` y la página coinciden: el servicio activo y el HTML que esperabas, no el de bienvenida.
    - Cambias una palabra del HTML, recargas, y se ve. Si no se ve, estás editando otro directorio del que Nginx lee.
    - Cierras el puerto 80 en UFW y la página deja de llegar desde fuera, mientras SSH sigue. Vuelves a abrirlo. Ese ida y vuelta vale más que otro tutorial.
