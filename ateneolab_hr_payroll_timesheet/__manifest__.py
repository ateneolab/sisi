# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': "Timesheet integration for Payroll Enterprise",
    'summary': """
       Timesheet integration for Payroll Enterprise
        """,
    'description': """
      Timesheet integration for Payroll Enterprise
    """,
    'author': "Yen Martinez<yenykm@gmail.com>",
    'website': "https://www.ateneolab.com",
    'category': "Human Resources",
    'version': "14.0.1.0.0",
    'depends': ['hr_payroll', 'hr_timesheet'],
    'data': [
        'data/hr_salary_rule_data.xml',
    ],
    'qweb': [
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
