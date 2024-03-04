# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one(string="Vehicle", comodel_name="fleet.vehicle")
    vehicle_category_id = fields.Many2one(string="Vehicle Category", comodel_name="fleet.vehicle.model.category")
    weight = fields.Float(string="Weight", compute="_compute_weight_volume")
    volume = fields.Float(string="Volume", compute="_compute_weight_volume")

    @api.depends("vehicle_category_id")
    def _compute_weight_volume(self):
        self.ensure_one()

        breakpoint()
        picking_list = []
        
        if self.vehicle_category_id:
            weight = 0
            volume = 0

            for picking in self.picking_ids:
                picking_list.append(picking)
            
            for picking in picking_list:
                for product in picking.product_id:
                    weight += product.weight

            self.weight = weight / self.vehicle_category_id.max_weight
            self.volume = volume / self.vehicle_category_id.max_volume
        else:
            self.weight = 0
            self.volume = 0



