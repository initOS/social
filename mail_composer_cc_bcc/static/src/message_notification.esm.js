/** @odoo-module **/

import {attr} from "@mail/model/model_field";
import {registerPatch} from "@mail/model/model_core";

registerPatch({
    name: "Notification",

    modelMethods: {
        /**
         * @override
         */
        convertData(data) {
            const data2 = this._super(data);
            data2.recipient_type = data.recipient_type;
            return data2;
        },
    },

    fields: {
        recipient_type: attr(),
    },
});
