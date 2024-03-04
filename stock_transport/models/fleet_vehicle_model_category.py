# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume")

    def _compute_display_name(self):
        for record in self:
            name = f"{record.name} ({record.max_weight}Kg,{record.max_volume})"
            record.display_name = name


    