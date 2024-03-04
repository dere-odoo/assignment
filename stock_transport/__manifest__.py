#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'stock_transport',
    'version' : '1.0',
    'description': 'connection module between stock and transfer',
    'summary': 'stock_transport',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'depends': ['stock_picking_batch', 'fleet', 'stock_delivery'],
    'data': [
        'views/fleet_category_model_view.xml',
        'views/stock_picking_batch_form.xml',
    ]
}
