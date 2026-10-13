---
tags:
  - ejercicio
  - largo
  - sistemas
---

# 07 — Proyecto: entorno de la clínica

!!! info "Antes de empezar"

    Cierre de la asignatura. Tiempo: medio día. Une la agenda de la base de datos (aunque sea solo el esquema) con Compose.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Entrega

Un repositorio pequeño con:

- `compose.yaml`: servicio de PostgreSQL y un servicio que aplique `esquema.sql` al arrancar la primera vez (un mecanismo oficial de la imagen, o un script de entrada que sea idempotente).
- Volumen para los datos.
- `.env.example`, `.gitignore`, `.dockerignore`.
- README: requisitos (Docker), comando de arranque, comando para abrir `psql` **dentro** del contenedor, puertos publicados y cómo resetear los datos sin borrar el archivo de esquema.
- Un párrafo que distinga este Compose, en HTTP y en tu máquina, de la VM de los ejercicios 8 y 9. No hace falta meter el certificado dentro de Compose. Sí hace falta decir qué puertos publicaría Nginx y cuáles no.

!!! warning "Restricciones"

    - Imágenes con etiqueta fija.
    - Ningún secreto real. La contraseña de ejemplo es obviamente de mentira.
    - No incluyas Kubernetes.

!!! success "Cómo sabes que está bien"

    - En una carpeta recién clonada, sigues el README y acabas dentro de `psql` viendo tus tablas.
    - `docker compose down` y `up` conservan una fila de prueba. El procedimiento de reset, documentado, la elimina.
    - Otra persona no necesita tu historial de terminal para repetirlo.
