# Huerta Comunitaria — Servidor (Django REST Framework)

API REST para intercambiar semillas y cosechas entre vecinos.
El cliente está en un repositorio aparte (React + Vite).

**Autor:** Daniel Astudillo

## Modelos

- **Agricultor**: nombre, barrio, teléfono.
- **Cultivo**: nombre, tipo, cantidad en kg, si está disponible para intercambio y **agricultor** (ForeignKey → Agricultor).

Un agricultor tiene muchos cultivos. Si se elimina un agricultor, se eliminan sus cultivos (`on_delete=CASCADE`).

## Endpoints

| Método | Ruta | Acción |
|---|---|---|
| GET | `/api/agricultores/` | Listar agricultores |
| POST | `/api/agricultores/` | Crear agricultor |
| GET | `/api/agricultores/{id}/` | Ver un agricultor |
| PUT / PATCH | `/api/agricultores/{id}/` | Editar agricultor |
| DELETE | `/api/agricultores/{id}/` | Eliminar agricultor |
| GET | `/api/cultivos/` | Listar cultivos |
| POST | `/api/cultivos/` | Crear cultivo |
| GET | `/api/cultivos/{id}/` | Ver un cultivo |
| PUT / PATCH | `/api/cultivos/{id}/` | Editar cultivo |
| DELETE | `/api/cultivos/{id}/` | Eliminar cultivo |

## Cómo ejecutarlo

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

La API queda en http://127.0.0.1:8000/api/agricultores/

CORS está habilitado para `http://localhost:5173` (el cliente de Vite).
