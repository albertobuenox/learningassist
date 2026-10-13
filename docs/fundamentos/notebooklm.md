# Fuentes para NotebookLM

Cinco cuadernos, uno por asignatura. En el plan gratuito cada cuaderno admite 50 fuentes y unas 500.000 palabras por fuente. Un solo cuaderno con todo el recorrido mezcla temas y responde peor.

NotebookLM no recorre un sitio: **una URL es una página**. Si al importar solo ves un índice, esa página no sirve; abre el capítulo que tiene el texto y súbelo ese.

## Cómo cargarlo

1. Crea el cuaderno con el nombre de la carpeta.
2. Sube el `README.md` y el `glosario.md` de esa carpeta (archivo local). Así las respuestas usan las mismas palabras que los enunciados.
3. Añade las URLs de abajo. Los PDF, descárgalos y súbelos como archivo: un enlace de descarga a veces llega como página intermedia y NotebookLM no ve el libro.
4. No subas los archivos de `ejercicios/`. El cuaderno te los resolvería, y el criterio de esta carpeta es que los cierres tú.

No sirven aquí los cursos de pago (Udemy, Laracasts cerrado, Refactoring UI), ni los gimnasios interactivos (SQLBolt, Flexbox Froggy, SQLZoo): no hay un texto que importar. El manual completo de PostgreSQL en PDF pasa el límite de palabras; usa las páginas sueltas.

Cuando una fuente esté en inglés, pregunta en español igual. Pide que cite la fuente.

---

## 1. Bases de datos

Cuaderno: `01 Bases de datos`. Archivos locales: `01-bases-de-datos/README.md`, `01-bases-de-datos/glosario.md`.

Modelo, claves, consultas, uniones, agregados, restricciones, transacciones, índices, `EXPLAIN`. El motor es PostgreSQL 18.

| Tema | Fuente |
| --- | --- |
| Consultar una tabla | https://www.postgresql.org/docs/current/tutorial-select.html |
| Join | https://www.postgresql.org/docs/current/tutorial-join.html |
| Agregados | https://www.postgresql.org/docs/current/tutorial-agg.html |
| `FROM`, `JOIN`, `GROUP BY`, `HAVING` | https://www.postgresql.org/docs/current/queries-table-expressions.html |
| Vistas | https://www.postgresql.org/docs/current/tutorial-views.html |
| Claves foráneas | https://www.postgresql.org/docs/current/tutorial-fk.html |
| `NOT NULL`, `UNIQUE`, `CHECK`, claves | https://www.postgresql.org/docs/current/ddl-constraints.html |
| Tipos | https://www.postgresql.org/docs/current/datatype.html |
| Transacciones | https://www.postgresql.org/docs/current/tutorial-transactions.html |
| Aislamiento | https://www.postgresql.org/docs/current/transaction-iso.html |
| Qué es un índice | https://www.postgresql.org/docs/current/indexes-intro.html |
| Índice único | https://www.postgresql.org/docs/current/indexes-unique.html |
| Índice parcial | https://www.postgresql.org/docs/current/indexes-partial.html |
| Ver si se usa el índice | https://www.postgresql.org/docs/current/indexes-examine.html |
| `EXPLAIN` | https://www.postgresql.org/docs/current/using-explain.html |
| Anatomía de un índice | https://use-the-index-luke.com/sql/anatomy |
| Índices y `WHERE` | https://use-the-index-luke.com/sql/where-clause |
| Plan de ejecución, en prosa | https://use-the-index-luke.com/sql/explain-plan |
| Formas normales (1FN a 5FN) | https://zimmer.fresnostate.edu/~sasanr/Teaching-Material/MIS/DBMS/Guide-To-5NF.pdf |

La última es el artículo de William Kent. Si la URL no entra, descarga el PDF en el navegador y súbelo como archivo. Con la primera, la segunda y la tercera forma normal basta para el ejercicio de diseño; la cuarta y la quinta pueden quedarse sin leer.

Si `datatype.html` entra como índice vacío, sustituye por las páginas hijas que nombren el tipo que estés usando (numérico, fecha, texto).

---

## 2. Frontend, Node y React

