---
tags:
  - agentes
  - leccion
  - medio
---

# 05 — El plan

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos.

    Fuente: https://cursor.com/docs/agent/plan-mode

??? tip "Pista"

    Úsala cuando el cambio toca más de un archivo o cuando hay dos formas razonables de hacerlo. Un renombre de variable no necesita plan. Glosario: [plan](../glosario.md#plan), [encargo](../glosario.md#encargo).

## Qué encargar

Una modificación real y pequeña, con dos opciones. Por ejemplo: validar el importe en la función pura, o validarlo en la frontera HTTP. Pide solo el plan.

=== "Cursor"

    Activa el modo **Plan**. No pases a implementar hasta haber editado el plan tú.

=== "Claude Code"

    Primera línea del mensaje: plan, sin editar, y espera. Prohíbe tocar archivos hasta que aceptes.

=== "Chat"

    El plan es el único entregable. No hay implementación automática: tú decides qué aplicar después.

El plan tiene que incluir:

- archivos que tocaría;
- qué no tocaría;
- cómo se comprueba;
- qué opción recomienda y qué pierde la otra.

## Qué hacer tú

Edita el plan antes de aceptar nada. Cambia una restricción (un archivo que no se toca, un caso que faltaba). Vuelve a pedirlo. Solo entonces, si el plan coincide con el encargo de la lección 2, deja que lo implemente.

Si el resultado no se parece al plan, no lo remiendes con cinco mensajes. Reviértelo, corrige el plan y arranca de nuevo. Eso es lo que la documentación de Plan mode recomienda, y aquí lo compruebas una vez para creértelo.

!!! success "Cómo sabes que está bien"

    - El plan cabe en una pantalla. Si parece un diseño de sistema, el encargo era demasiado grande: pártelo y quédate con una parte.
    - Puedes señalar la frase del plan que evitaba el archivo que no debía cambiar.
    - Tras implementar, `git diff` no contiene un archivo ausente del plan. Si lo contiene, o el plan mintió o aceptaste de más. ¿Cuál de las dos fue?
