# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one(string="Vehicle", comodel_name="fleet.vehicle")
    vehicle_category_id = fields.Many2one(string="Vehicle Category", comodel_name="fleet.vehicle.model.category", default=1)
    weight = fields.Float(string="Weight", compute="_compute_weight_volume", store=True)
    volume = fields.Float(string="Volume", compute="_compute_weight_volume", store=True)
    docking_id = fields.Many2one(comodel_name="stock.docking")
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")
    driver_id = fields.Many2one(related="vehicle_id.driver_id")
    number_of_transfers = fields.Integer(string="Transfers", compute="_compute_number_of_transfers", store=True)
    number_of_moves = fields.Integer(string="Moves", compute="_compute_number_of_moves", store=True)

    @api.depends("vehicle_category_id", "picking_ids")
    def _compute_weight_volume(self):
        for record in self:
            picking_list = []
            if record.vehicle_category_id:
                weight = 0
                volume = 0
                for picking in record.picking_ids:
                    picking_list.append(picking)
                for picking in picking_list:
                    for move in picking.move_line_ids:
                        weight += move.product_id.weight * move.quantity
                        volume += move.product_id.weight * move.quantity
                
                record.weight = 0 if not record.vehicle_category_id.max_volume  else weight / record.vehicle_category_id.max_weight
                record.volume = 0 if not record.vehicle_category_id.max_weight  else volume / record.vehicle_category_id.max_volume
            else:
                record.weight = 0
                record.volume = 0
        
    @api.depends("move_line_ids")
    def _compute_number_of_moves(self):
        self.number_of_moves = len(self.move_line_ids)
    
    @api.depends("picking_ids")
    def _compute_number_of_transfers(self):
        self.number_of_transfers = len(self.picking_ids)