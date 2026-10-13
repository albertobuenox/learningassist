# Términos

Lo que hace falta nombrar para trabajar: planear, cambiar código con otros, entregar, romper, arreglar y explicar la decisión.

## Planificación

**Ticket.** La unidad de trabajo con un título, un dueño y un estado. Si no cabe en un ticket, todavía es una conversación.

**Backlog.** La lista ordenada de lo que aún no se ha empezado. Ordenar es decidir qué espera.

**Sprint.** Un intervalo corto, a menudo dos semanas, con un conjunto de tickets que el equipo se comprometió a cerrar.

**Refinamiento.** La reunión en la que un ticket pasa de idea a trabajo ejecutable: alcance, dudas, dependencias.

**Criterio de aceptación.** La condición comprobable que dice que el ticket está resuelto. “Que se vea bien” no es un criterio.

**Definición de hecho.** El acuerdo del equipo sobre qué más hace falta además del código: prueba, revisión, documentación, desplegado en un entorno.

**Alcance.** Lo que entra en esta entrega. Lo que queda fuera también forma parte del alcance: hay que decirlo.

**Estimación.** Una apuesta informada de esfuerzo, no una promesa. Sirve para ordenar, y se revisa cuando aparece información nueva.

**Spike.** Un tiempo acotado para aprender lo justo y decidir. El resultado es una conclusión, no una funcionalidad.

**Dependencia.** Algo que este ticket no puede cerrar solo: otro equipo, un contrato, un dato, una decisión.

**Bloqueo.** Lo que impide avanzar hoy. Nombrarlo pronto cambia el plan; esconderlo solo alarga el sprint.

**Prioridad.** El orden real cuando no cabe todo. Dos cosas “urgentes” son una conversación pendiente.

**MVP.** La versión más pequeña que ya resuelve el problema para alguien. No es la versión descuidada.

**Deuda técnica.** Un atajo consciente que deja el sistema más caro de cambiar. Se paga con tiempo después, o se anota y se planifica.

**Trade-off.** Una cesión entre dos bienes que no caben a la vez: velocidad y claridad, consistencia y latencia, alcance y fecha.

## Código y revisión

**Pull request (PR).** La propuesta de incorporar un conjunto de commits a la rama compartida, con descripción y revisión.

**Diff.** La diferencia entre dos versiones. Es lo que se revisa; el ticket explica por qué existe esa diferencia.

**Code review.** La lectura del cambio por otra persona antes de integrarlo. Busca riesgos, no estilo personal.

**Aprobación.** El visto bueno explícito para mezclar. No sustituye a haber leído el diff.

**Convención.** Un acuerdo de nombres, estructura o formato para que el código se lea igual lo escriba quien lo escriba.

**Lint.** Una comprobación automática de esas convenciones. Falla antes de que una persona pierda tiempo en lo mismo.

**Refactor.** Cambiar la estructura interna sin cambiar el comportamiento observable. Si también cambia el comportamiento, es otra cosa y conviene separarlo.

**Regresión.** Un comportamiento que antes funcionaba y deja de funcionar tras un cambio.

**Caso límite.** El dato o la situación rara que el camino feliz no cubre: vacío, duplicado, límite, concurrencia, permiso denegado.

**Camino feliz.** El recorrido en el que todo llega bien y el usuario consigue lo que venía a hacer.

**Acoplamiento.** Cuánto tiene que cambiar una parte cuando cambia otra. Alto acoplamiento vuelve caro cualquier arreglo.

**Cohesión.** Cuánto se pertenece lo que vive junto. Una función con una sola razón para cambiar es cohesiva.

**Contrato.** Lo que una función, un módulo o una API promete a quien la usa: entradas, salidas, errores. Quien llama no debería depender de cómo está hecha por dentro.

**Interfaz.** La superficie pública de ese contrato. Lo interno puede cambiar si la interfaz se mantiene.

**Efecto secundario.** Un cambio fuera del valor devuelto: escribir en disco, enviar un correo, mutar una variable compartida.

**Invariante.** Una condición que el sistema debe cumplir siempre, antes y después de cada operación válida.

**Idempotencia.** Repetir la misma operación no cambia el resultado más allá de la primera vez. Importa cuando una petición puede llegar dos veces.

**Legado.** Código que ya está en producción y no puedes reescribir de un golpe. Se cambia por los bordes, con pruebas.

**Feature flag.** Un interruptor para activar un cambio a una parte de los usuarios, o para apagarlo sin un despliegue nuevo.

**Hotfix.** Un arreglo urgente sobre lo que está en producción, con el menor cambio posible. Después se reconcilia con la rama principal.

## Entrega

**Rama.** Una línea de commits con nombre. La rama del ticket aísla el trabajo hasta que está listo para mezclarse.

