# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume")
    weight = fields.Float(string="weight", compute="_compute_weight")

    @api.depends("move_line_ids")
    def _compute_volume(self):
        vol = 0
        for move_lines in self.move_line_ids:
            vol += move_lines.product_id.volume * move_lines.quantity
        self.volume = vol
    
    @api.depends("move_line_ids")
    def _compute_weight(self):
        weight = 0
        for move_lines in self.move_line_ids:
            weight += move_lines.product_id.weight * move_lines.quantity
        self.weight = weight