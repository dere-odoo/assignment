#-- coding: utf-8 --

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock_trasport = fields.Boolean(string="Stock Transport")