# Glosario

### Chat

Una respuesta a un texto. No hay herramientas: no lee tu disco ni ejecuta nada, salvo que tú pegues el material en el mensaje.

### Agente

Un modelo dentro de un bucle. Propone una acción, una herramienta la ejecuta, el resultado vuelve al modelo, y se repite hasta que para o lo paras tú.

### Herramienta

Una capacidad concreta: leer un archivo, buscar, editar, ejecutar un comando, abrir una página. Sin herramientas, Claude solo escribe. Con herramientas, cambia el mundo. Cada herramienta tiene un permiso.

### Bucle

El ciclo prompt, acción, resultado, siguiente prompt. “Se ha quedado pensando” a veces es una herramienta lenta. “Ha terminado” significa que el modelo dejó de pedir acciones, no que el programa funcione.

### Contexto

Todo lo que el modelo puede ver en ese turno: instrucciones fijas, conversación, archivos que leyó, salida de comandos. No es tu cabeza ni el repo entero.

### Ventana de contexto

El cupo de ese contexto. Cuando se llena, el agente resume o olvida el principio. Un archivo enorme pegado “por si acaso” empuja fuera el criterio de hecho.

### Encargo

Lo que pides. Uno bueno dice el resultado observable, las restricciones y cómo se comprueba. “Mejora esto” no es un encargo.

### Plan

Una descripción del cambio, revisable, anterior al diff. En Cursor es el modo Plan. En Claude Code puedes pedir el plan y prohibir editar hasta que lo aceptes. En el chat, el plan es el único entregable.

### Regla persistente

Texto que entra en cada conversación: `CLAUDE.md` en Claude Code, reglas de proyecto en Cursor. Gasta contexto siempre. Si no evita un error concreto, sobra.

### Skill

Un procedimiento que se carga cuando hace falta, no en todos los turnos. Un checklist de revisión o un flujo de “añadir una migración” vive mejor aquí que en la regla de siempre.

### Diff

La diferencia entre el código de antes y el de después. Es el producto del agente. El párrafo “he arreglado el bug” no lo es.

### Permiso

La decisión de dejar que una herramienta corra sola o pedir confirmación. Autorizar “cualquier comando” ahorra clics y también autoriza un `rm` o una subida de un secreto.

### Subagente

Otro bucle, con su propio contexto, al que el principal encarga una parte. Aísla ruido. También parte en dos la información: lo que descubrió uno no está en la cabeza del otro salvo que vuelva escrito.

### Modelo

El sistema que completa el texto. Uno más capaz cuesta más y tarda más; conviene para decidir. Uno más rápido conviene cuando el cambio ya está especificado. El nombre comercial cambia: míralo en el selector el día que elijas, no en un apunte viejo.
