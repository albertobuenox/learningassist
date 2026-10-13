# Git

Objetivo: que el resto del recorrido deje historia. Un cambio que no está en un commit no se puede comparar, deshacer ni enseñar. Esta carpeta se hace **el primer día**, aunque la asignatura que te interese sea otra. El ejercicio 1 cabe en una hora.

## Al terminar deberías poder

- Decir qué está guardado en el repositorio, qué está en el área de preparación y qué solo vive en el directorio de trabajo.
- Hacer un commit cuyo mensaje explica el motivo, y leer ese motivo un mes después en `git log`.
- Crear una rama, mezclarla y reconocer un conflicto sin borrarlo a ciegas.
- Subir el trabajo a un remoto privado sin subir `.env`, `vendor/` ni `node_modules/`.

## Orden

1. [Glosario](glosario.md)
2. [Cursos](cursos.md) — el libro Pro Git como consulta; Learn Git Branching si las ramas no se ven.
3. Ejercicios:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [Tres commits](ejercicios/01-tres-commits.md) | Estado, diff y mensaje |
| 2 | [Una rama](ejercicios/02-una-rama.md) | Bifurcar y mezclar |
| 3 | [El remoto](ejercicios/03-el-remoto.md) | Lo que sí se sube |
| 4 | [Historia de la clínica](ejercicios/04-historia-de-la-clinica.md) | El repo del integrador se lee solo |

## Criterio de cierre

Clonas el repositorio en otra carpeta y el proyecto arranca sin pedirte un archivo que solo existía en tu máquina. `git log --oneline` se puede leer en voz alta y se entiende qué se decidió.
