---
tags:
  - ejercicio
  - medio
  - ui-ux
---

# 02 — Flujo, antes de la pantalla

!!! info "Antes de empezar"

    Papel. Tiempo: 90 minutos. Glosario: [objetivo](../glosario.md#objetivo), [flujo](../glosario.md#flujo), [caso feliz](../glosario.md#caso-feliz), [fricción](../glosario.md#fricción).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [objetivo](../glosario.md#objetivo), [flujo](../glosario.md#flujo), [caso feliz](../glosario.md#caso-feliz), [fricción](../glosario.md#fricción).

## Persona y fin

Marta trabaja en el mostrador. El teléfono suena. Quien llama quiere una cita con la doctora Soler, el jueves por la mañana, lo antes posible. Si no hay hueco el jueves, acepta el viernes. Marta no debe pedir datos que no va a usar.

## Qué dibujar

Un flujo (cajas y flechas, no una UI) que cubra:

- el camino en el que el jueves tiene hueco;
- el camino en el que el jueves está lleno;
- la persona que llama cuelga a mitad;
- Marta se equivoca de paciente y necesita deshacer la reserva antes de colgar.

Al lado, la lista de datos que el sistema pide. Cada dato lleva una frase: para qué decisión hace falta. Si no hay frase, sobra.

!!! warning "Restricciones"

    - Un solo profesional en este flujo, para no diseñar un buscador de médicos que el relato no pide.
    - No dibujes el calendario todavía. Si lo dibujas, te habrás saltado el paso.

!!! success "Cómo sabes que está bien"

    - Hay una caja que representa “no hay hueco”, distinta de “error de red”.
    - Puedes señalar el momento exacto en que la cita queda confirmada, y qué ve Marta para estar segura antes de decírselo a quien llama.
    - Quitas un dato de la lista y el flujo sigue. Si no puedes quitar ninguno, revisa “observaciones”: casi siempre se pide por costumbre.
