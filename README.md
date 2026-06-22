# Gestión de Salas de Reuniones — Módulo Odoo

Módulo de **Odoo** para gestionar las salas de reuniones de una empresa y las reuniones que se celebran en ellas. Desarrollado como práctica de la asignatura, en pareja (Javier Ibarra · Sergi Oliver).

## Funcionalidades

- **Gestión de salas**: nombre, descripción y planta del edificio.
- **Gestión de reuniones**: nombre/motivo, fecha de inicio, duración, número de asientos, sala, responsable y asistentes.
- **Cálculo automático** del porcentaje de asientos ocupados (campo *computed* `asientos_ocupados`, recalculado al cambiar asistentes o asientos).
- **Grupo de seguridad "Reuniones"** con reglas de acceso (`ir.model.access.csv` + `security.xml`).
- **Datos iniciales**: tres salas precargadas (Sala A → planta 0, Sala B → planta 1, Sala C → planta 2).
- Vistas de formulario, lista y menús propios.

## Modelos

| Modelo | Descripción | Campos clave |
|---|---|---|
| `gestion.salas.sala` | Sala de reuniones | nombre, descripción, planta, `reunion_ids` (One2many) |
| `gestion.salas.reunion` | Reunión | nombre, fecha, duración, asientos, `sala_id`, `responsable_id`, `asistente_ids` (Many2many), `asientos_ocupados` (computed) |

## Estructura

```
gestion_salas_reuniones/      # carpeta del addon
├── __manifest__.py
├── models/      # sala.py, reunion.py
├── views/       # sala_views.xml, reunion_views.xml, menu_views.xml
├── security/    # ir.model.access.csv, security.xml
└── data/        # salas_data.xml
docs/            # documentación del módulo y manual de usuario (PDF)
```

## Instalación

1. Copiar la carpeta `gestion_salas_reuniones/` en el directorio de *addons* de Odoo.
2. Activar el **modo desarrollador** y *Actualizar lista de aplicaciones*.
3. Buscar **"Gestión de Salas de Reuniones"** e instalar.

Dependencias: `base`. Licencia: LGPL-3.

## Documentación

En la carpeta [`docs/`](docs/) están la documentación técnica del módulo y el manual de usuario.

---
Autores: **Javier Ibarra** · Sergi Oliver
