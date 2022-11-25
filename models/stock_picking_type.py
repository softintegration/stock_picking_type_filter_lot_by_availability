# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    filter_lot_by_availability = fields.Boolean(string='Filter lot by availability', default=False,
                                                help="If this case is checked,the system will get only the available lot in source location of transfers with this type.")
