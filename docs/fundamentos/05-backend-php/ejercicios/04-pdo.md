---
tags:
  - ejercicio
  - largo
  - php
---

# 04 — PDO y consultas parametrizadas

!!! info "Antes de empezar"

    Tiempo: 3 horas.

??? tip "Pista"

    Apoyo: el manual de PDO y PDOStatement. La base es la de tus ejercicios de SQL, u otra vacía.

## Esquema

Una tabla `facturas` con id, concepto, importe y `creado_en`. El importe no puede ser negativo. El concepto no puede ser vacío. Esas reglas están en la tabla, no solo en PHP.

## Comportamiento

- `GET /` lista las filas, de la más nueva a la más vieja.
- `POST /facturas` inserta y, si salió bien, **redirige** a `GET /` con 302 (o 303). Recargar no vuelve a insertar.
- Un concepto con comilla (`O'Brien`) se guarda y se lista.
- La cadena SQL no contiene el concepto interpolado. Los valores entran por parámetros.
- La contraseña de la base se lee de una variable de entorno o de un archivo fuera de git. En el repositorio hay un ejemplo con un valor falso.

!!! warning "Restricciones"

    - Una sola conexión por petición, no una por consulta.
    - El error de conexión no se imprime entero al navegador: al visitante, un 500 genérico; en tu terminal, el mensaje real. En el servidor de desarrollo puedes mostrar más, pero deja escrito el sitio donde lo apagarías.
    - Sin ORM.

!!! success "Cómo sabes que está bien"

    - Pones una comilla en el concepto y no aparece un error de sintaxis SQL.
    - Apagas PostgreSQL. La página no enseña la cadena de conexión.
    - Hay dos facturas. El orden es el que pediste, porque la consulta lleva `ORDER BY`, no porque “suele salir así”.
