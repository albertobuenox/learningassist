# Frases en el entorno laboral

Así suena el vocabulario cuando hay un ticket, una PR y un entorno que se puede romper. Léelas en voz alta. Después escribe la tuya.

## Al empezar el día

- En el standup: el ticket de las citas duplicadas sigue en curso; ayer dejé la validación y hoy cierro el caso del reintento.
- No tengo bloqueo. Si la revisión de la PR entra antes del mediodía, lo despliego en staging por la tarde.
- Estoy bloqueado: el contrato del endpoint de pacientes no está cerrado y no quiero inventarme el payload.
- Ayer el pipeline falló por un test flaky, no por el cambio. Lo miro el primero para no mezclar ruido con el bug.
- El refinamiento de hoy necesita criterio de aceptación. Ahora mismo el ticket solo dice “mejorar el listado”.
- Esta estimación era de un día y ha aparecido una dependencia con facturación. La reviso antes de prometer el sprint.
- El spike de la caché ya dio para decidir: no la metemos en esta entrega; el cuello de botella es la consulta.
- Dejo fuera de alcance el exportar a CSV. Cabe en otro ticket y este tiene fecha.
- Prioridad real: el hotfix de producción va antes que el refactor del carrito.
- Si alguien puede hacer de revisor de la PR 184, la dejo lista para merge hoy.

## Al escribir y partir el trabajo

- Parto el ticket en dos: uno para el camino feliz del alta, otro para el caso límite del paciente sin teléfono.
- El criterio de aceptación es este: si el importe llega vacío, el total queda en cero y la API responde 422, no 500.
- Esto no es un bug, es alcance nuevo. Lo anoto y lo hablamos en refinamiento, no lo cuelo en la PR.
- La deuda técnica de este módulo es que la validación está duplicada. No la pago entera ahora; dejo un ticket con el porqué.
- Hago un spike de medio día para ver si la migración cabe sin downtime. Si no cabe, volvemos con un plan.
- El MVP de las notas es crear, listar y borrar. Editar y permisos por rol esperan.
- Esta dependencia es de diseño, no de código: sin saber quién puede cancelar una cita, el endpoint de autorización es una suposición.
- Marco el ticket como bloqueado y escribo qué decisión hace falta, para que no parezca que estoy parado sin motivo.
- El trade-off es fecha contra integridad: o validamos en el servidor en esta entrega, o aceptamos datos imposibles y lo pagamos en soporte.
- No estimo “cuando acabe”. Estimo el caso que está escrito; si entra otro, la estimación se cae.

## En la pull request

- Abro la PR contra `main` con tres commits: el fix, la prueba de regresión y el ajuste del mensaje de error.
- El diff parece grande porque el formateo se mezcló con el cambio. Lo separo para que la review se lea.
- En la descripción dejo el ticket, el criterio de aceptación y cómo probarlo en local.
- Esta PR no cambia comportamiento; es un refactor del cálculo del total. Las pruebas existentes tienen que seguir en verde.
- ¿Puedes mirar sobre todo el contrato? El resto es mecánico.
- Dejo un comentario en la línea del reintento: esta operación es idempotente, por eso repetirla no duplica la cita.
- No apruebo todavía: si la sesión ha caducado, el código responde 200 y un JSON vacío. Eso es un 401.
- El conflicto está en el esquema. No acepto las dos versiones; la migración nueva tiene que ir después de la que ya está en `main`.
- Rebaseo sobre `main` antes de pedir review otra vez, que entraron dos merges mientras tanto.
- El lint falla por una convención de nombres. Lo corrijo yo; no hace falta discutirlo en la review.
- Hay un efecto secundario escondido: al guardar la ficha también envía un correo. Lo saco de esta PR.
- El caso límite que falta es la lista vacía. En la UI no debería quedar un spinner infinito.
- Apruebo con un comentario: el invariante “una cita pertenece a un paciente existente” ahora está en la base, no solo en PHP.
- No mezclo hasta que CI esté en verde. El build local no cuenta como pipeline.
- Esta PR lleva feature flag. En staging lo activamos; en producción nace apagado.

## Al hablar de diseño

