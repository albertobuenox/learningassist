---
tags:
  - ejercicio
  - largo
  - php
---

# 03 — Formulario, validación y salida

!!! info "Antes de empezar"

    Tiempo: 2 horas. Glosario: [escapar la salida](../glosario.md#escapar-la-salida), [superglobal](../glosario.md#superglobal).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [escapar la salida](../glosario.md#escapar-la-salida), [superglobal](../glosario.md#superglobal).

Sigue en memoria: un array en una variable no sobrevive entre peticiones. Para este ejercicio puedes acumular las facturas válidas en `$_SESSION` solo como almacén temporal, o volver a pintar únicamente la que acabas de enviar. Elige una y escríbela. La base llega en el siguiente.

## Qué añadir

- Lista de lo guardado en la sesión (si elegiste sesión): concepto e importe.
- Si el concepto contiene `<b>hola</b>` o una comilla, la página lo **muestra como texto**. El navegador no lo interpreta como etiqueta.
- Los mensajes de validación salen junto al campo, y el valor enviado se rellena de nuevo para no obligar a reescribirlo. Ese valor, rellenado, también pasa por el escape.
- Una función `e(string $texto): string` es el único sitio donde llamas a `htmlspecialchars`. El resto de las vistas la usa. Así puedes buscar los olvidos.

!!! warning "Restricciones"

    - `htmlspecialchars` con `ENT_QUOTES` y UTF-8. Mira en el manual por qué las comillas simples importan si el texto acaba dentro de un atributo.
    - No “limpies” el texto borrando `<` al guardarlo. Guarda el texto y escapa al pintarlo. Si lo borras, no podrás escribir “el importe es < 10” como concepto.

!!! success "Cómo sabes que está bien"

    - Ver código fuente de la página (no la pestaña Elements ya interpretada) y encontrar el concepto con los `<` convertidos en entidades.
    - Un concepto de solo espacios no se guarda. Decides si lo recortas con `trim` antes de medir la longitud, y lo pruebas.
    - La función que valida no imprime HTML. Devuelve una lista de errores. Si devuelve un string con un `<p>`, sigue mezclada.
