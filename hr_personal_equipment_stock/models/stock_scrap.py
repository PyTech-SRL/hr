from odoo import fields, models


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    personal_equipment_id = fields.Many2one("hr.personal.equipment")