Cuaderno: `02 Frontend`. Archivos locales: `02-frontend-node-react/README.md`, `02-frontend-node-react/glosario.md`.

HTML semántico, CSS, JavaScript, DOM, HTTP, Node sin framework, React con funciones.

| Tema | Fuente |
| --- | --- |
| JavaScript, DOM, eventos y HTTP en un solo libro | https://eloquentjavascript.net/Eloquent_JavaScript.pdf |
| Estructura de una página | https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_a_page_of_content |
| Especificidad | https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity |
| Flexbox | https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox |
| Grid | https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout |
| Chuleta de Flexbox | https://css-tricks.com/snippets/css/a-guide-to-flexbox/ |
| Chuleta de Grid | https://css-tricks.com/complete-guide-css-grid-layout/ |
| Eventos en el navegador | https://javascript.info/introduction-browser-events |
| `fetch` | https://javascript.info/fetch |
| Guía de `fetch` | https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch |
| Códigos de estado | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status |
| CORS | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS |
| Qué es Node | https://nodejs.org/en/learn/getting-started/introduction-to-nodejs |
| `node:http` | https://nodejs.org/api/http.html |
| `node:fs` | https://nodejs.org/api/fs.html |
| Proceso y argumentos | https://nodejs.org/api/process.html |
| Quick Start de React | https://react.dev/learn |
| Props | https://react.dev/learn/passing-props-to-a-component |
| Render condicional | https://react.dev/learn/conditional-rendering |
| Listas y `key` | https://react.dev/learn/rendering-lists |
| Estado | https://react.dev/learn/state-a-components-memory |
| Actualizar a partir del estado anterior | https://react.dev/learn/queueing-a-series-of-state-updates |
| Arrays en el estado | https://react.dev/learn/updating-arrays-in-state |
| Formulario controlado | https://react.dev/learn/reacting-to-input-with-state |
| `useEffect` | https://react.dev/learn/synchronizing-with-effects |
| Cuándo no hace falta un efecto | https://react.dev/learn/you-might-not-need-an-effect |

El PDF de Eloquent JavaScript cubre el lenguaje. Las páginas de javascript.info y de MDN están para el navegador y para HTTP, que es donde se atascan los ejercicios 2, 3 y 7. React va aparte: el libro no lo trata.

---

## 3. Sistemas

Cuaderno: `03 Sistemas`. Archivos locales: `04-sistemas/README.md`, `04-sistemas/glosario.md`.

Ubuntu, SSH, firewall, Nginx, y Docker (imagen, contenedor, volumen, red, Compose).

| Tema | Fuente |
| --- | --- |
| Shell, permisos, procesos, redirecciones | Descargar el PDF desde https://linuxcommand.org/tlcl.php (edición 25.12, `TLCL-25.12A.pdf`) y subirlo como archivo |
| Primer arranque: usuario, sudo, SSH, UFW | https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-24-04 |
| Clave SSH | https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server |
| UFW | https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu |
| systemd y `journalctl` | https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units |
| Nginx, guía breve oficial | https://nginx.org/en/docs/beginners_guide.html |
| Nginx en Ubuntu | https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-24-04 |
| Qué es un contenedor | https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/ |
| Qué es una imagen | https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/ |
| Capas | https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/ |
| Dockerfile | https://docs.docker.com/build/concepts/dockerfile/ |
| Publicar un puerto | https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/ |
| Volúmenes y bind mounts | https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/ |
| Varios contenedores y red | https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/ |
| Modelo de Compose | https://docs.docker.com/compose/intro/compose-application-model/ |
| PHP en Docker | https://docs.docker.com/guides/php/ |
| Imagen oficial de Postgres | https://hub.docker.com/_/postgres |
| Imagen oficial de Nginx | https://hub.docker.com/_/nginx |
| Imagen oficial de PHP | https://hub.docker.com/_/php |

En las páginas de Docker Hub importa la descripción de variables, puertos y volumen. Si NotebookLM solo captura el escaparate, copia esa sección a un documento y súbelo.

El libro de Shotts tiene traducción al español más vieja que la edición 25.12. Para el cuaderno usa el PDF inglés actual.

---

## 4. Backend PHP

Cuaderno: `04 PHP`. Archivos locales: `05-backend-php/README.md`, `05-backend-php/glosario.md`.

