# Glosario — pruebas

### Prueba automática

Un programa que llama a tu código con una entrada conocida y comprueba la salida. Si la comprobación falla, el proceso termina mal. Si solo imprime el resultado para que tú lo leas, no es una prueba: es un script.

### Caso

Una situación concreta: importe vacío, título de dos letras, hueco ocupado. Un caso, una razón para fallar. Un caso que comprueba cinco cosas a la vez no señala cuál se rompió.

### Sujeto

Lo que estás probando. En el ejercicio 1 es una función. En el ejercicio 3 es una ruta HTTP. No es “toda la aplicación” en una sola prueba.

### Esperado y obtenido

Los dos lados de la comparación. La prueba muestra ambos cuando fallan. Un `if` que no dice qué esperaba te obliga a depurar la prueba además del código.

### Rojo

La prueba falla. Es el estado correcto **antes** de escribir el comportamiento que falta. Si escribes el código primero y la prueba después, no has visto el rojo de ese caso.

### Verde

La prueba pasa. Verde no significa “terminado”: significa que los casos escritos se cumplen.

### Regresión

Un caso que ya pasó y vuelve a fallar después de un cambio. La prueba existe para pillarlo sin que te acuerdes.

### Frontera

El borde del sistema por el que entra o sale algo: la función pura, la ruta HTTP, la consulta. Probar la frontera HTTP no exige abrir el navegador. Probar el botón sí. Son pruebas distintas.

### Doblado

Sustituir un vecino lento o frágil (la base, el reloj) por un sustituto controlado. En este módulo no hace falta un framework de dobles. Hace falta no llamar a producción.

### Lo que no está probado

La lista de casos que conoces y no tienes escritos. Forma parte del cierre. Una suite en verde con esa lista vacía, de mentira, es peor que una suite corta y sincera.
