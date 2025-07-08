# © 2025 initOS GmbH
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class MailNotification(models.Model):
    _inherit = "mail.notification"

    def _notification_format(self):
        # Add information if the recipient was CC/BCC/TO
        result = super()._notification_format()
        for notif_vals in result:
            notif = self.browse(notif_vals["id"])
            if notif.res_partner_id in notif.mail_message_id.recipient_cc_ids:
                notif_vals["recipient_type"] = "cc"
            elif notif.res_partner_id in notif.mail_message_id.recipient_bcc_ids:
                notif_vals["recipient_type"] = "bcc"
            else:
                notif_vals["recipient_type"] = "to"
        return result
