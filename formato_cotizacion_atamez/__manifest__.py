# -*- coding: utf-8 -*-
{
    'name': "formato_cotizacion_atamez",

    'summary': """
        Formato de cotización""",

    'description': """
        Ajustes en formato de cotización
    """,

    'author': "NA Solutions ",
    'website': "https://nasolutions.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}