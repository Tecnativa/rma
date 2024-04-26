# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import Form, common


class TestOcaModuleMisc(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Mr Odoo"})
        cls.product_a = cls.env["product.product"].create(
            {"name": "Test product A", "list_price": 100}
        )
        cls.product_b = cls.env["product.product"].create(
            {"name": "Test product B", "list_price": 200}
        )

    def test_partner(self):
        self.assertEqual(self.partner.name, "Mr Odoo")

    def test_products(self):
        self.assertTrue(self.product_a.categ_id)
        self.assertTrue(self.product_b.categ_id)

    def test_sale_order_01(self):
        order_form = Form(self.env["sale.order"])
        order_form.partner_id = self.partner
        order = order_form.save()
        self.assertEqual(order.partner_id, self.partner)

    def test_sale_order_02(self):
        order_form = Form(self.env["sale.order"])
        order_form.partner_id = self.partner
        with order_form.order_line.new() as line_form:
            line_form.product_id = self.product_a
        with order_form.order_line.new() as line_form:
            line_form.product_id = self.product_b
            line_form.product_uom_qty = 2
        order = order_form.save()
        self.assertEqual(order.partner_id, self.partner)
        self.assertEqual(order.state, "draft")
        self.assertEqual(len(order.order_line), 2)
        line_a = order.order_line.filtered(lambda x: x.product_id == self.product_a)
        self.assertEqual(line_a.price_unit, 100)
        self.assertEqual(line_a.price_subtotal, 100)
        line_b = order.order_line.filtered(lambda x: x.product_id == self.product_b)
        self.assertEqual(line_b.price_unit, 200)
        self.assertEqual(line_b.price_subtotal, 400)
        self.assertEqual(order.amount_untaxed, 500)  # 500 = 100 + 400
        order.action_confirm()
        self.assertEqual(order.state, "sale")
        for move in order.picking_ids.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        order.picking_ids.button_validate()
        self.assertEqual(order.picking_ids.state, "done")
        invoice = order._create_invoices()
        self.assertEqual(invoice.partner_id, self.partner)
        self.assertEqual(invoice.state, "draft")
        invoice.action_post()
        self.assertEqual(invoice.state, "posted")

    # def test_sale_order_03(self):
    #     order_form = Form(self.env["sale.order"])
    #     order_form.name = "Test"
    #     order_form.save()

    def test_timesheet_form_view(self):
        project = self.env["project.project"].create({"name": "Test Project"})
        employee = self.env["hr.employee"].create({"name": "Test employee"})
        timesheet_form = Form(
            self.env["account.analytic.line"].with_context(
                default_employee_id=employee.id
            ),
            view="hr_timesheet.hr_timesheet_line_tree",
        )
        timesheet_form.project_id = project
        timesheet_form.save()
