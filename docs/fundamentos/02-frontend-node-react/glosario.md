# Glosario — frontend, Node y React

## Plataforma

### HTML semántico

Etiquetas que dicen qué es el contenido: `main`, `nav`, `button`, `label`, encabezados en orden. No es decoración. Un `div` con un listener de clic no es un botón.

### CSS

Cómo se presenta. Separado del significado. Si quitas la hoja de estilos, la página sigue siendo legible.

### Flexbox

Modelo para repartir espacio en una dirección (fila o columna): alinear, espaciar, crecer y encoger.

### Grid

Modelo para dos dimensiones a la vez: filas y columnas. Una ficha de producto suele ser Flexbox; una página con cabecera, aside y cuerpo suele ser Grid.

### Cascada y especificidad

Qué regla gana cuando varias tocan la misma propiedad. Antes de añadir `!important`, mira qué regla está ganando en las herramientas del navegador.

### DOM

El árbol de objetos que el navegador construye a partir del HTML. JavaScript lo lee y lo modifica. El usuario ve el resultado de ese árbol, no el archivo que escribiste.

### Evento

Algo que ocurre (clic, envío, tecla). Un listener es una función que corre cuando ocurre. El formulario, al enviarse, recarga la página salvo que lo evites a propósito.

### Estado

Los datos que, si cambian, deben cambiar lo que se ve. En vanilla vive en variables tuyas. El DOM es una vista de ese estado, no el sitio donde deberías buscar la verdad si también la guardas en un array.

## JavaScript

### Valor y referencia

Los objetos y arrays se comparten al asignarlos. Mutar un array “copiado” con `=` muta el original. Para un estado nuevo suele hacer falta una copia.

### `map`, `filter`, `reduce`

Transforman arrays sin un bucle manual. `map` devuelve otro array de la misma longitud. `filter` se queda con algunas filas. `reduce` acumula un solo resultado.

### Inmutabilidad práctica

En vez de hacer `push` al array que ya pintaste, construyes otro array y vuelves a pintar. En React esto deja de ser un estilo y pasa a ser el contrato.

### Módulo

Un archivo con `import` y `export`. Sirve para que no todo viva en un `script` global.

### Promesa

Un resultado que llegará o fallará más tarde. `async`/`await` es la forma legible de esperarlo. Una promesa no hace el código “en paralelo” por escribir `async`: hay que saber qué se espera y qué no.

### JSON

Texto que representa datos. No es un objeto hasta que lo parseas. `JSON.stringify` y `JSON.parse` cruzan esa frontera. Una fecha, al viajar en JSON, suele ir como texto.

## HTTP y Node

### Node.js

Un entorno para ejecutar JavaScript fuera del navegador. Tiene módulos para archivos, procesos y red. No es un framework.

### Proceso

El programa Node en marcha. Si sale, el servidor deja de escuchar. No es lo mismo que un archivo en disco.

### HTTP

Protocolo de la petición y la respuesta. Método (`GET`, `POST`, `PUT`, `DELETE`), camino (`/productos`), cabeceras, cuerpo y código de estado.

### Código de estado

Número que resume el resultado. 200 va bien, 201 se creó, 400 la petición es inválida, 404 no está, 500 fallaste tú. El cuerpo JSON no sustituye al código.

### `fetch`

API del navegador (y también de Node reciente) para hacer una petición. No lanza un error solo porque el servidor responda 404: hay que mirar `response.ok` o el estado.

### API

Aquí: un conjunto de rutas que devuelven datos, no HTML. El cliente decide cómo pintarlos.

### CORS

Regla del navegador: una página en un origen (puerto incluido) no lee la respuesta de otro origen salvo que el servidor lo permita. Si abres el HTML como archivo y llamas a `localhost`, vas a ver este problema. Servir el cliente desde un origen conocido lo evita o lo hace explícito.

### npm

El registro y la herramienta para instalar paquetes. El `package.json` declara de qué depende el proyecto. No instales un framework para un ejercicio que pide la plataforma a pelo.

## React

### Componente

Función que, dados unos datos, describe un trozo de interfaz. El nombre va en mayúscula. Si recibe los mismos datos y el mismo estado, describe lo mismo.

### JSX

Sintaxis que parece HTML dentro de JavaScript. Se transforma en llamadas. No es una cadena HTML. `class` se escribe `className`. Un evento es `onClick={funcion}`, no una cadena.

### Props

Argumentos del componente, de padre a hijo. El hijo no los reasigna. Si el hijo debe avisar de un cambio, el padre le pasa una función.

### Estado (`useState`)

Datos que, al actualizarse, hacen que React vuelva a describir el componente. La actualización con una función (`setX(prev => ...)`) importa cuando el valor nuevo depende del viejo.

### Render

Cada pasada en la que React llama a tu función para saber qué debería verse. No es “recargar la página”. Efectos secundarios (una petición, un temporizador) no van sueltos en el cuerpo del render: se repetirían.

### `useEffect`

Engancha un efecto al ciclo del componente. Para pedir datos al montar es una herramienta válida y fácil de usar mal (peticiones duplicadas, condiciones olvidadas). En el ejercicio 7, la pregunta es si sabes cuándo corre, no si memorizaste la firma.

### Lista y `key`

Al pintar un array, React necesita una clave estable por ítem (un id, no el índice si la lista se reordena o se filtra). La clave no se pasa como prop: identifica al ítem entre render y render.

### Controlado

Un campo cuyo valor vive en el estado de React. Cada tecla actualiza el estado y el estado pinta el campo. Así puedes validar mientras se escribe.

### Efecto de red

Cargar, vacío y error son tres interfaces, no un `console.log`. Si solo diseñaste el caso con datos, la pantalla está a medias.
