# Glosario — UI/UX

## Uso

### UX (experiencia de uso)

Cómo le va a una persona a conseguir un fin con el producto: si entiende el paso, si se equivoca, si puede deshacer, cuánto tarda. No es “que sea agradable” como adorno. Un flujo claro y un flujo simpático pueden no coincidir; el fin manda.

### UI (interfaz)

Lo que se ve y se toca: disposición, tipo, color, iconos, componentes. Una buena UI sirve a un flujo ya decidido. Decorarla antes de saber el flujo es pintar el mapa de una ciudad que aún no existe.

### Usuario

Aquí, una persona concreta con un fin, no “el usuario” en abstracto. En los ejercicios será el mostrador de la clínica o la persona que pide cita. Si no puedes decir qué intenta hacer hoy, el diseño no tiene criterio.

### Objetivo

El resultado que esa persona quiere (salir con una cita el martes). Distinto de una funcionalidad (un calendario). El calendario es un medio.

### Flujo

La secuencia de pasos, incluidas las vueltas atrás. Se dibuja antes que la pantalla de alta fidelidad.

### Caso feliz

Todo sale bien a la primera. Es el único que se diseña si nadie lo impide, y es el menos informativo.

### Fricción

Un paso de más, una duda, un dato que se pide y no hace falta. A veces es deliberada (confirmar un borrado). Si no es deliberada, es un estorbo.

### Modelo mental

La idea previa de cómo “debería” funcionar. Si el mostrador espera una agenda de día y le das un buscador, el choque es de modelo, no de color.

### Heurística

Regla práctica para revisar una interfaz sin un laboratorio. Las diez de Nielsen son el conjunto clásico. No sustituyen a mirar a una persona usar el producto; sirven para no llegar a esa prueba con fallos obvios.

### Affordancia

La pista de que algo se puede accionar. Un texto subrayado se lee como enlace. Un rectángulo plano sin borde, a veces, no se lee como botón. Si hace falta un cartel de “pulsa aquí”, la pista falló.

### Retroalimentación

La interfaz acusa recibo: el botón se desactiva al enviar, el mensaje dice que la cita quedó el martes, el error dice qué corregir. El silencio tras un clic es un fallo de diseño, no un detalle.

### Prevención de errores

Impedir el fallo antes de que ocurra (no ofrecer horas ya ocupadas) en vez de dejar elegir y luego regañar.

### Deshacer

Poder volver de un acción destructiva. Confirmar no es lo mismo que deshacer: la confirmación se acepta sin leer; deshacer salva después.

## Interfaz

### Jerarquía visual

El orden en que el ojo recibe las piezas. Se construye con tamaño, peso, contraste y espacio, no con más cajas. Si todo es importante, nada lo es.

### Tipografía

La elección y el uso del tipo. Para una interfaz de trabajo importan el tamaño de lectura, la longitud de línea y pocos estilos (título, cuerpo, meta). Dos familias ya son muchas en este curso.

### Escala

Un conjunto pequeño de tamaños (por ejemplo 12, 14, 16, 20, 28) en vez de un número nuevo en cada capa. La escala se nota cuando la quitas: todo eran 13, 15 y 17.

### Espacio en blanco

Separación que agrupa. Lo que está cerca se lee como junto (proximidad). No es “sitio que sobró”.

### Contraste

Diferencia de luminosidad entre texto y fondo. Sin ella, el texto no se lee. Hay una cifra orientativa en las WCAG; el ejercicio pide medirla, no memorizar el número.

### Color de acento

Un color para la acción principal. Si el acento está en cinco sitios, deja de señalar.

### Estado

Una misma pieza en situaciones distintas: por defecto, hover, foco, activo, desactivado, error, carga. Diseñar solo el de defecto es dejar la interfaz a medias.

### Vacío

La pantalla cuando no hay datos. Tiene que decir qué ocurre y cuál es el siguiente paso, no un hueco en blanco.

### Carga

La espera. Si dura, se indica. Un botón que no cambia tras el clic invita al segundo clic.

### Error

Qué falló y qué puede hacer la persona. “Ha ocurrido un error” no cumple las dos cosas.

### Componente

Pieza reutilizable con nombre y estados (botón, campo, tarjeta). Si copias y pegas el botón y luego cambias solo una copia, ya no es un componente.

### Sistema de diseño

El conjunto de esas piezas, más color, tipo y espacio, acordado para no decidirlo en cada pantalla. En este curso cabe en una página de Figma.

### Patrón

Una solución conocida (formulario, lista con filtro, diálogo de confirmación). Usar un patrón no es falta de originalidad: es no hacer pensar a la gente en el mecanismo.

## Trabajo

### Wireframe

Dibujo de baja fidelidad: estructura y textos reales, sin color de marca ni fotos. Sirve para discutir el flujo. Si ya parece un anuncio, es pronto.

### Alta fidelidad

La pantalla con tipo, color y componentes definitivos. Viene después del wireframe que ya convenció.

### Prototipo

Enlace entre pantallas para recorrer el flujo sin código. No tiene que cubrir todos los estados; sí el camino que vas a probar con alguien.

### Prueba de usabilidad

Ver a una persona intentar un fin, sin ayudarla enseguida. Cinco personas pillan los problemas gordos. Una ya enseña más que la opinión del autor.

### Accesibilidad

Que la interfaz se pueda usar con teclado, lector de pantalla, zoom o menos visión del color. No es una capa final: un `div` que parece botón ya nació mal. En código lo cierra el frontend; aquí se diseña para que ese código sea posible (foco visible, etiquetas, contraste, no informar solo con color).

### WCAG

Las pautas de referencia. Nivel AA es el objetivo habitual de contraste y de foco. El curso de web.dev las aterriza mejor que leer la especificación el primer día.

### Lector de pantalla

Software que lee la interfaz. Por eso el nombre del control tiene que existir de verdad (una etiqueta), no solo un placeholder gris que desaparece al escribir.
