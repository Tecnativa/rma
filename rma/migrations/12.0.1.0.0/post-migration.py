# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from ...hooks import post_init_hook


def migrate(env, version):
    post_init_hook(env.cr, env.registry)
