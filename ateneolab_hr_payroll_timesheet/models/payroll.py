from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Description'

    def get_sheet_amount(self, start_date, end_date):
        for record in self:
            ATagLine = self.env['account.analytic.line'].search(
                [('employee_id', '=', record.id), ('validated', '=', True),
                 ('date', '>=', start_date), ('date', '<=', end_date)])
            return sum(ATagLine.mapped('unit_amount'))
