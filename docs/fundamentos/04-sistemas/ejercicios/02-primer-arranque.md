---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 02 — Primer arranque

!!! info "Antes de empezar"

    Tiempo: 2–3 horas, en una VM o un VPS desechable. Guía: https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu y las lecciones de SSH de Linux Upskill Challenge.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Qué dejar hecho

1. Un usuario con tu nombre, en el grupo que puede usar `sudo`. Entras por SSH con ese usuario.
2. La autenticación por clave. La contraseña de SSH deja de ser el método de entrada. Antes de cerrar la sesión actual, abre **otra** terminal y comprueba que la clave funciona. Anota esa precaución en tu bitácora: es la diferencia entre configurar y quedarte fuera.
3. UFW activo. SSH permitido de forma explícita. Nada más abierto todavía.
4. Un archivo `NOTAS.md` en la VM, o en tu repo de práctica, con los comandos que usaste y la frase que demuestra cada uno (`whoami`, el estado de UFW, el puerto en el que sshd escucha).

!!! warning "Restricciones"

    - No desactives el firewall para “probar si era eso” sin apuntar cómo vuelves a activarlo en la misma sesión.
    - No subas la clave privada al repositorio. Si el repo es solo local, aun así no la copies ahí.
    - No hace falta un dominio ni HTTPS en este ejercicio.

!!! success "Cómo sabes que está bien"

    - Desde una terminal nueva, entras sin escribir la contraseña del servidor.
    - `sudo` pide **tu** contraseña de usuario, no la de root, y un comando privilegiado funciona.
    - Un intento de abrir el puerto 80 desde fuera (o desde el anfitrión, si la VM publica puertos) no obtiene una web, porque aún no hay nada escuchando y, además, el firewall no lo ha abierto. Separa esas dos causas en tus notas: las vas a confundir en el ejercicio 3 si no lo haces ahora.
