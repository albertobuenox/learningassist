# Bases de datos

Objetivo: volver a **modelar** un dominio pequeño y **consultar** con SQL hasta sentirte cómodo con uniones, agregados, restricciones e índices. El motor de práctica es PostgreSQL. Lo que aprendas se traslada a MySQL; la sintaxis de tipos y de “upsert” no.

## Al terminar deberías poder

- Dibujar entidades, claves y cardinalidades antes de crear tablas.
- Escribir `SELECT` con filtro, orden, unión y agrupación, y explicar qué fila sale y por qué.
- Decir qué forma normal estás rompiendo cuando repites un dato, y cuándo te compensa romperla.
- Leer un `EXPLAIN` lo bastante para proponer un índice, y saber que un índice no es gratis.

## Orden

1. [Glosario](glosario.md) — lectura rápida.
2. [Cursos](cursos.md) — no los hagas todos. Empieza por SQLBolt o CS50 SQL.
3. Ejercicios, en este orden:

| # | Archivo | Idea |
| --- | --- | --- |
| 1 | [Modelo en papel](ejercicios/01-modelo-en-papel.md) | Entidades antes que `CREATE TABLE` |
| 2 | [Consultas](ejercicios/02-consultas.md) | Filtro, orden, nulos |
| 3 | [Uniones y agregados](ejercicios/03-uniones-y-agregados.md) | Join y `GROUP BY` |
| 4 | [Diseño](ejercicios/04-diseno-y-normalizacion.md) | Un esquema malo que hay que partir |
| 5 | [Integridad](ejercicios/05-integridad-y-transacciones.md) | Restricciones y dos escrituras a la vez |
| 6 | [Índices](ejercicios/06-indices.md) | Qué acelerar y qué cuesta |
| 7 | [Proyecto](ejercicios/07-proyecto-clinica.md) | Esquema propio, con pruebas |

## Herramienta

Instala PostgreSQL en local o en Docker (el ejercicio de Docker está en Sistemas; aquí basta `psql`). Crea una base `practica` y no trabajes nunca contra una base que no sea tuya.

## Criterio de cierre

Cierras la asignatura cuando el proyecto de la clínica aguanta tres intentos de datos imposibles (cita duplicada, paciente borrado con citas, hueco sin profesional) y puedes mostrar la consulta que lista el día.
