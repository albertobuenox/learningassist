---
tags:
  - agentes
  - leccion
  - medio
---

# 07 — Instrucciones que duran

!!! info "Antes de empezar"

    Tiempo: 60 minutos.

    Fuentes: https://code.claude.com/docs/en/claude-md y, si estás en Cursor, https://cursor.com/docs/rules

??? tip "Pista"

    Una regla persistente entra en cada conversación. Cuesta contexto aunque la tarea no la necesite. Glosario: [regla persistente](../glosario.md#regla-persistente), [skill](../glosario.md#skill).

Una regla persistente entra en cada conversación. Cuesta contexto aunque la tarea no la necesite. Claude Code orienta a menos de unas 200 líneas. La prueba de cada línea es: si la quito, ¿el agente comete un error que el código no le habría evitado?

## El borrador malo

No lo instales. Recórtalo.

> Escribe código limpio, profesional y escalable. Sigue las best practices. Comenta todo. Usa el mejor patrón. Sé proactivo y no preguntes. Nunca te equivoques con la base de datos.

## Qué entregar

Un archivo de instrucciones de tu proyecto de práctica, de menos de 40 líneas, con solo reglas que hayas visto romperse:

- cómo se ejecutan los tests;
- una convención que no sea la obvia del lenguaje (dónde vive el SQL, cómo se nombra una ruta);
- qué no debe hacer (no añadir dependencias, no commitear `.env`).

=== "Cursor"

    Puede ser una regla de proyecto o un `AGENTS.md`.

=== "Claude Code"

    Un `CLAUDE.md` en la raíz del proyecto.

No hace falta cubrir los dos.

Deja fuera el procedimiento largo (“cómo añado una migración”). Eso, si lo necesitas a menudo, es una skill: https://cursor.com/docs/skills . Anota el título de esa skill en una línea. No la escribas entera salvo que ya la hayas repetido tres veces a mano.

## Comprobación

Conversación nueva. Pide una tarea pequeña que choque con una regla (por ejemplo, “instala una librería para sumar importes”). La regla tiene que notarse en lo que hace o en lo que pregunta. Si no se nota, la frase es ambigua o está enterrada. Acórtala y repite. Una sola repetición.

!!! success "Cómo sabes que está bien"

    - Cada línea supera la prueba de “si la quito, hay un error concreto”. Las que no, las has borrado.
    - No hay dos frases que puedan obedecerse a la vez de dos maneras distintas.
    - Sabes dónde vive el archivo y si entra en git. Una preferencia solo tuya no se commitea como si fuera del equipo.
