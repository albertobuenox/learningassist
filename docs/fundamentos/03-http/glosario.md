# Glosario — HTTP

### Recurso

La cosa de la que se habla: una nota, la agenda de un día, una cita. No es la página ni el JSON. Esos son representaciones.

### Representación

Una forma concreta del recurso. El mismo día de agenda puede ir en HTML para el mostrador y en JSON para React. El contrato dice cuál se pide y cuál se devuelve.

### Método

Qué se pide hacer con el recurso. `GET` lee. `POST` crea o dispara una acción. `PUT` sustituye. `DELETE` borra. El método viaja en la primera línea, no dentro del JSON.

### Camino

La parte de la URL que identifica el recurso (`/citas/12`). El `?` de detrás es la query, otro sitio para datos. No mezcles un id en la query y otro en el camino sin decidir cuál manda.

### Cabecera

Metadato de la petición o de la respuesta. `Content-Type` dice cómo está escrito el cuerpo. `Accept` dice qué representación se prefiere. `Authorization` y `Cookie` dicen quién llama. Una cabecera no sustituye al código de estado.

### Cuerpo

Los bytes que siguen a las cabeceras. Un `GET` normalmente no lleva cuerpo. Un `POST` con JSON lleva cuerpo y el `Content-Type: application/json`. Si el cuerpo es JSON y la cabecera dice otra cosa, el servidor tiene derecho a rechazarlo.

### Código de estado

El resumen de la respuesta, en la primera línea. 200 todo bien, 201 creado, 204 bien y sin cuerpo, 301 o 302 la dirección cambió, 400 la petición está mal, 401 no sé quién eres, 403 sé quién eres y no puedes, 404 no existe, 409 el estado actual no admite ese cambio, 500 fallé yo. El texto del JSON no cambia el código.

### Seguro

Un método que no debe cambiar estado en el servidor. `GET` es seguro. Un `GET` que borra una cita está mintiendo: un navegador, un proxy o un prefetch pueden llamarlo solos.

### Idempotente

Llamarlo una vez o varias deja el mismo estado. `PUT` de la misma cita y `DELETE` de la misma cita lo son. `POST` de “crear cita”, en general, no: la segunda llamada crea otra, salvo que el contrato defina una clave de idempotencia.

### Origen

Esquema, host y puerto. `http://localhost:3000` y `http://localhost:8000` son orígenes distintos. El navegador trata una petición entre orígenes de forma distinta a `curl`.

### CORS

Regla del navegador, no de HTTP. Una página de un origen solo lee la respuesta de otro si el servidor lo autoriza con cabeceras. `curl` no aplica esa regla. Por eso “en curl funciona” no demuestra que el navegador vaya a poder leerla.

### Cookie de sesión

El navegador la reenvía al host que la puso, también cuando quien construyó el formulario es otra página. Eso es el hueco que cierra el ejercicio de CSRF en PHP. Aquí basta ver que la cookie viaja sola, sin que el JavaScript de tu página la copie.

### Contrato

El documento que fija rutas, métodos, códigos y forma de los cuerpos. Se escribe antes de la implementación. Si el cliente y el servidor discrepan, se mira el contrato, no la memoria de quien programó primero.
