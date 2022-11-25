# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    """@api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        product_id = self.env.context.get('active_product_id',False)
        filter_lot_by_availability = self.env.context.get('filter_lot_by_availability',False)
        lots_visible = self.env.context.get('lots_visible',False)
        location_id = self.env.context.get('location_id',False)
        if not product_id or not filter_lot_by_availability or not lots_visible or not location_id:
            return super(StockProductionLot, self)._name_search(name=name,args=args,operator=operator,limit=limit,name_get_uid=name_get_uid)
        quants = self.env['stock.quant']._gather(self.env['product.product'].browse(product_id),self.env['stock.location'].browse(location_id))
        available_lots = quants.mapped('lot_id').ids
        args.append(['id','in',available_lots])
        return super(StockProductionLot, self)._name_search(name=name,args=args,operator=operator,limit=limit,name_get_uid=name_get_uid)"""


    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        # FIXME:We have to review this code in cae of performance issues
        # if the search is in the context of picking
        product_id = self.env.context.get('active_product_id', False)
        filter_lot_by_availability = self.env.context.get('filter_lot_by_availability', False)
        lots_visible = self.env.context.get('lots_visible', False)
        location_id = self.env.context.get('location_id', False)
        if not product_id or not filter_lot_by_availability or not lots_visible or not location_id:
            return super(StockProductionLot, self)._search(args, offset=offset, limit=limit, order=order,count=count,
                                                                access_rights_uid=access_rights_uid)
        quants = self.env['stock.quant']._gather(self.env['product.product'].browse(product_id),
                                                 self.env['stock.location'].browse(location_id)).filtered(lambda qt:qt.quantity - qt.reserved_quantity > 0)
        available_lots = quants.mapped("lot_id").ids
        args.append(('id', 'in', available_lots))
        return super(StockProductionLot, self)._search(args, offset=offset, limit=limit, order=order, count=count,
                                                       access_rights_uid=access_rights_uid)





    