- Esta función hace dos cosas. La cohesión mejora si el cálculo del total no conoce la sesión.
- El acoplamiento está en que el controlador arma el SQL. Si el esquema cambia, se rompe la capa de HTTP.
- El contrato público es este JSON. Por dentro podemos cambiar la consulta sin avisar a React.
- No añadiría una interfaz nueva hasta que haya un segundo caso. Ahora sería abstracción sin uso.
- El legado no se reescribe este sprint. Lo envolvemos con una prueba de integración y cambiamos un borde.
- Si el cliente reintenta el POST, ¿qué garantiza la idempotencia? Ahora mismo crearía dos facturas.
- El camino feliz ya está. Me falta decidir el error: 404 si la cita no existe, 403 si existe y no es tuya.
- Esto rompe el contrato. Es un breaking change; o versionamos el endpoint o avisamos y migramos el cliente en la misma release.
- La paginación no es un adorno. Sin límite, el listado de pacientes crece hasta tumbar la respuesta.
- Dejamos la consistencia fuerte en el alta de la cita. La réplica de lectura puede ir un segundo por detrás en el listado, y hay que decirlo en el ticket.

## Al hablar de datos

- La migración añade la clave foránea. En staging falla porque hay citas huérfanas; hay que limpiarlas antes de aplicar en producción.
- El índice nuevo acelera el filtro por fecha y encarece el alta. Con el volumen actual compensa.
- Esto es un N+1: una consulta de citas y otra por cada paciente. En local, con diez filas, no se ve.
- La transacción tiene que cubrir el alta y el movimiento de agenda. Si el segundo falla, el primero no puede quedar confirmado.
- No uses la base de producción para probar. Carga un seed en local y, si hace falta realismo, un backup anonimizado.
- El backup de anoche existe. Lo que no hemos ensayado es la restauración, así que no contaría con él en un incidente.
- Esta columna admite nulos y el código no. El esquema y el contrato se contradicen.
- La integridad la pone la base. Si solo validamos en el formulario, otro cliente de la API puede saltársela.
- La consulta del informe no está paginada y mantiene un lock largo. Por eso el alta se queda esperando.
- Reviso el `EXPLAIN` antes de pedir otro índice. A lo mejor el problema es el orden del filtro, no la falta de índice.

## Al desplegar

- El artefacto que pasó CI es el que sube. No despliego una carpeta local “que es casi igual”.
- Primero staging, con la migración. Si el arranque falla, no hay deploy a producción.
- La variable de entorno de staging apunta a su base. La de producción no está en el repositorio.
- El secreto del token se rotó. Quien no actualice el entorno verá 401 y parecerá un bug de login.
- El deploy de producción lo hago dentro de la ventana. Si pasa de veinte minutos con error, rollback.
- Hay downtime previsto de unos minutos porque la migración reescribe la tabla. Soporte ya lo sabe.
- La release lleva changelog: qué cambia para el usuario y qué tiene que hacer el otro equipo con el webhook.
- El feature flag está apagado en producción. El código ya está fuera; activarlo es otro paso, no otro build.
- CI está rojo en `main`. No salimos a producción hasta saber si es el test flaky o un fallo real.
- El rollback ya está hecho. Producción corre el artefacto de ayer. El arreglo va en un hotfix, no en “ya lo miro mañana”.

## Cuando algo se rompe

- Esto es un incidente, no un ticket para el próximo sprint. El alta de citas devuelve 500 desde hace doce minutos.
- Severidad alta: afecta al camino de reserva, que es el que usa la clínica en horario de mostrador. Impacto: no pueden crear citas.
- Mitigación primero. Desactivo el flag del cálculo nuevo y confirmo que el alta vuelve. La causa raíz va después.
- Los logs de esa petición no traen el identificador. Por eso no puedo cruzarla con la traza.
- La alerta de latencia saltó en el percentil 95, no en la media. La media seguía “bien” mientras una de cada veinte peticiones tardaba segundos.
- El cuello de botella es la llamada al proveedor de correo: no tiene timeout, y cuando va lento se quedan colgados los workers.
- El reintento sin idempotencia nos duplicó cobros. Cortamos los reintentos como mitigación.
- No es un fallo de disponibilidad total. El servicio responde; la función de cancelar es la que está rota.
- En el postmortem quiero línea de tiempo, qué vimos en las métricas y qué cambio evitaba este caso. Sin “fulano se equivocó”.
- El bug en staging no reproduce en local porque el seed no tiene el caso de dos citas a la misma hora.
- Esto es una regresión del merge de ayer. La prueba de regresión tiene que fallar si alguien vuelve a quitar la comprobación.
- El hotfix toca solo la condición del 500. El refactor que se nos ocurrió durante el incidente se queda fuera.

