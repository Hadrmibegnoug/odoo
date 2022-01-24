# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website - Payment Authorize',
    'version': '1.0',
    'category': 'Accounting/Payment Acquirers',
    'sequence': 365,
    'summary': 'Website - Payment Authorize',
    'description': """""",
    'depends': ['website_payment', 'payment_authorize'],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