PHP 8, petición y respuesta, validación, escapar la salida, PDO, sesión, Composer. Sin Laravel.

| Tema | Fuente |
| --- | --- |
| Mapa de prácticas actuales (una sola página larga) | https://phptherightway.com/ |
| Tipos | https://www.php.net/manual/es/language.types.php |
| Línea de comandos | https://www.php.net/manual/es/features.commandline.php |
| `$_GET`, `$_POST`, `$_SERVER` | https://www.php.net/manual/es/reserved.variables.php |
| Excepciones | https://www.php.net/manual/es/language.exceptions.php |
| `htmlspecialchars` | https://www.php.net/manual/es/function.htmlspecialchars.php |
| `password_hash` | https://www.php.net/manual/es/function.password-hash.php |
| `password_verify` | https://www.php.net/manual/es/function.password-verify.php |
| Sesiones | https://www.php.net/manual/es/book.session.php |
| Consultas preparadas con PDO | https://www.php.net/manual/es/pdo.prepared-statements.php |
| Errores de PDO | https://www.php.net/manual/es/pdo.error-handling.php |
| Composer | https://getcomposer.org/doc/01-basic-usage.md |
| Estilo PSR-12 | https://www.php-fig.org/psr/psr-12/ |
| Inyección SQL | https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html |
| XSS | https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html |
| Sesión, en producción | https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html |
| Configuración de PHP | https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html |

Si una página `/es/` entra vacía o a medias, cambia `es` por `en` en la misma ruta. El texto inglés del manual es el que se actualiza antes.

`book.session.php` es un índice. Si no trae el texto, sustituye por `session.examples.php`, `session.security.php` y `function.session-start.php` en el mismo manual.

---

## 5. UI/UX

Cuaderno: `05 UI UX`. Archivos locales: `07-ui-ux/README.md`, `07-ui-ux/glosario.md`.

Flujo, estados, jerarquía, accesibilidad, componentes, prueba con una persona. Figma no está: su curso vive dentro de la aplicación y no se importa.

| Tema | Fuente |
| --- | --- |
| Definición de accesibilidad | https://www.w3.org/WAI/fundamentals/accessibility-intro/ |
| Accesibilidad en la práctica | https://web.dev/learn/accessibility/ |
| Contraste, foco, nombre del control (WCAG 2.2, referencia rápida) | https://www.w3.org/WAI/WCAG22/quickref/ |
| Diez heurísticos | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| Estado vacío | https://www.nngroup.com/articles/empty-state-interface-design/ |
| Mensajes de error | https://www.nngroup.com/articles/error-message-guidelines/ |
| Errores en formularios | https://www.nngroup.com/articles/errors-forms-design-guidelines/ |
| Leyes de UX (índice; si entra vacío, sube cada ley) | https://lawsofux.com/ |
| Ley de Jakob | https://lawsofux.com/jakobs-law/ |
| Proximidad | https://lawsofux.com/law-of-proximity/ |
| Fitts | https://lawsofux.com/fittss-law/ |
| Hick | https://lawsofux.com/hicks-law/ |
| Diseño que se adapta al ancho | https://web.dev/learn/design/ |
| Tipografía: reglas cortas | https://practicaltypography.com/summary-of-key-rules.html |
| Cómo nombra otro sistema el color, el tipo y los componentes | https://m3.material.io/ |

Material Design es una aplicación web. Si la importación sale casi vacía, no insistas: los heurísticos, el estado vacío y el contraste ya cubren los ejercicios. El libro Refactoring UI no tiene edición pública; no lo subas.

`web.dev/learn/accessibility/` y `web.dev/learn/design/` pueden entrar como portada del curso. En ese caso sube los módulos sueltos que fallen en el ejercicio (contraste, foco, etiquetas, rejilla, tipo).

---

## Proyecto integrador

No necesita fuentes nuevas. El producto está descrito en `proyecto-integrador.md`: súbelo como archivo en un cuaderno aparte, junto con los cinco `README.md`, y pregunta ahí cómo encajan las piezas. El detalle de SQL, PHP, React, Docker o accesibilidad se consulta en el cuaderno de esa asignatura, no en este.
