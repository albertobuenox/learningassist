---
tags:
  - ejercicio
  - http
  - medio
---

# 02 — Dos representaciones

!!! info "Antes de empezar"

    Tiempo: 90 minutos. Glosario: [recurso](../glosario.md#recurso), [representación](../glosario.md#representación), [código de estado](../glosario.md#código-de-estado).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [recurso](../glosario.md#recurso), [representación](../glosario.md#representación), [código de estado](../glosario.md#código-de-estado).

Usa el servidor que ya tengas (Node o, más adelante, PHP). Si todavía no hay datos, un array fijo de dos productos basta.

## Contrato que vas a cumplir

- `GET /productos` con `Accept: text/html` responde **200** y un HTML mínimo con los nombres.
- `GET /productos` con `Accept: application/json` responde **200** y un JSON, un array de objetos.
- `GET /productos/no-existe` responde **404** en los dos casos. El cuerpo del 404 respeta el `Accept`: una frase en HTML o un objeto `{"error": ...}` en JSON.
- Un `Accept` que no sabes atender responde **406**.

Pruébalo con `curl -H`, no solo con el navegador. El navegador manda un `Accept` largo; anótalo y decide qué haces cuando pide varias cosas a la vez. Escribe esa decisión en el contrato de tres líneas.

!!! warning "Restricciones"

    - El código de estado no es siempre 200 con un campo `"ok": false`.
    - No instales un framework para negociar el contenido. Una condición sobre la cabecera basta.

!!! success "Cómo sabes que está bien"

    - El mismo camino devuelve dos cuerpos distintos según la cabecera, y el recurso (la lista) es el mismo.
    - El 404 JSON no es una página HTML con el código 404 escrito en un párrafo y un estado 200.
    - Sabes qué pasa si la cabecera `Accept` no viene. Lo has decidido y lo has probado.
