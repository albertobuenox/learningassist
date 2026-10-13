# Frases en una candidatura y en la entrevista

El mismo oficio, contado a quien no vio el ticket. Una frase concreta vale más que una lista de tecnologías.

## Al escribir al reclutador

- He trabajado con el ciclo completo de un cambio pequeño: ticket, rama, prueba, pull request y deploy en un entorno previo a producción.
- En el último proyecto el valor estaba en dejar el alta de citas consistente: transacción, validación en el servidor y un criterio de aceptación que soporte pudiera comprobar.
- Busco un equipo donde el código se revisa y los incidentes se escriben después, no solo se apagan.
- Puedo incorporarme a un legado. Me interesa cómo está probado y cómo se despliega, más que si el framework es el que yo habría elegido.
- Adjunto un repositorio pequeño que se arranca con el README: eso es lo que quiero decir con definición de hecho.

## Presentarte en un minuto

- Soy desarrollador de software. Me ocupo de que un cambio llegue a producción con el contrato claro, una prueba del caso que importa y una forma de volver atrás.
- Últimamente he trabajado en una aplicación de clínica: datos con integridad, una API HTTP y una interfaz que consume ese contrato.
- Lo que mejor hago es acotar. Prefiero un alcance que se puede entregar y explicar a una solución grande que no se puede operar.
- Trabajo bien con revisión. Espero comentarios sobre riesgos, y los hago cuando me toca leer el diff de otra persona.
- Me importa la operación: logs que se pueden seguir, un entorno de staging que se parece a producción y un rollback que el equipo conoce antes de necesitarlo.

## Cuando preguntan por un proyecto

- El sistema permitía reservar citas. El riesgo no era la pantalla; era dejar la agenda en un estado imposible si el segundo paso fallaba.
- Lo resolví con una transacción que confirma el alta y el hueco juntos, y con una clave que impide la cita huérfana aunque otro cliente se salte la interfaz.
- El contrato con el frontend era un JSON con códigos claros: 422 si el dato viene mal, 403 si la cita no es de quien llama, 500 solo cuando el fallo es nuestro.
- Medí el listado antes de optimizar. El problema era una consulta N+1, no “React va lento”.
- Entregamos un MVP: crear, listar y cancelar. El export y los roles finos quedaron en el backlog con el motivo escrito.
- La release salió con feature flag. El código estuvo en producción apagado un día, y lo activamos cuando staging llevaba el caso límite en verde.
- Lo que dejaría distinto: una prueba de regresión desde el primer bug de solape. La añadimos después del incidente, y debía estar antes.

## Cuando preguntan por una decisión difícil

- Había prisa por la fecha y el formulario validaba solo en el cliente. El trade-off era salir antes o impedir datos imposibles. Elegí validar en el servidor y recortar una pantalla secundaria.
- Nos pedían reescribir el módulo legado. Propuse no hacerlo: una prueba de integración en el borde y cambios pequeños. Reescribir sin red de pruebas era más riesgo que deuda.
- El índice aceleraba la lectura y encarecía el alta. Con el volumen real compensaba; lo dije con el plan de consulta, no con una preferencia.
- Dudamos entre consistencia inmediata en todos los listados o lecturas en la réplica. Para el alta exigí leer de la base principal; para el informe mensual, la réplica bastaba.
- Pudimos desplegar con downtime corto o alargar dos semanas un esquema compatible. Elegimos la ventana corta porque soporte podía avisar y la migración no era reversible a medias.
- La abstracción “por si luego hay otro proveedor” no entró. Había un solo caso. Añadir la interfaz entonces era acoplar el diseño a un futuro que no estaba en el ticket.

## Cuando preguntan por un fallo o un incidente

- El alta empezó a devolver 500 en producción. Lo traté como incidente: impacto primero, causa después.
- La mitigación fue el rollback al artefacto anterior. En unos minutos el mostrador volvió a reservar.
- La causa era un reintento sobre una operación que no era idempotente: el proveedor iba lento, reintentábamos y duplicábamos.
- La alerta no había saltado por la media. Saltó el percentil de latencia, y al principio lo miramos tarde porque el tablero “se veía bien”.
- En el postmortem quedó una acción concreta: timeout en esa llamada, idempotencia en el alta y una prueba con el payload del incidente.
- No fue un fallo de una persona. Fue un caso límite que el camino feliz no cubría y que CI no ejecutaba.
- Lo que cambiaría de mi respuesta aquella mañana: avisar a soporte en la primera mitigación, no cuando ya estaba el rollback hecho.

## Cuando preguntan cómo trabajas con otros

- En la review miro el contrato y los casos límite. El estilo que ya cubre el lint no lo comento.
- Si no apruebo, dejo el riesgo en una frase: qué entrada rompe qué invariante. No dejo “esto no me gusta”.
- Cuando discrepamos de diseño, propongo las dos opciones con el coste de cada una y un plazo para decidir. El consenso no es que guste a todos; es que podamos ejecutarlo.
- Con producto traduzco el pedido a criterio de aceptación. “Que se sienta rápido” pasa a un número en staging antes de estimarlo.
- Si el alcance crece a mitad de la PR, lo saco a otro ticket. Mezclarlo hace imposible revisar y imposible hacer rollback de una sola cosa.
- He estado bloqueado por una dependencia de otro equipo. Lo dije el mismo día, con la pregunta exacta que necesitaba, no “voy con retraso”.
- En el handoff dejo cómo desplegar, cómo deshacer y qué log mirar. El ownership incluye a quien llega después de mí.
- He pedido ayuda cuando el fallo estaba en el proxy y yo no tenía permiso para cambiar el timeout. Escalar ahí era el arreglo, no una derrota.
- A alguien nuevo le doy el README y un ticket pequeño de caso límite, no una charla de una hora sobre la arquitectura entera.
- Si la estimación se rompe, lo digo cuando lo sé. Esperar al último día convierte un dato en una sorpresa.

