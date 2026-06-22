# -*- coding: utf-8 -*-
from odoo import models, fields


class Sala(models.Model):
    _name = 'gestion.salas.sala'
    _description = 'Sala de reuniones'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre identificativo de la sala'
    )
    
    descripcion = fields.Text(
        string='Descripción',
        help='Descripción de la sala y sus características'
    )

    # Campo adicional necesario para los datos iniciales del enunciado
    # (Sala A -> Planta 0, Sala B -> Planta 1, Sala C -> Planta 2)
    planta = fields.Integer(
        string='Planta',
        default=0,
        help='Planta del edificio en la que se ubica la sala'
    )

    reunion_ids = fields.One2many(
        comodel_name='gestion.salas.reunion',
        inverse_name='sala_id',
        string='Reuniones',
        help='Reuniones programadas en esta sala'
    )