## APIs, permisos y seguridad

- El endpoint espera `patient_id` y devuelve 422 si falta. Un 500 aquí significa que la validación no corrió.
- Autenticado no implica autorizado. El usuario entra, pero cancelar la cita de otro tiene que ser 403.
- El token va en memoria o en una cookie bien marcada, no en el repositorio ni en un mensaje de Slack.
- CORS no es el bug de lógica. Si la petición ni siquiera sale del navegador, el síntoma es otro: origen, método o cabecera.
- El rate limit del login está para frenar fuerza bruta. Si lo subimos “para que no moleste”, también subimos el abuso.
- Este webhook puede llegar dos veces. El receptor tiene que ser idempotente.
- No concateno el texto del buscador dentro del SQL. Eso es inyección, aunque en la demo nadie la pruebe.
- El nombre del paciente se pinta como texto. Si lo metemos como HTML, abrimos la puerta a XSS.
- La acción de borrar por POST necesita la protección CSRF. El enlace GET que borra no debería existir.
- El principio aquí es mínimo privilegio: el proceso que solo lee citas no necesita la clave que escribe en facturación.
- Cambio de contrato: el campo `hour` pasa a `starts_at`. Es breaking; el cliente viejo tiene que seguir hasta la versión nueva.
- La sesión caduca a las ocho horas. Lo que hoy “se queda logueado para siempre” es un bug, no una comodidad.

## Pruebas y calidad

- La unitaria cubre el total con importe vacío. No levanta base ni servidor.
- La de integración usa una base de prueba y comprueba que la transacción hace rollback si el segundo insert falla.
- La de extremo a extremo reserva una cita desde el formulario y comprueba que aparece en el listado.
- El fixture deja un paciente y cero citas. Si la prueba depende de lo que hubiera en tu máquina, no es una prueba.
- He mockeado el correo, no la base. Quiero ver el dato escrito de verdad.
- La cobertura subió y el bug de las citas solapadas sigue sin caso. La cifra no nos cubre.
- Este test es flaky: falla cuando el orden de la lista cambia. La aserción tiene que ser sobre el contenido, no sobre la posición casual.
- Añado el caso de regresión con el payload que vimos en el incidente. Si vuelve el 500, CI se pone rojo.
- No mezclo “arreglar el bug” y “reescribir el módulo” en la misma PR. La review no podría distinguir el arreglo.
- La definición de hecho de este equipo incluye prueba y deploy en staging, no solo la PR aprobada.

## Con producto, soporte y diseño

- Producto pide el flujo completo. Yo puedo cerrar el camino feliz esta semana si el caso de pago fallido sale del alcance.
- Traduzco “que sea más rápido” a una métrica: el listado, en el percentil 95, por debajo de 300 ms en staging con datos de seed grandes.
- Soporte ve el síntoma: “no deja guardar”. El bug, cuando lo reproducimos, es un 422 por un campo que la UI no muestra.
- El handoff a quien esté de guardia: flag, cómo hacer rollback, y qué log mirar. Sin eso, el ownership se queda en mi cabeza.
- El stakeholder que más duele si fallamos es mostrador, no el informe mensual. Por eso el alta va antes que el export.
- No hace falta consenso eterno. Hay dos opciones; propongo la del feature flag y, si en diez minutos no aparece un riesgo nuevo, seguimos.
- Escalo a plataforma porque el timeout está en el proxy, no en nuestro código, y nosotros no podemos cambiarlo.
- La documentación que falta es el README: cómo levantar local, qué variables hacen falta y cómo correr las pruebas.
- El onboarding de esta semana se atasca en el secreto local. Si no está escrito, cada persona nueva nos interrumpe con la misma pregunta.
- UI propone el estado vacío del listado. Encaja con el caso límite que la API ya devuelve como lista vacía y 200, no como error.

## Al cerrar

- El ticket cumple el criterio de aceptación. Lo paso a hecho cuando staging lo confirme, no cuando la PR se mezcle.
- Dejo en el ticket qué quedó fuera, para que el backlog no pierda el caso de la cita solapada.
- El changelog de la release menciona el arreglo del total y el cambio de campo, que es breaking para quien consuma la API.
- Mañana el primer punto del standup es el resultado del deploy, no un resumen de todas las horas.
- Si el hotfix aguanta la mañana sin alerta, cierro el incidente y dejo el postmortem para después del mediodía, con la cabeza fría.