## Cuando preguntan por calidad

- Una prueba unitaria me protege el cálculo puro. Una de integración me protege la transacción con la base. No sustituyo la segunda con mocks de todo.
- No persigo cobertura como objetivo. Persigo el caso que, si se rompe, duele en producción.
- Un test flaky se trata como un bug del pipeline. Si el equipo aprende a ignorar el rojo, la integración continua ya no informa.
- La definición de hecho que uso: criterio de aceptación cubierto, review hecha, CI en verde, probado en staging.
- La deuda técnica se anota con el coste de no pagarla. “Ya lo limpiaremos” sin ticket es una forma de perderla.
- Refactor y cambio de comportamiento van en commits distintos, a ser posible en PR distintas. Si no, nadie puede decir qué se estaba arreglando.
- Un secreto en el repositorio no se arregla solo con borrarlo del último commit. Sigue en la historia, y hay que rotarlo.
- El backup cuenta cuando alguien ha restaurado. En una entrevista lo diría así, aunque el ensayo sea en un entorno pequeño.

## Cuando preguntan por cómo aprendes un sistema nuevo

- Empiezo por cómo se arranca y cómo se despliega. Si no puedo repetir el build, todavía no entiendo el sistema.
- Sigo una petición desde la interfaz hasta la base: ruta, validación, transacción, respuesta. Un camino real enseña más que el mapa de carpetas.
- Miro los incidentes recientes y las alertas. Dicen qué duele, mejor que el diagrama ideal.
- Busco los invariantes: qué cosa el código da por cierta siempre. Ahí suelen estar los bugs serios.
- Hago un cambio pequeño y lo llevo hasta staging. El onboarding termina cuando mi PR pasa el mismo camino que las del equipo, no cuando acabo de leer.

## Cuando te hacen una pregunta técnica abierta

- Depende del contrato que queramos garantizar. Si el cliente puede reintentar, diseño la operación como idempotente antes de hablar de colas.
- Lo primero que preguntaría es el impacto: ¿falla para todos o para un caso? ¿Hay pérdida de datos o solo lentitud?
- No añadiría caché hasta tener el cuello de botella medido. La caché introduce otro problema, que es saber cuándo el dato guardado ya no vale.
- Para un cambio de esquema en producción pensaría en compatibilidad: ¿el código viejo puede convivir con el esquema nuevo durante el deploy?
- Un 500 en validación de entrada es un bug nuestro. Esa entrada tenía que acabar en 4xx.
- Autenticación y autorización las separaría en la respuesta. Saber quién eres no dice qué puedes hacer.
- Si la lista puede crecer, la paginación forma parte del contrato desde la primera versión. Añadirla después es un breaking change de hecho.
- Elegiría la solución más simple que preserve el invariante. La más ingeniosa, si nadie más puede operarla, es peor.

## Preguntas que haces tú

- ¿Cómo llega un cambio a producción? Quiero oír si hay staging, CI y una forma de rollback conocida.
- Cuando hay un incidente, ¿quién decide la mitigación y dónde queda escrito el postmortem?
- ¿Qué significa aquí “hecho”? ¿La PR mezclada, o el cambio comprobado en un entorno compartido?
- ¿Cómo tratáis la deuda técnica? ¿Tiene sitio en el sprint o solo entra cuando ya duele?
- ¿Qué se espera de la code review? ¿Riesgos y casos límite, o también el estilo que podría cubrir un lint?
- ¿El equipo que escribe el servicio es el que está de guardia cuando se cae?
- ¿Qué caso límite os ha mordido en el último trimestre? Me dice más que la lista de tecnologías.
- ¿Cómo es el onboarding en el primer mes? ¿Hay un ticket real o solo lectura?
- Si entro, ¿cuál sería un primer cambio pequeño con el que podría aprender el pipeline sin frenar al equipo?
- ¿Qué trade-off estáis aceptando ahora mismo a propósito?

## Al cerrar

- Me encaja un equipo que prefiere alcance cerrado y operación clara antes que acumular funcionalidad sin dueño.
- Puedo empezar por un legado si el camino de deploy y las pruebas están a la vista. Ahí contribuyo pronto.
- De lo que hemos hablado, me llevo que el cuello de botella actual es la consulta del listado y que el próximo paso es medirla, no reescribir el front.
- Si avanzamos, me ayudaría un ejemplo de ticket tal como lo cerráis: criterio de aceptación, PR y cómo se verificó en staging.
- Gracias por el rato. Si queréis, el siguiente paso puede ser un caso corto sobre un bug y su mitigación; es el tipo de conversación en el que más se me ve el oficio.
