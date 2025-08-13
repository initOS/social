# Copyright 2019 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_get_recipients_non_follower_partners(self, message, msg_vals):
        # filter out all the followers
        return (
            msg_vals.get("partner_ids", [])
            if msg_vals
            else message.sudo().partner_ids.ids
        )

    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        """Compute recipients to notify based on subtype and followers. This
        method returns data structured as expected for ``_notify_recipients``."""
        recipient_data = super()._notify_get_recipients(message, msg_vals, **kwargs)
        if "notify_followers" in self.env.context and not self.env.context.get(
            "notify_followers", False
        ):
            # filter out all the followers
            pids = self._notify_get_recipients_non_follower_partners(message, msg_vals)
            recipient_data = [d for d in recipient_data if d["id"] in pids]
        return recipient_data
