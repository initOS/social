# Copyright 2025 initOS GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Email CC and BCC",
    "summary": """This module bridges the functions of Email CC and BB with Mail optional
    follower notification.""",
    "version": "16.0.2.0.6",
    "development_status": "Alpha",
    "category": "Social",
    "website": "https://github.com/OCA/social",
    "author": "initOS GmbH, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": True,
    "depends": [
        "mail_composer_cc_bcc",
        "mail_optional_follower_notification",
    ],
}
