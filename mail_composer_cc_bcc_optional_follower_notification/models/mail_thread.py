# © 2025 initOS GmbH
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_get_recipients_non_follower_partners(self, message, msg_vals):
        pids = set(
            super()._notify_get_recipients_non_follower_partners(message, msg_vals)
        )
        partners_cc = self.env.context.get("partner_cc_ids", None)
        if partners_cc:
            pids.update(partners_cc.ids)

        partners_bcc = self.env.context.get("partner_bcc_ids", None)
        if partners_bcc:
            pids.update(partners_bcc.ids)
        return list(pids)
