# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Salas de Reuniones',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Módulo para la gestión de salas y reuniones de la empresa',
    'description': """
Gestión de Salas de Reuniones
==============================
Este módulo permite gestionar las salas de reuniones de la empresa y
las reuniones que se realizan en ellas.

Funcionalidades:
----------------
* Gestión de salas (nombre, descripción, planta)
* Gestión de reuniones (nombre, fecha, duración, asientos, sala, responsable, asistentes)
* Cálculo automático del porcentaje de asientos ocupados
* Grupo de seguridad "Reuniones" para controlar el acceso
* Datos iniciales con tres salas precargadas
    """,
    'author': 'Alumno',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sala_views.xml',
        'views/reunion_views.xml',
        'views/menu_views.xml',
        'data/salas_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