**Commit.** Un conjunto de cambios con autor, fecha y mensaje. El mensaje dice por qué.

**Merge.** Incorporar una rama en otra. Si las dos tocaron lo mismo, aparece un conflicto.

**Rebase.** Reescribir tus commits encima de la punta actual de otra rama. La historia queda lineal; los commits ya publicados no se reescriben a la ligera.

**Conflicto.** Dos cambios incompatibles sobre el mismo sitio. Resolverlo es decidir el resultado correcto, no borrar marcas.

**Rama principal.** La línea que el equipo trata como integrable y desplegable. El nombre habitual es `main`.

**Integración continua (CI).** El sistema que, en cada cambio, instala, construye y ejecuta comprobaciones solas.

**Pipeline.** La secuencia de esos pasos: instalar, test, construir, publicar, desplegar.

**Build.** El resultado de transformar el código fuente en algo ejecutable.

**Artefacto.** El archivo producido por el build y que se despliega: imagen, paquete, bundle.

**Entorno.** Un sitio concreto donde corre el sistema, con su configuración y sus datos. Local, staging y producción no son el mismo sitio.

**Local.** La máquina de quien desarrolla.

**Staging.** El entorno compartido que imita producción para probar antes de exponer el cambio a usuarios reales.

**Producción.** El entorno que usan los usuarios reales. Un error aquí es un incidente, no un ensayo.

**Configuración.** Lo que cambia entre entornos sin cambiar el código: URLs, límites, opciones.

**Variable de entorno.** Un valor de configuración inyectado al proceso al arrancar, fuera del código fuente.

**Secreto.** Una credencial, clave o token. Vive en un gestor de secretos o en el entorno, nunca en el repositorio.

**Deploy.** Poner un artefacto concreto a correr en un entorno.

**Release.** Una versión nombrada que se entrega. Puede agrupar varios deploys o uno solo, según el equipo.

**Rollback.** Volver al artefacto anterior porque el actual hace daño. Es una decisión de operación, no un fracaso moral.

**Migración.** Un cambio versionado del esquema de la base de datos. Se aplica en orden y se puede razonar hacia atrás.

**Downtime.** El tiempo en que el servicio no atiende. Hay despliegues que lo evitan y despliegues que lo aceptan a propósito.

**Changelog.** La lista legible de qué cambió entre versiones, pensada para quien no lee los commits.

## Fallos y operación

**Bug.** Un comportamiento que contradice lo que el sistema debía hacer.

**Incidente.** Una degradación o caída que afecta a usuarios ahora. Se atiende para restaurar, y la causa se investiga después.

**Severidad.** Cuánto daño hace el fallo: cuánta gente, qué función, si hay pérdida de datos.

**Impacto.** A quién le pasa y qué no puede hacer. La severidad se argumenta con impacto, no con lo interesante que sea el bug.

**Mitigación.** Una acción que reduce el daño antes de tener la causa: apagar un flag, hacer rollback, cortar una ruta.

**Causa raíz.** La razón de fondo, no el síntoma. “El servidor se quedó sin memoria” todavía pide por qué creció la memoria.

**Postmortem.** El escrito posterior al incidente: qué pasó, qué se hizo, qué cambia para que no se repita igual. Sin culpar a una persona.

**Log.** Una línea que el proceso escribe para poder reconstruir qué ocurrió. Sin contexto (usuario, petición, error) no sirve.

**Métrica.** Un número que se mide en el tiempo: latencia, errores, uso de CPU. Sirve para ver una tendencia, no un caso concreto.

**Alerta.** Un aviso automático cuando una métrica cruza un umbral. Si salta por todo, se deja de leer.

**Latencia.** El tiempo que tarda una operación en responder. Se mira en percentiles, no solo en la media.

**Disponibilidad.** La proporción de tiempo en que el servicio responde como debe.

**Cuello de botella.** El recurso que limita al resto: una consulta, un candado, un servicio externo.

**Caché.** Una copia guardada para no recalcular o no volver a pedir lo mismo. Hay que saber cuándo deja de ser válida.

**Timeout.** El tiempo máximo de espera antes de rendirse. Sin él, un servicio lento arrastra a quien lo llama.

**Reintento.** Volver a intentar una operación fallida. Solo es seguro si la operación es idempotente o si sabes que la anterior no llegó a hacerse.

**Observabilidad.** Poder responder qué está pasando por dentro con logs, métricas y trazas, sin entrar a la máquina a adivinar.

**Traza.** El recorrido de una petición a través de varios servicios, con un identificador común.

## APIs, HTTP y seguridad

**Endpoint.** Una URL con un método que el servidor acepta como operación.

**Petición y respuesta.** El par de la transacción HTTP: el cliente pide, el servidor contesta con un estado y un cuerpo.

