# -*- coding: utf-8 -*-
from odoo import models, fields

class stockDocking(models.Model):
    _name = "stock.docking"
    _description = "Docking Locations for vehicle"

    name = fields.Char(string="Dock")