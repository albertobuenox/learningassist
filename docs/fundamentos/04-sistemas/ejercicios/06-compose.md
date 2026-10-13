---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 06 — Compose: aplicación y base de datos

!!! info "Antes de empezar"

    Tiempo: 3 horas.

??? tip "Pista"

    Apoyo: la documentación de Compose y la página en Docker Hub de la imagen oficial de PostgreSQL (variables y volumen).

## Qué levantar

Dos servicios en `compose.yaml`:

- `db`: PostgreSQL. Los datos en un volumen con nombre. La contraseña llega por variable de entorno, leída desde un `.env` que está en `.gitignore`. Hay un `.env.example` sin secreto real.
- `app`: un servicio que **solo** comprueba la conexión (un script Node o PHP de diez líneas que haga `SELECT 1` y lo imprima) o, si ya tienes API, la API. El host de la base, visto desde `app`, es el nombre del servicio, no `localhost`.

`docker compose up` deja los dos en marcha. `docker compose down` para y quita contenedores, y **no** borra el volumen. Lo compruebas insertando una fila, bajando, subiendo y viendo la fila. Después, el comando que sí borra el volumen, ejecutado a conciencia, deja la base vacía. Anótalo para no usarlo por costumbre.

!!! warning "Restricciones"

    - El puerto de PostgreSQL no tiene por qué publicarse en el anfitrión. La app sí, si necesitas llamarla. Justifica cada `ports`.
    - Nada de copiar la contraseña dentro del Dockerfile.

!!! success "Cómo sabes que está bien"

    - Desde el contenedor de la app, el nombre `db` resuelve. Desde tu portátil, ese nombre no tiene por qué existir. Si te sorprende, vuelve al glosario, entrada “red de Docker”.
    - Un compañero clona el repo, copia `.env.example` a `.env`, pone una contraseña local y levanta el entorno sin editar YAML.
    - Puedes decir qué pieza es efímera (contenedor) y qué pieza guarda los datos (volumen).
