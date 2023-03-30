/** @odoo-module **/

import {registerPatch} from "@mail/model/model_core";
import {session} from "@web/session";

registerPatch({
    name: "ActivityMenuView",
    lifecycleHooks: {
        _created() {
            this._super();
            this.filter = "my";
            this.user_context = Object.assign({}, session.user_context, {
                team_activities: this.filter !== "my",
            });
            this._update_team_activities_context();
        },
    },
    recordMethods: {
        _update_team_activities_context() {
            this.user_context.team_activities = this.filter === "team";
        },
        async fetchData() {
            if (this.filter !== "team") {
                return await this._super();
            }
            const data = await this.messaging.rpc({
                model: "res.users",
                method: "systray_get_activities",
                args: [],
                kwargs: {context: this.user_context},
            });
            this.update({
                activityGroups: data.map((vals) =>
                    this.messaging.models.ActivityGroup.convertData(vals)
                ),
                extraCount: 0,
            });
            this.user_context.team_activities = false;
        },
        onClickDropdownToggle(ev) {
            ev.preventDefault();
            var $siblingNav = $(ev.currentTarget).parent().find("a");
            if ($(ev.currentTarget).data("filter") === "team") {
                this.filter = $(ev.currentTarget).data("filter");
                this._update_team_activities_context();
                $siblingNav.removeClass("active");
                $(ev.currentTarget).addClass("active");
                this.fetchData();
            } else if ($(ev.currentTarget).data("filter") === "my") {
                this.filter = $(ev.currentTarget).data("filter");
                this._update_team_activities_context();
                $siblingNav.removeClass("active");
                $(ev.currentTarget).addClass("active");
                this.fetchData();
            } else {
                return this._super(ev);
            }
        },
    },
});
