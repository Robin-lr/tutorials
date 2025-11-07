{
    'name': 'Hello Odoo',
    'version': '1.0',
    'summary': 'First Odoo module - minimal',
    'description': 'Adds a menu item that says Hello Odoo',
    'author': 'Robin',
    'depends': ['base', 'web'],
    'category': 'Heil Robin',
    'data': [
        'views/hello_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hello_odoo/static/src/js/hello_action.js',
            'hello_odoo/static/src/xml/hello_template.xml',
        ],
    },
    #'installable': True,
    'application': True,
}
