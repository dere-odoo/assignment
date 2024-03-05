# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one(string="Vehicle", comodel_name="fleet.vehicle")
    vehicle_category_id = fields.Many2one(string="Vehicle Category", comodel_name="fleet.vehicle.model.category", default=1)
    weight_numeric = fields.Float(string="Weight", compute="_compute_weight_volume_numeric")
    volume_numeric = fields.Float(string="Volume", compute="_compute_weight_volume_numeric")
    weight = fields.Float(string="Weight", compute="_compute_weight_volume", store=True)
    volume = fields.Float(string="Volume", compute="_compute_weight_volume", store=True)
    docking_id = fields.Many2one(string="", comodel_name="stock.docking")
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")
    number_of_transfers = fields.Integer(string="Transfers", compute="_compute_number_of_transfers", store=True)
    number_of_moves = fields.Integer(string="Moves", compute="_compute_number_of_moves", store=True)

    @api.depends("vehicle_category_id", "picking_ids")
    def _compute_weight_volume(self):
        for record in self:
            record.weight = sum(record.picking_ids.mapped('weight'))*100 / record.vehicle_category_id.max_weight if record.vehicle_category_id.max_weight else 0
            record.volume = sum(record.picking_ids.mapped('volume'))*100 / record.vehicle_category_id.max_volume if record.vehicle_category_id.max_volume else 0
        
    @api.depends("move_line_ids")
    def _compute_number_of_moves(self):
        self.number_of_moves = len(self.move_line_ids)
    
    @api.depends("picking_ids")
    def _compute_number_of_transfers(self):
        self.number_of_transfers = len(self.picking_ids)
    
    @api.depends("vehicle_category_id", "picking_ids")
    def _compute_weight_volume_numeric(self):
        for record in self:
            record.weight_numeric = sum(record.picking_ids.mapped('weight'))
            record.volume_numeric = sum(record.picking_ids.mapped('volume'))
        