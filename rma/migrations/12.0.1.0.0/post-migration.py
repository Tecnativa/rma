# Copyright 2020 Tecnativa - Ernesto Tejeda
# Copyright 2020 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade
from odoo.addons.rma.hooks import post_init_hook


@openupgrade.migrate()
def migrate(env, version):
    post_init_hook(env.cr, env.registry)
    # assign max sequence number
    env.cr.execute(
        "SELECT max(name), company_id FROM rma GROUP BY company_id"
    )
    for row in env.cr.fetchall():
        env["ir.sequence"].search([
            ("code", "=", "rma"),
            ("company_id", "=", row[1]),
        ]).write({
            "number_next_actual": int(row[0][3:]) + 1,
        })
