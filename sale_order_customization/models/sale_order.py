# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_order_name = fields.Char(string='Sale Order Name')
