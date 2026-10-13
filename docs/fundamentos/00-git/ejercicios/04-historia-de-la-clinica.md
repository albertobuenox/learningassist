---
tags:
  - ejercicio
  - git
  - medio
---

# 04 — Historia de la clínica

!!! info "Antes de empezar"

    Cierre. Tiempo: se hace encima del repositorio del proyecto integrador, no en una tarde aislada. Cada vez que cierres un ejercicio de otra asignatura dentro de ese repo, la historia tiene que seguir siendo legible.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Qué se tiene que poder leer

`git log --oneline` del integrador, sin abrir el código, responde:

- cuándo apareció el esquema de la base;
- cuándo la API empezó a devolver JSON;
- cuándo un `POST` sin token dejó de aceptarse;
- cuándo el entorno pasó a levantarse con Compose.

Eso implica commits separados. Un solo commit “clínica” al final no cierra este ejercicio.

!!! warning "Restricciones"

    - `.env`, dependencias instaladas y certificados privados no están en la historia. Hay un `.env.example`.
    - El README dice cómo clonar y arrancar. Lo pruebas tú, en una carpeta nueva, antes de darlo por bueno.
    - Los mensajes están en español y dicen el motivo.

!!! success "Cómo sabes que está bien"

    Otra persona clona, sigue el README y no te pregunta por un archivo que olvidaste commitear. Si te pregunta, ese archivo es el siguiente commit, con un mensaje que explica qué faltaba.
