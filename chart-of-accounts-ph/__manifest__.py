# -*- coding: utf-8 -*-
{
    "name": "General Business COA for Philippine Enterprises (OmniTechnical) ",
    "summary": """
        General Business COA for Philippine Enterprises (OmniTechnical) """,
    "description": """
        General Business COA for Philippine Enterprises (OmniTechnical) 
    """,
    "author": "OmniTechnical Global Solutions, Inc.",
    "website": "http://www.omnitechnical.com",
    "depends": ["base", "sale", "account"],
    # always loaded
    "data": [
        # 'security/user_groups.xml',
        # 'security/security_data.xml',
        "views/views.xml",
        "data/chart_of_accounts_ph.xml",
        # 'views/templates.xml',
    ],
    "qweb": [
        # 'static/src/xml/extend_thread_fields.xml',
    ],
    'images': ['static/description/banner.gif'],
    "category": "Invoicing",
    "price": 99,
    "currency":"USD" ,
    "version": "1.0",
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
