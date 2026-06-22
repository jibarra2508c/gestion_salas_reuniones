# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Reunion(models.Model):
    _name = 'gestion.salas.reunion'
    _description = 'Reunión'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre o motivo de la reunión'
    )
    fecha_inicio = fields.Date(
        string='Fecha inicio',
        help='Fecha de inicio de la reunión'
    )
    duracion = fields.Integer(
        string='Duración (minutos)',
        help='Duración prevista de la reunión, en minutos'
    )
    asientos = fields.Integer(
        string='Asientos',
        help='Número de asientos disponibles para la reunión'
    )
    sala_id = fields.Many2one(
        comodel_name='gestion.salas.sala',
        string='Sala',
        help='Sala en la que se celebra la reunión'
    )
    responsable_id = fields.Many2one(
        comodel_name='res.partner',
        string='Responsable',
        help='Persona responsable de la reunión'
    )
    asistente_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Asistentes',
        help='Personas que asisten a la reunión'
    )
    asientos_ocupados = fields.Float(
        string='Asientos ocupados',
        compute='_compute_asientos_ocupados',
        store=True,
        help='Porcentaje de asientos ocupados en cada reunión'
    )

    @api.depends('asistente_ids', 'asientos')
    def _compute_asientos_ocupados(self):
        for reunion in self:
            if reunion.asientos > 0:
                num_asistentes = len(reunion.asistente_ids)
                reunion.asientos_ocupados = (num_asistentes / reunion.asientos) * 100
            else:
                reunion.asientos_ocupados = 0
