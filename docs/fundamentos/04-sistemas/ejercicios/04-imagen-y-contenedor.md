---
tags:
  - ejercicio
  - medio
  - sistemas
---

# 04 — Imagen y contenedor

!!! info "Antes de empezar"

    Tiempo: 90 minutos. Guía: https://docs.docker.com/get-started/

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

En tu máquina de trabajo, no hace falta la VM.

## Qué observar

1. Arranca el contenedor de una imagen oficial de Nginx publicando un puerto. Ves la página de bienvenida en el navegador.
2. Entra en un shell de ese contenedor y cambia el `index.html`. Recarga el navegador: se ve el cambio. Para el contenedor y arranca otro **nuevo** desde la misma imagen. ¿Sigue tu cambio? Anota dónde vivía el cambio y por qué desapareció.
3. Repite el cambio montando una carpeta tuya sobre la raíz que Nginx sirve. Reinicia el contenedor. ¿El cambio sobrevive? ¿Sobreviviría si borras la carpeta del anfitrión?
4. Escribe en diez líneas la diferencia entre imagen, contenedor y bind mount usando solo lo que acabas de ver, no la definición del glosario de memoria.

!!! warning "Restricciones"

    - No escribas todavía un Dockerfile. Estás usando una imagen hecha.
    - No publiques nada en Docker Hub en este ejercicio.

!!! success "Cómo sabes que está bien"

    - Puedes predecir, antes de pulsar enter, si un archivo concreto seguirá ahí tras `docker rm`.
    - Sabes en qué puerto escucha Nginx **dentro** y en cuál lo abres **fuera**. Si solo recuerdas uno de los dos números, el mapeo no está entendido.
