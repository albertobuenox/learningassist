---
tags:
  - agentes
  - corto
  - leccion
---

# 10 — Parar

!!! info "Antes de empezar"

    Tiempo: 45 minutos, más la lectura. Fuente: https://www.anthropic.com/engineering/building-effective-agents

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

Léela cuando hayas vivido un bucle que no converge. El artículo dice, en sustancia, que un agente es un modelo con herramientas, y que añadir agentes especializados antes de que el simple falle complica la depuración.

## Provocar el atasco, en pequeño

Pide un cambio con un criterio de hecho ambiguo (“déjalo más sólido”) sobre un archivo real. Deja que responda dos veces. No corrijas el encargo todavía.

A la tercera respuesta, para. No escribas “no, mejor hazlo bien”. Reviértelo todo. Escribe el encargo como en la lección 2 y empieza una conversación nueva.

Compara los dos diffs: el de la conversación larga y el de la conversación nueva. Cuál es más corto y cuál coincide con una sola conducta.

## Subagentes

No los configures en esta lección. Responde por escrito:

- qué parte del trabajo era exploración que ensuciaba el contexto (leer diez archivos para tocar uno);
- qué parte era la decisión, que tenía que quedarse en la conversación principal;
- qué se perdería si la exploración ocurriera en otro bucle y solo volviera un párrafo.

Si no se te ocurre una pérdida, todavía no te hace falta un subagente. Cuando se te ocurra, el artículo y la documentación de tu herramienta bastan para probarlo en una tarea, no para adoptarlos por defecto.

!!! success "Cómo sabes que está bien"

    - Tienes un diff revertido y otro que lo reemplaza. El segundo salió de un encargo más preciso, no de insistir.
    - Puedes decir en una frase por qué “sigue, casi está” alarga el bucle.
    - La decisión de no usar subagentes está escrita. Cambiarla exige un ejemplo concreto, no una preferencia.
