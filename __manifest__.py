{
    "name": "Vendor Self Service Portal",
    "version": '1.0',
    "category": "Interview/Purchase & Inventory",
    "license": "AGPL-3",
    "summary": "Vendor Self Service Portal",
    'description': """
        ==========================
        Vendor Self Service Portal
        ==========================
    """,
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.exyz.com",
    "depends": ['base_setup', 'product', 'sale', 'mail', 'base'],
    "data": [
        'security/vendor_self_service_portal_security.xml',
        "security/ir.model.access.csv",

        'data/ir_sequence_data.xml',
        'data/vendor_adjustment_request_mail_template.xml',

        "views/vendor_forecast_views.xml",
        "views/vendor_adjustment_request.xml",
        "views/menuitem.xml",
        # "report/.xml", 
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
}
