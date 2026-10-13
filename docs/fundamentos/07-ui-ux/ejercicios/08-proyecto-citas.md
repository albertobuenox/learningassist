---
tags:
  - ejercicio
  - largo
  - ui-ux
---

# 08 — Proyecto: pedir cita

!!! info "Antes de empezar"

    Cierre de la asignatura. Tiempo: un día. Es el mismo producto que el proyecto integrador, visto solo desde el uso. Quien implemente después (tú, en React) debería poder hacerlo sin volver a inventar los textos.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Entrega

Un archivo (Figma o PDF) con:

1. El flujo de Marta en el mostrador y el flujo de quien pide cita **sin** Marta, desde el móvil. Los dos existen. No tienen las mismas pantallas: quien pide desde casa no ve al resto de pacientes.
2. Wireframes de baja fidelidad de ambos, con vacío, carga y error en la lista de huecos.
3. Alta fidelidad de una sola pantalla por flujo, usando los tres componentes. Si un componente no encaja en el móvil, se adapta en el sistema, no se redibuja aparte sin decirlo.
4. La nota de accesibilidad: contraste medido, etiquetas, foco, estado ocupado que no depende solo del color.
5. Lo que cambiaste tras la prueba del ejercicio 7, en dos frases.

!!! warning "Restricciones"

    - Quien pide cita desde casa no elige “observaciones clínicas”. Elige hueco y deja un nombre y un teléfono.
    - No hay registro con contraseña en este diseño. Si lo añades, justifica la fricción con el fin de “salir con una cita”.
    - Textos en castellano, escritos del todo, incluidos los de error.

!!! success "Cómo sabes que está bien"

    - Una persona que no ha visto el archivo puede señalar, en el flujo de casa, el paso en el que la cita ya es suya.
    - La pantalla de Marta no muestra datos de otros pacientes en la vista de quien pide desde el móvil. Si el prototipo enlaza las dos por accidente, el enlace sobra.
    - Los textos de error caben en el componente de campo. Si no caben, el texto o el componente están sin resolver; no se recorta con puntos suspensivos para que “quepa”.
