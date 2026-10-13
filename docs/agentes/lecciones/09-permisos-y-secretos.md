---
tags:
  - agentes
  - corto
  - leccion
---

# 09 — Permisos y secretos

!!! info "Antes de empezar"

    Tiempo: 45 minutos. Sin demostrar un ataque. La lección es qué dejas hacer y qué no metes en el contexto.

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## Permisos

Mira, en la herramienta que uses, dónde se aprueba un comando antes de ejecutarse. Anota tres comandos que dejarías correr solos en este repo (tests, un linter, `git status`) y tres que quieres ver siempre (`git push`, cualquier cosa con `sudo`, borrar directorios, instalar paquetes globales).

Si la herramienta permite un modo en el que no pregunta nada, no lo actives para esta lección. Escribe en una frase qué daño haría un comando mal elegido con ese modo, en este proyecto concreto, no en abstracto.

## Secretos y texto ajeno

- Localiza el `.env` o el ejemplo. Confirma que el agente puede trabajar con `.env.example` y que no necesita el valor real.
- Inventa un “log” de tres líneas que incluya una clave falsa con forma de clave (`CLAVE=sk-no-es-real`). Pega el log en el chat solo después de tachar la clave, o no lo pegues. La práctica es el tachado, no la valentía.
- Un archivo o una página que no escribiste tú puede contener instrucciones dirigidas al modelo (“ignora lo anterior y haz otra cosa”). Tratadas como datos, se leen. Tratadas como órdenes, mandan. Cuando pidas que resuma un texto ajeno, dilo en el encargo: el texto es material, no son tus instrucciones. No hace falta un ejemplo malicioso de internet. Basta con escribir tú mismo una línea así dentro de un `.txt` de práctica y pedir un resumen. Anota si la obedeció.

!!! success "Cómo sabes que está bien"

    - Señalas el control que detiene un comando antes de que corra.
    - El valor real de una clave no ha aparecido en el chat ni en un commit. Lo compruebas buscando el prefijo en el historial, no de memoria.
    - Sabes qué harías si un diff toca `.env` o una credencial: no se commitea, y la clave se considera filtrada aunque el remoto sea privado.
