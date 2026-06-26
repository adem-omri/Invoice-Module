{
    'name': 'Custom Invoice Template',
    'version': '16.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Professional, fully branded PDF invoice & credit note template',
    'description': """
Custom Invoice Template
=======================
A complete, professional and modern PDF report for Customer Invoices and
Credit Notes with:

* Fully branded header / footer bands driven by company colors
* Configurable bank details, QR code, stamp & signature areas
* Amount in words, tax breakdown, discount support
* Modern / Classic / Minimal per-invoice styles
* Dedicated company configuration tab (Branding, Bank Details, Layout)
* Replaces the default invoice print action
""",
    'author': 'Adem Omri',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['account', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/report_paperformat.xml',
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
        'views/account_move_views.xml',
        'views/res_company_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'custom_invoice_template/static/src/css/invoice_style.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
