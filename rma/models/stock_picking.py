# Copyright 2020 Tecnativa - Ernesto Tejeda
# Copyright 2026 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    rma_id = fields.Many2one(
        comodel_name="rma",
        compute="_compute_rma_id",
        string="RMA",
        store=True,
        index="btree_not_null",
    )
    rma_count = fields.Integer(
        string="RMA count",
        compute="_compute_rma_count",
    )

    @api.depends("group_id", "group_id.rma_id")
    def _compute_rma_id(self):
        for rec in self:
            rec.rma_id = rec.group_id.rma_id

    def _compute_rma_count(self):
        for rec in self:
            rec.rma_count = len(rec.move_ids.mapped("rma_ids"))

    def action_view_rma(self):
        self.ensure_one()
        action = self.env["ir.actions.act_window"]._for_xml_id("rma.rma_action")
        rma = self.move_ids.rma_ids
        if len(rma) == 1:
            action.update(
                res_id=rma.id,
                view_mode="form",
                view_id=False,
                views=False,
            )
        else:
            action["domain"] = [("id", "in", rma.ids)]
        return action
