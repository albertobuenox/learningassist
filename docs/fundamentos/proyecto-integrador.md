# Proyecto integrador — Clínica de barrio

Une las asignaturas. Hazlo cuando hayas cerrado al menos el ejercicio de proyecto de cada carpeta, el contrato HTTP y el ejercicio de la frontera HTTP. Tiempo orientativo: 2 o 3 fines de semana.

## Producto

Una aplicación pequeña para una clínica con un mostrador y un profesional.

- El paciente pide cita eligiendo día y hueco libre.
- El mostrador ve el día, marca llegada y cancela.
- Nadie ve la historia clínica de otro paciente. En esta versión no hay historia clínica: solo nombre, teléfono y citas.

## Entregables

Trabaja en un repositorio aparte, no dentro de esta carpeta de apuntes. La historia de commits es la del ejercicio 4 de Git: se puede leer.

1. **UI/UX.** Flujo de 3 o 4 pantallas en baja fidelidad, más una pantalla en alta. Incluye vacío, error y carga. Una nota de accesibilidad: contraste, etiquetas, foco.
2. **Datos.** Esquema relacional con claves, una restricción que impida dos citas en el mismo hueco y tres consultas que el mostrador haría el lunes por la mañana.
3. **HTTP.** El contrato del ejercicio 5 de esa carpeta, actualizado si al implementar cambió un campo. El commit dice si cambió el contrato o el código.
4. **PHP.** Un backend que liste huecos, cree una cita y la cancele, en JSON, con los códigos del contrato. Consultas parametrizadas. Login de mostrador con `password_hash`. Un `POST` con la cookie de sesión y sin token no escribe.
5. **React.** Un cliente que consuma ese backend y muestre los tres estados de red: cargando, vacío, error. Si vive en otro origen, el navegador puede leer la respuesta, y lo has probado en el navegador, no solo con `curl`.
6. **Prueba.** Al menos una prueba automática de la frontera: el hueco ocupado no crea una segunda cita, o el `POST` sin sesión no escribe. Borrar la protección pone la prueba en rojo.
7. **Sistemas.** `docker compose` levanta PHP, base de datos y el frontend (o el estático ya construido). El README dice qué comando arranca todo, qué puertos se publican y que este entorno local es HTTP. El `.env` de ejemplo no contiene secretos reales. Si hiciste los ejercicios 8 y 9 de sistemas, el README enlaza qué tendría que ocurrir en la VM (443, redirección, puerto interno cerrado) sin meter la clave privada en el repositorio.

## Restricciones

- Un solo profesional y una sola sala. No añadas facturación.
- PostgreSQL o MySQL, el que hayas practicado. Documenta cuál.
- Sin Laravel ni Next.js, salvo que reescribas el mismo alcance **después** y compares qué te ahorraron.
- Nada de copiar un tutorial de “cita médica en 2 horas”. Si una pieza viene de un curso, cita el curso y explica qué cambiaste.

## Cómo sabes que está bien

- ¿Otra persona clona el repositorio y lo arranca con los pasos del README, en una máquina con Docker, sin llamarte y sin un `.env` que no está en git?
- ¿Puedes señalar en el esquema dónde se impediría una cita duplicada, y la prueba automática falla si quitas esa restricción?
- ¿El botón principal de cada pantalla es obvio sin que te lo expliquen?
- ¿Qué pasa si la base de datos no responde? ¿La interfaz lo dice o se queda en blanco?
- ¿Un `POST` de crear cita, con sesión y sin token, deja la agenda igual?

Escribe las respuestas en el README del proyecto. Si no puedes responder una, esa asignatura no está cerrada.