**Código de estado.** El número que clasifica la respuesta: 2xx salió bien, 4xx falló el cliente, 5xx falló el servidor.

**Payload.** El cuerpo de la petición o de la respuesta. El contrato dice qué campos lleva.

**Breaking change.** Un cambio de contrato que rompe a quien ya integraba la versión anterior.

**Versionado.** La forma de convivir con más de un contrato a la vez mientras los clientes migran.

**Autenticación.** Saber quién es quien llama.

**Autorización.** Decidir si esa identidad puede hacer esta acción. Estar autenticado no concede todos los permisos.

**Token.** Un testigo que demuestra identidad o permiso durante un rato. Se trata como un secreto.

**Sesión.** El estado que el servidor asocia a un usuario entre peticiones.

**CORS.** La regla del navegador sobre si una página de un origen puede llamar a otro origen.

**Rate limit.** Un tope de peticiones por intervalo. Protege el servicio y obliga al cliente a respetar un ritmo.

**Webhook.** Una llamada que tu sistema hace a otra URL cuando ocurre un hecho, en lugar de esperar a que le pregunten.

**Validación.** Comprobar que la entrada tiene la forma y los límites acordados antes de usarla.

**Inyección.** Meter datos de usuario donde el sistema los interpreta como código o como consulta. Se evita separando datos e instrucciones.

**XSS.** Ejecutar en el navegador de la víctima un script que llegó como dato.

**CSRF.** Hacer que el navegador de un usuario autenticado envíe una acción que él no decidió.

**Principio de mínimo privilegio.** Cada proceso, usuario o token solo tiene los permisos que necesita para su trabajo.

## Datos y rendimiento

**Esquema.** La forma acordada de los datos: tablas, columnas, tipos, relaciones.

**Integridad.** Las reglas que impiden datos imposibles: una cita no puede apuntar a un paciente que no existe.

**Transacción.** Un grupo de cambios que se confirman juntos o no se confirman. A medias dejaría el sistema incoherente.

**Índice.** Una estructura que acelera ciertas búsquedas a cambio de espacio y de coste al escribir.

**Consulta N+1.** Traer una lista y, por cada fila, lanzar otra consulta. Con pocos datos no se nota; con datos reales sí.

**Consistencia.** Que quien lee ve un estado que las reglas permiten. A veces se relaja a propósito entre copias, y hay que saber qué lee cada uno.

**Réplica.** Una copia de la base que absorbe lecturas. Puede ir un instante por detrás de la principal.

**Paginación.** Devolver un trozo de una lista, con una forma de pedir el siguiente. Una lista sin límite acaba tumbando cliente y servidor.

**Seed.** Datos iniciales o de prueba cargados a propósito para poder desarrollar. No son datos de producción.

**Backup.** Una copia desde la que se puede restaurar. Sin un ensayo de restauración, es una esperanza.

## Pruebas

**Prueba unitaria.** Comprueba una unidad pequeña, aislada de red y de base de datos.

**Prueba de integración.** Comprueba que dos o más partes reales colaboran: código y base, código y HTTP.

**Prueba de extremo a extremo.** Recorre el sistema como lo haría un usuario, de la interfaz al dato.

**Aserción.** La comprobación que hace fallar la prueba si el resultado no es el esperado.

**Fixture.** El estado conocido que preparas antes de la prueba para que el resultado sea interpretable.

**Mock.** Un sustituto de una dependencia que controlas en la prueba. Si mockeas todo, ya no estás probando el sistema.

**Cobertura.** El porcentaje de código que las pruebas ejecutan. Una cifra alta no dice que los casos importantes estén probados.

**Flaky.** Una prueba que a veces pasa y a veces falla sin que el código haya cambiado. Erosiona la confianza en el pipeline.

**Caso de regresión.** Una prueba que se añade cuando un bug se corrige, para que ese bug no vuelva en silencio.

## Personas y decisiones

**Ownership.** La responsabilidad de un trozo del sistema: no solo escribirlo, también operarlo y explicar cómo se cambia.

**Stakeholder.** Quien tiene interés en el resultado y puede cambiar prioridades: producto, soporte, un cliente, otro equipo.

**Handoff.** El paso de un trabajo a otra persona o equipo con el contexto necesario para continuarlo.

**Onboarding.** El camino para que alguien nuevo pueda contribuir sin depender de la memoria oral.

**Documentación.** El texto que sigue siendo verdad cuando quien lo escribió no está. El README que permite arrancar el proyecto es documentación.

**Alcance cerrado.** Un acuerdo de que no entran más cambios en esta entrega. Un cambio nuevo es otro ticket.

**Consenso.** Una decisión que el equipo puede ejecutar aunque no fuera la opción favorita de cada uno.

**Escalado.** Pedir ayuda a quien tiene contexto o autoridad cuando el problema ya no cabe en el equipo.
