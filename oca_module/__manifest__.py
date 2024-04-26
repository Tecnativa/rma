# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "OCA module",
    "version": "16.0.1.0.0",
    "website": "https://github.com/OCA/rma",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["sale_stock", "hr_timesheet"],
    "assets": {
        "web.assets_tests": ["oca_module/static/src/js/tours/oca_module_tour.js"],
    },
    "application": False,
}
