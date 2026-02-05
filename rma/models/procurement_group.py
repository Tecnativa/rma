# Copyright 2026 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProcurementGroup(models.Model):
    _inherit = "procurement.group"

    rma_id = fields.Many2one(comodel_name="rma", string="RMA")
