---
tags:
  - agentes
  - largo
  - leccion
---

# 11 — Cierre

!!! info "Antes de empezar"

    Tiempo: una sesión de trabajo. Une las anteriores. No hay herramienta nueva.

??? tip "Pista"

    Si una palabra no te dice nada, ábrela en el [glosario](../glosario.md). No leas el glosario entero antes de la lección.

## El bug

Elige uno que ya sepas reproducir, en un repo de práctica. Sirve un caso de `fundamentos/` que hayas dejado a medias: un total que cuenta el importe vacío, un `POST` que escribe sin token, un 404 que en realidad es un 200.

Tiene que ser un bug de comportamiento, no “el código no me gusta”.

## El recorrido

En orden, y cada paso deja rastro (un mensaje, un plan, un diff, una nota tuya):

1. Lectura, sin editar. El agente dice dónde está la decisión. Tú confirmas la línea.
2. Encargo de una rebanada, con entrada, salida y comando.
3. Plan solo si el cambio toca más de un archivo. Si toca uno, sáltatelo y anota por qué.
4. Implementación. Tú ejecutas la comprobación.
5. Lectura del diff. Quitas lo que no pediste.
6. Un commit, si el resultado es el que querías. El mensaje dice el comportamiento, no “fix del agente”.

Si a mitad el bucle se descarrila, paras y abres conversación nueva, como en la lección 10. Eso también cierra, siempre que el segundo intento quede registrado.

!!! success "Cómo sabes que está bien"

    - Alguien que no vio el chat entiende el commit leyendo el mensaje y el diff.
    - La comprobación falla si deshaces a mano la condición que arreglaba el bug.
    - No hay secretos en el diff ni un comando destructivo que hayas aprobado sin leer.
    - Puedes decir qué parte no delegarías la próxima vez. Si la respuesta es “ninguna”, no has leído el diff con el cuidado de la lección 8.
