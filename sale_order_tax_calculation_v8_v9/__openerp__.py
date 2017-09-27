# -*- coding: utf-8 -*-
# (c) 2017 Vignesh
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Subtotal with tax in SO v8/v9",

    'summary': """
       Subtotal with TAX""",

    'description': """
        * This module calculates TAX percentage in "amount" for each SO line and display tax amount it in SO Line. V10 also available in app store.
    """,
    'author': "Vignesh",
    'website': "viki2.odoo.com",
    'category': 'sale',
    'version': '8.0.0.1.0',
    'depends': ['base','sale',
                ],
    'images': ['images/main_screenshot.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'data': [
        'views/sale_order_view.xml',
    ],
    'demo': [
    ],
}
