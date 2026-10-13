---
tags:
  - ejercicio
  - largo
  - php
---

# 07 — CSRF

!!! info "Antes de empezar"

    Tiempo: 2–3 horas. Léelo después de la sesión. Lectura: la chuleta de prevención, no un tutorial de ataque.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## El hueco

La cookie de sesión la reenvía el navegador al host que la puso, también si el formulario que provocó el `POST` no lo pintó tu aplicación. Comprobar “hay sesión” no demuestra que quien pulsó sea quien está viendo tu página. La defensa que vas a practicar es un token ligado a la sesión: tu HTML lo incluye, el `POST` lo devuelve, y sin él la escritura se rechaza.

No construyas una página en otro dominio para disparar el formulario contra nadie. La prueba es contra tu propio servidor, con `curl`.

## Comportamiento

Sobre las facturas o las notas, las que ya exijan sesión:

- Cada formulario de escritura incluye un token que solo conoce esa sesión.
- `POST` con cookie de sesión y sin token responde **403**. No escribe.
- `POST` con cookie y con el token correcto escribe, como antes.
- `POST` sin cookie sigue respondiendo como en el ejercicio de sesión (redirige al login o 401). No lo conviertas en 403 para no mezclar “no sé quién eres” con “tu formulario no es el mío”.
- Un token de otra sesión no vale. Puedes probarlo guardando dos tokens y cruzándolos.
- El `GET` que pinta el formulario no exige token. Exigirlo en la lectura no aporta y rompe el enlace.

!!! warning "Restricciones"

    - El token no va en la cookie como único secreto: la cookie ya viaja sola, que es el problema. Va en el cuerpo o en una cabecera que un formulario de otro origen no puede rellenar con el valor de tu página.
    - No lo desactives “en local”. Si molesta al probar con `curl`, el `curl` lleva el token. Anótalo en el README.
    - `htmlspecialchars` sigue aplicando al pintar el token dentro del HTML.

!!! success "Cómo sabes que está bien"

    - El `curl` que antes creaba una factura con solo la cookie ahora recibe 403 y la tabla no crece.
    - El mismo `curl` con el token crea una fila.
    - Recargas el formulario, envías, y funciona. Si el token cambia en cada lectura, el que envías es el último que pintaste. Si es estable durante la sesión, también vale: escribe cuál de las dos políticas elegiste.
