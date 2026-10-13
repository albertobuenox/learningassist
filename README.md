# Learning Assisted

Sitio de documentación con [MkDocs](https://www.mkdocs.org/) y el tema [Material](https://squidfunk.github.io/mkdocs-material/).

## Arrancar en local

```bash
cd "Learning Assisted"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en el navegador. Los cambios en `docs/` se recargan solos.

## Comandos útiles

| Comando | Qué hace |
| --- | --- |
| `mkdocs serve` | Servidor local con recarga en caliente |
| `mkdocs build` | Genera el sitio estático en `site/` |
| `mkdocs build --strict` | Falla si hay enlaces rotos o avisos |

## Estructura

```
Learning Assisted/
├── mkdocs.yml          # Configuración y menú
├── requirements.txt
├── docs/
│   ├── index.md        # Portada
│   ├── fundamentos/    # Asignaturas y ejercicios
│   ├── agentes/        # Lecciones con agentes
│   └── compendio/      # Términos y frases
└── site/               # Salida de mkdocs build (no versionar)
```
