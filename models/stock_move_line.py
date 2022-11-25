# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    filter_lot_by_availability = fields.Boolean(related='picking_id.picking_type_id.filter_lot_by_availability',
                                                readonly=True)

