---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 09 — El proxy y el puerto de dentro

!!! info "Antes de empezar"

    Tiempo: 2 horas. Encima del HTTPS del ejercicio 8. Glosario: [reverse proxy](../glosario.md#reverse-proxy).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [reverse proxy](../glosario.md#reverse-proxy).

El visitante solo habla con Nginx en el 443. PHP o Node escuchan en un puerto que **no** está abierto en UFW, por ejemplo el 9000 solo en la máquina local.

## Qué lograr

- Una ruta, `/api/` o el sitio entero, la atiende el proceso de detrás. Nginx termina TLS y reenvía la petición en claro por el puerto interno. No hace falta que inventes otro certificado para PHP.
- Desde fuera, el puerto interno no responde. Lo pruebas desde el anfitrión, no solo con una corazonada.
- Una petición `https://tu-nombre/...` llega al proceso. El proceso ve que el esquema original era HTTPS. Si no se lo dices en una cabecera, PHP puede generar enlaces `http://` y el navegador se quejará de contenido mixto. Anota qué cabecera usaste (`X-Forwarded-Proto` es la pista) y dónde la lees. No te fíes de esa cabecera si cualquiera puede hablarle a PHP directamente: por eso el puerto interno no está publicado.
- El log de Nginx muestra la petición. Si algo falla, la primera lectura es ese log, no un cambio de puerto al azar.

!!! warning "Restricciones"

    - No abras el puerto de PHP “un momento” en el firewall y te olvides. Si lo abres para diagnosticar, ciérralo antes de dar el ejercicio por hecho y anota que lo abriste.
    - No pongas la contraseña de la base en el archivo de Nginx.

!!! success "Cómo sabes que está bien"

    - Apagas el proceso de detrás y Nginx sigue en pie: el 443 responde un error de proxy, no un silencio. Distingues ese error del de “el firewall tragó el paquete”.
    - Vuelves a encender el proceso y la ruta responde otra vez, sin rehacer el certificado.
    - En tus notas caben tres puertos y el papel de cada uno: 22, 443, y el interno que no viaja.
