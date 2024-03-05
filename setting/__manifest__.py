#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Setting",
    "description": "Setting to enable stock transport",
    "summary": "Stock Transport",
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "OEEL-1",
    "version": "1.0",
    "depends": ["stock"],
    "data": [
        "views/res_config_setting_view.xml",
    ]
}