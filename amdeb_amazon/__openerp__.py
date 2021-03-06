# __openerp__.py

{
    'name': 'Amdeb Amazon Integration',
    'summary': 'Integrate Amazon Marketplace as an Odoo sales channel',
    'version': '0.2',
    'category': 'Amdeb Integration',
    'website': 'https://github.com/amdeb/amdeb-amazon',
    'author': 'Amdeb Developers',
    'description': """
Amdeb Amazon Integrator
=========================

This is an Odoo module that integrates Odoo with Amazon
Marketplace Web Service (MWS). It supports the following functions:

* Product Synchronization
    - Upload newly created product data
    - Upload product data update: price, quantity, images, keywords etc
    - Upload product deletion
* Order Synchronization
    - Download newly created order data
    - Download order update (order cancellation)
    - Download order return request
    - Upload order confirmation
    - Upload order shipment and tracking number
    - Upload order cancellation
    - Upload return order refund

All synchronization supports two modes: an automatic mode and a manual mode.
In automatic mode, all synchronizations (including both upload and download)
are executed by background processes at the specific interval. In manual mode,
an Odoo user can request a synchronization at any time. It can specify
the range of synchronization or a full data synchronization.
Following are several manual synchronization examples:

* Upload all product data to Amazon
* Download last two month's order data
* Upload this month's shipping data

Authorized Odoo users should be able to check the synchronization logs and
should be notified when there is any error.

        """,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/cron_job.xml',
        'views/res_config_view.xml',
        'views/product_view.xml',
    ],
    'depends': ['sale', 'stock', 'amdeb_integrator', ],
    'installable': True,
    'application': True,
}
