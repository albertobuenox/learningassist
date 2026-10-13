---
tags:
  - corto
  - ejercicio
  - sistemas
---

# 01 — La web no carga

!!! info "Antes de empezar"

    Sin servidor todavía. Tiempo: 45 minutos. Es un ejercicio de vocabulario aplicado. Glosario: [proceso](../glosario.md#proceso-y-servicio), [puerto](../glosario.md#puerto), [firewall](../glosario.md#firewall), [DNS](../glosario.md#dns), [raíz del sitio](../glosario.md#raíz-del-sitio), [log](../glosario.md#log).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [proceso](../glosario.md#proceso-y-servicio), [puerto](../glosario.md#puerto), [firewall](../glosario.md#firewall), [DNS](../glosario.md#dns), [raíz del sitio](../glosario.md#raíz-del-sitio), [log](../glosario.md#log).

## Síntoma

Un compañero dice “la web no carga” y te manda cuatro datos sueltos. No son un caso real de un extraño: es un relato para ordenar causas. No busques su máquina. Clasifica.

Caso A. El navegador dice que no encuentra el servidor. `ping` al nombre del dominio falla. La IP escrita a mano en el navegador abre una página.

Caso B. El navegador dice “conexión rechazada” en el puerto 80. En el servidor, Nginx no aparece en `systemctl status`. El puerto 22 sí acepta tu SSH.

Caso C. Ves el HTML por defecto de Nginx, no el de la tienda. El servicio está activo. Los archivos de la tienda están en `/home/ana/tienda`.

Caso D. Ayer funcionaba. Hoy el navegador espera y acaba en tiempo agotado. SSH también espera. La consola del proveedor muestra la máquina encendida. Ayer se activó UFW.

## Qué entregar

Para cada caso: la capa que falla (nombre, puerto, proceso, archivos, filtro), qué mirarías primero y qué cambio **no** harías todavía. Una tabla basta.

!!! success "Cómo sabes que está bien"

    - Ningún caso se resuelve con “reinstalar Nginx” como primer paso.
    - En el caso C no culpas al DNS.
    - En el caso D, el riesgo de quedarte fuera aparece en tu respuesta antes que cualquier otro arreglo.
