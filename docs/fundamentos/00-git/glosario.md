# Glosario — Git

### Repositorio

La carpeta del proyecto más el directorio `.git`, donde está la historia. Copiar la carpeta sin `.git` copia el código y pierde los commits.

### Commit

Una foto con nombre del proyecto en un momento, más el autor, la fecha y un mensaje. No es “guardar el archivo”. Es declarar que ese conjunto de cambios tiene un sentido.

### Directorio de trabajo

Los archivos que ves y editas.

### Área de preparación (index)

Lo que entrará en el próximo commit. `git add` mete cambios ahí. Puedes dejar fuera un archivo a medias.

### `HEAD`

El commit en el que estás. Si `HEAD` es una rama, avanzar la rama mueve `HEAD`.

### Rama

Un nombre que apunta a un commit. `main` no es especial para Git: es el nombre que habéis acordado para la línea que se publica.

### Mezcla (merge)

Unir la historia de dos ramas. Si las dos tocaron las mismas líneas, hay un conflicto: Git se detiene y te deja el archivo con las dos versiones marcadas. Resolverlo es elegir, no pulsar “aceptar todo”.

### Conflicto

Las dos versiones no caben solas. El archivo queda con marcas `<<<<<<<`. Un commit con esas marcas todavía dentro es un commit roto.

### Remoto

Otra copia del repositorio, casi siempre en un servidor (GitHub, GitLab, el de tu empresa). `origin` es el nombre habitual de esa copia.

### `push` y `pull`

`push` manda commits tuyos al remoto. `pull` trae commits del remoto y los mezcla con los tuyos. No son un disco en la nube: si no hay commit, no hay nada que subir.

### `.gitignore`

Lista de lo que Git no debe versionar. Dependencias instaladas, secretos, basura del editor. Un secreto que ya se commiteó sigue en la historia aunque luego lo añadas al ignore.

### `clone`

Copia el remoto, historia incluida, a una carpeta nueva. Es la prueba de que el README basta: la otra carpeta no tiene tus archivos sin commitear.

### Mensaje de commit

Una frase que dice por qué, no un inventario de archivos. “Corrige el total cuando el importe viene vacío” se puede leer. “Cambios” no.
