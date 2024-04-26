# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import HttpCase


class TestOcaModuleJs(HttpCase):
    def test_tour(self):
        self.start_tour("/", "oca_module_tour", login="portal")
