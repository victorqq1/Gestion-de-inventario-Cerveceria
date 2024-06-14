# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo288w(models.Model):
    _name = 'odoo288w.modelo288w'
    _description = 'model modelo288w'

    name = fields.Char('id',required=True)
    tipo = fields.Char(String='Tipo',required=True)
    altura = fields.Char(String='altura',required=True)
    ancho = fields.Char(String='ancho',required=True)
    profundidad = fields.Char(String='profundidad',required=True)

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
